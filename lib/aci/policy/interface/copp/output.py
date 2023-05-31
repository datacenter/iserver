class PolicyInterfaceCoppOutput():
    def __init__(self):
        pass

    def print_policy_interface_copp(self, info):
        self.print_policy_interface_copp_properties(
            info
        )

        self.print_policy_interface_copp_interfaces(
            info['l1RsCoppIfPolCons']
        )

        self.print_policy_interface_copp_references(
            info['relnFrom']
        )

    def print_policy_interface_copp_properties(self, info):
        order = [
            'name',
            'tf',
            'protocolCount'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Protocol Count'
        ]

        self.my_output.dictionary(
            info,
            title='CoPP Policy Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_policy_interface_copp_interfaces(self, info):
        if info is None or len(info) == 0:
            return

        order = [
            'pod_node_name',
            'interfaceId'
        ]

        headers = [
            'Node',
            'Interface'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policy_interface_copp_references(self, info):
        if info is None or len(info) == 0:
            return

        order = [
            'policyName',
            'policyType',
            'tCl'
        ]

        headers = [
            'Policy Name',
            'Policy Type',
            'Policy Class'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policies_interface_copp_summary(self, info):
        order = [
            'name',
            'tfTick',
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

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policies_interface_copp_usage(self, info):
        order = [
            'name',
            'tfTick',
            'protocolCount',
            'nodeInterfaces.pod_node_name',
            'nodeInterfaces.interfaces',
            'relnFrom.policyType',
            'relnFrom.policyName'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Protocols',
            'Node',
            'Interface Count',
            'Ref Policy Type',
            'Ref Policy Name'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['nodeInterfaces', 'relnFrom']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policies_interface_copp_interfaces(self, info):
        order = [
            'name',
            'tfTick',
            'protocolCount',
            'l1RsCoppIfPolCons.pod_node_name',
            'l1RsCoppIfPolCons.interfaceId'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Protocols',
            'Node',
            'Interface'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['l1RsCoppIfPolCons']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
