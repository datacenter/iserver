class ProtocolLacpOutput():
    def __init__(self):
        pass

    def print_proto_lacp_instances(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol LACP - Instance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'instance.pod_node_name',
            'instance.adminSt',
            'instance.sysMac',
            'instance.adminPrio',
            'instance.operPrio',
            'instance.summary.portUp',
            'instance.summary.portDown',
            'instance.summary.portCount'
        ]

        headers = [
            'Node',
            'Admin',
            'System MAC',
            'Admin Prio',
            'Oper Prio',
            'Intf Up',
            'Intf Down',
            'Intf Count'
        ]

        self.my_output.my_table(
            info,
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_proto_lacp_interfaces(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol LACP - Port Channels [#%s]' % (len(info)),
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
            'Node',
            'Intf Id',
            'Name',
            'Admin',
            'Oper',
            'Member',
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
                info,
                order,
                ['lacp']
            ),
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_proto_lacp_interfaces_stats(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol LACP - Interface Stats [#%s]' % (len(info)),
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
            'Node',
            'Intf Id',
            'Name',
            'Admin',
            'Oper',
            'Member',
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
                info,
                order,
                ['lacp']
            ),
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_proto_lacp_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol LACP - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol LACP - Event Logs last %s [#%s]' % (when, len(info)),
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
