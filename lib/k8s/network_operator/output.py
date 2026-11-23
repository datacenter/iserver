class K8sNetworkOperatorOutput():
    def __init__(self):
        pass

    def print_network_operators(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Network Operator', 'title'],
                ['CNI', 'cni'],
                ['Condition', 'conditionT'],
                ['CIDR', 'cidrT'],
                ['Settings', 'settingsT']
            ]
        )
