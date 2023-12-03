class MacOutput():
    def __init__(self):
        pass

    def print_macs(self, info, title=False):
        if title:
            self.my_output.default(
                'MAC [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'vlan',
            'mac_addr',
            'type',
            'age',
            'is_secure',
            'is_ntfy',
            'port'
        ]

        headers = [
            'Device',
            'VLAN',
            'MAC',
            'Type',
            'Age',
            'Sec',
            'Ntfy',
            'Port'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
