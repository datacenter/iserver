class ProtocolLacpOutput():
    def __init__(self):
        pass

    def print_proto_lacp(self, info):
        self.print_proto_lacp_instance(
            info['instance']
        )

        self.print_proto_lacp_interfaces(
            info['interfaces']
        )

        self.print_proto_lacp_interfaces_stats(
            info['interfaces']
        )

    def print_proto_lacp_instance(self, info):
        order = [
            'pod_node_name',
            'adminSt',
            'sysMac',
            'adminPrio',
            'operPrio',
            'summary.portSummary'
        ]

        headers = [
            'Node',
            'Admin State',
            'System MAC',
            'Admin Priority',
            'Oper Priority',
            'Port Channel Interfaces'
        ]

        self.my_output.dictionary(
            info,
            title='LACP Instance',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_lacp_instances(self, info):
        order = [
            'instance.pod_node_name',
            'instance.adminSt',
            'instance.sysMac',
            'instance.adminPrio',
            'instance.operPrio',
            'instance.summary.portSummary'
        ]

        headers = [
            'Node',
            'Admin State',
            'System MAC',
            'Admin Priority',
            'Oper Priority',
            'Port Channel Interfaces'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_proto_lacp_interfaces(self, interfaces):
        order = [
            'id',
            'name',
            'adminSt',
            'state.operSt',
            'lacp.id',
            'lacp.key',
            'lacp.adjacency.sysId',
            'lacp.adjacency.sysPrio',
            'lacp.adjacency.key',
            'lacp.adjacency.port',
            'lacp.adjacency.portPrio',
            'lacp.adjacency.activityFlags'
        ]

        headers = [
            'Id',
            'Name',
            'Admin State',
            'Oper State',
            'Interface',
            'Oper Key',
            'Nbr System MAC',
            'Nbr System Prio',
            'Nbr Oper Key',
            'Nbr Port',
            'Nbr Port Prio',
            'Nbr Port State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                ['lacp']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_proto_lacp_interfaces_stats(self, interfaces):
        order = [
            'id',
            'name',
            'adminSt',
            'state.operSt',
            'lacp.id',
            'lacp.stats.pduSent',
            'lacp.stats.pduRcvd',
            'lacp.stats.errPktRcvd',
            'lacp.stats.markerSent',
            'lacp.stats.markerRcvd',
            'lacp.stats.markerRspSent',
            'lacp.stats.markerRspRcvd'
        ]

        headers = [
            'Id',
            'Name',
            'Admin State',
            'Oper State',
            'Interface',
            'PDU Sent',
            'PDU Recv',
            'PDU Recv Err',
            'Marker Sent',
            'Marker Recv',
            'Marker Response Sent',
            'Marker Response Recv'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                ['lacp']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
