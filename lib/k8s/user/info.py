class K8sUserInfo():
    def __init__(self):
        self.user = None

    def get_user_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )
        info['full_name'] = self.get(managed_object, 'fullName')
        info['groups'] = self.get(managed_object, 'groups', on_error=[], on_none=[])
        info['identities'] = self.get(managed_object, 'identities', on_error=[], on_none=[])
        return info

    def add_users_identity(self, infos, cache_enabled=False):
        identities = self.get_identitys(cache_enabled=cache_enabled)
        for info in infos:
            info['info']['identityT'] = []
            if identities is None:
                continue

            for item in info['info']['identities']:
                identity_info = {}
                identity_info['provider_name'] = None
                identity_info['provider_username'] = None
                identity_info['user_name'] = None
                identity_info['user_id'] = None
                for identity in identities:
                    if identity['name'] == item:
                        identity_info['provider_name'] = identity['provider_name']
                        identity_info['provider_username'] = identity['provider_username']
                        identity_info['user_name'] = identity['user_name']
                        identity_info['user_id'] = identity['user_id']
                        info['info']['identityT'].append(identity_info)

        return infos

    def add_users_group(self, infos, cache_enabled=False):
        groups = self.get_groups(cache_enabled=cache_enabled)
        if groups is None:
            return infos

        for info in infos:
            for group in groups:
                for group_user in group['users']:
                    if group_user == info['info']['name']:
                        if group['name'] not in info['info']['groups']:
                            info['info']['groups'].append(group['name'])

        return infos
        
    def get_users(self, identity_info=True, group_info=True, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'user', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            add=dict(identity=identity_info,group=group_info)
        )
        return infos
    
    def get_user(self, name, identity_info=True, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'user', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            identity_info=identity_info,
            optimized=optimized
        )

    def is_user(self, name, return_mo=False, cache_enabled=True, optimized=True):
        if self.get_user(name, return_mo=return_mo, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True
