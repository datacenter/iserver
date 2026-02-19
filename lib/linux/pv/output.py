class LinuxPvOutput():
    def __init__(self):
        pass

    def print_linux_pv(self, info, title=False, server=None):
        if title:
            if server is None:
                self.my_output.default(
                    'Physical Volume (LVM)',
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Physical Volume (LVM) [%s]' % (server),
                    underline=True,
                    before_newline=True
                )

        order = [
            'pv_name',
            'vg_name',
            'pv_fmt',
            'pv_attr',
            'pv_size',
            'pv_free'
        ]

        headers = [
            'PV',
            'VG',
            'Fmt',
            'Attr',
            'PSize',
            'PFree'
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
