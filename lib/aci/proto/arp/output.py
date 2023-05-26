class ProtocolArpOutput():
    def __init__(self):
        pass

    def print_protocol_arp(self, info):
        self.print_protocol_arp_domains(
            info['domains']
        )

        self.print_protocol_arp_interface_summary(
            info['interface']
        )

    def print_protocol_arp_interface_summary(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'interface',
            'count'
        ]

        headers = [
            'Node',
            'Interface',
            'Adjacency'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_protocol_arp_domains(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'name',
            'adjacency_count'
        ]

        headers = [
            'Node',
            'VRF',
            'Adjacency'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_protocol_arp_domain(self, info):
        order = [
            'pod_node_name',
            'name',
            'adjacency_count'
        ]

        headers = [
            'Node',
            'VRF',
            'Adjacency'
        ]

        self.my_output.dictionary(
            info,
            title='ARP VRF',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        if info['adjacency'] is not None and len(info['adjacency']) > 0:
            self.print_protocol_arp_adjacencies(
                info['adjacency']
            )

    def print_protocol_arp_adjacencies(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'domain_name',
            'mac',
            'ip',
            'operSt',
            'ifId',
            'physIfId',
            'upTS'
        ]

        headers = [
            'Node',
            'VRF',
            'MAC',
            'IP',
            'State',
            'Interface',
            'Phy Interface',
            'Timestamp'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )
