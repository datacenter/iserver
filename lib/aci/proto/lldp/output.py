class ProtocolLldpOutput():
    def __init__(self):
        pass

    def print_proto_lldp_instance(self, info):
        order = [
            'pod_node_name',
            'adminSt',
            'holdTime',
            'initDelayTime',
            'txFreq',
            'adjacencyCount',
            'errorsTick'
        ]

        headers = [
            'Node',
            'Admin State',
            'Hold Time',
            'Init Delay Time',
            'Transmission Frequency',
            'Neighbors',
            'Errors'
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
            'pod_node_name',
            'pktSent',
            'pktRcvd',
            'pktDiscarded',
            'errPktRcvd',
            'unrecogTLV',
            'numAdjAdded',
            'numAdjRemoved',
            'entriesAged'
        ]

        headers = [
            'Node',
            'Packets Sent',
            'Packets Received',
            'Packets Discarded',
            'Error Received Packets',
            'Unrecognized TLV',
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
