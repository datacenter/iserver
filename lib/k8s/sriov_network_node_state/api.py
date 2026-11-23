class K8sSriovNetworkNodeStateApi():
    def __init__(self):
        self.sriov_network_node_state_mo = None
        self.sriov_network_node_state_namespace_mo = {}

    def get_sriov_network_node_state_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.sriov_network_node_state_mo,
            self.sriov_network_node_state_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.sriov_network_node_state_mo, self.sriov_network_node_state_namespace_mo = self.get_namespaced_resources(
            'SriovNetworkNodeState', 
            'sriovnetwork.openshift.io/v1', 
            self.sriov_network_node_state_mo,
            self.sriov_network_node_state_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response