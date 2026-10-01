class K8sHostApi():
    def __init__(self):
        self.host_mo = None
        self.host_namespace_mo = {}

    def get_host_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.host_mo,
            self.host_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.host_mo, self.host_namespace_mo = self.get_namespaced_resources(
            'Host', 
            'forklift.konveyor.io/v1beta1', 
            self.host_mo,
            self.host_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response