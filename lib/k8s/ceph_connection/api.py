class K8sCephConnectionApi():
    def __init__(self):
        self.ceph_connection_mo = None
        self.ceph_connection_namespace_mo = {}

    def get_ceph_connection_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.ceph_connection_mo,
            self.ceph_connection_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.ceph_connection_mo, self.ceph_connection_namespace_mo = self.get_namespaced_resources(
            'CephConnection', 
            'csi.ceph.io/v1alpha1', 
            self.ceph_connection_mo,
            self.ceph_connection_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response