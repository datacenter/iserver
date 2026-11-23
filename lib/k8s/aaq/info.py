class K8sAaqInfo():
    def __init__(self):
        self.aaq = None

    def get_aaqs(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'aaq', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_aaq(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'aaq', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_aaq(self, name, cache_enabled=True, optimized=True):
        if self.get_aaq(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True