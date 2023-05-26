class ProtocolCdpOutput():
    def __init__(self):
        pass

    def print_proto_cdp(self, info):
        self.print_proto_cdp_instance(
            info['instance']
        )

        self.print_proto_cdp_neighbors(
            info['neighbors']
        )

        self.print_proto_cdp_interfaces(
            info['interfaces']
        )

    def print_proto_cdp_instance(self, info):
        order = [
            'sysName',
            'adminSt',
            'ver',
            'txFreq',
            'holdIntvl',
            'neighborCount',
            'activeInterfaceCount'
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

        self.my_output.dictionary(
            info,
            title='CDP Instance',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_cdp_instances(self, info):
        if len(info) == 0:
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

    def print_proto_cdp_neighbors(self, info):
        if len(info) == 0:
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

    def print_proto_cdp_interfaces(self, info):
        if len(info) == 0:
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

    def print_protocol_cdp_interface_stats(self, info):
        order = [
            'v2Sent',
            'validV2Rcvd',
            'v1Sent',
            'validV1Rcvd',
            'cksumErrRcvd',
            'failedSent',
            'malformRcvd',
            'unSupVerRcvd'
        ]

        headers = [
            'CDPv2 Sent',
            'CDPv2 Received',
            'CDPv1 Sent',
            'CDPv2 Received',
            'Checksum Error Received',
            'Failed Sent',
            'Malformed Received',
            'Unsupported Version Received'
        ]

        self.my_output.dictionary(
            info,
            title='CDP Interface Stats',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
