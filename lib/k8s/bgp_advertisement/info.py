class K8sBgpAdvertisementInfo():
    def __init__(self):
        self.bgp_advertisement = None

    def get_bgp_advertisement_info(self, managed_object):
        return self.get_base_info(managed_object)

    def get_bgp_advertisements(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'bgp_advertisement', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_bgp_advertisement(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_bgp_advertisement(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_bgp_advertisement(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'bgp_advertisement', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
