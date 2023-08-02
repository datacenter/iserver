class DomainPhyOutput():
    def __init__(self):
        pass

    def print_domains_phy(self, info, title=False):
        if title:
            self.my_output.default(
                'Physical Domain [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        for item in info:
            item['fvnsEncapBlk'] = []
            if item['vlan_info'] is not None:
                item['fvnsEncapBlk'] = item['vlan_info']['fvnsEncapBlk']

        for item in info:
            if len(item['aaaDomain']) == 0:
                item['aaaDomain'].append('--')

        order = [
            'faults',
            'name',
            'aaep_names',
            'vlan',
            'vlan_info.allocMode',
            'fvnsEncapBlk.blockInfo',
            'aaaDomain'
        ]

        headers = [
            'Faults',
            'Domain',
            'AAEP',
            'VLAN Pool',
            'Mode',
            'Encapsulation Block',
            'Sec Domain'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['aaep_names', 'fvnsEncapBlk', 'aaaDomain']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_domains_phy_node(self, info, title=False):
        if title:
            self.my_output.default(
                'Physical Domain - Node [#%s]' % (len(info)),
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
            'aaep_names',
            'vlan',
            'node.name',
            'node.interfaces'
        ]

        headers = [
            'Faults',
            'Domain',
            'AAEP',
            'VLAN Pool',
            'Node',
            'Interfaces'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['aaep_names', 'node']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_domains_phy_interface(self, info, title=False):
        if title:
            self.my_output.default(
                'Physical Domain - Interfaces [#%s]' % (len(info)),
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
            'aaep_names',
            'vlan',
            'interface.node_name',
            'interface.intf_name'
        ]

        headers = [
            'Faults',
            'Domain',
            'AAEP',
            'VLAN Pool',
            'Node',
            'Interface'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['aaep_names', 'interface']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_domains_phy_vlan(self, info, title=False):
        if title:
            self.my_output.default(
                'Physical Domain - Interfaces VLAN [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        for item in info:
            item['fvnsEncapBlk'] = []
            if item['vlan_info'] is not None:
                item['fvnsEncapBlk'] = item['vlan_info']['fvnsEncapBlk']

        order = [
            'faults',
            'name',
            'aaep_names',
            'vlan',
            'fvnsEncapBlk.blockInfo',
            'interface.node_name',
            'interface.intf_name',
            'interface.operSt',
            'interface.operMode',
            'interface.vlans'
        ]

        headers = [
            'Faults',
            'Domain',
            'AAEP',
            'VLAN Pool',
            'Encapsulation Block',
            'Node',
            'Interface',
            'State',
            'Mode',
            'VLANs'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['aaep_names', 'interface', 'fvnsEncapBlk']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_domains_phy_reln(self, info, title=False):
        if title:
            self.my_output.default(
                'Physical Domain - Policy Relationships [#%s]' % (len(info)),
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
            'reln.type',
            'reln.name'
        ]

        headers = [
            'Faults',
            'Domain',
            'Policy Type',
            'Policy Name'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['reln']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_domains_phy_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Physical Domain - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Physical Domain - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'domainName',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Domain',
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

    def print_domains_phy_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Physical Domain - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'domainName',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Domain',
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

    def print_domains_phy_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Physical Domain - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Physical Domain - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'domainName',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Domain',
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

    def print_domains_phy_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Physical Domain - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Physical Domain - Audit Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'domainName',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Domain',
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
