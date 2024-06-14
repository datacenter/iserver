class LacpOutput():
    def __init__(self):
        pass

    def print_lacps(self, info, title=False):
        if title:
            self.my_output.default(
                'LACP [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'interface',
            'port.port',
            'port.partner_mac',
            'port.partner_port_num',
            'port.partner_port_state'
        ]

        headers = [
            'Device',
            'Interface',
            'Port',
            'Partner MAC',
            'Partner Port',
            'Partner State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['port']
            ),
            order=order,
            headers=headers,
            underline=True,
            table=True,
            allow_order_subkeys=True
        )
