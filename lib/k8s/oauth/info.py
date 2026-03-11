class K8sOAuthInfo():
    def __init__(self):
        self.oauth = None

    def get_oauth_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )
        return info

    def get_oauths(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'oauth', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos
    
    def get_oauth(self, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'oauth', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

    def is_oauth(self, name, return_mo=False, cache_enabled=True):
        if self.get_oauth(name, return_mo=return_mo, cache_enabled=cache_enabled) is None:
            return False
        return True
