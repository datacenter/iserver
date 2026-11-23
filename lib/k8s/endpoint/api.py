class K8sEndpointApi():
    def __init__(self):
        self.endpoint_mo = None
        self.endpoint_namespace_mo = {}

    def get_endpoint_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.endpoint_mo,
            self.endpoint_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.endpoint_mo, self.endpoint_namespace_mo = self.get_namespaced_resources(
            'Endpoints', 
            'v1', 
            self.endpoint_mo,
            self.endpoint_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response