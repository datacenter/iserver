class K8sNodeOutput():
    def __init__(self):
        pass

    def print_nodes_state(self, info, title=False):
        if title:
            self.my_output.default(
                'Node - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'readyTick',
            'memoryTick',
            'diskTick',
            'pidTick',
            'cnvTick',
            'mcpTick',
            'role',
            'ipT',
            'age'
        ]

        headers = [
            'Name',
            'Ready',
            'Memory',
            'Disk',
            'PID',
            'CNV',
            'MCP',
            'Role',
            'IP',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['ipT', 'role']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_nodes_version(self, info, title=False):
        if title:
            self.my_output.default(
                'Node - Versions [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'node_info.kubelet_version',
            'node_info.os_image',
            'node_info.kernel_version',
            'node_info.container_runtime_version'
        ]

        headers = [
            'Name',
            'Version',
            'OS Image',
            'Kernel Version',
            'Container Runtime'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_nodes_capacity(self, info, title=False):
        if title:
            self.my_output.default(
                'Node - Capacity [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'capacity_pod',
            'capacity_cpu',
            'capacity_memory',
            'capacity_storage',
            'capacity_hp2m',
            'capacity_hp1g',
            'capacity_kubevirt',
            'capacity_vendor'
        ]

        headers = [
            'Name',
            'POD',
            'CPU',
            'Memory',
            'Storage',
            'HP 2Mi',
            'HP 1Gi',
            'Kubevirt',
            'Vendor'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['capacity_vendor', 'capacity_kubevirt']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_nodes_label(self, info, title=False):
        if title:
            self.my_output.default(
                'Node - Label [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['labelT'] = []
            for key in item['label']:
                label_info = {}
                label_info['key'] = key
                label_info['value'] = item['label'][key]
                if label_info['value'] == '':
                    label_info['value'] = '--'

                item['labelT'].append(
                    label_info
                )

        order = [
            'name',
            'labelT.key',
            'labelT.value'
        ]

        headers = [
            'Name',
            'Label Key',
            'Label Value'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['labelT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_ocp_nodes_sriov_phy(self, info, title=False):
        if title:
            self.my_output.default('SR-IOV Node Interfaces', underline=True, before_newline=True)

        order = [
            'cluster',
            'name',
            'sriov_phy.name',
            'sriov_phy.state',
            'sriov_phy.flags',
            'sriov_phy.mtu',
            'sriov_phy.mac',
            'sriov_phy.numa',
            'sriov_phy.pci.driver',
            'sriov_phy.pci.slot',
            'sriov_phy.policyCount',
            'sriov_phy.numVfs',
            'sriov_phy.vfUsage'
        ]

        headers = [
            'Cluster',
            'Node',
            'Interface',
            'State',
            'Flags',
            'MTU',
            'MAC',
            'Numa',
            'Driver',
            'PCI',
            'Policies',
            'Num VFs',
            'Policies VF Usage'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['sriov_phy']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_ocp_nodes_sriov_policy(self, info, title=False):
        if title:
            self.my_output.default('SR-IOV Node Policy', underline=True, before_newline=True)

        order = [
            'cluster',
            'name',
            'sriov_policy.policyName',
            'sriov_policy.selector',
            'sriov_policy.name',
            'sriov_policy.deviceType',
            'sriov_policy.resourceName',
            'sriov_policy.numVfs',
            'sriov_policy.vfUsage'
        ]

        headers = [
            'Cluster',
            'Node',
            'Policy',
            'Selector',
            'Interface',
            'Device Type',
            'Resource Name',
            'Num VFs',
            'Policy VF Usage'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['sriov_policy']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_ocp_nodes_sriov_network(self, info, title=False):
        if title:
            self.my_output.default('SR-IOV Network', underline=True, before_newline=True)

        order = [
            'cluster',
            'name',
            'sriov_network.namespace_name',
            'sriov_network.policyName',
            'sriov_network.deviceType',
            'sriov_network.interfaceName',
            'sriov_network.vf',
            'sriov_network.ipamTick',
            'sriov_network.vlan',
            'sriov_network.usedBy'
        ]

        headers = [
            'Cluster',
            'Node',
            'SR-IOV Network',
            'Policy Name',
            'Device Type',
            'Interface',
            'VF',
            'IPAM',
            'VLAN',
            'Used By'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['sriov_network']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_ocp_nodes_sriov_vf(self, info, title=False):
        if title:
            self.my_output.default('SR-IOV Node Interface VFs', underline=True, before_newline=True)

        order = [
            'cluster',
            'name',
            'sriov_vf.name',
            'sriov_vf.index',
            'sriov_vf.mac',
            'sriov_vf.vlan',
            'sriov_vf.spoof',
            'sriov_vf.link',
            'sriov_vf.trust',
            'sriov_vf.policyName',
            'sriov_vf.usedTick',
            'sriov_vf.networkName',
            'sriov_vf.usedBy'
        ]

        headers = [
            'Cluster',
            'Node',
            'Interface',
            'VF Index',
            'MAC',
            'VLAN',
            'Spoof',
            'Link',
            'Trust',
            'Policy Name',
            'Used',
            'Network Name',
            'Used By'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['sriov_vf']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
