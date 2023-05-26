class InterfaceAdjacencyLldpOutput():
    def __init__(self):
        pass

    def print_lldp_adjacency_endpoints(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
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
            remove_empty_columns=True,
            underline=True,
            table=True
        )
