class ProtocolArpOutput():
    def __init__(self):
        pass

    def print_proto_arp_instances(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ARP - Instance [#%s]' % (len(info)),
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
            'faults'
        ]

        headers = [
            'Node',
            'Admin State',
            'Health',
            'Faults'
        ]

        self.my_output.my_table(
            info,
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_arp_domains(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ARP - Domain [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'name',
            'health',
            'faults',
            'adjacency_count'
        ]

        headers = [
            'Node',
            'VRF',
            'Health',
            'Faults',
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

    def print_proto_arp_interface_summary(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ARP - Interface Adjacency Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
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

    def print_proto_arp_adjacencies(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ARP - Adjacency [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
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

    def print_proto_arp_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ARP - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Node',
            'Sev',
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

    def print_proto_arp_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol ARP - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol ARP - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Node',
            'Sev',
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

    def print_proto_arp_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol ARP - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol ARP - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT',
            'affectedT'
        ]

        headers = [
            'Node',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Description',
            'Change Set',
            'Affected'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT', 'changeSetT', 'affectedT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            row_separator=True,
            underline=True,
            table=True
        )
