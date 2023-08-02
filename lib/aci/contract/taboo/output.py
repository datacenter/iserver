import copy


class ContractTabooOutput():
    def __init__(self):
        pass

    def print_taboo_contracts(self, info, show_taboo_filters=False, title=False):
        if title:
            self.my_output.default(
                'Taboo Contract [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'faults',
            'nameTenant',
            'vzFilter.subjectNameTenant',
            'vzFilter.nameTenant'
        ]

        headers = [
            'Faults',
            'Taboo',
            'Subject',
            'Filter'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vzFilter']
            ),
            order=order,
            headers=headers,
            underline=True,
            row_separator=True,
            allow_order_subkeys=True,
            table=True
        )

        if show_taboo_filters:
            filters_in_the_list = []
            filters = []
            for taboo in info:
                for item in taboo['vzFilter']:
                    if item['nameTenant'] not in filters_in_the_list:
                        filters_in_the_list.append(
                            item['nameTenant']
                        )
                        new_entry = copy.deepcopy(item)
                        filters.append(new_entry)

            self.print_contract_filters(
                filters,
                title=title
            )

    def print_taboo_contracts_usage(self, info, title=False):
        if title:
            self.my_output.default(
                'Taboo Contract - Usage [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return
        order = [
            'faults',
            'nameTenant',
            'protectedEpg.nameLong'
        ]

        headers = [
            'Faults',
            'Taboo',
            'Protected EPG'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['protectedEpg']
            ),
            order=order,
            headers=headers,
            underline=True,
            row_separator=True,
            allow_order_subkeys=True,
            table=True
        )

    def print_taboo_contracts_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Taboo Contract - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Taboo Contract - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameTenant',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Taboo Contract',
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

    def print_taboo_contracts_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Taboo Contract - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameTenant',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Taboo Contract',
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

    def print_taboo_contracts_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Taboo Contract - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Taboo Contract - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameTenant',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Taboo Contract',
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

    def print_taboo_contracts_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Taboo Contract - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Taboo Contract - Audit Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameTenant',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Taboo Contract',
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
