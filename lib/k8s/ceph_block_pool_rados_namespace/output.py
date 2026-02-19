class K8sCephBlockPoolRadosNamespaceOutput():
    def __init__(self):
        pass

    def print_ceph_block_pool_rados_namespaces(self, info, title=False):
        if title:
            self.my_output.default(
                'CephBlockPoolRadosNamespace [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name'
        ]

        headers = [
            'Ceph Block Pool Rados Namespace'
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
