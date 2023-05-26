class InterfaceLoopbackOutput():
    def __init__(self):
        pass

    def print_interfaces_loopback(self, interfaces):
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
            'state.operStQual',
            'ipv4.addr',
            'state.lastErrors',
            'state.currErrIndex'
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
            'IPv4 Address',
            'Last Errors',
            'Current Error Index'
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

    def print_interface_loopback(self, interface):
        order = [
            'id',
            'adminSt',
            'state.operSt',
            'state.operStQual',
            'ipv4.addr',
            'state.lastErrors',
            'state.currErrIndex'
        ]

        headers = [
            'Interface',
            'Admin State',
            'Oper State',
            'Reason',
            'IPv4 Address',
            'Last Errors',
            'Current Error Index'
        ]

        self.my_output.dictionary(
            interface,
            title='Interface Loopback',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
