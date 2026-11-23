class InterfaceVirtualPortChannelOutput():
    def __init__(self):
        pass

    def print_interfaces_virtual_port_channel_state(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Virtual Port Channel - State [#%s]' % (len(info)),
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
            'lacpRole',
            'summOperRole',
            'operSt',
            'peerSt',
            'peerStQual',
            'compatSt',
            'compatQualStr',
            'localMemberSummary',
            'peerMemberSummary'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Health',
            'Faults',
            'Domain',
            'LACP Role',
            'Oper Role',
            'Oper State',
            'Peer State',
            'Reason',
            'Constistency',
            'Reason',
            'Local Members',
            'Remote Members'
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

    def print_interfaces_virtual_port_channel_address(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Virtual Port Channel - Address [#%s]' % (len(info)),
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
            'virtualIp',
            'vpcMAC',
            'localMAC',
            'localPrio',
            'peerIp',
            'peerMAC',
            'peerPrio'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Domain',
            'VPC IP',
            'VPC MAC',
            'Local MAC',
            'Local Prio',
            'Peer IP',
            'Peer MAC',
            'Peer Prio'
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

    def print_interfaces_virtual_port_channel_member(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Virtual Port Channel - Members [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'domainId',
            'health',
            'faults',
            'id',
            'pc.id',
            'name',
            'pcMode',
            'localOperSt',
            'remoteOperSt'
        ]

        headers = [
            'Node',
            'Domain',
            'Health',
            'Faults',
            'Member',
            'PC',
            'Description',
            'PC Mode',
            'Local State',
            'Remote State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['pc']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_virtual_port_channel_vlan(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Virtual Port Channel Member - Configured VLANs [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'domainId',
            'health',
            'faults',
            'id',
            'pc.id',
            'cfgdAccessVlan',
            'cfgdTrunkVlansT',
            'cfgdVlansT',
            'upVlansT',
            'suspVlansT',
            'peerCfgdVlansT',
            'peerUpVlansT'
        ]

        headers = [
            'Node',
            'Domain',
            'Health',
            'Faults',
            'Member',
            'PC',
            'Cfg Access Vlans',
            'Cfg Trunk Vlans',
            'Cfg Vlans',
            'Up Vlans',
            'Susp Vlans',
            'Peer Cfg Vlans',
            'Peer Up Vlans'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['pc', 'cfgdTrunkVlansT', 'cfgdVlansT', 'upVlansT', 'suspVlansT', 'peerCfgdVlansT', 'peerUpVlansT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_interfaces_virtual_port_channel_vlan_epg(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Virtual Port Channel Member - VLAN [#%s]' % (len(info)),
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
            'domainId',
            'health',
            'faults',
            'id',
            'pc.id',
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
            'Domain',
            'Health',
            'Faults',
            'Member',
            'PC',
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
                ['pc', 'vlan']
            ),
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_interface_virtual_port_channel_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Interface Virtual Port Channel - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Interface Virtual Port Channel - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'domainId',
            'interfaceIdT',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Node',
            'Domain',
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

    def print_interface_virtual_port_channel_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Virtual Port Channel - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'domainId',
            'interfaceIdT',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Node',
            'Domain',
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

    def print_interface_virtual_port_channel_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Interface Virtual Port Channel - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Interface Virtual Port Channel - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'domainId',
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
            'Domain',
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

    def print_interface_virtual_port_channel_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Interface Virtual Port Channel - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Interface Virtual Port Channel - Audit Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'domainId',
            'interfaceIdT',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Node',
            'Domain',
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

