class K8sStorageProfileOutput():
    def __init__(self):
        pass

    def print_storage_profiles(self, info, title=False):
        if title:
            self.my_output.default(
                'StorageProfile [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name'
        ]

        headers = [
            'StorageProfile'
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
