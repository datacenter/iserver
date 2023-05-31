class PoolVlanOutput():
    def __init__(self):
        pass

    def print_pool_vlan(self, info):
        self.print_pool_vlans(
            [info]
        )

    def print_pool_vlans(self, info):
        if len(info) == 0:
            return

        order = [
            'name',
            'allocMode',
            'fvnsEncapBlk.blockInfo',
            'fvnsEncapBlk.role',
            'fvnsRtVlanNs.domainName',
            'epgUsage'
        ]

        headers = [
            'VLAN Pool Name',
            'Allocation Mode',
            'Encapsulation Block',
            'Role',
            'Domain',
            'EPG Usage'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['fvnsEncapBlk', 'fvnsRtVlanNs']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
