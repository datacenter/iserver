class K8sCephBlockPoolRadosNamespaceApi():
    def __init__(self):
        self.ceph_block_pool_rados_namespace_mo = None
        self.ceph_block_pool_rados_namespace_namespace_mo = {}

    def get_ceph_block_pool_rados_namespace_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.ceph_block_pool_rados_namespace_mo,
            self.ceph_block_pool_rados_namespace_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.ceph_block_pool_rados_namespace_mo, self.ceph_block_pool_rados_namespace_namespace_mo = self.get_namespaced_resources(
            'CephBlockPoolRadosNamespace', 
            'ceph.rook.io/v1', 
            self.ceph_block_pool_rados_namespace_mo,
            self.ceph_block_pool_rados_namespace_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response