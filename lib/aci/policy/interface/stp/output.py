class PolicyInterfaceStpOutput():
    def __init__(self):
        pass

    def print_policy_interface_stp(self, info):
        self.print_policy_interface_stp_properties(
            info
        )

        self.print_policy_interface_stp_interfaces(
            info['l1RsStpIfPolCons']
        )

        self.print_policy_interface_stp_references(
            info['relnFrom']
        )

    def print_policy_interface_stp_properties(self, info):
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

        self.my_output.dictionary(
            info,
            title='CDP Policy Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_policy_interface_stp_interfaces(self, info):
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

    def print_policy_interface_stp_references(self, info):
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

    def print_policies_interface_stp_summary(self, info):
        order = [
            'name',
            'tfTick',
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

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policies_interface_stp_usage(self, info):
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

    def print_policies_interface_stp_interfaces(self, info):
        order = [
            'name',
            'l1RsStpIfPolCons.pod_node_name',
            'l1RsStpIfPolCons.interfaceId'
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
                ['l1RsStpIfPolCons']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
