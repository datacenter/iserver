class LinuxLvOutput():
    def __init__(self):
        pass

    def print_linux_lv(self, info, title=False, check_pvc=True, server=None):
        if title:
            if server is None:
                self.my_output.default(
                    'Logical Volumes (LVM)',
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Logical Volumes (LVM) [%s]' % (server),
                    underline=True,
                    before_newline=True
                )

        order = [
            'names',
            'vg_name',
            'pool_lv',
            'block_device',
            'lv_size',
            'data_percentT',
            'layout',
            'role',
            'snapshotCountT'
        ]

        headers = [
            'LV Name',
            'VG',
            'LV Pool',
            'Dev',
            'LV Size',
            'MSize',
            'Layout',
            'Role',
            'Snap'
        ]

        is_openshift = False
        if len(info) > 0 and 'orphan' in info[0]:
            is_openshift = True
            order.append('usage')
            headers.append('K8s Usage')

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['names', 'role', 'layout']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

        if check_pvc and is_openshift:
            orphan = False
            for item in info:
                if item['is_pool']:
                    continue

                orphan = orphan or item['orphan']

            if orphan:
                self.my_output.default(
                    '%s some logical volumes not backed with kube resources' % (
                        self.my_output.add_color('[WARNING]', 'Red')
                    ),
                    before_newline=True
                )
