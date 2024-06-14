class InterfacePortChannelOutput():
    def __init__(self):
        pass

    def print_interfaces_port_channel_state(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Port Channel - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'health',
            'faults',
            'id',
            'name',
            'operChannelModeT',
            'adminSt',
            'state.operSt',
            'state.operStQual',
            'vpcDomain',
            'memberSummary',
            'layerT',
            'state.operMode',
            'state.operSpeed'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Health',
            'Faults',
            'Id',
            'Name',
            'Protocol',
            'Admin',
            'State',
            'Reason',
            'VPC',
            'Members',
            'Layer',
            'Mode',
            'Speed'
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

    def print_interfaces_port_channel_member(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Port Channel Member - Phy State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'member.isActiveMemberTick',
            'member.tSKey',
            'member.health',
            'member.faults',
            'member.adminSt',
            'member.operSt',
            'member.operMode',
            'member.operDuplex',
            'member.operSpeed',
            'member.operVlans'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Id',
            'Active',
            'Interface Id',
            'Health',
            'Faults',
            'Admin',
            'Oper',
            'Mode',
            'Duplex',
            'Speed',
            'VLAN'
        ]

        row_separator = False
        for item in info:
            if len(item['member']) > 1:
                row_separator = True

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['member']
            ),
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=row_separator,
            underline=True,
            table=True
        )

    def print_interfaces_port_channel_lacp(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Port Channel Member - LACP State [#%s]' % (len(info)),
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
            'isActiveMemberTick',
            'local.id',
            'local.adminSt',
            'local.port',
            'local.operPrio',
            'local.activityFlags',
            'local.key'
        ]

        headers = [
            'Node',
            'Id',
            'Active',
            'Interface',
            'Admin',
            'Port Num',
            'Port Priority',
            'Activity Flags',
            'Key'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

        if title:
            self.my_output.default(
                'Interface Port Channel Member - LACP Neighbor [#%s]' % (len(info)),
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
            'isActiveMemberTick',
            'local.id',
            'adjacency.port',
            'adjacency.portPrio',
            'adjacency.sysId',
            'adjacency.activityFlags',
            'adjacency.key'
        ]

        headers = [
            'Node',
            'Id',
            'Active',
            'Interface',
            'Nbr Port Num',
            'Nbr Port Priority',
            'Nbr System Id',
            'Nbr Activity Flags',
            'Nbr Key'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

        if title:
            self.my_output.default(
                'Interface Port Channel Member - LACP PDU [#%s]' % (len(info)),
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
            'isActiveMemberTick',
            'local.id',
            'stats.pduSent',
            'stats.pduRcvd',
            'stats.pduTimeOut',
            'stats.markerSent',
            'stats.markerRcvd',
            'stats.markerRspSent',
            'stats.markerRspRcvd'
        ]

        headers = [
            'Node',
            'Id',
            'Active',
            'Interface',
            'PDU Sent',
            'PDU Rcvd',
            'PDU Timeout',
            'Marker Sent',
            'Marker Rcvd',
            'Marker Rsp Sent',
            'Marker Rsp Rcvd'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_port_channel_vlan(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Port Channel - VLAN [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'state.allowedVlans',
            'state.operVlans',
            'state.primaryVlan',
            'vlan.id',
            'vlan.hwId',
            'vlan.encap',
            'vlan.name',
            'vlan.fabEncap'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Id',
            'Allowed VLANs',
            'Oper VLANs',
            'Primary VLAN',
            'VLAN ID',
            'HW ID',
            'Encap',
            'EPG',
            'Fabric Encap'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vlan']
            ),
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_interfaces_port_channel_stats(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Port Channel - Traffic Counters [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'rmonIfIn.octets',
            'rmonIfIn.nUcastPkts',
            'rmonIfIn.multicastPkts',
            'rmonIfIn.broadcastPkts',
            'rmonIfIn.discards',
            'rmonIfIn.errors',
            'rmonIfOut.octets',
            'rmonIfOut.nUcastPkts',
            'rmonIfOut.multicastPkts',
            'rmonIfOut.broadcastPkts',
            'rmonIfOut.discards',
            'rmonIfOut.errors',
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Id',
            'Bytes In',
            'Ucast',
            'Mcast',
            'Bcast',
            'Disc',
            'Err',
            'Bytes Out',
            'Ucast',
            'Mcast',
            'Bcast',
            'Disc',
            'Err',
        ]

        self.my_output.my_table(
            info,
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=False,
            underline=True,
            table=True
        )

    def print_interfaces_port_channel_ether(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Port Channel - Ether Counters [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'rmonEtherStats.pkts',
            'rmonEtherStats.octets',
            'rmonEtherStats.multicastPkts',
            'rmonEtherStats.broadcastPkts',
            'rmonEtherStats.pkts64Octets',
            'rmonEtherStats.pkts65to127Octets',
            'rmonEtherStats.pkts128to255Octets',
            'rmonEtherStats.pkts256to511Octets',
            'rmonEtherStats.pkts512to1023Octets',
            'rmonEtherStats.pkts1024to1518Octets'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Id',
            'Packets',
            'Bytes',
            'Mcast',
            'Bcast',
            '<64B',
            '65B-127B',
            '128B-255B',
            '256B-511B',
            '512B-1023B',
            '1024B-1518B'
        ]

        self.my_output.my_table(
            info,
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=False,
            underline=True,
            table=True
        )

    def print_interface_port_channel_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Interface Port Channel - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Interface Port Channel Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'interfaceId',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Node',
            'Interface',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Description',
            'Change Set'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT', 'changeSetT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_interface_port_channel_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Port Channel - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'interfaceId',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Node',
            'Interface',
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

    def print_interface_port_channel_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Interface Port Channel - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Interface Port Channel - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'interfaceId',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Node',
            'Interface',
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

    def print_interface_port_channel_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Interface Port Channel - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Interface Port Channel - Audit Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'interfaceId',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Node',
            'Interface',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Description',
            'Change Set'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT', 'changeSetT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            row_separator=True,
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
