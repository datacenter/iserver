class PolicyInterfaceStormControlOutput():
    def __init__(self):
        pass

    def print_policy_interface_storm_control(self, info):
        self.print_policy_interface_storm_control_properties(
            info
        )

        self.print_policy_interface_storm_control_interfaces(
            info['l1RsStormctrlIfPolCons']
        )

        self.print_policy_interface_storm_control_references(
            info['relnFrom']
        )

    def print_policy_interface_storm_control_properties(self, info):
        order = [
            'name',
            'tf',
            'packetType.type',
            'packetType.rate',
            'packetType.burstRate',
            'packetType.ratePps',
            'packetType.burstPps',
            'packetType.stormCtrlAction',
            'packetType.stormCtrlSoakInstCount',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Packet Type',
            'Rate [%]',
            'Burst Rate [%]',
            'Rate [pps]',
            'Burst Rate [pps]',
            'Storm Control Action',
            'Storm Soak',
            'Instances',
            'Ref Policies'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                [info],
                order,
                ['packetType']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policy_interface_storm_control_interfaces(self, info):
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

    def print_policy_interface_storm_control_references(self, info):
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

    def print_policies_interface_storm_control_summary(self, info):
        order = [
            'name',
            'tf',
            'packetType.type',
            'packetType.rate',
            'packetType.burstRate',
            'packetType.ratePps',
            'packetType.burstPps',
            'packetType.stormCtrlAction',
            'packetType.stormCtrlSoakInstCount',
            'interfaces',
            'references'
        ]

        headers = [
            'Policy Name',
            'TF',
            'Packet Type',
            'Rate [%]',
            'Burst Rate [%]',
            'Rate [pps]',
            'Burst Rate [pps]',
            'Storm Control Action',
            'Storm Soak',
            'Instances',
            'Ref Policies'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['packetType']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policies_interface_storm_control_usage(self, info):
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

    def print_policies_interface_storm_control_interfaces(self, info):
        order = [
            'name',
            'l1RsStormctrlIfPolCons.pod_node_name',
            'l1RsStormctrlIfPolCons.interfaceId'
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
                ['l1RsStormctrlIfPolCons']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
