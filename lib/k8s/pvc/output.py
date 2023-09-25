class K8sPvcOutput():
    def __init__(self):
        pass

    def print_pvcs(self, info, title=False):
        if title:
            self.my_output.default(
                'PVC [#%s]' % (len(info)),
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
            'owner',
            'phase',
            'volume_name',
            'volume_phase',
            'volume_mode',
            'capacity.storage',
            'access_modes',
            'storage_class_name',
            'storage_provisioner',
            'selected_node',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Owner',
            'Status',
            'PV Name',
            'PV Status',
            'Mode',
            'Size',
            'Access Mode',
            'Storage Class',
            'Storege Type',
            'Storage Node',
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
