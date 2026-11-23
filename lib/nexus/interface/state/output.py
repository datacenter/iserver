class InterfaceStateOutput():
    def __init__(self):
        pass

    def print_interfaces(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'interface',
            'admin_state',
            'state',
            'eth_mtu',
            'eth_duplex',
            'eth_speed'
        ]

        headers = [
            'Device',
            'Interface',
            'Admin',
            'Oper',
            'MTU',
            'Duplex',
            'Speed'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
