class PolicyInterfaceAuthOutput():
    def __init__(self):
        pass

    def print_policy_interface_auth(self, info):
        self.print_policy_interface_auth_properties(
            info
        )

        self.print_policy_interface_auth_interfaces(
            info['l1RsL2PortAuthCons']
        )

        self.print_policy_interface_auth_references(
            info['relnFrom']
        )

    def print_policy_interface_auth_properties(self, info):
        order = [
            'name',
            'tf',
            'adminSt',
            'hostMode'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Host Mode'
        ]

        self.my_output.dictionary(
            info,
            title='802.1x Policy Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_policy_interface_auth_interfaces(self, info):
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

    def print_policy_interface_auth_references(self, info):
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

    def print_policies_interface_auth_summary(self, info):
        order = [
            'name',
            'tfTick',
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

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policies_interface_auth_usage(self, info):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'hostMode',
            'nodeInterfaces.pod_node_name',
            'nodeInterfaces.interfaces',
            'relnFrom.policyType',
            'relnFrom.policyName'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Host Mode',
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

    def print_policies_interface_auth_interfaces(self, info):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'hostMode',
            'l1RsL2PortAuthCons.pod_node_name',
            'l1RsL2PortAuthCons.interfaceId'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Host Mode',
            'Node',
            'Interface'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['l1RsL2PortAuthCons']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
