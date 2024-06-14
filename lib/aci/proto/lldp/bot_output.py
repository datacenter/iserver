from lib import filter_helper


class ProtocolLldpBotOutput():
    def __init__(self):
        pass

    def print_proto_lldp_instances(self, info, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'Protocol LLDP - Instance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'pod_node_name',
            'adminSt',
            'health',
            'faults',
            'holdTime',
            'initDelayTime',
            'txFreq',
            'adjacencyCount',
            'errorsTick'
        ]

        headers = [
            'Node',
            'Admin State',
            'Health',
            'Faults',
            'Hold Time',
            'Init Delay Time',
            'Transmission Frequency',
            'Neighbors',
            'Errors'
        ]

        self.my_output.my_table(
            info,
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Protocol LLDP - Instance'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_proto_lldp_adjacency(self, info, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'Protocol LLDP - Adjacency [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        for item in info:
            item['portDescT'] = filter_helper.get_string_chunks(
                item['portDesc'],
                30
            )

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
            'portDescT',
            'capability'
        ]

        headers = [
            'Node',
            'Health',
            'Faults',
            'Intf',
            'Hold',
            'Neighbor',
            'MAC',
            'Port',
            'VLAN',
            'Description',
            'Cap'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['portDescT']
            ),
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Protocol LLDP - Adjacency'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_proto_lldp_interfaces_stats(self, info, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'Protocol LLDP - Stats [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Protocol LLDP - Stats'
        )

        html_output = self.my_output.get_output()

        return output, html_output
