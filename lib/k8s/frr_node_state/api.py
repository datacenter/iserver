class K8sFrrNodeStateApi():
    def __init__(self):
        self.frr_node_state_mo = None

    def get_frr_node_state_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.frr_node_state_mo
        )
        if cache_hit:
            return response

        response, self.frr_node_state_mo = self.get_resources(
            'FRRNodeState', 
            'frrk8s.metallb.io/v1beta1', 
            self.frr_node_state_mo,
            name=name
        )

        return response
    