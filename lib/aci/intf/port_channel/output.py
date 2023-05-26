class InterfacePortChannelOutput():
    def __init__(self):
        pass

    def print_interfaces_port_channel_state(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'name',
            'adminSt',
            'switchingSt',
            'state.operSt',
            'state.operStQual',
            'operChannelMode',
            'vpcDomain',
            'activePorts'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Id',
            'Name',
            'Admin',
            'Switching',
            'State',
            'Reason',
            'Oper Mode',
            'VPC Domain',
            'Active Links'
        ]

        self.my_output.my_table(
            interfaces,
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_port_channel_port(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'name',
            'state.operSt',
            'state.operMode',
            'state.operSpeed',
            'state.portIds'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Id',
            'Name',
            'State',
            'Mode',
            'Speed',
            'Ports'
        ]

        self.my_output.my_table(
            interfaces,
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interface_port_channel_summary(self, interface):
        order = [
            'apic',
            'pod_node_name',
            'id',
            'name',
            'adminSt',
            'switchingSt',
            'operChannelMode',
            'layerT',
            'minLinks',
            'maxLinks',
            'activePorts',
            'mode',
            'speed',
            'state.backplaneMac',
            'vpcDomain'

        ]

        headers = [
            'Apic',
            'Node',
            'Id',
            'Name',
            'Admin State',
            'Switching State',
            'Operational Mode',
            'Layer',
            'Min Links',
            'Max Links',
            'Active Links',
            'Mode',
            'Speed',
            'MAC Address',
            'vpcDomain'
        ]

        self.my_output.dictionary(
            interface,
            title='Interface Port Channel',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_interface_port_channel_vlan(self, interface):
        order = [
            'state.allowedVlans',
            'state.operVlans',
            'state.cfgAccessVlan',
            'state.accessVlan',
            'state.cfgNativeVlan',
            'state.nativeVlan'
        ]

        headers = [
            'Allowed VLANs',
            'Oper VLANs',
            'Configured Access VLAN',
            'Access VLAN',
            'Configured Native VLAN',
            'Native VLAN'
        ]

        self.my_output.dictionary(
            interface,
            title='VLANs',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_interface_port_channel(self, interface):
        self.print_interface_port_channel_summary(interface)
        self.print_interface_port_channel_vlan(interface)
        self.print_lacp_instance(interface['lacp'])
        if len(interface['members']) == 0:
            self.my_output.default('No LACP member interfaces found')

        if len(interface['members']) == 1:
            self.print_interface_port_channel_lacp_member(interface['members'][0])

        if len(interface['members']) > 1:
            self.print_interface_port_channel_lacp_members(interface['members'])

    def print_interface_port_channel_lacp_member(self, member):
        order = [
            'local.id',
            'local.adminSt',
            'local.port',
            'local.operPrio',
            'local.activityFlags',
            'local.lastActive',
            'local.key',
            'port',
            'portPrio',
            'sysId',
            'activityFlags',
            'key',
            'stats.pduSent',
            'stats.pduRcvd',
            'stats.pduTimeOut',
            'stats.markerSent',
            'stats.markerRcvd',
            'stats.markerRspSent',
            'stats.markerRspRcvd'
        ]

        headers = [
            'LACP Interface',
            'Admin State',
            'Local Port Num',
            'Local Port Priority',
            'Local Activity Flags',
            'Last Active',
            'Key',
            'Nbr Port Num',
            'Nbr Port Priority',
            'Nbr System Id',
            'Nbr Activity Flags',
            'Nbr Key',
            'PDU Sent',
            'PDU Rcvd',
            'PDU Timeout',
            'Marker Sent',
            'Marker Rcvd',
            'Marker Rsp Sent',
            'Marker Rsp Rcvd'
        ]

        self.my_output.dictionary(
            member,
            title='LACP Interface',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_interface_port_channel_lacp_members(self, members):
        order = [
            'local.id',
            'local.adminSt',
            'local.port',
            'local.operPrio',
            'local.activityFlags',
            'local.key'
        ]

        headers = [
            'LACP Interface',
            'Admin State',
            'Port Num',
            'Port Priority',
            'Activity Flags',
            'Key'
        ]

        self.my_output.my_table(
            members,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

        order = [
            'port_id',
            'port',
            'portPrio',
            'sysId',
            'activityFlags',
            'key'
        ]

        headers = [
            'LACP Interface',
            'Nbr Port Num',
            'Nbr Port Priority',
            'Nbr System Id',
            'Nbr Activity Flags',
            'Nbr Key'
        ]

        self.my_output.my_table(
            members,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

        order = [
            'port_id',
            'stats.pduSent',
            'stats.pduRcvd',
            'stats.pduTimeOut',
            'stats.markerSent',
            'stats.markerRcvd',
            'stats.markerRspSent',
            'stats.markerRspRcvd'
        ]

        headers = [
            'LACP Interface',
            'PDU Sent',
            'PDU Rcvd',
            'PDU Timeout',
            'Marker Sent',
            'Marker Rcvd',
            'Marker Rsp Sent',
            'Marker Rsp Rcvd'
        ]

        self.my_output.my_table(
            members,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
