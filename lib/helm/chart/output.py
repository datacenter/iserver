class HelmChartOutput():
    def __init__(self):
        pass

    def print_charts(self, info, title=False):
        if title:
            self.my_output.default(
                'Chart [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'directory',
            'apiVersion',
            'version',
            'appVersion',
            'release.namespace_name'
        ]

        headers = [
            'Name',
            'Directory',
            'API',
            'Version',
            'App',
            'Release'
        ]

        for item in info:
            if len(item['release']) == 0:
                item['release'].append(
                    dict(
                        namespace_name='--'
                    )
                )

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['release']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_chart_values(self, info):
        for item in info:
            self.my_output.default(
                'Chart: %s' % (item['chart']),
                underline=True,
                before_newline=True,
                after_newline=True
            )

            self.my_output.default(
                'Path: %s/values.yaml' % (item['directory']),
                after_newline=True
            )

            self.my_output.default(
                item['values']
            )

    def print_chart_files(self, info, title=False):
        if title:
            self.my_output.default(
                'Chart Files [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            for key in ['base', 'templates', 'charts', 'tests', 'crds', 'day0', 'custom']:
                if len(item[key]) == 0:
                    item[key].append('--')

        order = [
            'chart',
            'base',
            'templates',
            'charts',
            'tests',
            'crds',
            'day0',
            'custom'
        ]

        headers = [
            'Chart',
            'Base',
            'Template',
            'Chart Dependency',
            'Test',
            'CRD',
            'Day0',
            'Custom'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['base', 'templates', 'charts', 'tests', 'crds', 'day0', 'custom']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
