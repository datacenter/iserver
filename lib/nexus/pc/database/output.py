class PcDatabaseOutput():
    def __init__(self):
        pass

    def print_pc_database(self, info, title=False):
        if title:
            self.my_output.default(
                'Port Channel Database [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'interface',
            'total-ports',
            'total-up-ports',
            'age-of-channel',
            'member.port',
            'member.mode',
            'member.status'
        ]

        headers = [
            'Device',
            'Interface',
            'Count',
            'Up',
            'Age',
            'Port',
            'Mode',
            'State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['member']
            ),
            order=order,
            headers=headers,
            underline=True,
            table=True,
            row_separator=True,
            allow_order_subkeys=True
        )
