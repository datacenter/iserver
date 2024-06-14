class ProtocolLldpOutput():
    def __init__(self):
        pass

    def print_proto_lldp_instance(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol LLDP - Instance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

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
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_proto_lldp_instances_stats(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol LLDP - Stats [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

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

    def print_proto_lldp_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol LLDP - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol LLDP - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'interface_id',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'affectedT'
        ]

        headers = [
            'Node',
            'Intf',
            'Severity',
            'Code',
            'Cause',
            'Created Time',
            'Description',
            'Affected'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT', 'affectedT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_lldp_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol LLDP - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'interface_id',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Node',
            'Intf',
            'Severity',
            'Code',
            'Cause',
            'Created Time',
            'Lifecycle',
            'Description'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_lldp_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol LLDP - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol LLDP - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'interface_id',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Node',
            'Intf',
            'Severity',
            'Code',
            'Cause',
            'Created Time',
            'Lifecycle',
            'Description'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )
