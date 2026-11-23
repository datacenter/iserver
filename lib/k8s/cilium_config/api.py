class K8sCiliumConfigApi():
    def __init__(self):
        self.cilium_config_mo = None

    def get_cilium_config_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.isovalent_bgp_cluster_config_mo
        )
        if cache_hit:
            return response

        response, self.isovalent_bgp_cluster_config_mo = self.get_resources(
            'CiliumConfig', 
            'cilium.io/v1alpha1', 
            self.isovalent_bgp_cluster_config_mo,
            name=name
        )

        return response