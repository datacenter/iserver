class K8sCephConnectionInfo():
    def __init__(self):
        self.ceph_connection = None

    def get_ceph_connection_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_ceph_connections(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'ceph_connection', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_ceph_connection(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'ceph_connection', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_ceph_connection(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_ceph_connection(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_ceph_connection(self, cache_enabled=True):
        infos = self.get_ceph_connections(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True