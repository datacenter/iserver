class K8sBareMetalHostApi():
    def __init__(self):
        self.bare_metal_host_mo = None
        self.bare_metal_host_namespace_mo = {}

    def get_bare_metal_host_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.bare_metal_host_mo,
            self.bare_metal_host_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.bare_metal_host_mo, self.bare_metal_host_namespace_mo = self.get_namespaced_resources(
            'BareMetalHost', 
            'metal3.io/v1alpha1', 
            self.bare_metal_host_mo,
            self.bare_metal_host_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
