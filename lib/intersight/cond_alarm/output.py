from lib import filter_helper


class ComputeCondAlarmOutput():
    def __init__(self):
        pass

    def print_alarm_summary(self, servers, title=False):
        info = []
        for server in servers:
            if 'AlarmSummary' in server:
                item = server['AlarmSummary']
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Alarm Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Critical',
            'Warning',
            'Info'
        ]

        headers = [
            'Server',
            'Critical',
            'Warning',
            'Info'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_alarm(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['AlarmInfo']:
                item['ServerName'] = server['Name']
                item['DescriptionT'] = filter_helper.get_string_chunks(
                    item['Description'],
                    40,
                    separator=' '
                )
                info.append(
                    item
                )

        if len(info) > 0:
            if title:
                self.my_output.default(
                    'Alarm [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )

            order = [
                'ServerName',
                'Severity',
                'DescriptionT',
                'CreateTime',
                'AffectedType',
                'AffectedName'
            ]

            headers = [
                'Server',
                'Severity',
                'Description',
                'Create Time',
                'Affected Type',
                'Affected Name'
            ]

            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    ['DescriptionT']
                ),
                order=order,
                headers=headers,
                remove_empty_columns=False,
                allow_order_subkeys=True,
                row_separator=True,
                underline=True,
                table=True
            )

