class PolicyInterfaceCoppOutput():
    def __init__(self):
        pass

    def print_policy_interface_copp(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'protocolCount',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Protocols',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'CoPP Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_copp(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'protocolCount'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Protocols'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_copp_node(self, info):
        order = [
            'policy.name',
            'policy.protocolCount'
        ]

        headers = [
            'CoPP Policy Name',
            'CoPP Policy Protocols'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
