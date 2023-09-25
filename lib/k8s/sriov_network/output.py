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

        order = [
            'namespace',
            'name',
            'network_namespace',
            'resource_name',
            'vlanT',
            'ipamT',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Network Namespace',
            'Resource',
            'VLAN',
            'IPAM',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['ipamT']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
