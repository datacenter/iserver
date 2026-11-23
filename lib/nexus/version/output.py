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
            'nxos_ver_str',
            'chassis_id',
            'uptime',
            'cpu_name',
            'memory_size'
        ]

        headers = [
            'Device',
            'SW',
            'HW',
            'Uptime',
            'CPU',
            'Memory'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
