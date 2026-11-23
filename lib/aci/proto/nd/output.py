import json


class ProtocolNdOutput():
    def __init__(self):
        pass

    def print_proto_nd_instances(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ND - Instance [#%s]' % (len(info)),
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
            'adminSt',
            'agingIntvl',
            'neighborCount',
            'activeInterfaceCount'
        ]

        headers = [
            'Node',
            'Health',
            'Faults',
            'Admin State',
            'Aging Interval',
            'Neighbor Count',
            'Active Interface Count'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_proto_nd_domains(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ND - Domain [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'name',
            'health',
            'faults',
            'interfacesCount',
            'neighborsCount'
        ]

        headers = [
            'VRF',
            'Health',
            'Faults',
            'Interfaces',
            'Neighbors'
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

    def print_proto_nd_interfaces(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ND - Interface [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'domainName',
            'id',
            'health',
            'faults',
            'adminSt',
            'hopLimit',
            'mtu',
            'nsIntvl',
            'nsRetries',
            'raIntvl',
            'raIntvlMin',
            'raLifetime',
            'reachableTime',
            'retransTimer'
        ]

        headers = [
            'Node',
            'VRF',
            'Interface',
            'Health',
            'Faults',
            'Admin',
            'Hop',
            'MTU',
            'NS Intvl',
            'NS Retr',
            'RA Intvl',
            'RA Min Int',
            'RA Life',
            'Reachable',
            'Retransmit'
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

    def print_proto_nd_interface_stats(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ND - Interface Stats [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'domainName',
            'id',
            'nsSent',
            'nsRcvd',
            'naSent',
            'naRcvd',
            'rsSent',
            'rsRcvd',
            'raSent',
            'raRcvd'
        ]

        headers = [
            'Node',
            'VRF',
            'Interface',
            'NS Sent',
            'NS Rcvd',
            'NA Sent',
            'NA Rcvd',
            'RS Sent',
            'RS Rcvd',
            'RA Sent',
            'RA Rcvd'
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

    def print_proto_nd_neighbors(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ND - Neighbor [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        self.my_output.default(
            json.dumps(
                info,
                indent=4
            )
        )

    def print_proto_nd_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ND - Faults [#%s]' % (len(info)),
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

    def print_proto_nd_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol ND - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol ND - Fault Records last %s [#%s]' % (when, len(info)),
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

    def print_proto_nd_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol ND - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol ND - Event Logs last %s [#%s]' % (when, len(info)),
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
