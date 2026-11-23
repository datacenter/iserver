class K8sSspApi():
    def __init__(self):
        self.ssp_mo = None
        self.ssp_namespace_mo = {}

    def get_ssp_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.ssp_mo,
            self.ssp_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.ssp_mo, self.ssp_namespace_mo = self.get_namespaced_resources(
            'SSP', 
            'ssp.kubevirt.io/v1beta3', 
            self.ssp_mo,
            self.ssp_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response