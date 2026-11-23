class K8sCdiConfigApi():
    def __init__(self):
        self.cdi_config_mo = None

    def get_cdi_config_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.cdi_config_mo
        )
        if cache_hit:
            return response

        response, self.cdi_config_mo = self.get_resources(
            'CDIConfig', 
            'cdi.kubevirt.io/v1beta1', 
            self.cdi_config_mo,
            name=name
        )

        return response