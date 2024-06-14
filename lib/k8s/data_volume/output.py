class K8sDataVolumeOutput():
    def __init__(self):
        pass

    def print_data_volumes(self, info, title=False):
        if title:
            self.my_output.default(
                'Data Volume - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        row_separator = False
        for item in info:
            if len(item['access_modes']) > 1:
                row_separator = True

        order = [
            'namespace',
            'name',
            'runningTick',
            'boundTick',
            'readyTick',
            'access_modes',
            'storage',
            'claim_name',
            'phase',
            'progress',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'POD Running',
            'Bound',
            'Ready',
            'Access Mode',
            'Storage',
            'PVC',
            'Phase',
            'Progress',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['access_modes']
            ),
            order=order,
            headers=headers,
            row_separator=row_separator,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
