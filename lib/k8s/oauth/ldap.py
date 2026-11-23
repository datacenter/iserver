import json
from lib import ip_helper


class K8sOAuthLdap():
    def __init__(self):
        pass

    def set_ldap_identity_provider_oauth_from_body(self, body, secret=None, name='cluster', confirmation=False, my_output=None):
        if my_output is not None:
            my_output.default('Set LDAP identity provider', before_newline=True, underline=True)
            my_output.default('- oauth: %s' % (name))
            my_output.default('- provider: %s' % (body['name']))

        oauth_mo = self.get_oauth(name, return_mo=True, cache_enabled=False)
        if oauth_mo is None:
            if my_output is not None:
                my_output.error('oauth not found')

            self.log.error(
                'add_htpasswd_identity_provider_oauth',
                'OAuth not found: %s' % (name)
            )
            return False

        if 'identityProviders' not in oauth_mo['spec']:
            oauth_mo['spec']['identityProviders'] = []

        providers = []
        secret_name = None
        for provider_mo in oauth_mo['spec']['identityProviders']:
            if provider_mo['name'] == body['name']:
                secret_name = self.get(provider_mo, 'bindPassword:name')
            else:
                providers.append(provider_mo)

        if secret is None:
            if secret_name is not None:
                provider_mo['attributes']['bindPassword'] = dict(name=secret_name)

        if secret is not None:
            secret_name = self.generate_secret_name(
                'openshift-config',
                name=body['name']
            )
            provider_mo['attributes']['bindPassword'] = dict(name=secret_name)

        oauth_mo = self.cleanup_managed_object(oauth_mo, exclude=['resourceVersion'])
        providers.append(provider_mo)
        oauth_mo['spec']['identityProviders'] = providers

        oauth_pods = self.get_oauth_pods(cache_enabled=False)
        success = self.replace_resource(oauth_mo, object_name='oauth', my_output=my_output, confirmation=confirmation)
        if not success:
            return False
        
        if secret is not None:
            success = self.create_or_update_secret_kv(
                'openshift-config', 
                secret_name,
                dict(bindPassword=ip_helper.encode_text_64(secret)), 
                secret_type='Opaque',
                replace=True,
                confirmation=confirmation, 
                my_output=my_output, 
                wait=True
            )
            if not success:
                return False
        
        success = self.wait_oauth_pods_restart(oauth_pods, my_output=my_output)
        return success

    def set_ldap_identity_provider_oauth_from_params(self, provider_name, url, bind, secret, attribute_id, attribute_name, attribute_username, attribute_email, insecure=False, mapping='claim', name='cluster', confirmation=False, my_output=None):
        if my_output is not None:
            my_output.default('Set LDAP identity provider', before_newline=True, underline=True)
            my_output.default('- oauth: %s' % (name))
            my_output.default('- provider: %s' % (provider_name))

        oauth_mo = self.get_oauth(name, return_mo=True, cache_enabled=False)
        if oauth_mo is None:
            if my_output is not None:
                my_output.error('oauth not found')

            self.log.error(
                'add_htpasswd_identity_provider_oauth',
                'OAuth not found: %s' % (name)
            )
            return False

        if 'identityProviders' not in oauth_mo['spec']:
            oauth_mo['spec']['identityProviders'] = []

        providers = []
        secret_name = None
        reference_provider = None
        for provider_mo in oauth_mo['spec']['identityProviders']:
            if provider_mo['name'] == provider_name:
                secret_name = self.get(provider_mo, 'ldap:bindPassword:name')
                reference_provider = provider_mo
            else:
                providers.append(provider_mo)

        provider_mo = {}
        provider_mo['type'] = 'LDAP'
        provider_mo['mappingMethod'] = mapping
        provider_mo['name'] = provider_name
        provider_mo['ldap'] = {}
        provider_mo['ldap']['attributes'] = {}
        provider_mo['ldap']['attributes']['id'] = attribute_id
        provider_mo['ldap']['attributes']['name'] = attribute_name
        provider_mo['ldap']['attributes']['preferredUsername'] = attribute_username
        provider_mo['ldap']['attributes']['email'] = attribute_email
        provider_mo['ldap']['bindDN'] = bind
        provider_mo['ldap']['url'] = url
        provider_mo['ldap']['insecure'] = insecure
        if secret_name is not None:
            provider_mo['ldap']['bindPassword'] = dict(name=secret_name)
        else:
            secret_name = self.generate_secret_name(
                'openshift-config',
                name=provider_name
            )
            provider_mo['ldap']['bindPassword'] = dict(name=secret_name)

        changed = False
        if reference_provider is None:
            changed = True
        if reference_provider is not None:
            if json.dumps(reference_provider, sort_keys=True) != json.dumps(provider_mo, sort_keys=True):
                changed = True

        if not changed:
            if my_output is not None:
                my_output.default('No provider change detected', before_newline=True)

        if changed:
            oauth_mo = self.cleanup_managed_object(oauth_mo, exclude=['resourceVersion'])
            providers.append(provider_mo)
            oauth_mo['spec']['identityProviders'] = providers

            oauth_pods = self.get_oauth_pods(cache_enabled=False)
            success = self.replace_resource(oauth_mo, object_name='oauth', my_output=my_output, confirmation=confirmation)
            if not success:
                return False
        
        success = self.create_or_update_secret_kv(
            'openshift-config', 
            secret_name,
            dict(bindPassword=ip_helper.encode_text_64(secret)), 
            secret_type='Opaque',
            replace=True,
            confirmation=confirmation, 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
        
        if changed:
            success = self.wait_oauth_pods_restart(oauth_pods, my_output=my_output)
            if not success:
                return False

        return True

    def get_identity_providers_ldap(self, name=None, namespace='openshift-config', cache_enabled=True):
        oauth_mos = self.get_oauths(user_info=True, cache_enabled=cache_enabled)
        if oauth_mos is None:
            return None

        info = []

        for oauth_mo in oauth_mos:
            if 'spec' not in oauth_mo or oauth_mo['spec'] is None:
                continue

            if 'identityProviders' not in oauth_mo['spec'] or oauth_mo['spec']['identityProviders'] is None:
                continue

            for identity_provider_mo in oauth_mo['spec']['identityProviders']:
                if identity_provider_mo['type'] == 'LDAP':
                    if name is not None and identity_provider_mo['name'] != name:
                        continue
                    
                    item = {}
                    item['mo'] = identity_provider_mo
                    item['oauth'] = self.get(oauth_mo, 'name')
                    item['name'] = self.get(identity_provider_mo, 'name')
                    item['url'] = self.get(identity_provider_mo, 'ldap:url')
                    item['bind_dn'] = self.get(identity_provider_mo, 'ldap:bindDN')
                    item['insecure'] = self.get(identity_provider_mo, 'ldap:insecure', on_error=False, on_none=False)
                    item['secret'] = self.get(identity_provider_mo, 'ldap:bindPassword:name')
                    item['password'] = None
                    item['isSecret'] = False
                    item['mappingMethod'] = self.get(identity_provider_mo, 'mappingMethod')
                    for key in ['id', 'name', 'email', 'preferredUsername']:
                        item['attribute_%s' % (key)] = self.get(identity_provider_mo, 'ldap:attributes:%s' % (key), on_error=[], on_none=[])
    
                    if item['secret'] is not None:
                        secret_mo = self.get_secret(
                            namespace,
                            item['secret'],
                            return_mo=True,
                            cache_enabled=cache_enabled
                        )
                        if secret_mo is not None:
                            item['isSecret'] = True

                        try:
                            item['password'] = self.get(secret_mo, 'data:bindPassword')
                            if item['password'] is not None:
                                item['password'] = ip_helper.decode_text_64(
                                    item['password']
                                )
                        except BaseException:
                            pass

                    item['ldapT'] = [
                        item['url'],
                        'bindDN: %s' % (item['bind_dn']),
                        'secret: %s [exists:%s]' % (item['secret'], item['isSecret']),
                        'mapping: %s' % (item['mappingMethod'])
                    ]

                    item['attributeT'] = [
                        'id: %s' % (','.join(item['attribute_id'])),
                        'name: %s' % (','.join(item['attribute_name'])),
                        'email: %s' % (','.join(item['attribute_email'])),
                        'preferredUsername: %s' % (','.join(item['attribute_preferredUsername']))
                    ]

                    item['userCount'] = 0
                    for idp_info in oauth_mo['idp']:
                        if idp_info['type'] == 'LDAP' and idp_info['name'] == item['name']:
                            item['userCount'] = idp_info['userCount']

                    info.append(
                        item
                    )

        return info
