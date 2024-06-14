class PolicyGroupAccessInterfacePortOutput():
    def __init__(self):
        pass

    def print_policy_groups_access_interface_port(self, info, title=False):
        if title:
            self.my_output.default(
                'Policy Group - Access Interface Port [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'faults',
            'name',
            'infraRsAttEntP.name',
            'infraRsHIfPol.name',
            'infraRsLinkFlapPol.name',
            'infraRsCdpIfPol.name',
            'infraRsMcpIfPol.name',
            'infraRsLldpIfPol.name',
            'infraRsStpIfPol.name',
            'infraRsStormctrlIfPol.name'
        ]

        headers = [
            'Faults',
            'Name',
            'AAEP',
            'Link Level',
            'Link Flap',
            'CDP',
            'MCP',
            'LLDP',
            'STP',
            'Storm Control'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_policy_groups_access_interface_port_aaep(self, info, title=False):
        if title:
            self.my_output.default(
                'Policy Group - Access Interface Port - AAEP [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return
        order = [
            'name',
            'infraRsAttEntP.name',
            'infraRsDomP.domainType',
            'infraRsDomP.domainName',
            'vlanPool',
            'vlanBlock'
        ]

        headers = [
            'Name',
            'AAEP',
            'Domain Type',
            'Domain Name',
            'VLAN Pool',
            'VLAN Range'
        ]

        for item in info:
            item['infraRsDomP'] = item['aaep']['infraRsDomP']
            item['vlanPool'] = item['aaep']['vlanPool']
            item['vlanBlock'] = item['aaep']['vlanBlock']

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['infraRsDomP', 'vlanPool', 'vlanBlock']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_policy_groups_access_interface_port_node(self, info, title=False):
        if title:
            self.my_output.default(
                'Policy Group - Access Interface Port - Deployed Nodes [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        for item in info:
            item['vlanPool'] = item['aaep']['vlanPool']
            item['vlanBlock'] = item['aaep']['vlanBlock']

        order = [
            'name',
            'infraRsAttEntP.name',
            'vlanPool',
            'vlanBlock',
            'node.name',
            'node.interfaces'
        ]

        headers = [
            'PG Name',
            'AAEP',
            'VLAN Pool',
            'VLAN Range',
            'Node',
            'Interfaces'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vlanPool', 'vlanBlock', 'node']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_policy_groups_access_interface_port_interface(self, info, title=False):
        if title:
            self.my_output.default(
                'Policy Group - Access Interface Port - Deployed Interfaces [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        for item in info:
            item['vlanPool'] = item['aaep']['vlanPool']
            item['vlanBlock'] = item['aaep']['vlanBlock']

        order = [
            'name',
            'infraRsAttEntP.name',
            'vlanPool',
            'vlanBlock',
            'interface.node_name',
            'interface.intf_name'
        ]

        headers = [
            'PG Name',
            'AAEP',
            'VLAN Pool',
            'VLAN Range',
            'Node',
            'Intf Name'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vlanPool', 'vlanBlock', 'interface']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_policy_groups_access_interface_port_vlan(self, info, title=False):
        if title:
            self.my_output.default(
                'Policy Group - Access Interface Port - Deployed Interfaces with State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        for item in info:
            item['vlanPool'] = item['aaep']['vlanPool']
            item['vlanBlock'] = item['aaep']['vlanBlock']

        order = [
            'name',
            'infraRsAttEntP.name',
            'vlanPool',
            'vlanBlock',
            'interface.node_name',
            'interface.intf_name',
            'interface.operSt',
            'interface.operMode',
            'interface.vlans'
        ]

        headers = [
            'PG Name',
            'AAEP',
            'VLAN Pool',
            'VLAN Range',
            'Node',
            'Intf Name',
            'State',
            'Mode',
            'VLANs'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vlanPool', 'vlanBlock', 'interface']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_policy_groups_access_interface_port_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Policy Group - Access Interface Port - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Policy Group - Access Interface Port - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pgName',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'PG Name',
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

    def print_policy_groups_access_interface_port_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Policy Group - Access Interface Port - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pgName',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'PG Name',
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

    def print_policy_groups_access_interface_port_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Policy Group - Access Interface Port - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Policy Group - Access Interface Port - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pgName',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'PG Name',
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

    def print_policy_groups_access_interface_port_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Policy Group - Access Interface Port - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Policy Group - Access Interface Port - Audit Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pgName',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'PG Name',
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
