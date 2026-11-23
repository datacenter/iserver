class K8sCephObjectStoreApi():
    def __init__(self):
        self.ceph_object_store_mo = None
        self.ceph_object_store_namespace_mo = {}

    def get_ceph_object_store_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.ceph_object_store_mo,
            self.ceph_object_store_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.ceph_object_store_mo, self.ceph_object_store_namespace_mo = self.get_namespaced_resources(
            'CephObjectStore', 
            'ceph.rook.io/v1', 
            self.ceph_object_store_mo,
            self.ceph_object_store_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response