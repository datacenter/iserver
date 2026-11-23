class K8sNodeNetworkStateApi():
    def __init__(self):
        self.node_network_state_mo = None

    def get_node_network_state_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.node_network_state_mo
        )
        if cache_hit:
            return response

        response, self.node_network_state_mo = self.get_resources(
            'NodeNetworkState', 
            'nmstate.io/v1beta1', 
            self.node_network_state_mo,
            name=name
        )

        return response
