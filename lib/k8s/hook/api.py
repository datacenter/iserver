class K8sHookApi():
    def __init__(self):
        self.hook_mo = None
        self.hook_namespace_mo = {}

    def get_hook_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.hook_mo,
            self.hook_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.hook_mo, self.hook_namespace_mo = self.get_namespaced_resources(
            'Hook', 
            'forklift.konveyor.io/v1beta1', 
            self.hook_mo,
            self.hook_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response