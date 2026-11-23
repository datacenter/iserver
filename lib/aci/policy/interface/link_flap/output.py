class PolicyInterfaceLinkFlapOutput():
    def __init__(self):
        pass

    def print_policy_interface_link_flap(self, info):
        self.print_policy_interface_link_flap_properties(
            info
        )

        self.print_policy_interface_link_flap_interfaces(
            info['l1RsLinkFlapPolCons']
        )

        self.print_policy_interface_link_flap_references(
            info['relnFrom']
        )

    def print_policy_interface_link_flap_properties(self, info):
        order = [
            'name',
            'tf',
            'linkFlapErrorMax',
            'linkFlapErrorSeconds',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Max Flaps',
            'Max Flaps Duration [sec]',
            'Interfaces',
            'Ref Policies'
        ]

        self.my_output.dictionary(
            info,
            title='Link Flap Policy Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_policy_interface_link_flap_interfaces(self, info):
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

    def print_policy_interface_link_flap_references(self, info):
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

    def print_policies_interface_link_flap_summary(self, info):
        order = [
            'name',
            'tfTick',
            'linkFlapErrorMax',
            'linkFlapErrorSeconds',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Max Flaps',
            'Max Flaps Duration [sec]',
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

    def print_policies_interface_link_flap_usage(self, info):
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

    def print_policies_interface_link_flap_interfaces(self, info):
        order = [
            'name',
            'l1RsLinkFlapPolCons.pod_node_name',
            'l1RsLinkFlapPolCons.interfaceId'
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
                ['l1RsLinkFlapPolCons']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
