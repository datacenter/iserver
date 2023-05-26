class InterfaceMgmtOutput():
    def __init__(self):
        pass

    def print_interfaces_management_state(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'adminSt',
            'switchingSt',
            'state.operSt',
            'autoNeg',
            'state.operDuplex',
            'state.operMtu',
            'state.operSpeed',
            'state.lastLinkStChg'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Name',
            'Admin State',
            'Switching State',
            'OperState',
            'Auto Negotiation',
            'Duplex',
            'MTU',
            'Speed',
            'Last Link State Change'
        ]

        self.my_output.my_table(
            interfaces,
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_interfaces_management_address(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'adminSt',
            'state.operSt',
            'state.backplaneMac',
            'stats.addr',
            'state.operRouterMac'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Name',
            'Admin State',
            'OperState',
            'MAC Address',
            'IP Address',
            'Router MAC'
        ]

        self.my_output.my_table(
            interfaces,
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_interfaces_management_neighbor(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'adminSt',
            'state.operSt',
            'cdp.platId',
            'cdp.sysName',
            'cdp.portId',
            'lldp.sysName',
            'lldp.portIdV'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Name',
            'Admin State',
            'OperState',
            'CDP - Platform',
            'CDP - System Name',
            'CDP - Port',
            'LLDP - System Name',
            'LLDP - Port'
        ]

        self.my_output.my_table(
            interfaces,
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interface_management(self, interface):
        order = [
            'id',
            'adminSt',
            'switchingSt',
            'state.operSt',
            'autoNeg',
            'state.operDuplex',
            'state.operMtu',
            'state.operSpeed',
            'state.backplaneMac',
            'stats.addr',
            'state.operRouterMac',
            'cdp.platId',
            'cdp.sysName',
            'cdp.portId',
            'lldp.sysName',
            'lldp.portIdV',
            'state.lastLinkStChg'
        ]

        headers = [
            'Management Interface Name',
            'Admin State',
            'Switching State',
            'OperState',
            'Auto Negotiation',
            'Duplex',
            'MTU',
            'Speed',
            'MAC Address',
            'IP Address',
            'Router MAC',
            'CDP Neighbor - Platform',
            'CDP Neighbor - System Name',
            'CDP Neighbor - Port',
            'LLDP Neighbor - System Name',
            'LLDP Neighbor - Port',
            'Last Link State Change'
        ]

        self.my_output.dictionary(
            interface,
            title='Node Interface Management: %s' % (interface['id']),
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
