class PolicyInterfacePfcOutput():
    def __init__(self):
        pass

    def print_policy_interface_pfc(self, info, verbose=False):
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
            'State',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'Priority Flow Control Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_pfc(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'adminSt'
        ]

        headers = [
            'Policy Name',
            'TF',
            'State'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_pfc_node(self, info):
        order = [
            'policy.name',
            'policy.adminSt'
        ]

        headers = [
            'Priority Flow Control Policy Name',
            'State'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
