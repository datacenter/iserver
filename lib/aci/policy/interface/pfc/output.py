class PolicyInterfacePfcOutput():
    def __init__(self):
        pass

    def print_policy_interface_pfc(self, info):
        self.print_policy_interface_pfc_properties(
            info
        )

        self.print_policy_interface_pfc_interfaces(
            info['l1RsQosPfcIfPolCons']
        )

        self.print_policy_interface_pfc_references(
            info['relnFrom']
        )

    def print_policy_interface_pfc_properties(self, info):
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
            title='Priority Flow Control Policy Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_policy_interface_pfc_interfaces(self, info):
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

    def print_policy_interface_pfc_references(self, info):
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

    def print_policies_interface_pfc_summary(self, info):
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

    def print_policies_interface_pfc_usage(self, info):
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

    def print_policies_interface_pfc_interfaces(self, info):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'l1RsQosPfcIfPolCons.pod_node_name',
            'l1RsQosPfcIfPolCons.interfaceId'
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
                ['l1RsQosPfcIfPolCons']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
