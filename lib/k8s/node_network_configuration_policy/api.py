class K8sNodeNetworkConfigurationPolicyApi():
    def __init__(self):
        self.node_network_configuration_policy_mo = None

    def get_node_network_configuration_policy_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.node_network_configuration_policy_mo
        )
        if cache_hit:
            return response

        response, self.node_network_configuration_policy_mo = self.get_resources(
            'NodeNetworkConfigurationPolicy', 
            'nmstate.io/v1', 
            self.node_network_configuration_policy_mo,
            name=name
        )

        return response  

    def delete_node_network_configuration_policy_mo(self, name):
        return self.delete_resource('NodeNetworkConfigurationPolicy', 'nmstate.io/v1', name)
    