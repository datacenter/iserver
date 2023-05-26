class PoolVlanOutput():
    def __init__(self):
        pass

    def print_pool_vlan(self, info):
        self.print_pool_vlans(
            [info]
        )

        if len(info['epg']) > 0:
            self.print_domain_vmm_epg(
                info['epg']
            )

    def print_pool_vlans(self, pool_vlans, verbose=False):
        if len(pool_vlans) == 0:
            self.my_output.default('No vlan pool found')
            return

        if verbose:
            for pool_vlan in pool_vlans:
                self.print_pool_vlan(pool_vlan)
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
                pool_vlans,
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
