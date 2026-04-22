class K8sOAuthInfo():
    def __init__(self):
        self.oauth = None

    def get_oauth_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )
        info['spec'] = self.get(managed_object, 'spec')
        info['idp'] = []

        idp_mos = self.get(managed_object, 'spec:identityProviders', on_error=[], on_none=[])
        for idp_mo in idp_mos:
            idp_type = self.get(idp_mo, 'type')
            idp_name = self.get(idp_mo, 'name')
            if idp_name is None or idp_type is None:
                continue
            info['idp'].append(dict(name=idp_name, type=idp_type))

        return info

    def add_oauths_user(self, infos, cache_enabled=False):
        for info in infos:
            for idp in info['info']['idp']:
                idp['user'] = []
                idp['userCount'] = 0

        users = self.get_users(cache_enabled=cache_enabled)
        if users is not None:
            for idp in info['info']['idp']:
                for user in users:
                    for identity in user['identityT']:
                        if identity['provider_name'] == idp['name']:
                            idp['user'].append(user['name'])
                            idp['userCount'] += 1

        return infos

    def get_oauths(self, user_info=False, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'oauth', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            add=dict(user=user_info)
        )
        return infos
    
    def get_oauth(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'oauth', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_oauth(self, name, return_mo=False, cache_enabled=True, optimized=True):
        if self.get_oauth(name, return_mo=return_mo, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True
