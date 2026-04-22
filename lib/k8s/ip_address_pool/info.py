class K8sIpAddressPoolInfo():
    def __init__(self):
        self.ip_address_pool = None

    def get_ip_address_pool_info(self, managed_object):
        info = self.get_base_info(managed_object)
        info['addr'] = self.get(managed_object, 'spec:addresses')
        return info

    def get_ip_address_pools(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'ip_address_pool', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_ip_address_pool(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_ip_address_pool(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_ip_address_pool(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'ip_address_pool', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
