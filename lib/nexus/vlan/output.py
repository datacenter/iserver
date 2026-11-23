class VlanOutput():
    def __init__(self):
        pass

    def print_vlans(self, info, title=False):
        if title:
            self.my_output.default(
                'VLAN [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'id',
            'name',
            'state',
            'type',
            'mode',
            'interfaces'
        ]

        headers = [
            'Device',
            'VLAN ID',
            'Name',
            'State',
            'Media Type',
            'Mode',
            'Interfaces'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['interfaces']
            ),
            order=order,
            headers=headers,
            underline=True,
            table=True,
            row_separator=True
        )
