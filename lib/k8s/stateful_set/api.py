class K8sStatefulSetApi():
    def __init__(self):
        self.stateful_set_mo = None
        self.stateful_set_namespace_mo = {}

    def get_stateful_set_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.stateful_set_mo,
            self.stateful_set_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.stateful_set_mo, self.stateful_set_namespace_mo = self.get_namespaced_resources(
            'StatefulSet', 
            'apps/v1', 
            self.stateful_set_mo,
            self.stateful_set_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response