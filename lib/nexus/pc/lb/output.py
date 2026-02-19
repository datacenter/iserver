class PcLbOutput():
    def __init__(self):
        pass

    def print_pc_lb(self, info, title=False):
        if title:
            self.my_output.default(
                'Port Channel Load Balance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'non-ip-sel',
            'non-ip-val',
            'ipv4-sel',
            'ipv4-val',
            'module.id',
            'module.non-ip-sel',
            'module.non-ip-val',
            'module.ipv4-sel',
            'module.ipv4-val'
        ]

        headers = [
            'Device',
            'Non-IP Sel',
            'Non-IP Val',
            'IP Sel',
            'IP Val',
            'Module',
            'Non-IP Sel',
            'Non-IP Val',
            'IP Sel',
            'IP Val',
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['module']
            ),
            order=order,
            headers=headers,
            underline=True,
            table=True,
            allow_order_subkeys=True
        )
