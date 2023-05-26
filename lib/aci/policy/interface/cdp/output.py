class PolicyInterfaceCdpOutput():
    def __init__(self):
        pass

    def print_policy_interface_cdp(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'adminSt',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'CDP Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_cdp(self, info, verbose=False):
        order = [
            'name',
            'adminSt',
            'tfTick'
        ]

        headers = [
            'Policy Name',
            'Admin State',
            'TF'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_cdp_node(self, info):
        order = [
            'policy.name',
            'policy.adminSt'
        ]

        headers = [
            'CDP Policy Name',
            'CDP Admin State'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
