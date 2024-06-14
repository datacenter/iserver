class SystemFaultOutput():
    def __init__(self):
        pass

    def print_system_faults(self, info, title=False):
        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'System Faults Details [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        order = [
            'severity',
            'domain',
            'type',
            'code',
            'cause',
            'dnT',
            'descrT'
        ]

        headers = [
            'Severity',
            'Domain',
            'Type',
            'Code',
            'Cause',
            'Object',
            'Description'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['dnT', 'descrT']
            ),
            order=order,
            headers=headers,
            underline=True,
            remove_empty_columns=True,
            row_separator=True,
            table=True
        )

    def print_system_faults_summary(self, info, title=False):
        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'System Faults Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        order = [
            'severity',
            'domain',
            'type',
            'code',
            'count',
            'cause',
            'codeT'
        ]

        headers = [
            'Severity',
            'Domain',
            'Type',
            'Code',
            'Count',
            'Cause',
            'Explanation'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            remove_empty_columns=True,
            row_separator=True,
            table=True
        )

    def print_system_faults_type_count(self, info, title=False):
        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'System Fault Counts by Type',
                underline=True,
                before_newline=True
            )

        order = [
            'typeT',
            'critical',
            'major',
            'minor',
            'warning'
        ]

        headers = [
            'Type',
            'Critical',
            'Major',
            'Minor',
            'Warning'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            remove_empty_columns=True,
            row_separator=True,
            table=True
        )

    def print_system_faults_domain_count(self, info, title=False):
        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'System Fault Counts by Domain',
                underline=True,
                before_newline=True
            )

        order = [
            'domainT',
            'critical',
            'major',
            'minor',
            'warning'
        ]

        headers = [
            'Domain',
            'Critical',
            'Major',
            'Minor',
            'Warning'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            remove_empty_columns=True,
            row_separator=True,
            table=True
        )
