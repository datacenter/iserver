from lib import filter_helper


class TamAdvisoryInstanceOutput():
    def __init__(self):
        pass

    def print_advisory(self, servers, title=False):
        info = []
        for server in servers:
            if 'AdvisorySummary' in server:
                item = server['AdvisorySummary']
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Advisory Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'High',
            'Info'
        ]

        headers = [
            'Server',
            'High',
            'Info'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

        advisories = {}
        for server in servers:
            for server_advisory in server['AdvisoryInfo']:
                if server_advisory['Name'] not in advisories:
                    advisories[server_advisory['Name']] = server_advisory
                    advisories[server_advisory['Name']]['Server'] = []

                advisories[server_advisory['Name']]['Server'].append(
                    server['Name']
                )

        info = []
        for advisory_name in advisories:
            item = advisories[advisory_name]
            item['NameT'] = filter_helper.get_string_chunks(
                item['Name'],
                40,
                separator=' '
            )
            item['DescriptionT'] = filter_helper.get_string_chunks(
                item['Description'].replace('\n', ''),
                40,
                separator=' '
            )
            item['Server'] = sorted(
                item['Server'],
                key=lambda i: i.lower()
            )
            info.append(
                item
            )

        if len(info) > 0:
            if title:
                self.my_output.default(
                    'Advisory [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )

            order = [
                'Server',
                'Severity',
                'BaseScore',
                'NameT',
                'DescriptionT',
                'CveIds',
                'DatePublished',
                'DateUpdated'
            ]

            headers = [
                'Server',
                'Severity',
                'Score',
                'Name',
                'Description',
                'CveIds',
                'DatePublished',
                'DateUpdated'
            ]

            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    ['Server', 'DescriptionT', 'NameT', 'CveIds']
                ),
                order=order,
                headers=headers,
                remove_empty_columns=True,
                allow_order_subkeys=True,
                row_separator=True,
                underline=True,
                table=True
            )

        if len(info) > 0:
            if title:
                self.my_output.default(
                    'Advisory Url [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )

            order = [
                'Server',
                'NameT',
                'Urls'
            ]

            headers = [
                'Server',
                'Name',
                'Urls'
            ]

            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    ['Server', 'NameT', 'Urls']
                ),
                order=order,
                headers=headers,
                remove_empty_columns=True,
                allow_order_subkeys=True,
                row_separator=True,
                underline=True,
                table=True
            )
