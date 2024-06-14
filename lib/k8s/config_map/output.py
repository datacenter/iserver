class K8sConfigMapOutput():
    def __init__(self):
        pass

    def print_config_maps(self, info, title=False):
        if title:
            self.my_output.default(
                'Config Map - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace',
            'name',
            'dataCount',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Data',
            'Age'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_config_maps_name(self, info, title=False):
        if title:
            self.my_output.default(
                'Config Map - Data Name [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        row_separator = False

        for item in info:
            item['dataName'] = []
            for key in item['data']:
                item['dataName'].append(
                    key
                )

            item['dataName'] = sorted(item['dataName'])
            if len(item['dataName']) == 0:
                item['dataName'].append('--')

            if len(item['dataName']) > 1:
                row_separator = True

        order = [
            'namespace',
            'name',
            'dataName',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Data Name',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['dataName']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=row_separator,
            table=True
        )

    def print_config_maps_data(self, info, title=False):
        if title:
            self.my_output.default(
                'Config Map - Data [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace',
            'name',
            'dataCount',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Data',
            'Age'
        ]

        for item in info:
            self.my_output.my_table(
                [item],
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                underline=True,
                row_separator=False,
                table=True
            )

            if len(item['data']) > 0:
                for key in item['data']:
                    self.my_output.default('')
                    self.my_output.default('Data: %s' % (key), underline=True)
                    self.my_output.default(item['data'][key])

    def print_config_maps_pod(self, info, title=False):
        if title:
            self.my_output.default(
                'Config Map - Pod [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        row_separator = False

        for item in info:
            for pod in item['pod']:
                pod['namespace_name'] = '%s/%s' % (
                    pod['namespace'],
                    pod['name']
                )

            if len(item['pod']) > 1:
                row_separator = True

            if len(item['pod']) == 0:
                item['pod'].append(
                    dict(
                        namespace_name='--'
                    )
                )

        order = [
            'namespace',
            'name',
            'dataCount',
            'pod.namespace_name'
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Data Name',
            'Pod',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['pod']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=row_separator,
            table=True
        )
