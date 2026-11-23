class K8sNodeNetworkConfigurationEnactmentOutput():
    def __init__(self):
        pass

    def print_node_network_configuration_enactments_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Node Network Configuration Enactment', 'name'],
                ['Status', 'status']
            ]
        )