class PolicyInterfacePortSecurityOutput():
    def __init__(self):
        pass

    def print_policy_interface_port_security(self, info):
        self.print_policy_interface_port_security_properties(
            info
        )

        self.print_policy_interface_port_security_interfaces(
            info['l1RsL2PortSecurityCons']
        )

        self.print_policy_interface_port_security_references(
            info['relnFrom']
        )

    def print_policy_interface_port_security_properties(self, info):
        order = [
            'name',
            'tf',
            'timeout',
            'maximum',
            'violation',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Timeout',
            'Maximum Endpoints',
            'Violation Action',
            'Interfaces',
            'Ref Policies'
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

    def print_policy_interface_port_security_interfaces(self, info):
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

    def print_policy_interface_port_security_references(self, info):
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

    def print_policies_interface_port_security_summary(self, info):
        order = [
            'name',
            'tfTick',
            'timeout',
            'maximum',
            'violation',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Timeout',
            'Maximum Endpoints',
            'Violation Action',
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

    def print_policies_interface_port_security_usage(self, info):
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

    def print_policies_interface_port_security_interfaces(self, info):
        order = [
            'name',
            'l1RsL2PortSecurityCons.pod_node_name',
            'l1RsL2PortSecurityCons.interfaceId'
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
                ['l1RsL2PortSecurityCons']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
