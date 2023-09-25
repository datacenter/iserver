class K8sPerformanceProfileOutput():
    def __init__(self):
        pass

    def print_performance_profiles(self, info, title=False):
        if title:
            self.my_output.default(
                'Performance Profile [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['pages'] = item['hp']['pages']
            for key in ['isolated', 'reserved', 'offlined']:
                if item['cpu'][key] is None:
                    item['cpu'][key] = '--'

            if len(item['pages']) == 0:
                item['pages'].append(
                    dict(descr='--')
                )

            if len(item['kernel']) == 0:
                item['kernel'].append('--')

            if item['hp']['default_size'] is None:
                item['hp']['default_size'] = '--'

            item['hintsT'] = []
            for key in item['hints']:
                item['hintsT'].append(
                    '%s:%s' % (
                        key,
                        item['hints'][key]
                    )
                )

            if len(item['hintsT']) == 0:
                item['hintsT'].append('--')

        order = [
            'name',
            'availableTick',
            'upgradeableTick',
            'progressingTick',
            'degradedTick',
            'cpu.isolated',
            'cpu.reserved',
            'cpu.offlined',
            'kernel',
            'rt.enabledTick',
            'hp.default_size',
            'pages.descr',
            'mcp_selector',
            'node_selector',
            'hintsT',
            'age'
        ]

        headers = [
            'Name',
            'Available',
            'Upgradable',
            'Upgrading',
            'Degraded',
            'CPU Isolated',
            'CPU Reserved',
            'CPU Offlined',
            'Kernel Args',
            'RT',
            'HP Def',
            'HP',
            'MCP Selector',
            'Node Selector',
            'HintsT',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['kernel', 'pages', 'mcp_selector', 'node_selector', 'hintsT']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
