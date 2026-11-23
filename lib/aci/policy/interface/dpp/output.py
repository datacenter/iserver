class PolicyInterfaceDppOutput():
    def __init__(self):
        pass

    def print_policy_interface_dpp(self, info):
        self.print_policy_interface_dpp_properties(
            info
        )

        self.print_policy_interface_dpp_interfaces(
            info['l1RsQosEgressDppIfPolCons']
        )

        self.print_policy_interface_dpp_references(
            info['relnFrom']
        )

    def print_policy_interface_dpp_properties(self, info):
        order = [
            'name',
            'tf',
            'adminSt',
            'type',
            'conformAction',
            'violateAction',
            'sharingMode',
            'burstT',
            'beT',
            'rateT',
            'pirT',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Type',
            'Conform Action',
            'Violate Action',
            'Sharing Mode',
            'Burst',
            'Excessive Burst',
            'Rate',
            'Peak Rate',
            'Interfaces',
            'Ref Policies'
        ]

        self.my_output.dictionary(
            info,
            title='Data Plane Policing Policy Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_policy_interface_dpp_interfaces(self, info):
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

    def print_policy_interface_dpp_references(self, info):
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

    def print_policies_interface_dpp_summary(self, info):
        order = [
            'name',
            'tfTick',
            'adminSt',
            'type',
            'conformAction',
            'violateAction',
            'sharingMode',
            'burstT',
            'beT',
            'rateT',
            'pirT',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Admin State',
            'Type',
            'Conform Action',
            'Violate Action',
            'Sharing Mode',
            'Burst',
            'Excessive Burst',
            'Rate',
            'Peak Rate',
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

    def print_policies_interface_dpp_usage(self, info):
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

    def print_policies_interface_dpp_interfaces(self, info):
        order = [
            'name',
            'l1RsQosEgressDppIfPolCons.pod_node_name',
            'l1RsQosEgressDppIfPolCons.interfaceId'
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
                ['l1RsQosEgressDppIfPolCons']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
