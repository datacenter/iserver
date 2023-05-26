class PolicyInterfaceLinkLevelFcOutput():
    def __init__(self):
        pass

    def print_policy_interface_link_level_fc(self, info, verbose=False):
        order = [
            'name',
            'tf',
            'llfcRcvAdminSt',
            'llfcSendAdminSt',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Receive Flow Control',
            'Send Flow Control',
            'Interfaces',
            'Ref Policies'
        ]

        self.print_policy_interface(
            info,
            'Link Level Flow Control Policy Properties',
            order,
            headers,
            verbose
        )

    def print_policies_interface_link_level_fc(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'llfcRcvAdminSt',
            'llfcSendAdminSt'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Receive Flow Control',
            'Send Flow Control'
        ]

        self.print_policies_interface(
            info,
            order,
            headers,
            verbose
        )

    def print_policy_interface_link_level_fc_node(self, info):
        order = [
            'policy.name',
            'policy.llfcRcvAdminSt',
            'policy.llfcSendAdminSt'
        ]

        headers = [
            'Link Level Policy Name',
            'Receive Flow Control',
            'Send Flow Control'
        ]

        self.print_policy_interface_node(
            info,
            order,
            headers
        )
