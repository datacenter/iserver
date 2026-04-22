class K8sLeaseInfo():
    def __init__(self):
        self.lease = None

    def get_lease_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        info['identity'] = self.get(managed_object, 'spec:holderIdentity')
        return info
    
    def get_leases(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'lease', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_lease(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_lease(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_lease(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        info = self.get_info(
            'lease', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
        return info