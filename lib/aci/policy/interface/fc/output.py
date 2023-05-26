class PolicyInterfaceFcOutput():
    def __init__(self):
        pass

    def print_policy_interface_fc(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'portMode',
            'trunkMode',
            'speed',
            'fillPattern',
            'rxBBCredit',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Port Mode',
            'Trunk Mode',
            'Speed',
            'Fill Pattern',
            'Receive Buffer Credit',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'FC Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_fc(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'portMode',
            'trunkMode',
            'speed',
            'fillPattern',
            'rxBBCredit'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Port Mode',
            'Trunk Mode',
            'Speed',
            'Fill Pattern',
            'Receive Buffer Credit'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_fc_node(self, info):
        order = [
            'policy.name',
            'policy.portMode',
            'policy.trunkMode',
            'policy.speed',
            'policy.fillPattern',
            'policy.rxBBCredit'
        ]

        headers = [
            'FC Policy Name',
            'Port Mode',
            'Trunk Mode',
            'Speed',
            'Fill Pattern',
            'Receive Buffer Credit',
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
