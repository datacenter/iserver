class InterfaceFcOutput():
    def __init__(self):
        pass

    def print_interfaces_fc(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default('No fc interfaces')
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface'
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

    def print_interface_fc(self, interface):
        order = [
            'id'
        ]

        headers = [
            'Interface'
        ]

        self.my_output.dictionary(
            interface,
            title='Interface fc',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
