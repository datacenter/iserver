class PolicyInterfaceL2Output():
    def __init__(self):
        pass

    def print_policy_interface_l2(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'qinq',
            'vepa',
            'vlanScopeT',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'QinQ',
            '802.1Qbg',
            'VLAN Scope',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'L2 Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_l2(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'qinq',
            'vepa',
            'vlanScopeT'
        ]

        headers = [
            'Policy Name',
            'TF',
            'QinQ',
            '802.1Qbg',
            'VLAN Scope'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_l2_node(self, info):
        order = [
            'policy.name',
            'policy.qinq',
            'policy.vepa',
            'policy.vlanScopeT'
        ]

        headers = [
            'L2 Policy Name',
            'QinQ',
            '802.1Qbg',
            'VLAN Scope'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
