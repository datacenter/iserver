class PcTrafficOutput():
    def __init__(self):
        pass

    def print_pc_traffic(self, info, title=False):
        if title:
            self.my_output.default(
                'Port Channel Traffic [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'chanId',
            'port',
            'rx-ucst',
            'tx-ucst',
            'rx-mcst',
            'tx-mcst',
            'rx-bcst',
            'tx-bcst'
        ]

        headers = [
            'Device',
            'chanId',
            'port',
            'rx-ucst',
            'tx-ucst',
            'rx-mcst',
            'tx-mcst',
            'rx-bcst',
            'tx-bcst'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
