class InterfaceVlanStatsOutput():
    def __init__(self):
        pass

    def print_vlan_stats(self, info):
        order = [
            'adminSt',
            'operSt',
            'id',
            'encap',
            'epgDn'
        ]

        headers = [
            'Admin State',
            'Oper State',
            'Internal VLAN',
            'Encapsulation VLAN',
            'EPG Dn'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
