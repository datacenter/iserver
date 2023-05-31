class PolicyInterfaceMcpOutput():
    def __init__(self):
        pass

    def print_policy_interface_mcp(self, info):
        self.print_policy_interface_mcp_properties(
            info
        )

        self.print_policy_interface_mcp_interfaces(
            info['l1RsMcpIfPolCons']
        )

        self.print_policy_interface_mcp_references(
            info['relnFrom']
        )

    def print_policy_interface_mcp_properties(self, info):
        order = [
            'name',
            'tf',
            'adminSt'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State'
        ]

        self.my_output.dictionary(
            info,
            title='CDP Policy Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_policy_interface_mcp_interfaces(self, info):
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

    def print_policy_interface_mcp_references(self, info):
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

    def print_policies_interface_mcp_summary(self, info):
        order = [
            'name',
            'tfTick',
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

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policies_interface_mcp_usage(self, info):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'nodeInterfaces.pod_node_name',
            'nodeInterfaces.interfaces',
            'relnFrom.policyType',
            'relnFrom.policyName'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
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

    def print_policies_interface_mcp_interfaces(self, info):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'l1RsMcpIfPolCons.pod_node_name',
            'l1RsMcpIfPolCons.interfaceId'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Node',
            'Interface'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['l1RsMcpIfPolCons']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
