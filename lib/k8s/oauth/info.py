import base64
from lib import filter_helper


class K8sOAuthInfo():
    def __init__(self):
        self.oauth = None

    def get_oauth_info(self, oauth_mo):
        if oauth_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            oauth_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(oauth_mo, 'spec')
        return info

    def get_oauths_info(self, cache_enabled=True):
        if cache_enabled:
            if self.oauth is not None:
                return self.oauth

        managed_objects = self.get_oauth_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.oauth = []
        for managed_object in managed_objects:
            oauth_info = {}
            oauth_info['info'] = self.get_oauth_info(
                managed_object
            )
            oauth_info['mo'] = managed_object
            self.oauth.append(
                oauth_info
            )

        return self.oauth

    def match_oauth(self, oauth_info, oauth_filter):
        if oauth_filter is None or len(oauth_filter) == 0:
            return True

        for ap_rule in oauth_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, oauth_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_oauth',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_oauths(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_oauths = self.get_oauths_info(cache_enabled=cache_enabled)
        if all_oauths is None:
            return None

        oauths = []

        for oauth_info in all_oauths:
            if not self.match_oauth(oauth_info['info'], object_filter):
                continue

            if return_mo:
                oauths.append(
                    oauth_info['mo']
                )
                continue

            oauths.append(
                oauth_info['info']
            )

        return oauths

    def get_oauth(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        crbs = self.get_oauths(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )

        if crbs is None:
            return None

        if len(crbs) == 1:
            return crbs[0]

        return None

    def is_oauth(self, name, return_mo=False, cache_enabled=True):
        if self.get_oauth(name, return_mo=return_mo, cache_enabled=cache_enabled) is None:
            return False
        return True

    def add_identity_provider_oauth(self, secret_name, provider_name='my_htpasswd_provider', name='cluster'):
        oauth_mo = self.get_oauth(name, return_mo=True, cache_enabled=False)
        if oauth_mo is None:
            self.log.error(
                'add_identity_provider_oauth',
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
        oauth_mo['spec']['identityProviders'].append(
            provider_mo
        )

        return self.update_oauth_mo(oauth_mo)

    def del_identity_provider_oauth(self, provider_name, name='cluster'):
        oauth_mo = self.get_oauth(name, return_mo=True, cache_enabled=False)
        if oauth_mo is None:
            self.log.error(
                'del_identity_provider_oauth',
                'OAuth not found: %s' % (name)
            )
            return False

        if 'identityProviders' not in oauth_mo['spec']:
            self.log.error(
                'del_identity_provider_oauth',
                'Unexpected oauth: %s' % (name)
            )
            return False

        new_identity_providers = []
        for provider_mo in oauth_mo['spec']['identityProviders']:
            if provider_mo['name'] == provider_name:
                continue
            new_identity_providers.append(
                provider_mo
            )

        oauth_mo['spec']['identityProviders'] = new_identity_providers

        return self.update_oauth_mo(oauth_mo)

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
