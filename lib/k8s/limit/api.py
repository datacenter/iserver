class K8sLimitApi():
    def __init__(self):
        self.limit_mo = None
        self.limit_namespace_mo = {}

    def get_limit_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.limit_mo,
            self.limit_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.limit_mo, self.limit_namespace_mo = self.get_namespaced_resources(
            'LimitRange', 
            'v1', 
            self.limit_mo,
            self.limit_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response