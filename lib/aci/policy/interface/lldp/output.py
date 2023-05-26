class PolicyInterfaceLldpOutput():
    def __init__(self):
        pass

    def print_policy_interface_lldp(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'adminRxSt',
            'adminTxSt',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Receive State',
            'Transmit State',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'LLDP Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_lldp(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'adminRxSt',
            'adminTxSt'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Receive State',
            'Transmit State'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_lldp_node(self, info):
        order = [
            'policy.name',
            'policy.adminRxSt',
            'policy.adminTxSt'
        ]

        headers = [
            'LLDP Policy Name',
            'Receive State',
            'Transmit State'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
