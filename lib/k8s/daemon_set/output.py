class K8sDaemonSetOutput():
    def __init__(self):
        pass

    def print_daemon_sets_state(self, info):
        for item in info:
            item['node_selectorT'] = []
            for key in item['node_selector']:
                item['node_selectorT'].append(
                    '%s: %s' % (
                        key,
                        item['node_selector'][key]
                    )
                )

        self.my_output.my_table_ng(
            info,
            [
                ['Daemon Set', 'namespace_nameT'],
                ['Owner', 'ownerT'],
                ['Scheduled', 'scheduled_summary'],
                ['Available', 'available_summary'],
                ['Node Selector', 'node_selectorT'],
                ['Age', 'age']
            ]
        )

    def print_daemon_sets_metadata(self, info, title=False):
        if title:
            self.my_output.default(
                'Daemon Set - Metadata [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['namespace_nameT'] = []
            item['namespace_nameT'].append(
                item['namespace']
            )
            item['namespace_nameT'].append(
                item['name']
            )

            if item['owner'] is None:
                item['ownerT'] = ['--']
            else:
                item['ownerT'] = item['owner'].split('/')

        order = [
            'namespace_nameT',
            'ownerT',
            'labelT',
            'annotationT'
        ]

        headers = [
            'Daemon Set',
            'Owner',
            'Label',
            'Annotation'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['namespace_nameT', 'labelT', 'annotationT', 'ownerT']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
