class ProtocolCdpOutput():
    def __init__(self):
        pass

    def print_proto_cdp_instances(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol CDP - Instance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'instance.sysName',
            'instance.adminSt',
            'instance.ver',
            'instance.txFreq',
            'instance.holdIntvl',
            'instance.neighborCount',
            'instance.activeInterfaceCount'
        ]

        headers = [
            'System Name',
            'Admin State',
            'CDP Version',
            'Transmit Frequency',
            'Hold Interval',
            'CDP Neighbors',
            'Active Interfaces'
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

    def print_proto_cdp_neighbors(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol CDP - Neighbor [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'interfaceId',
            'sysName',
            'platId',
            'portId',
            'duplex',
            'mtu',
            'nativeVlan',
            'cap'
        ]

        headers = [
            'Node',
            'Local Interface',
            'Neighbor System Name',
            'Platform',
            'Port',
            'Duplex',
            'MTU',
            'Native VLAN',
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

    def print_proto_cdp_interfaces(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol CDP - Interface Stats [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'id',
            'adminSt',
            'operSt',
            'neighborCount',
            'neighborList',
            'stats.v2Sent',
            'stats.validV2Rcvd',
            'stats.v1Sent',
            'stats.validV1Rcvd',
            'stats.failedSent',
            'stats.cksumErrRcvd',
            'stats.malformRcvd',
            'stats.unSupVerRcvd'
        ]

        headers = [
            'Node',
            'Interface ID',
            'Admin State',
            'Oper State',
            'Count',
            'Neighbors',
            'v2 Sent',
            'v2 Received',
            'v1 Sent',
            'v2 Received',
            'Failed Sent',
            'Checksum Error',
            'Malformed',
            'Unsupported Version'
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

    def print_proto_cdp_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol CDP - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol CDP - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'interfaceT',
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
            'Interface',
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
