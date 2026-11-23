class MdK8sNodeOutput():
    def __init__(self):
        pass

    def add_k8s_node_network_dns(self, nns_info):
        if 'dns' not in nns_info or nns_info['dns'] is None:
            return

        self.my_output.print_stream('## DNS Settings', 'output')

        self.my_output.print_stream('- DNS Server', 'output')
        for server in nns_info['dns']['server']:
            self.my_output.print_stream('\t- %s' % (server), 'output')

        self.my_output.print_stream('- Search Domain', 'output')
        for search in nns_info['dns']['search']:
            self.my_output.print_stream('\t- %s' % (search), 'output')

    def add_k8s_node_network_route(self, nns_info):
        if 'route' not in nns_info or nns_info['route'] is None:
            return

        self.my_output.print_stream('## Route Table', 'output')

        order = [
            'Table ID',
            'Destination',
            'Next Hop',
            'Interface'
        ]
        self.print_table_header(order)

        for item in nns_info['route']:
            line = ''
            line = self.add_column(line, item['table-id'])
            line = self.add_column(line, item['destination'])
            line = self.add_column(line, item['next-hop-address'])
            line = self.add_column(line, item['next-hop-interface'])
            self.my_output.print_stream(line, 'output')

    def add_k8s_node_network_bond_interface_list(self, nns_info):
        if 'interface' not in nns_info or nns_info['interface'] is None:
            return

        bond_interfaces = []
        bond_names = []
        for item in nns_info['interface']:
            if item['lacp_enabled']:
                bond_interfaces.append(
                    item
                )
                bond_names.append(
                    item['name']
                )

        for item in nns_info['interface']:
            if item['type'] == 'vlan' and item['vlan_base'] in bond_names:
                item['lacp_port'] = []
                bond_interfaces.append(
                    item
                )

        if len(bond_interfaces) == 0:
            return

        bond_interfaces = sorted(
            bond_interfaces,
            key=lambda i: i['name']
        )

        self.my_output.print_stream('## Bond Interface (nmstate)', 'output')

        order = [
            'Name',
            'Type',
            'State',
            'Def',
            'MAC',
            'IP',
            'LACP Ports'
        ]
        self.print_table_header(order)

        for item in bond_interfaces:
            line = ''
            line = self.add_column(
                line,
                '[%s](./%s-eth.md)' % (item['name'], item['hash'])
            )
            line = self.add_column(line, item['type'])
            line = self.add_column_tick_string(line, 'up', item['state'])
            line = self.add_column_tick_bool(line, item['default'])
            line = self.add_column(line, item['mac'])
            line = self.add_column(line, ', '.join(item['address']))
            line = self.add_column(line, ', '.join(item['lacp_port']))
            self.my_output.print_stream(line, 'output')

    def add_k8s_node_network_ethernet_interface_list(self, nns_info):
        if 'interface' not in nns_info or nns_info['interface'] is None:
            return

        if len(nns_info['interface']) == 0:
            return

        self.my_output.print_stream('## Ethernet Interface (nmstate)', 'output')

        order = [
            'Name',
            'State',
            'Def',
            'MAC',
            'IP',
            'LACP',
            'LLDP',
            'SRIOV',
            'VF'
        ]
        self.print_table_header(order)

        for item in nns_info['interface']:
            if item['type'] != 'ethernet':
                continue

            line = ''
            line = self.add_column(
                line,
                '[%s](./%s-eth.md)' % (item['name'], item['hash'])
            )
            line = self.add_column_tick_string(line, 'up', item['state'])
            line = self.add_column_tick_bool(line, item['default'])
            line = self.add_column(line, item['mac'])
            line = self.add_column(line, ', '.join(item['address']))
            line = self.add_column(line, item['lacp_parent'])
            line = self.add_column_tick_bool(line, item['lldp_enabled'])
            line = self.add_column_tick_bool(line, item['ethernet_sriov_enabled'])
            line = self.add_column(line, item['ethernet_sriov_vfs_summary'])
            self.my_output.print_stream(line, 'output')

    def add_k8s_node_network_ethernet_interface_fabric(self, nns_info):
        if 'interface' not in nns_info or nns_info['interface'] is None:
            return

        if len(nns_info['interface']) == 0:
            return

        self.my_output.print_stream('## Ethernet Interface (fabric)', 'output')

        order = [
            'Name',
            'State',
            'Def',
            'PCI',
            'Model',
            'Interface',
            'Fabric',
            'Device',
            'Interface',
            'LLDP'
        ]
        self.print_table_header(order)

        for item in nns_info['interface']:
            if item['type'] != 'ethernet':
                continue

            line = ''
            line = self.add_column(
                line,
                '[%s](./%s-eth.md)' % (item['name'], item['hash'])
            )
            line = self.add_column_tick_string(line, 'up', item['state'])
            line = self.add_column_tick_bool(line, item['default'])

            if 'Server' not in item or item['Server'] is None:
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                self.my_output.print_stream(line, 'output')
                continue

            if item['Server']['AdapterPciSlot'] is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, item['Server']['AdapterPciSlot'])

            line = self.add_column(
                line,
                self.get_adapter_model(item['Server']['AdapterModel'])
            )
            line = self.add_column(line, item['Server']['InterfaceName'])

            if len(item['Server']['intfRef']) == 0:
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                self.my_output.print_stream(line, 'output')
                continue

            line = self.add_column(line, item['Server']['intfRef'][0]['fabric'])

            if item['Server']['intfRef'][0]['type'] not in ['Nexus', 'ACI']:
                line = self.add_column(line, item['Server']['intfRef'][0]['device'])
                line = self.add_column(line, item['Server']['intfRef'][0]['intf'])
                line = self.add_column(line, '---', last=True)

            if item['Server']['intfRef'][0]['type'] == 'Nexus':
                line = self.add_column(
                    line,
                    '[%s](../../nexus/%s-eth.md)' % (
                        item['Server']['intfRef'][0]['device'],
                        item['Server']['intfRef'][0]['device']
                    )
                )
                line = self.add_column(
                    line,
                    '[%s](../../nexus/eth/%s.md)' % (
                        item['Server']['intfRef'][0]['intf'],
                        item['Server']['intfRef'][0]['intf_hash']
                    )
                )
                if item['Server']['intfRef'][0]['lldp_hash'] is None:
                    line = self.add_column(line, '---', last=True)
                else:
                    line = self.add_column(
                        line,
                        '[Link](../../nexus/lldp/%s.md)' % (
                            item['Server']['intfRef'][0]['lldp_hash']
                        ),
                        last=True
                    )

            if item['Server']['intfRef'][0]['type'] == 'ACI':
                line = self.add_column(
                    line,
                    '[%s](../../apic/%s-%s-phy.md)' % (
                        item['Server']['intfRef'][0]['device'],
                        item['Server']['intfRef'][0]['fabric'],
                        item['Server']['intfRef'][0]['device_name']
                    )
                )
                line = self.add_column(
                    line,
                    '[%s](../../apic/phy/%s.md)' % (
                        item['Server']['intfRef'][0]['intf'],
                        item['Server']['intfRef'][0]['intf_hash']
                    )
                )
                if item['Server']['intfRef'][0]['lldp_hash'] is None:
                    line = self.add_column(line, '---', last=True)
                else:
                    line = self.add_column(
                        line,
                        '[Link](../../apic/lldp/%s.md)' % (
                            item['Server']['intfRef'][0]['lldp_hash']
                        ),
                        last=True
                    )

            self.my_output.print_stream(line, 'output')

            if len(item['Server']['intfRef']) > 1:
                for i in range(len(item['Server']['intfRef'])):
                    if i == 0:
                        continue

                    line = ''
                    line = self.add_column(line, '')
                    line = self.add_column(line, '')
                    line = self.add_column(line, '')
                    line = self.add_column(line, '')
                    line = self.add_column(line, '')
                    line = self.add_column(line, '')
                    line = self.add_column(line, item['Server']['intfRef'][i]['fabric'])
                    if item['Server']['intfRef'][i]['type'] not in ['Nexus', 'ACI']:
                        line = self.add_column(line, item['Server']['intfRef'][i]['device'])
                        line = self.add_column(line, item['Server']['intfRef'][i]['intf'])
                        line = self.add_column(line, '---', last=True)

                    if item['Server']['intfRef'][i]['type'] == 'Nexus':
                        line = self.add_column(
                            line,
                            '[%s](../../nexus/%s-eth.md)' % (
                                item['Server']['intfRef'][i]['device'],
                                item['Server']['intfRef'][i]['device']
                            )
                        )
                        line = self.add_column(
                            line,
                            '[%s](../../nexus/eth/%s.md)' % (
                                item['Server']['intfRef'][i]['intf'],
                                item['Server']['intfRef'][i]['intf_hash']
                            )
                        )
                        if item['Server']['intfRef'][i]['lldp_hash'] is None:
                            line = self.add_column(line, '---', last=True)
                        else:
                            line = self.add_column(
                                line,
                                '[Link](../../nexus/lldp/%s.md)' % (
                                    item['Server']['intfRef'][i]['lldp_hash']
                                ),
                                last=True
                            )

                    if item['Server']['intfRef'][i]['type'] == 'ACI':
                        line = self.add_column(
                            line,
                            '[%s](../../apic/%s-%s-phy.md)' % (
                                item['Server']['intfRef'][i]['device'],
                                item['Server']['intfRef'][i]['fabric'],
                                item['Server']['intfRef'][i]['device_name']
                            )
                        )
                        line = self.add_column(
                            line,
                            '[%s](../../apic/phy/%s.md)' % (
                                item['Server']['intfRef'][i]['intf'],
                                item['Server']['intfRef'][i]['intf_hash']
                            )
                        )
                        if item['Server']['intfRef'][i]['lldp_hash'] is None:
                            line = self.add_column(line, '---', last=True)
                        else:
                            line = self.add_column(
                                line,
                                '[Link](../../apic/lldp/%s.md)' % (
                                    item['Server']['intfRef'][i]['lldp_hash']
                                ),
                                last=True
                            )

                    self.my_output.print_stream(line, 'output')

    def add_k8s_node_network_interface_ethernet_server(self, interface_info):
        if 'Server' not in interface_info or interface_info['Server'] is None:
            return

        self.my_output.print_stream('## Server', 'output')

        self.my_output.print_stream(
            '- Name: [%s](../../compute/%s-net.md)' % (
                interface_info['Server']['ServerName'],
                interface_info['Server']['ServerMoid']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- PCI: %s' % (interface_info['Server']['AdapterPciSlot']),
            'output'
        )
        self.my_output.print_stream(
            '- Adapter: %s' % (interface_info['Server']['AdapterModel']),
            'output'
        )
        self.my_output.print_stream(
            '- Interface: %s' % (interface_info['Server']['InterfaceDn']),
            'output'
        )

        if 'intfRef' in interface_info['Server'] and len(interface_info['Server']['intfRef']) > 0:
            self.my_output.print_stream('', 'output')

            order = [
                'Fabric',
                'Device',
                'Interface',
                'LLDP'
            ]
            self.print_table_header(order)

            for item in interface_info['Server']['intfRef']:
                line = ''
                line = self.add_column(line, item['fabric'])

                if item['type'] not in ['Nexus', 'ACI']:
                    line = self.add_column(line, item['device'])
                    line = self.add_column(line, item['intf'])
                    line = self.add_column(line, '---', last=True)

                if item['type'] == 'Nexus':
                    line = self.add_column(
                        line,
                        '[%s](../../nexus/%s-eth.md)' % (
                            item['device'],
                            item['device']
                        )
                    )
                    line = self.add_column(
                        line,
                        '[%s](../../nexus/eth/%s.md)' % (
                            item['intf'],
                            item['intf_hash']
                        )
                    )
                    if item['lldp_hash'] is None:
                        line = self.add_column(line, '---', last=True)
                    else:
                        line = self.add_column(
                            line,
                            '[Link](../../nexus/lldp/%s.md)' % (
                                item['lldp_hash']
                            ),
                            last=True
                        )

                if item['type'] == 'ACI':
                    line = self.add_column(
                        line,
                        '[%s](../../apic/%s-%s-phy.md)' % (
                            item['device'],
                            item['fabric'],
                            item['device_name']
                        )
                    )
                    line = self.add_column(
                        line,
                        '[%s](../../apic/phy/%s.md)' % (
                            item['intf'],
                            item['intf_hash']
                        )
                    )
                    if item['lldp_hash'] is None:
                        line = self.add_column(line, '---', last=True)
                    else:
                        line = self.add_column(
                            line,
                            '[Link](../../apic/lldp/%s.md)' % (
                                item['lldp_hash']
                            ),
                            last=True
                        )

                self.my_output.print_stream(line, 'output')

    def add_k8s_node_network_interface_ethernet_ethtool(self, interface_info):
        if 'ethtool' not in interface_info or interface_info['ethtool'] is None:
            return

        self.my_output.print_stream('## Ethtool', 'output')

        order = [
            'Type',
            'Key',
            'Value'
        ]
        self.print_table_header(order)

        for key in interface_info['ethtool']:
            line = ''
            if len(key.split(':')) == 1:
                line = self.add_column(line, key)
                line = self.add_column(line, '---')
            if len(key.split(':')) == 2:
                line = self.add_column(line, key.split(':')[0])
                line = self.add_column(line, key.split(':')[1])
            if len(key.split(':')) > 2:
                line = self.add_column(line, key.split(':')[0])
                line = self.add_column(line, ':'.join(key.split(':')[1:]))

            if isinstance(interface_info['ethtool'][key], bool):
                line = self.add_column_tick_bool(line, interface_info['ethtool'][key], last=True)
            else:
                line = self.add_column(line, interface_info['ethtool'][key], last=True)

            self.my_output.print_stream(line, 'output')

    def add_k8s_node_network_interface_ethernet_ip(self, interface_info):
        self.my_output.print_stream('## IP Settings', 'output')

        self.my_output.print_stream('### IPv4', 'output')
        if interface_info['v4enabled']:
            self.my_output.print_stream('- Enabled :white_check_mark:', 'output')
            if interface_info['v4dhcp']:
                self.my_output.print_stream('- DHCP :white_check_mark:', 'output')
            else:
                self.my_output.print_stream('- DHCP :x:', 'output')

            if len(interface_info['v4address']) == 0:
                self.my_output.print_stream('- Address: ---', 'output')
            else:
                self.my_output.print_stream('- Address: %s' % (', '.join(interface_info['v4address'])), 'output')
        else:
            self.my_output.print_stream('- Enabled :x:', 'output')

        self.my_output.print_stream('### IPv6', 'output')
        if interface_info['v6enabled']:
            self.my_output.print_stream('- Enabled :white_check_mark:', 'output')
            if interface_info['v6dhcp']:
                self.my_output.print_stream('- DHCP :white_check_mark:', 'output')
            else:
                self.my_output.print_stream('- DHCP :x:', 'output')

            if len(interface_info['v6address']) == 0:
                self.my_output.print_stream('- Address: ---', 'output')
            else:
                self.my_output.print_stream('- Address: %s' % (', '.join(interface_info['v6address'])), 'output')
        else:
            self.my_output.print_stream('- Enabled :x:', 'output')

    def add_k8s_node_network_interface_ethernet_sriov(self, interface_info):
        if not interface_info['ethernet_sriov_enabled']:
            return

        if interface_info['ethernet_sriov_vfs_count'] == 0:
            return

        if 'ethernet_sriov_vfs' not in interface_info:
            return

        if len(interface_info['ethernet_sriov_vfs']) == 0:
            return

        self.my_output.print_stream('## SRIOV VF', 'output')

        order = [
            'ID',
            'Interface',
            'MAC',
            'Min Tx',
            'Max Tx',
            'QoS',
            'Spoof',
            'Trust',
            'VLAN ID',
            'VLAN Proto'
        ]
        self.print_table_header(order)

        for item in interface_info['ethernet_sriov_vfs']:
            line = ''
            line = self.add_column(line, item['id'])
            if 'iface-name' in item:
                line = self.add_column(line, item['iface-name'])
            else:
                line = self.add_column(line, '---')
            line = self.add_column(line, item['mac-address'])
            line = self.add_column(line, item['max-tx-rate'])
            line = self.add_column(line, item['min-tx-rate'])
            line = self.add_column(line, item['qos'])
            line = self.add_column_tick_bool(line, item['spoof-check'])
            line = self.add_column_tick_bool(line, item['trust'])
            line = self.add_column(line, item['vlan-id'])
            line = self.add_column(line, item['vlan-proto'])
            self.my_output.print_stream(line, 'output')

    def print_k8s_node_network_interface_ethernet_details(self, cluster_name, nns_info, interface_info):
        self.print_page_header('Kubernetes Node - Ethernet Interface')
        self.my_output.print_stream('## Overview', 'output')
        self.my_output.print_stream('', 'output')
        self.my_output.print_stream('- Cluster: [%s](../nodes-%s.md)' % (cluster_name, cluster_name), 'output')
        self.my_output.print_stream('- Node: [%s](./%s-net.md)' % (nns_info['owner_name'], nns_info['node_hash']), 'output')
        self.my_output.print_stream('- Interface: %s' % (interface_info['name']), 'output')

        if interface_info['state']:
            self.my_output.print_stream('- State :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- State :x:', 'output')

        self.my_output.print_stream('- MAC: %s' % (interface_info['mac']), 'output')
        self.my_output.print_stream('- MTU: %s' % (interface_info['mtu']), 'output')
        self.my_output.print_stream('- Mode Auto: %s' % (interface_info['ethernet_auto']), 'output')
        self.my_output.print_stream('- Speed: %s' % (interface_info['ethernet_speed']), 'output')
        self.my_output.print_stream('- Duplex: %s' % (interface_info['ethernet_duplex']), 'output')
        if interface_info['ethernet_sriov_enabled']:
            self.my_output.print_stream('- SRIOV :white_check_mark:', 'output')
            self.my_output.print_stream('- VF Summary: %s' % (interface_info['ethernet_sriov_vfs_summary']), 'output')
        else:
            self.my_output.print_stream('- SRIOV :x:', 'output')

        self.add_k8s_node_network_interface_ethernet_server(interface_info)
        self.add_k8s_node_network_interface_ethernet_ip(interface_info)
        self.add_k8s_node_network_interface_ethernet_ethtool(interface_info)
        self.add_k8s_node_network_interface_ethernet_sriov(interface_info)

        self.save_output('%s-eth' % (interface_info['hash']), subdir='ocp/node')

    def print_k8s_node_network_details(self, cluster_name, node_info):
        self.print_page_header('Kubernetes Node - Networking')

        self.my_output.print_stream('## Overview', 'output')
        self.my_output.print_stream('', 'output')
        self.my_output.print_stream('- Cluster: [%s](../nodes-%s.md)' % (cluster_name, cluster_name), 'output')
        self.my_output.print_stream('- Node: %s' % (node_info['name']), 'output')
        self.my_output.print_stream('- IP: %s' % (node_info['ssh_ip']), 'output')
        if node_info['ServerMoid'] is not None:
            self.my_output.print_stream(
                '- Server: [%s](../../compute/%s-net.md)' % (
                    node_info['ServerName'],
                    node_info['ServerMoid']
                ),
                'output'
            )

        if node_info['master']:
            self.my_output.print_stream('- Master :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Master :x:', 'output')
        if node_info['worker']:
            self.my_output.print_stream('- Worker :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Worker :x:', 'output')
        self.my_output.print_stream('- [Kubernetes State](./%s.md)' % (node_info['hash']), 'output')

        nns_info = self.xd_handler.get_k8s_nns_node(
            cluster_name,
            node_info['name']
        )
        if nns_info is None:
            self.my_output.print_stream('', 'output')
            self.my_output.print_stream(':x: Node Network State inforamtion missing - possibly lack of nmstate operator', 'output')
            self.save_output('%s-net' % (node_info['hash']), subdir='ocp/node')
            return

        self.add_k8s_node_network_route(nns_info)
        self.add_k8s_node_network_dns(nns_info)
        self.add_k8s_node_network_bond_interface_list(nns_info)
        self.add_k8s_node_network_ethernet_interface_list(nns_info)
        self.add_k8s_node_network_ethernet_interface_fabric(nns_info)

        self.save_output('%s-net' % (node_info['hash']), subdir='ocp/node')

        if 'interface' in nns_info and nns_info['interface'] is not None:
            for item in nns_info['interface']:
                if item['type'] == 'ethernet':
                    self.print_k8s_node_network_interface_ethernet_details(
                        cluster_name,
                        nns_info,
                        item
                    )

    def print_k8s_node_details(self, cluster_name, node_info):
        self.print_page_header('Kubernetes Node - State')

        self.my_output.print_stream('## Overview', 'output')
        self.my_output.print_stream('', 'output')
        self.my_output.print_stream('- Cluster: [%s](../nodes-%s.md)' % (cluster_name, cluster_name), 'output')
        self.my_output.print_stream('- Node: %s' % (node_info['name']), 'output')
        if node_info['ServerMoid'] is not None:
            self.my_output.print_stream(
                '- Server: [%s](../../compute/%s-inv.md)' % (
                    node_info['ServerName'],
                    node_info['ServerMoid']
                ),
                'output'
            )

        self.my_output.print_stream('- IP: %s' % (node_info['ssh_ip']), 'output')
        if node_info['master']:
            self.my_output.print_stream('- Master :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Master :x:', 'output')
        if node_info['worker']:
            self.my_output.print_stream('- Worker :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Worker :x:', 'output')

        self.my_output.print_stream('- [Networking State](./%s-net.md)' % (node_info['hash']), 'output')

        self.my_output.print_stream('## State', 'output')
        self.my_output.print_stream('', 'output')

        if node_info['ready']:
            self.my_output.print_stream('- Ready :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Ready :x:', 'output')

        if not node_info['memory_pressure']:
            self.my_output.print_stream('- Memory :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Memory :x:', 'output')

        if not node_info['disk_pressure']:
            self.my_output.print_stream('- Disk :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Disk :x:', 'output')

        if not node_info['pid_pressure']:
            self.my_output.print_stream('- PID :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- PID :x:', 'output')

        if node_info['mcp_current_config'] == node_info['mcp_desired_config']:
            self.my_output.print_stream('- MCP :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- MCP :x:', 'output')

        self.my_output.print_stream('- MCP current: %s' % (node_info['mcp_current_config']), 'output')
        self.my_output.print_stream('- MCP desired: %s' % (node_info['mcp_desired_config']), 'output')
        self.my_output.print_stream('- Age: %s' % (node_info['age']), 'output')

        if 'node_info' in node_info and node_info['node_info'] is not None:
            self.my_output.print_stream('## Node Details', 'output')
            self.my_output.print_stream('', 'output')
            if 'container_runtime_version' in node_info['node_info']:
                self.my_output.print_stream('- Container Runtime Version: %s' % (node_info['node_info']['container_runtime_version']), 'output')
            if 'kernel_version' in node_info['node_info']:
                self.my_output.print_stream('- Kernel Version: %s' % (node_info['node_info']['kernel_version']), 'output')
            if 'kube_proxy_version' in node_info['node_info']:
                self.my_output.print_stream('- Kube Proxy Version: %s' % (node_info['node_info']['kube_proxy_version']), 'output')
            if 'kubelet_version' in node_info['node_info']:
                self.my_output.print_stream('- Kubelet Version: %s' % (node_info['node_info']['kubelet_version']), 'output')
            if 'architecture' in node_info['node_info']:
                self.my_output.print_stream('- Architecture: %s' % (node_info['node_info']['architecture']), 'output')
            if 'operating_system' in node_info['node_info']:
                self.my_output.print_stream('- Operating System: %s' % (node_info['node_info']['operating_system']), 'output')
            if 'os_image' in node_info['node_info']:
                self.my_output.print_stream('- OS Image: %s' % (node_info['node_info']['os_image']), 'output')
            if 'boot_id' in node_info['node_info']:
                self.my_output.print_stream('- Boot Id: %s' % (node_info['node_info']['boot_id']), 'output')
            if 'machine_id' in node_info['node_info']:
                self.my_output.print_stream('- Machine Id: %s' % (node_info['node_info']['machine_id']), 'output')
            if 'system_uuid' in node_info['node_info']:
                self.my_output.print_stream('- System UUID: %s' % (node_info['node_info']['system_uuid']), 'output')

        if 'capacity' in node_info and node_info['capacity'] is not None:
            self.my_output.print_stream('## Node Capacity', 'output')
            self.my_output.print_stream('', 'output')

            order = [
                'Key',
                'Value'
            ]
            self.print_table_header(order)

            for key in node_info['capacity']:
                line = ''
                line = self.add_column(line, key)
                line = self.add_column(line, node_info['capacity'][key], last=True)
                self.my_output.print_stream(line, 'output')

        if 'label' in node_info and node_info['label'] is not None:
            self.my_output.print_stream('## Node Label', 'output')
            self.my_output.print_stream('', 'output')

            order = [
                'Key',
                'Value'
            ]
            self.print_table_header(order)

            for key in node_info['label']:
                line = ''
                line = self.add_column(line, key)
                line = self.add_column(line, node_info['label'][key], last=True)
                self.my_output.print_stream(line, 'output')

        self.save_output(node_info['hash'], subdir='ocp/node')

    def print_k8s_nodes(self, cluster_name, nodes_info):
        if nodes_info is None:
            return

        self.print_page_header('Kubernetes Nodes ([%s](./cluster-%s.md))' % (cluster_name, cluster_name))

        self.my_output.print_stream('## State', 'output')

        order = [
            'Name',
            'IP',
            'Master',
            'Worker',
            'Ready',
            'Mem',
            'Disk',
            'PID',
            'CNV',
            'MCP'
        ]
        self.print_table_header(order)

        for item in nodes_info:
            line = ''
            line = self.add_column(line, '[%s](./node/%s.md)' % (item['name'], item['hash']))
            line = self.add_column(line, item['ssh_ip'])
            line = self.add_column_tick_bool(line, item['master'])
            line = self.add_column_tick_bool(line, item['worker'])
            line = self.add_column_tick_bool(line, item['ready'])
            line = self.add_column_tick_bool(line, not item['memory_pressure'])
            line = self.add_column_tick_bool(line, not item['disk_pressure'])
            line = self.add_column_tick_bool(line, not item['pid_pressure'])
            line = self.add_column_tick_bool(line, item['cnv'])
            if item['mcp_current_config'] == item['mcp_desired_config']:
                line = self.add_column_tick_bool(line, True, last=True)
            else:
                line = self.add_column_tick_bool(line, False, last=True)

            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('## Networking', 'output')

        order = [
            'Name',
            'IP',
            'Ethernet'
        ]
        self.print_table_header(order)

        for item in nodes_info:
            line = ''
            line = self.add_column(line, '[%s](./node/%s-net.md)' % (item['name'], item['hash']))
            line = self.add_column(line, item['ssh_ip'])
            if item['EthernetSummary'] is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, item['EthernetSummary'])

            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('## Node-to-Server', 'output')

        order = [
            'Name',
            'IP',
            'Server',
            'Model',
            'Serial'
        ]
        self.print_table_header(order)

        for item in nodes_info:
            server_info = None
            if item['ServerMoid'] is not None:
                server_info = self.xd_handler.get_server_by_moid(
                    item['ServerMoid']
                )

            line = ''
            line = self.add_column(line, '[%s](./node/%s.md)' % (item['name'], item['hash']))
            line = self.add_column(line, item['ssh_ip'])
            if item['ServerName'] is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(
                    line,
                    '[%s](../compute/%s-inv.md)' % (
                        item['ServerName'],
                        item['ServerMoid']
                    )
                )

            if server_info is None:
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, server_info['Model'])
                line = self.add_column(line, server_info['Serial'])

            self.my_output.print_stream(line, 'output')

        self.save_output('nodes-%s' % (cluster_name), subdir='ocp')

        for item in nodes_info:
            self.print_k8s_node_details(
                cluster_name,
                item
            )
            self.print_k8s_node_network_details(
                cluster_name,
                item
            )
