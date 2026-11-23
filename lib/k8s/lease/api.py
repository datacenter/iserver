class K8sLeaseApi():
    def __init__(self):
        self.lease_mo = None
        self.lease_namespace_mo = {}

            
    def get_lease_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.lease_mo,
            self.lease_namespace_mo
        )
        if cache_hit:
            return response

        response, self.lease_mo, self.lease_namespace_mo = self.get_namespaced_resources(
            'Lease', 
            'coordination.k8s.io/v1', 
            self.lease_mo,
            self.lease_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
