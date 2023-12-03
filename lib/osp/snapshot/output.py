class OspSnapshotOutput():
    def __init__(self):
        pass

    def print_snapshots(self, info, title=False):
        if title:
            self.my_output.default(
                'Volume Snapshot [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'tenant_name',
            'volume_name',
            'size',
            'status',
            'progress',
            'created_age'
        ]

        headers = [
            'Name',
            'Tenant',
            'Volume',
            'Size',
            'Status',
            'Progress',
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

    def print_snapshots_id(self, info, title=False):
        if title:
            self.my_output.default(
                'Volume Snapshot - Identifier [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'id',
            'name'
        ]

        headers = [
            'Id',
            'Name'
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
