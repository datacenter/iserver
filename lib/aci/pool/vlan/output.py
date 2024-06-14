class PoolVlanOutput():
    def __init__(self):
        pass

    def print_pool_vlans(self, info, title=False):
        if title:
            self.my_output.default(
                'Pool VLAN [#%s]' % (len(info)),
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
            'allocMode',
            'fvnsEncapBlk.blockInfo',
            'fvnsEncapBlk.role',
            'fvnsRtVlanNs.domainName',
            'epgUsage'
        ]

        headers = [
            'Faults',
            'VLAN Pool Name',
            'Allocation Mode',
            'Encapsulation Block',
            'Role',
            'Domain',
            'EPG Usage'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['fvnsEncapBlk', 'fvnsRtVlanNs']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_pool_vlans_epg(self, info, title=False):
        epg = []
        for item in info:
            for epg_info in item['epg']:
                epg_info['poolName'] = item['name']
                epg.append(
                    epg_info
                )

        epg = sorted(
            epg,
            key=lambda i: (
                i['poolName'],
                i['tenantAppEpg']
            )
        )

        if title:
            self.my_output.default(
                'Pool VLAN - Associated EPG [#%s]' % (len(epg)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'poolName',
            'tenantAppEpg',
            'encapCtx',
            'allocMode',
            'vlanId',
            'instrImedcy',
            'resImedcy',
            'switchingMode'
        ]

        headers = [
            'Pool Name',
            'EPG',
            'VLAN Pool',
            'Alloc Mode',
            'VLAN',
            'Deployment',
            'Resolution',
            'Switching'
        ]

        self.my_output.my_table(
            epg,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_pool_vlans_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Pool VLAN - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Pool VLAN - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'poolName',
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

    def print_pool_vlans_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Pool VLAN - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'poolName',
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

    def print_pool_vlans_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Pool VLAN - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Pool VLAN - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'poolName',
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

    def print_pool_vlans_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Pool VLAN - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Pool VLAN - Audit Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'poolName',
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
