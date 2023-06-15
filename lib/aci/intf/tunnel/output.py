class InterfaceTunnelOutput():
    def __init__(self):
        pass

    def print_interfaces_tunnel(self, info):
        if len(info) == 0:
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
            'typeT',
            'requestor',
            'src_ip',
            'dest_ip',
            'dest_node',
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
            'Encap',
            'Type',
            'Req',
            'Source IP',
            'Destination IP',
            'Destination Node',
            'VRF',
            'MTU'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['dest_node', 'typeT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_interface_tunnel(self, info):
        order = [
            'id',
            'adminSt',
            'operSt',
            'operStQual',
            'tLayer',
            'tType',
            'type',
            'src_ip',
            'dest_ip',
            'dest_node',
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
            'Source IP',
            'Destination IP',
            'Destiation Node',
            'VRF',
            'MTU',
            'Keepalive Interval',
            'Keepalive Retries'
        ]

        self.my_output.dictionary(
            info,
            title='Interface Tunnel',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
