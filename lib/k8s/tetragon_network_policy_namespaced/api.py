class K8sTetragonNetworkPolicyNamespacedApi():
    def __init__(self):
        self.tetragon_network_policy_namespaced_mo = None
        self.tetragon_network_policy_namespaced_namespace_mo = {}

    def get_tetragon_network_policy_namespaced_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.tetragon_network_policy_namespaced_mo,
            self.tetragon_network_policy_namespaced_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.tetragon_network_policy_namespaced_mo, self.tetragon_network_policy_namespaced_namespace_mo = self.get_namespaced_resources(
            'TetragonNetworkPolicyNamespaced', 
            'cilium.io/v1alpha1', 
            self.tetragon_network_policy_namespaced_mo,
            self.tetragon_network_policy_namespaced_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response