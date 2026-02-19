class VrfOutput():
    def __init__(self):
        pass

    def print_vrfs(self, info, title=False):
        if title:
            self.my_output.default(
                'VRF [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'vrf_id',
            'vrf_name',
            'vrf_state',
            'rd',
            'vni',
            'table.af'
        ]

        headers = [
            'Device',
            'VRF ID',
            'Name',
            'State',
            'RD',
            'VNI',
            'AF'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['table']
            ),
            order=order,
            headers=headers,
            underline=True,
            table=True,
            allow_order_subkeys=True,
            row_separator=True
        )
