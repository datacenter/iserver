class InterfaceTransOutput():
    def __init__(self):
        pass

    def print_interfaces_trans(self, info, title=False):
        if title:
            self.my_output.default(
                'Interface Transceiver [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'interface',
            'sfp',
            'type',
            'name',
            'partnum',
            'serialnum',
            'cisco_product_id'
        ]

        headers = [
            'Device',
            'Interface',
            'SFP',
            'Type',
            'Name',
            'PN',
            'SN',
            'PID'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True,
            cast_none=True
        )
