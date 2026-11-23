class K8sTunedApi():
    def __init__(self):
        self.tuned_mo = None
        self.tuned_namespace_mo = {}

    def get_tuned_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.tuned_mo,
            self.tuned_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.tuned_mo, self.tuned_namespace_mo = self.get_namespaced_resources(
            'Tuned', 
            'tuned.openshift.io/v1', 
            self.tuned_mo,
            self.tuned_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response