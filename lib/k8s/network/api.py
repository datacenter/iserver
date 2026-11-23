class K8sNetworkApi():
    def __init__(self):
        self.network_mo = None
        
    def get_network_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.network_mo
        )
        if cache_hit:
            return response

        response, self.network_mo = self.get_resources(
            'Network', 
            'config.openshift.io/v1', 
            self.network_mo,
            name=name
        )

        return response