class K8sSriovNetworkNodePolicyOutput():
    def __init__(self):
        pass

    def print_sriov_network_node_policies(self, info, title=False):
        if title:
            self.my_output.default(
                'SR-IOV Network Node Policy [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace',
            'name',
            'resource_nameT',
            'device_typeT',
            'node_selectorT',
            'nic_selectorT',
            'vfs',
            'priorityT',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Resource',
            'Device Type',
            'Node',
            'NIC',
            'VF',
            'Prio',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['node_selectorT', 'nic_selectorT']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
