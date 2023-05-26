class PolicyInterfaceStormControlOutput():
    def __init__(self):
        pass

    def print_policy_interface_storm_control(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'packetType.type',
            'packetType.rate',
            'packetType.burstRate',
            'packetType.ratePps',
            'packetType.burstPps',
            'packetType.stormCtrlAction',
            'packetType.stormCtrlSoakInstCount'
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
            'Instances'

        ]

        self.my_output.my_table(
            self.my_output.expand_list(
                [info],
                order,
                'packetType'
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

        self.print_policy_interface_reln_from(info['relnFrom'])
        self.print_policy_interface_node_interfaces(info['nodeInterfaces'], verbose)

    def print_policies_interface_storm_control(self, info, verbose=False):
        order = [
            'name',
            'tfTick',
            'packetType.type',
            'packetType.rate',
            'packetType.burstRate',
            'packetType.ratePps',
            'packetType.burstPps',
            'packetType.stormCtrlAction',
            'packetType.stormCtrlSoakInstCount'
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
            'Instances'

        ]

        if not verbose:
            order.append('interfaces')
            headers.append('Interfaces')
            order.append('references')
            headers.append('Ref Policies')

            self.my_output.my_table(
                self.my_output.expand_list(
                    info,
                    order,
                    'packetType'
                ),
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )

        if verbose:
            order.append('nodeInterfaces.node_name')
            headers.append('Node Name')
            order.append('nodeInterfaces.interfacesCount')
            headers.append('Interfaces')
            order.append('relnFrom.policyType')
            headers.append('Ref Policy Type')
            order.append('relnFrom.policyName')
            headers.append('Ref Policy Name')

            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    ['packetType', 'relnFrom', 'nodeInterfaces']
                ),
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )

    def print_policy_interface_storm_control_node(self, info):
        for item in info:
            if 'packetType' in item['policy']:
                item['packetType'] = item['policy']['packetType']
            else:
                item['packetType'] = []

        order = [
            'policy.name',
            'packetType.type',
            'packetType.rate',
            'packetType.burstRate',
            'packetType.ratePps',
            'packetType.burstPps',
            'packetType.stormCtrlAction',
            'packetType.stormCtrlSoakInstCount'
        ]

        headers = [
            'Storm Control Policy Name',
            'Packet Type',
            'Rate [%]',
            'Burst Rate [%]',
            'Rate [pps]',
            'Burst Rate [pps]',
            'Storm Control Action',
            'Instances'
        ]

        self.print_policy_interface_node(
            self.my_output.expand_list(
                info,
                order,
                'packetType'
            ),
            order,
            headers
        )
