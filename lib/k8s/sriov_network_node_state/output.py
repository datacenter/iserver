from lib import filter_helper


class K8sSriovNetworkNodeStateOutput():
    def __init__(self):
        pass

    def print_sriov_network_nodes_state(self, info, title=False):
        if title:
            self.my_output.default(
                'SR-IOV Network Node State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_items = []
        for item in info:
            for interface_info in item['interface']:
                new_item = {}
                new_item['node'] = item['name']
                new_item['syncStatusTick'] = item['syncStatusTick']
                new_item['policyCount'] = len(
                    interface_info['vfGroups']
                )
                for key in interface_info:
                    new_item[key] = interface_info[key]

                new_item['deviceIdTT'] = filter_helper.get_string_chunks(
                    new_item['deviceIdT'],
                    30
                )

                new_items.append(
                    new_item
                )

        order = [
            'node',
            'syncStatusTick',
            'name',
            'policyCount',
            'vfUsage',
            'pciAddress',
            'driver',
            'vendorT',
            'deviceIdTT',
            'mac',
            'mtu',
            'linkSpeed'
        ]

        headers = [
            'Node',
            'Sync',
            'Intf',
            'Pol',
            'VF',
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
                new_items,
                order,
                ['deviceIdTT']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_sriov_network_nodes_state_policy(self, info, title=False):
        new_info = []
        for item in info:
            for interface in item['interface']:
                new_item = {}
                new_item['namespace'] = item['namespace']
                new_item['name'] = item['name']
                new_item['interfaceName'] = interface['name']
                new_item['vfGroups'] = interface['vfGroups']
                if len(new_item['vfGroups']) == 0:
                    empty = {}
                    for key in ['deviceType', 'policyName', 'resourceName', 'vfRange']:
                        empty[key] = '--'
                    new_item['vfGroups'].append(empty)
                new_info.append(
                    new_item
                )

        if title:
            self.my_output.default(
                'SR-IOV Network Node State - VF Groups [#%s]' % (len(new_info)),
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
                if len(new_item['vfs']) == 0:
                    empty = {}
                    for key in ['vfId', 'nameT', 'macT', 'mtuT', 'pciAddress', 'driver']:
                        empty[key] = '--'
                    new_item['vfs'].append(empty)
                new_info.append(
                    new_item
                )

        if title:
            self.my_output.default(
                'SR-IOV Network Node State - VF [#%s]' % (len(new_info)),
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
