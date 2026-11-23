class PolicyInterfaceLldpOutput():
    def __init__(self):
        pass

    def print_policy_interface_lldp(self, info):
        self.print_policy_interface_lldp_properties(
            info
        )

        self.print_policy_interface_lldp_interfaces(
            info['l1RsLldpIfPolCons']
        )

        self.print_policy_interface_lldp_references(
            info['relnFrom']
        )

    def print_policy_interface_lldp_properties(self, info):
        order = [
            'name',
            'tf',
            'adminRxSt',
            'adminTxSt',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Receive State',
            'Transmit State',
            'Interfaces',
            'Ref Policies'
        ]

        self.my_output.dictionary(
            info,
            title='LLDP Policy Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_policy_interface_lldp_interfaces(self, info):
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

    def print_policy_interface_lldp_references(self, info):
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

    def print_policies_interface_lldp_summary(self, info):
        order = [
            'name',
            'tfTick',
            'adminRxSt',
            'adminTxSt',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Receive State',
            'Transmit State',
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

    def print_policies_interface_lldp_usage(self, info):
        order = [
            'name',
            'nodeInterfaces.pod_node_name',
            'nodeInterfaces.interfaces',
            'relnFrom.policyType',
            'relnFrom.policyName'
        ]

        headers = [
            'Policy Name',
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

    def print_policies_interface_lldp_interfaces(self, info):
        order = [
            'name',
            'l1RsLldpIfPolCons.pod_node_name',
            'l1RsLldpIfPolCons.interfaceId'
        ]

        headers = [
            'Policy Name',
            'Node',
            'Interface'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['l1RsLldpIfPolCons']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
