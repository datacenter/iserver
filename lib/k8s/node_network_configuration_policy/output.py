class K8sNodeNetworkConfigurationPolicyOutput():
    def __init__(self):
        pass

    def print_node_network_configuration_policys_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Node Network Configuration Policy', 'name'],
                ['Status', 'status'],
                ['Reason', 'reason']
            ]
        )

