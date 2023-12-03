class PolicyGeneralAaeOutput():
    def __init__(self):
        pass

    def print_policies_global_aae(self, info, title=False):
        if title:
            self.my_output.default(
                'Attachable Access Entity Profile (AAEP) [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        for item in info:
            if len(item['infraRsFuncToEpg']) == 0:
                item['infraRsFuncToEpg'].append(
                    dict(
                        epgName='--'
                    )
                )

        order = [
            'faults',
            'name',
            'infraVlanEnabledTick',
            'infraRsDomP.domainType',
            'infraRsDomP.domainName',
            'infraRsDomP.state',
            'infraRsFuncToEpg.epgEncap',
            'infraRtAttEntP.typeName',
            'infraRtAttEntP.name'
        ]

        headers = [
            'Faults',
            'Name',
            'Infra VLAN',
            'Domain Type',
            'Domain Name',
            'Domain State',
            'EPG',
            'PG Interface Type',
            'PG Name'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['infraRsDomP', 'infraRtAttEntP', 'infraRsFuncToEpg']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_policies_global_aae_epg(self, info, title=False):
        if title:
            self.my_output.default(
                'Attachable Access Entity Profile (AAEP) - EPG Usage [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        for item in info:
            item['epg'] = []
            if 'vlan_info' in item:
                if item['vlan_info'] is not None:
                    item['epg'] = item['vlan_info']['epg']

        order = [
            'faults',
            'name',
            'aaep_names',
            'vlan',
            'epg.vlanId',
            'epg.tenantAppEpg'
        ]

        headers = [
            'Faults',
            'Domain',
            'AAEP',
            'VLAN Pool',
            'Vlan',
            'EPG'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['aaep_names', 'epg']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_policies_global_aae_node(self, info, title=False):
        if title:
            self.my_output.default(
                'Attachable Access Entity Profile (AAEP) - Nodes [#%s]' % (len(info)),
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
            'node.name',
            'node.interfaces'
        ]

        headers = [
            'Faults',
            'Name',
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

    def print_policies_global_aae_reln(self, info, title=False):
        if title:
            self.my_output.default(
                'Attachable Access Entity Profile (AAEP) - Relationships [#%s]' % (len(info)),
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

    def print_policies_global_aae_interface(self, info, title=False):
        if title:
            self.my_output.default(
                'Attachable Access Entity Profile (AAEP) - Interfaces [#%s]' % (len(info)),
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
            'interface.node_name',
            'interface.intf_type',
            'interface.intf_name'
        ]

        headers = [
            'Faults',
            'Name',
            'Node',
            'Intf Type',
            'Intf Name'
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

    def print_policies_global_aae_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Attachable Access Entity Profile (AAEP) - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Attachable Access Entity Profile (AAEP) - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'policyName',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Name',
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

    def print_policies_global_aae_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Attachable Access Entity Profile (AAEP) - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'policyName',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Name',
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

    def print_policies_global_aae_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Attachable Access Entity Profile (AAEP) - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Attachable Access Entity Profile (AAEP) - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'policyName',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Name',
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

    def print_policies_global_aae_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Attachable Access Entity Profile (AAEP) - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Attachable Access Entity Profile (AAEP) - Audit Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'policyName',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Name',
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
