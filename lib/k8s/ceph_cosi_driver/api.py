class K8sCephCosiDriverApi():
    def __init__(self):
        self.ceph_cosi_driver_mo = None
        self.ceph_cosi_driver_namespace_mo = {}

    def get_ceph_cosi_driver_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.ceph_cosi_driver_mo,
            self.ceph_cosi_driver_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.ceph_cosi_driver_mo, self.ceph_cosi_driver_namespace_mo = self.get_namespaced_resources(
            'CephCOSIDriver', 
            'ceph.rook.io/v1', 
            self.ceph_cosi_driver_mo,
            self.ceph_cosi_driver_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response