class VersionOutput():
    def __init__(self):
        pass

    def print_versions(self, info, title=False):
        if title:
            self.my_output.default(
                'Version [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'chassis_id',
            'cpu_name',
            'nxos_ver_str'
        ]

        headers = [
            'Device',
            'HW',
            'CPU',
            'SW'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
