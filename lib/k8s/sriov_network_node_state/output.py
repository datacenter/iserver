class K8sSriovNetworkNodeStateOutput():
    def __init__(self):
        pass

    def print_sriov_network_nodes_state(self, info, title=False):
        if title:
            self.my_output.default(
                'SR-IOV Network Node - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'syncStatusTick',
            'interface.name',
            'interface.vfUsage',
            'interface.totalVfs',
            'interface.pciAddress',
            'interface.driver',
            'interface.vendorT',
            'interface.deviceIdT',
            'interface.mac',
            'interface.mtu',
            'interface.linkSpeed'
        ]

        headers = [
            'Node',
            'Sync',
            'Interface',
            'VF Usage',
            'Total VFs',
            'PCI',
            'Driver',
            'Vendor',
            'Device',
            'MAC',
            'MTU',
            'Speed'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['namespace_nameT', 'interface']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_sriov_network_nodes_state_vfg(self, info, title=False):
        new_info = []
        for item in info:
            for interface in item['interface']:
                new_item = {}
                new_item['namespace'] = item['namespace']
                new_item['name'] = item['name']
                new_item['interfaceName'] = interface['name']
                new_item['vfGroups'] = interface['vfGroups']
                new_info.append(
                    new_item
                )

        if title:
            self.my_output.default(
                'SR-IOV Network Node - VF Groups [#%s]' % (len(new_info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'interfaceName',
            'vfGroups.deviceType',
            'vfGroups.policyName',
            'vfGroups.resourceName',
            'vfGroups.vfRange'
        ]

        headers = [
            'Node',
            'Interface',
            'Device Type',
            'Policy',
            'Resource',
            'VF Range'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['vfGroups']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_sriov_network_nodes_state_vf(self, info, title=False):
        new_info = []
        for item in info:
            for interface in item['interface']:
                new_item = {}
                new_item['namespace'] = item['namespace']
                new_item['name'] = item['name']
                new_item['interfaceName'] = interface['name']
                new_item['vfs'] = interface['vfs']
                new_info.append(
                    new_item
                )

        if title:
            self.my_output.default(
                'SR-IOV Network Node - VF [#%s]' % (len(new_info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'interfaceName',
            'vfs.vfId',
            'vfs.nameT',
            'vfs.macT',
            'vfs.mtuT',
            'vfs.pciAddress',
            'vfs.driver'
        ]

        headers = [
            'Node',
            'Interface',
            'VF ID',
            'VF Name',
            'MAC',
            'MTU',
            'PCI',
            'Driver'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['vfs']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
