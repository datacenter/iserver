import base64


class K8sOAuthHtpasswd():
    def __init__(self):
        pass

    def add_htpasswd_identity_provider_oauth(self, secret_name, provider_name, name='cluster', confirmation=False, my_output=None):
        if my_output is not None:
            my_output.default('Add htpasswd identity provider to oauth', before_newline=True, underline=True)
            my_output.default('- oauth: %s' % (name))
            my_output.default('- provider: %s' % (provider_name))
            my_output.default('- secret: %s' % (secret_name))

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

        for provider_mo in oauth_mo['spec']['identityProviders']:
            if provider_mo['name'] == provider_name:
                return True

        provider_mo = {}
        provider_mo['htpasswd'] = {}
        provider_mo['htpasswd']['fileData'] = {}
        provider_mo['htpasswd']['fileData']['name'] = secret_name
        provider_mo['mappingMethod'] = 'claim'
        provider_mo['name'] = provider_name
        provider_mo['type'] = 'HTPasswd'

        oauth_mo = self.cleanup_managed_object(oauth_mo, exclude=['resourceVersion'])
        oauth_mo['spec']['identityProviders'].append(
            provider_mo
        )

        oauth_pods = self.get_oauth_pods(cache_enabled=False)
        success = self.replace_resource(oauth_mo, object_name='oauth', my_output=my_output, confirmation=confirmation)
        if not success:
            return False
        
        success = self.wait_oauth_pods_restart(oauth_pods, my_output=my_output)
        return success

    def get_identity_providers_htpasswd(self, namespace='openshift-config', cache_enabled=True):
        oauth_mos = self.get_oauths(cache_enabled=cache_enabled)
        if oauth_mos is None:
            return None

        info = []

        admins = self.get_cluster_role_binding_users(
            'cluster-admin',
            cache_enabled=cache_enabled
        )

        for oauth_mo in oauth_mos:
            if 'spec' not in oauth_mo or oauth_mo['spec'] is None:
                continue

            if 'identityProviders' not in oauth_mo['spec'] or oauth_mo['spec']['identityProviders'] is None:
                continue

            for identity_provider_mo in oauth_mo['spec']['identityProviders']:
                if identity_provider_mo['type'] == 'HTPasswd':
                    item = {}
                    item['oauth'] = oauth_mo['name']
                    item['name'] = identity_provider_mo['name']
                    item['secret'] = identity_provider_mo['htpasswd']['fileData']['name']

                    secret_mo = self.get_secret(
                        namespace,
                        item['secret'],
                        return_mo=True,
                        cache_enabled=cache_enabled
                    )
                    if secret_mo is None:
                        item['data'] = None
                        item['users'] = []
                        item['password'] = {}
                        item['usersT'] = []
                        item['isSecret'] = False
                    else:
                        item['data'] = None
                        item['isSecret'] = True
                        item['users'] = []
                        item['password'] = {}
                        item['usersT'] = []

                        if 'htpasswd' in secret_mo['data']:
                            item['data'] = secret_mo['data']['htpasswd']
                            decoded = base64.b64decode(
                                item['data']
                            ).decode('utf-8')

                            for line in decoded.split('\n'):
                                if len(line) > 0 and len(line.split(':')) > 1:
                                    (username, password) = line.split(':')
                                    item['users'].append(
                                        username
                                    )
                                    item['password'][username] = password
                                    if username in admins:
                                        item['usersT'].append(
                                            '%s (admin)' % (username)
                                        )
                                    else:
                                        item['usersT'].append(
                                            username
                                        )

                    item['users'] = sorted(item['users'])
                    item['usersT'] = sorted(item['usersT'])
                    item['mappingMethod'] = identity_provider_mo['mappingMethod']
                    info.append(
                        item
                    )

        return info

    def get_identity_provider_htpasswd(self, name, namespace='openshift-config', cache_enabled=True):
        providers = self.get_identity_providers_htpasswd(
            namespace=namespace,
            cache_enabled=cache_enabled
        )
        if providers is None:
            return None

        for provider in providers:
            if provider['name'] == name:
                return provider

        return None

    def is_identity_provider_htpasswd(self, name, namespace='openshift-config', cache_enabled=True):
        if self.get_identity_provider_htpasswd(name, namespace=namespace, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_identity_provider_htpasswd_user_map(self, namespace='openshift-config', cache_enabled=True):
        providers = self.get_identity_providers_htpasswd(
            namespace=namespace,
            cache_enabled=cache_enabled
        )
        if providers is None:
            return None

        users = {}

        for provider in providers:
            for username in provider['users']:
                users[username] = provider['name']

        return users
