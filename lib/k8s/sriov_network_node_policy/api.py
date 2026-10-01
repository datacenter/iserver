class K8sSriovNetworkNodePolicyApi():
    def __init__(self):
        self.sriov_network_node_policy_mo = None
        self.sriov_network_node_policy_namespace_mo = {}

    def get_sriov_network_node_policy_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.sriov_network_node_policy_mo,
            self.sriov_network_node_policy_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.sriov_network_node_policy_mo, self.sriov_network_node_policy_namespace_mo = self.get_namespaced_resources(
            'SriovNetworkNodePolicy', 
            'sriovnetwork.openshift.io/v1', 
            self.sriov_network_node_policy_mo,
            self.sriov_network_node_policy_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response