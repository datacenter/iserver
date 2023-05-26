class InterfaceEncapsulatedRoutedOutput():
    def __init__(self):
        pass

    def print_interfaces_encap_routed(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default('No encapsulated routed interfaces')
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'adminSt',
            'state.operSt',
            'state.operStQual',
            'encap',
            'mplsEnable',
            'state.operMtu',
            'donorIf'
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
            'Encap',
            'SR-MPLS',
            'MTU',
            'IP Unnumbered Intf'
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

    def print_interface_encap_routed(self, interface):
        order = [
            'id',
            'adminSt',
            'state.operSt',
            'state.operStQual',
            'encap',
            'mplsEnable',
            'state.operMtu',
            'donorIf',
            'delay',
            'routerMac'
        ]

        headers = [
            'Interface',
            'Admin State',
            'Oper State',
            'Reason',
            'Encap',
            'SR-MPLS',
            'MTU',
            'IP Unnumbered Intf',
            'Delay',
            'Router MAC'
        ]

        self.my_output.dictionary(
            interface,
            title='Encapsulated Routed Interface',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
