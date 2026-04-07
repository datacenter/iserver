class K8sNetworkOperatorApi():
    def __init__(self):
        self.network_operator_mo = None

    def get_network_operator_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.network_operator_mo
        )
        if cache_hit:
            return response

        response, self.network_operator_mo = self.get_resources(
            'Network', 
            'operator.openshift.io/v1', 
            self.network_operator_mo,
            name=name
        )

        return response