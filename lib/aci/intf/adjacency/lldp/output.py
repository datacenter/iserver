from lib import ip_helper


class InterfaceAdjacencyLldpOutput():
    def __init__(self):
        pass

    def print_lldp_adjacency_endpoints(self, info, title=False):
        if title:
            self.my_output.default(
                'LLDP Adjacency [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'health',
            'faults',
            'interface_id',
            'ttl',
            'sysName',
            'mac',
            'portId',
            'portVlan',
            'portDesc',
            'capability'
        ]

        headers = [
            'Node',
            'Health',
            'Faults',
            'Interface ID',
            'Hold Time',
            'Neighbor Device',
            'MAC',
            'Port',
            'VLAN',
            'Port Description',
            'Capabilities'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_lldp_adjacency_interface_endpoints(self, adjacency, interface, title=False):
        if title:
            self.my_output.default(
                'LLDP Adjacency - Endpoints [#%s]' % (len(interface)),
                underline=True,
                before_newline=True
            )

        if len(interface) == 0:
            if title:
                self.my_output.default('None')
            return

        for interface_info in interface:
            for adjacency_info in adjacency:
                if ip_helper.is_mac_equal(interface_info['mac'], adjacency_info['mac']):
                    for key in adjacency_info:
                        interface_info[key] = adjacency_info[key]

        order = [
            'host',
            'mac',
            'pci',
            'interface',
            'model',
            'pod_node_name',
            'interface_id'
        ]

        headers = [
            'Server',
            'MAC',
            'PCI',
            'Interface',
            'Model',
            'LLDP Node',
            'LLDP Interface ID'
        ]

        self.my_output.my_table(
            interface,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )
