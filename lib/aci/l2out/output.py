class L2OutOutput():
    def __init__(self):
        pass

    def print_l2outs(self, info):
        order = [
            'nameTenant',
            'targetDscp',
            'fvBD.nameTenant',
            'fvBD.encap',
            'l2extDomP.name',
            'path'
        ]

        headers = [
            'L2 Out',
            'Target DSCP',
            'Bridge Domain',
            'Encapsulation',
            'Ext Phy Domain',
            'Path'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['path']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
