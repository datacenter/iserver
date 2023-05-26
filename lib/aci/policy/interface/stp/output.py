class PolicyInterfaceStpOutput():
    def __init__(self):
        pass

    def print_policy_interface_stp(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'bpduFilter',
            'bpduGuard',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'BPDU Filter',
            'BPDU Guard',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'STP Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_stp(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'bpduFilterTick',
            'bpduGuardTick'
        ]

        headers = [
            'Policy Name',
            'TF',
            'BPDU Filter',
            'BPDU Guard'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_stp_node(self, info):
        order = [
            'policy.name',
            'policy.bpduFilterTick',
            'policy.bpduGuardTick'
        ]

        headers = [
            'STP Policy Name',
            'BPDU Filter',
            'BPDU Guard'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
