class ProtocolBfdOutput():
    def __init__(self):
        pass

    def print_proto_bfd(self, info):
        self.print_proto_bfd_instance(
            info['instance']
        )

        self.print_proto_bfd_sessions(
            info['sessions']
        )

        self.print_proto_bfd_interfaces(
            info['interfaces']
        )

    def print_proto_bfd_instance(self, info):
        order = [
            'adminSt',
            'echoIf',
            'sessionSummary'
        ]

        headers = [
            'Admin State',
            'Echo Interface',
            'Sessions'
        ]

        self.my_output.dictionary(
            info,
            title='BFD Instance',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_bfd_instances(self, info):
        if len(info) == 0:
            return

        order = [
            'instance.pod_node_name',
            'instance.adminSt',
            'instance.echoIf',
            'instance.sessionSummary',
            'interfaces.id',
            'interfaces.adminSt',
            'interfaces.sessionSummary'
        ]

        headers = [
            'Node',
            'Admin',
            'Echo Intf',
            'Session Summary',
            'Interface',
            'Interface State',
            'Interface Sessions'
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

    def print_proto_bfd_interfaces(self, info):
        if len(info) == 0:
            return

        order = [
            'id',
            'adminSt',
            'sessionSummary'
        ]

        headers = [
            'Interface ID',
            'Admin State',
            'BFD Sessions'
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

    def print_proto_bfd_sessions(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'srcAddr',
            'operSt',
            'discr',
            'destAddr',
            'remoteOperSt',
            'remoteDiscr',
            'sessionType',
            'vrfName',
            'ifId'
        ]

        headers = [
            'Node',
            'Local Address',
            'State',
            'Session Id',
            'Remote Address',
            'State',
            'Session Id',
            'Type',
            'VRF',
            'Interface'
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

    def print_proto_bfd_session(self, info):
        order = [
            'pod_node_name',
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
            title='BFD Session',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        self.print_proto_bfd_session_peer(info['peer'])
        self.print_proto_bfd_session_stats(info['stats'])

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
            title='BFD Peer',
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
            title='BFD Session Stats',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
