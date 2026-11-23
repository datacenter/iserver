class PcStateOutput():
    def __init__(self):
        pass

    def print_pc_state(self, info, title=False):
        if title:
            self.my_output.default(
                'Port Channel State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'group',
            'port-channel',
            'layer',
            'status',
            'prtcl',
            'member.port',
            'member.status'
        ]

        headers = [
            'Device',
            'Group',
            'Interface',
            'Layer',
            'Status',
            'Type',
            'Protocol',
            'Port',
            'Status'
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
