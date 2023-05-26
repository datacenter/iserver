class PolicyInterfaceAuthOutput():
    def __init__(self):
        pass

    def print_policy_interface_auth(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'adminSt',
            'hostMode',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Host Mode',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            '802.1x Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_auth(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'hostMode'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Host Mode'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_auth_node(self, info):
        order = [
            'policy.name',
            'policy.adminSt',
            'policy.hostMode'
        ]

        headers = [
            '802.1x Policy Name',
            '802.1x Admin State',
            '802.1x Host Mode'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
