class ProtocolLldpOutput():
    def __init__(self):
        pass

    def print_proto_lldp(self, info):
        self.print_proto_lldp_instance(
            info['instance']
        )

        self.print_proto_lldp_instance_stats(
            info['stats']
        )

        self.print_lldp_adjacency_endpoints(
            info['adjacency']
        )

    def print_proto_lldp_instance(self, info):
        order = [
            'adminSt',
            'holdTime',
            'initDelayTime',
            'txFreq',
            'adjacencyCount'
        ]

        headers = [
            'Admin State',
            'Hold Time',
            'Init Delay Time',
            'Transmission Frequency',
            'Neighbors'
        ]

        self.my_output.dictionary(
            info,
            title='LLDP Instance',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_lldp_instance_stats(self, info):
        order = [
            'pktSent',
            'pktRcvd',
            'pktDiscarded',
            'errPktRcvd',
            'numAdjAdded',
            'numAdjRemoved',
            'entriesAged'
        ]

        headers = [
            'Packets Sent',
            'Packets Received',
            'Packets Discarded',
            'Error Packets',
            'Adjacencies Added',
            'Adjacencies Removed',
            'Entries Aged'
        ]

        self.my_output.dictionary(
            info,
            title='LLDP Instance Stats',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_lldp_instances(self, info):
        order = [
            'instance.pod_node_name',
            'instance.adminSt',
            'instance.holdTime',
            'instance.initDelayTime',
            'instance.txFreq',
            'instance.adjacencyCount'
        ]

        headers = [
            'Node',
            'Admin State',
            'Hold Time',
            'Init Delay Time',
            'Transmission Frequency',
            'Neighbors'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_proto_lldp_instances_stats(self, info):
        order = [
            'instance.pod_node_name',
            'instance.adminSt',
            'stats.pktSent',
            'stats.pktRcvd',
            'stats.pktDiscarded',
            'stats.errPktRcvd',
            'stats.numAdjAdded',
            'stats.numAdjRemoved',
            'stats.entriesAged'
        ]

        headers = [
            'Node',
            'Admin State',
            'Packets Sent',
            'Packets Received',
            'Packets Discarded',
            'Error Packets',
            'Adjacencies Added',
            'Adjacencies Removed',
            'Entries Aged'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
