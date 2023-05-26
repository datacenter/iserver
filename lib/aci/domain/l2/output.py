class DomainL2Output():
    def __init__(self):
        pass

    def print_domains_l2(self, info):
        if len(info) == 0:
            self.my_output.default('No domain found')
            return

        for item in info:
            item['fvnsEncapBlk'] = []
            if item['vlan_info'] is not None:
                item['fvnsEncapBlk'] = item['vlan_info']['fvnsEncapBlk']

        order = [
            'name',
            'aaep_names',
            'vlan',
            'fvnsEncapBlk.blockInfo',
            'vlan_info.epgUsage'
        ]

        headers = [
            'Domain Name',
            'AAEP',
            'VLAN Pool',
            'Encapsulation Block',
            'EPG Usage'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['aaep_names', 'fvnsEncapBlk']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
