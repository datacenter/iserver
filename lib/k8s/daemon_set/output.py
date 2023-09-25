class K8sDaemonSetOutput():
    def __init__(self):
        pass

    def print_daemon_sets(self, info, title=False):
        if title:
            self.my_output.default(
                'Daemon Set [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['node_selectorT'] = []
            for key in item['node_selector']:
                item['node_selectorT'].append(
                    '%s: %s' % (
                        key,
                        item['node_selector'][key]
                    )
                )

        order = [
            'namespace',
            'name',
            'owner',
            'scheduled_summary',
            'available_summary',
            'node_selectorT',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Owner',
            'Scheduled',
            'Available',
            'Node Selector',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['node_selectorT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
