class K8sCdiApi():
    def __init__(self):
        self.cdi_mo = None

    def get_cdi_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.cdi_mo
        )
        if cache_hit:
            return response

        response, self.cdi_mo = self.get_resources(
            'CDI', 
            'cdi.kubevirt.io/v1beta1', 
            self.cdi_mo,
            name=name
        )

        return response