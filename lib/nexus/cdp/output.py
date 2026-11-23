class CdpOutput():
    def __init__(self):
        pass

    def print_cdps(self, info, title=False):
        if title:
            self.my_output.default(
                'CDP [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'intf_id',
            'sysname',
            'platform_id',
            'port_id'
        ]

        headers = [
            'Device',
            'Local Interface',
            'Device Name',
            'Device ID',
            'Port ID'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
