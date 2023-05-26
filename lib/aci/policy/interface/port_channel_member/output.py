class PolicyInterfacePortChannelMemberOutput():
    def __init__(self):
        pass

    def print_policy_interface_port_channel_member(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'prio',
            'txRate',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Priority',
            'Transmit Rate',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'Port Channel Member Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_port_channel_member(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'prio',
            'txRate'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Priority',
            'Transmit Rate'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_port_channel_member_node(self, info):
        order = [
            'policy.name',
            'policy.prio',
            'policy.txRate'
        ]

        headers = [
            'Port Channel Member Policy Name',
            'Priority',
            'Transmit Rate',
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
