class K8sStorageSystemOutput():
    def __init__(self):
        pass

    def print_storage_systems(self, info, title=False):
        if title:
            self.my_output.default(
                'Storage System [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'availableTick'
        ]

        headers = [
            'Storage System',
            'Available'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=False,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
