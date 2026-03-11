class K8sIdentityInfo():
    def __init__(self):
        self.identity = None

    def get_identity_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )
        info['provider_name'] = self.get(managed_object, 'providerName')
        info['provider_username'] = self.get(managed_object, 'providerUserName')
        info['user_name'] = self.get(managed_object, 'user:name')
        info['user_id'] = self.get(managed_object, 'user:uid')
        return info

    def get_identitys(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'identity', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos
    
    def get_identity(self, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'identity', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

    def is_identity(self, name, return_mo=False, cache_enabled=True):
        if self.get_identity(name, return_mo=return_mo, cache_enabled=cache_enabled) is None:
            return False
        return True
