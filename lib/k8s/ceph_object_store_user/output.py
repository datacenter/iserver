class K8sCephObjectStoreUserOutput():
    def __init__(self):
        pass

    def print_ceph_object_store_users(self, info, title=False):
        if title:
            self.my_output.default(
                'CephObjectStoreUser [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'phase',
            'readyTick',
            'secret'
        ]

        headers = [
            'Ceph Object Store User',
            'Phase',
            'Ready',
            'Secret'
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
