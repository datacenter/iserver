class InterfaceSviOutput():
    def __init__(self):
        pass

    def print_interfaces_svi_state(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default('No svi interfaces')
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'sviIf.id',
            'sviIf.adminSt',
            'sviIf.operSt',
            'sviIf.operStQual',
            'sviIf.vlanT',
            'sviIf.medium',
            'mcastAllow',
            'sviIf.mtu',
            'fabEncap'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Admin State',
            'Oper State',
            'Reason',
            'Type',
            'Medium',
            'Multicast',
            'MTU',
            'Fabric Encap'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_interfaces_svi_address(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default('No svi interfaces')
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'sviIf.id',
            'sviIf.adminSt',
            'sviIf.operSt',
            'sviIf.vlanId',
            'sviIf.mac',
            'ipv4_address'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Admin State',
            'Oper State',
            'Vlan ID',
            'MAC',
            'IPv4'
        ]

        self.my_output.my_table(
            self.my_output.expand_list(
                interfaces,
                order,
                'ipv4_address'
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_interfaces_svi_counter(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default('No svi interfaces')
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'sviIf.id',
            'sviIf.adminSt',
            'sviIf.operSt',
            'counters.inPackets',
            'counters.outPackets',
            'counters.inMcast',
            'counters.outMcast',
            'counters.inDiscards',
            'counters.outDiscards',
            'counters.inErrors',
            'counters.outErrors'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Admin State',
            'Oper State',
            'Pkts In',
            'Pkts Out',
            'Mcast In',
            'Mcast Out',
            'Disc In',
            'Disc Out',
            'Err In',
            'Err Out'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_interface_svi(self, interface):
        order = [
            'sviIf.id',
            'sviIf.adminSt',
            'sviIf.operSt',
            'sviIf.operStQual',
            'sviIf.vlanId',
            'sviIf.vlanT',
            'sviIf.medium',
            'mcastAllow',
            'sviIf.mtu',
            'sviIf.mac',
            'sviIf.bw',
            'sviIf.carDel',
            'sviIf.delay',
            'fabEncap'
        ]

        headers = [
            'Interface',
            'Admin State',
            'Oper State',
            'Reason',
            'Vlan ID',
            'Vlan Type',
            'Medium',
            'Multicast',
            'MTU',
            'MAC',
            'Bandwidth',
            'Carrier Delay',
            'Delay',
            'Fabric Encap'
        ]

        self.my_output.dictionary(
            interface,
            title='Interface SVI',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        order = [
            'addr',
            'operSt',
            'operStQual',
            'type'
        ]

        headers = [
            'Address',
            'Oper State',
            'Reason',
            'Type'
        ]

        self.my_output.my_table(
            interface['ipv4_info'],
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

        order = [
            'inOctets',
            'inPackets',
            'inMcast',
            'inDiscards',
            'inErrors',
            'outOctets',
            'outPackets',
            'outMcast',
            'outDiscards',
            'outErrors'
        ]

        headers = [
            'Input Octets',
            'Input Unicast Packets',
            'Input Multicast Packets',
            'Input Discards',
            'Input Errors',
            'Output Octets',
            'Output Unicast Packets',
            'Output Multicast Packets',
            'Output Discards',
            'Output Errors'
        ]

        self.my_output.dictionary(
            interface['counters'],
            title='Interface Traffic Counters',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
