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
            'sriov_network_count',
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
            'Srn',
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

    def print_sriov_network_node_policies_srn(self, info, title=False):
        if title:
            self.my_output.default(
                'SR-IOV Network Node Policy - SR-IOV Network [#%s]' % (len(info)),
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
            'sriov_network.namespace_name',
            'sriov_network.vlanT',
            'sriov_network.age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Resource',
            'Srn',
            'VLAN',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['sriov_network']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
