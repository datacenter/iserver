class K8sCephFilesystemOutput():
    def __init__(self):
        pass

    def print_ceph_filesystems(self, info, title=False):
        if title:
            self.my_output.default(
                'CephFilesystem [#%s]' % (len(info)),
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
            'Ceph Filesystem',
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
