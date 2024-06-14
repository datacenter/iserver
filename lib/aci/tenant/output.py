class TenantOutput():
    def __init__(self):
        pass

    def print_tenants(self, info, title=False):
        if title:
            self.my_output.default(
                'Tenant [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'health',
            'name'
        ]

        headers = [
            'Health',
            'Name'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            remove_empty_columns=True,
            table=True
        )

    def print_tenants_count(self, info, title=False):
        if title:
            self.my_output.default(
                'Tenant - Object Counts [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'health',
            'name',
            'apCount',
            'aEpgCount',
            'bdCount',
            'vrfCount',
            'l2OutCount',
            'l3OutCount',
            'mplsL3OutCount',
            'contractStandardCount',
            'contractTabooCount',
            'contractFilterCount',
            'endpointCount'
        ]

        headers = [
            'Health',
            'Name',
            'App Profile',
            'EPG',
            'BD',
            'VRF',
            'L2Out',
            'L3Out',
            'MPLS-SR L3Out',
            'Standard Contr',
            'Taboo Contr',
            'Filter',
            'Endpoint'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            remove_empty_columns=True,
            table=True
        )

    def print_tenants_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Tenant - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Tenant - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'tenantName',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Tenant',
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

    def print_tenants_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Tenant - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'tenantName',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Tenant',
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

    def print_tenants_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Tenant - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Tenant - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'tenantName',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Tenant',
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

    def print_tenants_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Tenant - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Tenant - Audit Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'tenantName',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Tenant',
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
