class InterfaceTunnelOutput():
    def __init__(self):
        pass

    def print_interfaces_tunnel(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default('No tunnel interfaces')
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'adminSt',
            'operSt',
            'operStQual',
            'tLayer',
            'tType',
            'type',
            'requestor',
            'src',
            'dest_ip_node',
            'vrfName',
            'cfgdMtu'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Admin',
            'Oper',
            'Reason',
            'Layer',
            'Tunnel Type',
            'Type',
            'Req',
            'Source',
            'Destination',
            'VRF',
            'MTU'
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

    def print_interface_tunnel(self, interface):
        order = [
            'id',
            'adminSt',
            'operSt',
            'operStQual',
            'tLayer',
            'tType',
            'type',
            'src',
            'dest_ip_node',
            'vrfName',
            'cfgdMtu',
            'keepAlvIntvl',
            'keepAlvRetries'
        ]

        headers = [
            'Interface',
            'Admin State',
            'Oper State',
            'Reason',
            'Tunnel Layer',
            'Tunnel Type',
            'Type',
            'Source',
            'Destination',
            'VRF',
            'MTU',
            'Keepalive Interval',
            'Keepalive Retries'
        ]

        self.my_output.dictionary(
            interface,
            title='Interface tunnel',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
