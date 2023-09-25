class K8sPvOutput():
    def __init__(self):
        pass

    def print_pvs(self, info, title=False):
        if title:
            self.my_output.default(
                'PV [#%s]' % (len(info)),
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
            'name',
            'phase',
            'volume_mode',
            'capacity.storage',
            'access_modes',
            'csi_driver',
            'pvc_namespace',
            'pvc_name',
            'age'
        ]

        headers = [
            'Name',
            'Status',
            'Mode',
            'Size',
            'Access Mode',
            'CSI Driver',
            'PVC Namespace',
            'PVC Name',
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
