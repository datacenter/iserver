class K8sEgressRouterApi():
    def __init__(self):
        self.egress_router_mo = None
        self.egress_router_namespace_mo = {}

    def get_egress_router_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.egress_router_mo,
            self.egress_router_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.egress_router_mo, self.egress_router_namespace_mo = self.get_namespaced_resources(
            'EgressRouter', 
            'network.operator.openshift.io/v1', 
            self.egress_router_mo,
            self.egress_router_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response