class K8sSriovNetworkOutput():
    def __init__(self):
        pass

    def print_sriov_networks(self, info, title=False):
        if title:
            self.my_output.default(
                'SR-IOV Network [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['namespace_nameT'] = []
            item['namespace_nameT'].append(
                item['namespace']
            )
            item['namespace_nameT'].append(
                item['name']
            )

        order = [
            'namespace_nameT',
            'network_namespace',
            'resource_name',
            'vlanT',
            'spoof',
            'trust',
            'capabilitiesT',
            'ipamT',
            'age'
        ]

        headers = [
            'SR-IOV Network',
            'NetNamespace',
            'Resource',
            'VLAN',
            'Spoof',
            'Trust',
            'Caps',
            'IPAM',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['namespace_nameT', 'ipamT', 'capabilitiesT']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
