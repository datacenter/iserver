class ProtocolBfdOutput():
    def __init__(self):
        pass

    def print_proto_bfd_instances(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol BFD - Instance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'instance.pod_node_name',
            'node.roleUi',
            'node.model',
            'instance.adminSt',
            'instance.health',
            'instance.faults',
            'instance.echoIf',
            'instance.sessionSummary',
            'interfaces.id',
            'interfaces.adminSt',
            'interfaces.sessionSummary'
        ]

        headers = [
            'Node',
            'Role',
            'HW',
            'Admin',
            'Health',
            'Faults',
            'Echo Intf',
            'Sessions',
            'Intf',
            'State',
            'Sessions'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['interfaces']
            ),
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_bfd_sessions(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol BFD - Session [#%s]' % (len(info)),
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
            'vrfName',
            'ifId',
            'sessionType',
            'srcAddr',
            'localMac',
            'operSt',
            'discr',
            'destAddr',
            'remoteMac',
            'remoteOperSt',
            'remoteDiscr',
        ]

        headers = [
            'Node',
            'Health',
            'Faults',
            'VRF',
            'Interface',
            'Type',
            'Local Address',
            'Local MAC',
            'State',
            'Session Id',
            'Remote Address',
            'Remote MAC',
            'State',
            'Session Id'
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

    def print_proto_bfd_sessions_stats(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol BFD - Session Stats [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'vrfName',
            'srcAddr',
            'destAddr',
            'stats.upCnt',
            'stats.downCnt',
            'stats.rxCnt',
            'rxIntvl',
            'stats.rxMin',
            'stats.rxAvg',
            'stats.rxMax',
            'stats.txCnt',
            'txIntvl',
            'stats.txMin',
            'stats.txAvg',
            'stats.txMax'
        ]

        headers = [
            'Node',
            'VRF',
            'Local Address',
            'Remote Address',
            'Up',
            'Down',
            'Rx Cnt',
            'Rx Interval [msec]',
            'Min',
            'Avg',
            'Max',
            'Tx Cnt',
            'Tx Interval [msec]',
            'Min',
            'Avg',
            'Max'
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

    def print_proto_bfd_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol BFD - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol BFD - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'session_id',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'affectedT'
        ]

        headers = [
            'Node',
            'Session Id',
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

    def print_proto_bfd_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol BFD - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'session_id',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Node',
            'Session Id',
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

    def print_proto_bfd_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol BFD - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol BFD - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'session_id',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Node',
            'Session Id',
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

    def print_proto_bfd_session(self, info, when=None):
        order = [
            'pod_node_name',
            'health',
            'faults',
            'srcAddr',
            'operSt',
            'discr',
            'localMac',
            'destAddr',
            'remoteOperSt',
            'remoteDiscr',
            'remoteMac',
            'vrfName',
            'ifId',
            'sessionType',
            'iod',
            'lastDownTime',
            'lastTransTime',
            'lastDiag',
            'authSeqno',
            'asyncPort',
            'diag',
            'detectMult',
            'localDetectMult',
            'rxIntvl',
            'txIntvl',
            'slowIntvl',
            'localRxIntvl',
            'localTxIntvl',
            'echoPort',
            'echoTxIntvl'
        ]

        headers = [
            'Node',
            'Health',
            'Faults',
            'Local Address',
            'Local State',
            'Local Session Id',
            'Local MAC',
            'Remote Address',
            'Remote State',
            'Remote Session Id',
            'Remote MAC',
            'VRF',
            'Interface',
            'Session Type',
            'IOD',
            'Last Down Time',
            'Last Trans Time',
            'Last Diag Code',
            'Authentication Sequence Number',
            'Async mode source port',
            'Protocol diag code',
            'Detect Multiplier',
            'Local Detect Multiplier',
            'Active Receive Interval (msec)',
            'Active Transmit Interval (msec)',
            'Active Slow Interval (msec)',
            'Local Receive Interval (msec)',
            'Local Transmit Interval (msec)',
            'Echo mode source port',
            'Active Echo Transmit Interval (msec)'
        ]

        self.my_output.dictionary(
            info,
            title='Protocol BFD - Session',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        self.print_proto_bfd_session_peer(info['peer'])
        self.print_proto_bfd_session_stats(info['stats'])
        self.print_proto_bfd_event_logs(
            info['eventLog'],
            when=when,
            title=True
        )
        self.print_proto_bfd_fault_inst(
            info['faultInst'],
            title=True
        )
        self.print_proto_bfd_fault_record(
            info['faultRecord'],
            when=when,
            title=True
        )

    def print_proto_bfd_session_peer(self, info):
        order = [
            'operSt',
            'diag',
            'flags',
            'minRx',
            'minRx',
            'minTx',
            'minEcho',
            'myDisc',
            'yourDisc',
            'CBit'
        ]

        headers = [
            'Oper State',
            'Diag Code',
            'BFD Flags',
            'Detect Multiplier',
            'Min Receive Interval (msec)',
            'Min Transmit Interval (msec)',
            'Min Echo Interval (msec)',
            'My discriminator',
            'Your discriminator',
            'C-Bit'
        ]

        self.my_output.dictionary(
            info,
            title='Protocol BFD - Peer',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_bfd_session_stats(self, info):
        order = [
            'upCnt',
            'downCnt',
            'lastRxPkt',
            'lastTxPkt',
            'rxCnt',
            'rxAvg',
            'rxMax',
            'rxMin',
            'txCnt',
            'txAvg',
            'txMax',
            'txMin'
        ]

        headers = [
            'Up State Counts',
            'Down State Counts',
            'Last packet received',
            'Last packet transmitted',
            'Packets Received',
            'Average Received Packets Interval',
            'Maximum Received Packets Interval',
            'Minimum Received Packets Interval',
            'Packets Transmitted',
            'Average Transmitted Packets Interval',
            'Maximum Transmitted Packets Interval',
            'Minimum Transmitted Packets Interval'
        ]

        self.my_output.dictionary(
            info,
            title='Protocol BFD - Session Stats',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
