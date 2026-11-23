class K8sNetworkAddonsConfigApi():
    def __init__(self):
        self.network_addons_config_mo = None

    def get_network_addons_config_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.network_addons_config_mo
        )
        if cache_hit:
            return response

        response, self.network_addons_config_mo = self.get_resources(
            'NetworkAddonsConfig', 
            'networkaddonsoperator.network.kubevirt.io/v1', 
            self.network_addons_config_mo,
            name=name
        )

        return response