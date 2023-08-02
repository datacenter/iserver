import copy


class ContractStandardOutput():
    def __init__(self):
        pass

    def print_standard_contracts(self, info, show_contract_filters=False, title=False):
        if title:
            self.my_output.default(
                'Standard Contract [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'faults',
            'nameTenant',
            'scope',
            'intent',
            'targetDscp',
            'vzFilter.subjectNameTenant',
            'vzFilter.nameTenant'
        ]

        headers = [
            'Faults',
            'Contract',
            'Scope',
            'Intent',
            'Target DSCP',
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

        if show_contract_filters:
            filters_in_the_list = []
            filters = []
            for contract in info:
                for item in contract['vzFilter']:
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

    def print_standard_contracts_usage(self, info, title=False):
        if title:
            self.my_output.default(
                'Standard Contract - Usage [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'faults',
            'nameTenant',
            'consumerEpg.nameLong',
            'providerEpg.nameLong'
        ]

        headers = [
            'Faults',
            'Contract',
            'Consumer EPG',
            'Provider EPG'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['consumerEpg', 'providerEpg']
            ),
            order=order,
            headers=headers,
            underline=True,
            row_separator=True,
            allow_order_subkeys=True,
            table=True
        )

    def print_standard_contracts_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Standard Contract - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Standard Contract - Event Logs last %s [#%s]' % (when, len(info)),
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
            'Standard Contract',
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

    def print_standard_contracts_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Standard Contract - Faults [#%s]' % (len(info)),
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
            'Standard Contract',
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

    def print_standard_contracts_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Standard Contract - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Standard Contract - Fault Records last %s [#%s]' % (when, len(info)),
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
            'Standard Contract',
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

    def print_standard_contracts_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Standard Contract - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Standard Contract - Audit Logs last %s [#%s]' % (when, len(info)),
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
            'Standard Contract',
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
