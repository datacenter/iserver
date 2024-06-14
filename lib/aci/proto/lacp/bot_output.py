class ProtocolLacpBotOutput():
    def __init__(self):
        pass

    def print_proto_lacp_instances(self, info, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'Protocol LACP - Instance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'pod_node_name',
            'adminSt',
            'sysMac',
            'adminPrio',
            'operPrio',
            'summary.portUp',
            'summary.portDown',
            'summary.portCount'
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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Protocol LACP - Instance'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_proto_lacp_interfaces(self, info, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'Protocol LACP - Port Channel [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Protocol LACP - Port Channel'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_proto_lacp_interfaces_stats(self, info, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'Protocol LACP - Interface Stats [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Protocol LACP - Interface Stats'
        )

        html_output = self.my_output.get_output()

        return output, html_output
