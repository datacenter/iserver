class K8sNodeNetworkConfigurationEnactmentApi():
    def __init__(self):
        self.node_network_configuration_enactment_mo = None

    def get_node_network_configuration_enactment_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.node_network_configuration_enactment_mo
        )
        if cache_hit:
            return response

        response, self.node_network_configuration_enactment_mo = self.get_resources(
            'NodeNetworkConfigurationEnactment', 
            'nmstate.io/v1beta1', 
            self.node_network_configuration_enactment_mo,
            name=name
        )

        return response

    def delete_node_network_configuration_enactment_mo(self, name):
        success, _ = self.delete_resource('NodeNetworkConfigurationEnactment', 'nmstate.io/v1beta1', name)
        return success  