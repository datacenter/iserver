class K8sCephObjectStoreOutput():
    def __init__(self):
        pass

    def print_ceph_object_stores(self, info, title=False):
        if title:
            self.my_output.default(
                'CephObjectStore [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'phase',
            'readyTick'
        ]

        headers = [
            'Ceph Object Store',
            'Phase',
            'Ready'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
