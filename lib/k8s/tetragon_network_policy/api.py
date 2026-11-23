class K8sTetragonNetworkPolicyApi():
    def __init__(self):
        self.tetragon_network_policy_mo = None

    def get_tetragon_network_policy_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.tetragon_network_policy_mo
        )
        if cache_hit:
            return response

        response, self.tetragon_network_policy_mo = self.get_resources(
            'TetragonNetworkPolicy', 
            'cilium.io/v1alpha1', 
            self.tetragon_network_policy_mo,
            name=name
        )

        return response