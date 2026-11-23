class LinuxVgOutput():
    def __init__(self):
        pass

    def print_linux_vg(self, info, title=False, server=None):
        if title:
            if server is None:
                self.my_output.default(
                    'Volume Groups (LVM)',
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Volume Groups (LVM) [%s]' % (server),
                    underline=True,
                    before_newline=True
                )

        order = [
            'vg_name',
            'pv_count',
            'lv_count',
            'vg_attr',
            'vg_size',
            'vg_free'
        ]

        headers = [
            'VG',
            '#PV',
            '#LV',
            'Attr',
            'VSize',
            'VFree'
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
