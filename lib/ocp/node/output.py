class OcpNodeOutput():
    def __init__(self):
        pass

    def print_ocp_nodes_list(self, info):
        order = [
            'cluster',
            'name',
            'ready',
            'mcp.tick',
            'cnv.tick',
            'roles',
            'age'
        ]

        headers = [
            'Cluster',
            'Node',
            'Status',
            'MCP',
            'CNV',
            'Roles',
            'Age'
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

    def print_ocp_nodes_version(self, info, title=False):
        if title:
            self.my_output.default('Cluster Node Software Versions', underline=True, before_newline=True)

        order = [
            'cluster',
            'name',
            'node_info.os_image',
            'node_info.kernel_version',
            'node_info.kubelet_version',
            'node_info.container_runtime_version'
        ]

        headers = [
            'Cluster',
            'Node',
            'OS',
            'Kernel',
            'Kubelet',
            'CRI-O'
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

    def print_ocp_nodes_label(self, info, title=False):
        if title:
            self.my_output.default('Cluster Node Labels', underline=True, before_newline=True)

        order = [
            'cluster',
            'name',
            'labels.key',
            'labels.value'
        ]

        headers = [
            'Cluster',
            'Node',
            'Label Key',
            'Label Value'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['labels']
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
