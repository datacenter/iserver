import time
from lib import filter_helper
from lib.workflow.ocp_interface_state_up import get as ocp_workflow


class K8sNodeNetworkStateInterfaceInfo():
    def __init__(self):
        pass
    
    def get_node_network_state_interface_ipv4_info(self, interface_mo):
        info = {}

        info['v4dhcp'] = self.get(interface_mo, 'ipv4:dhcp', on_error=False, on_none=False)
        info['v4enabled'] = self.get(interface_mo, 'ipv4:enabled', on_error=False, on_none=False)
        info['v4address'] = []

        addresses_mo = self.get(interface_mo, 'ipv4:address', on_error=[], on_none=[])
        for address_mo in addresses_mo:
            address_ip = self.get(address_mo, 'ip')
            prefix_length = self.get(address_mo, 'prefix-length')
            if address_ip is None or prefix_length is None:
                self.log.error(
                    'get_node_network_state_interface_ipv4_info',
                    'Failed to parse v4 address mo: %s' % (address_mo)
                )
                continue

            info['v4address'].append(
                '%s/%s' % (
                    address_ip,
                    prefix_length
                )
            )

        return info

    def get_node_network_state_interface_ipv6_info(self, interface_mo):
        info = {}

        info['v6dhcp'] = self.get(interface_mo, 'ipv6:dhcp', on_error=False, on_none=False)
        info['v6enabled'] = self.get(interface_mo, 'ipv6:enabled', on_error=False, on_none=False)
        info['v6autoconf'] = self.get(interface_mo, 'ipv6:autoconf', on_error=False, on_none=False)
        info['v6address'] = []

        addresses_mo = self.get(interface_mo, 'ipv6:address', on_error=[], on_none=[])
        for address_mo in addresses_mo:
            address_ip = self.get(address_mo, 'ip')
            prefix_length = self.get(address_mo, 'prefix-length')
            if address_ip is None or prefix_length is None:
                self.log.error(
                    'get_node_network_state_interface_ipv6_info',
                    'Failed to parse v6 address mo: %s' % (address_mo)
                )
                continue

            info['v6address'].append(
                '%s/%s' % (
                    address_ip,
                    prefix_length
                )
            )

        return info

    def get_node_network_state_interface_ethtool_info(self, interface_mo):
        info = {}
        info['ethtool'] = {}

        ethtool_mo = self.get(interface_mo, 'ethtool', on_error={}, on_none={})
        for key in ethtool_mo:
            if key not in ['feature', 'coalesce', 'pause', 'ring', 'fec']:
                self.log.error(
                    'get_node_network_state_interface_ethtool_info',
                    'Unsupported ethtool section: %s' % (key)
                )

        ethtool_mo = self.get(interface_mo, 'ethtool:feature', on_error={}, on_none={})
        for key in ethtool_mo:
            info['ethtool']['feature:%s' % (key)] = ethtool_mo[key]

        ethtool_mo = self.get(interface_mo, 'ethtool:coalesce', on_error={}, on_none={})
        for key in ethtool_mo:
            info['ethtool']['coalesce:%s' % (key)] = ethtool_mo[key]

        ethtool_mo = self.get(interface_mo, 'ethtool:pause', on_error={}, on_none={})
        for key in ethtool_mo:
            info['ethtool']['pause:%s' % (key)] = ethtool_mo[key]

        ethtool_mo = self.get(interface_mo, 'ethtool:ring', on_error={}, on_none={})
        for key in ethtool_mo:
            info['ethtool']['ring:%s' % (key)] = ethtool_mo[key]

        ethtool_mo = self.get(interface_mo, 'ethtool:fec', on_error={}, on_none={})
        for key in ethtool_mo:
            info['ethtool']['fec:%s' % (key)] = ethtool_mo[key]

        return info

    def get_node_network_state_interface_lacp_info(self, interface_mo):
        info = {}
        lacp_mo = self.get(interface_mo, 'link-aggregation', on_error=None, on_none=None)
        if lacp_mo is None:
            info['lacp_enabled'] = False
        else:
            info['lacp_enabled'] = True
            info['lacp_mode'] = self.get(interface_mo, 'link-aggregation:mode')
            info['lacp_port'] = self.get(interface_mo, 'link-aggregation:port', on_error=[], on_none=[])
            info['lacp_option'] = self.get(interface_mo, 'link-aggregation:options', on_error={}, on_none={})

        return info

    def get_node_network_state_interface_lldp_neighbor_info(self, neighbor_mo):
        info = {}

        for item in neighbor_mo:
            item_type = self.get(item, 'type')
            if item_type is None:
                continue

            if item_type == 5:
                info['system'] = self.get(item, 'system-name')

            if item_type == 6:
                info['description'] = self.get(item, 'system-description')

            if item_type == 7:
                info['capabilities'] = self.get(item, 'system-capabilities')

            if item_type == 1:
                info['chassis_id'] = self.get(item, 'chassis-id')

            if item_type == 2:
                info['interface'] = self.get(item, 'port-id')

            if item_type == 127:
                item_subtype = self.get(item, 'subtype')
                if item_subtype is None:
                    continue

                if item_subtype == 3:
                    info['oui'] = self.get(item, 'oui')
                    info['vlans'] = self.get(item, 'ieee-802-1-vlans', on_error=[], on_none=[])

                if item_subtype == 4:
                    info['max_frame_size'] = self.get(item, 'ieee-802-3-max-frame-size')

            if item_type == 8:
                info['mgmt_ip'] = None
                info['mgmt_mac'] = None
                addresses_mo = self.get(item, 'management-addresses')
                if addresses_mo is not None:
                    for address_mo in addresses_mo:
                        address_type = self.get(address_mo, 'address-subtype')
                        if address_type is None:
                            continue

                        if address_type == 'IPv4':
                            info['mgmt_ip'] = self.get(address_mo, 'address')

                        if address_type == 'MAC':
                            info['mgmt_mac'] = self.get(address_mo, 'address')

        return info

    def get_node_network_state_interface_lldp_info(self, interface_mo):
        info = {}
        lldp_mo = self.get(interface_mo, 'lldp', on_error=None, on_none=None)
        if lldp_mo is None:
            info['lldp_enabled'] = False
        else:
            info['lldp_enabled'] = self.get(interface_mo, 'lldp:enabled', on_error=False, on_none=False)

        if info['lldp_enabled']:
            info['lldp_enabledTick'] = '\u2713'
        else:
            info['lldp_enabledTick'] = '\u2717'

        info['lldp_neighbors'] = []
        neighbors_mo = self.get(interface_mo, 'lldp:neighbors', on_error=None)
        if neighbors_mo is not None:
            for neighbor_mo in neighbors_mo:
                info['lldp_neighbors'].append(
                    self.get_node_network_state_interface_lldp_neighbor_info(
                        neighbor_mo
                    )
                )

        return info

    def get_node_network_state_interface_bridge_info(self, interface_mo):
        info = {}
        bridge_mo = self.get(interface_mo, 'bridge', on_error=None, on_none=None)
        if bridge_mo is None:
            info['bridge_enabled'] = False
            info['bridge_port'] = []
        else:
            info['bridge_enabled'] = True
            info['bridge_port'] = []
            ports_mo = self.get(interface_mo, 'bridge:port', on_error=[], on_none=[])
            for port_mo in ports_mo:
                port_info = {}
                port_info['name'] = self.get(port_mo, 'name')
                port_info['stp-hairpin-mode'] = self.get(port_mo, 'stp-hairpin-mode')
                port_info['stp-path-cost'] = self.get(port_mo, 'stp-path-cost')
                port_info['stp-priority'] = self.get(port_mo, 'stp-priority')
                port_vlan_mo = self.get(port_mo, 'vlan')
                if port_vlan_mo is None:
                    port_info['vlan_enabled'] = False
                else:
                    port_info['vlan_enabled'] = True
                    port_info['vlan_native'] = self.get(port_vlan_mo, 'enable-native', on_error=False, on_none=False)
                    port_info['vlan_mode'] = self.get(port_vlan_mo, 'mode')
                    if port_info['vlan_mode'] == 'trunk':
                        trunk_range_mo = self.get(port_vlan_mo, 'trunk-tags')
                        port_info['vlan_range'] = []
                        for range_mo in trunk_range_mo:
                            if 'id-range' in range_mo:
                                port_info['vlan_range'].append(
                                    '%s-%s' % (
                                        range_mo['id-range']['min'],
                                        range_mo['id-range']['max']
                                    )
                                )

                    if port_info['vlan_mode'] == 'access':
                        port_info['vlan_range'] = []
                        access_vlan = str(self.get(port_vlan_mo, 'tag'))
                        if access_vlan is not None:
                            port_info['vlan_range'].append(
                                access_vlan
                            )

                info['bridge_port'].append(
                    port_info
                )

            info['bridge_option'] = {}
            options_mo = self.get(interface_mo, 'bridge:options', on_error={}, on_none={})
            for key in options_mo:
                if key == 'stp' and isinstance(options_mo[key], dict):
                    for stp_key in options_mo[key]:
                        info['bridge_option']['stp:%s' % (stp_key)] = options_mo[key][stp_key]
                else:
                    info['bridge_option'][key] = options_mo[key]

        return info

    def get_node_network_state_interface_ethernet_info(self, interface_mo):
        info = {}
        ethernet_mo = self.get(interface_mo, 'ethernet', on_error=None, on_none=None)
        if ethernet_mo is not None:
            info['ethernet_auto'] = self.get(interface_mo, 'ethernet:auto-negotiation')
            info['ethernet_duplex'] = self.get(interface_mo, 'ethernet:duplex')
            info['ethernet_speed'] = self.get(interface_mo, 'ethernet:speed')
            sriov_mo = self.get(interface_mo, 'ethernet:sr-iov')
            if sriov_mo is None:
                info['ethernet_sriov_enabled'] = False
                info['ethernet_sriov_vfs_count'] = 0
                info['ethernet_sriov_vfs_summary'] = '--'
            else:
                info['ethernet_sriov_enabled'] = True
                info['ethernet_sriov_num_vfs'] = self.get(sriov_mo, 'total-vfs')
                info['ethernet_sriov_vfs'] = self.get(sriov_mo, 'vfs', on_error=[], on_none=[])

                info['ethernet_sriov_vfs_count'] = 0
                for vf_info in info['ethernet_sriov_vfs']:
                    if 'iface-name' in vf_info:
                        if vf_info['iface-name'] is not None:
                            info['ethernet_sriov_vfs_count'] = info['ethernet_sriov_vfs_count'] + 1

                info['ethernet_sriov_vfs_summary'] = '%s/%s' % (
                    info['ethernet_sriov_vfs_count'],
                    info['ethernet_sriov_num_vfs']
                )

        return info

    def get_node_network_state_interface_vlan_info(self, interface_mo):
        info = {}
        vlan_mo = self.get(interface_mo, 'vlan', on_error=None, on_none=None)
        if vlan_mo is not None:
            info['vlan_base'] = self.get(vlan_mo, 'base-iface')
            info['vlan_id'] = self.get(vlan_mo, 'id')

        return info

    def get_node_network_state_interface_info(self, node_name, interface_mo):
        info = {}
        info['__Output'] = {}

        keys = [
            'name',
            'state',
            'type',
            'mtu'
        ]
        for key in keys:
            info[key] = self.get(interface_mo, key)

        if self.node_network_state_interface_up is not None:
            if node_name in self.node_network_state_interface_up:
                if self.node_network_state_interface_up[node_name] is not None:
                    if info['name'] in self.node_network_state_interface_up[node_name]:
                        if info['state'] == 'up' and not self.node_network_state_interface_up[node_name][info['name']]:
                            info['state'] = 'ip-cli-down'

        if info['state'] == 'up':
            info['stateTick'] = '\u2713'
            info['__Output']['stateTick'] = 'Green'
            info['__Output']['state'] = 'Green'

        if info['state'] == 'ignore':
            info['stateTick'] = '--'

        if info['state'] not in ['up', 'ignore']:
            info['stateTick'] = '\u2717'
            info['__Output']['stateTick'] = 'Red'
            info['__Output']['state'] = 'Red'

        if info['type'] not in ['bond', 'vlan', 'ethernet', 'ovs-interface', 'ovs-bridge', 'linux-bridge', 'loopback']:
            if interface_mo['type'] != 'unknown' and interface_mo['name'] == 'lo':
                self.log.error(
                    'get_node_network_state_interface_info',
                    'Unsupported interface: %s' % (interface_mo)
                )
                return None

            if interface_mo['type'] == 'unknown' and interface_mo['name'] != 'lo':
                self.log.error(
                    'get_node_network_state_interface_info',
                    'Unsupported interface: %s' % (interface_mo)
                )
                return None

        info['accept'] = self.get(interface_mo, 'accept-all-mac-addresses', on_error=False, on_none=False)
        info['mac'] = self.get(interface_mo, 'mac-address')

        ethtool_info = self.get_node_network_state_interface_ethtool_info(
            interface_mo
        )
        info.update(ethtool_info)

        ipv4_info = self.get_node_network_state_interface_ipv4_info(
            interface_mo
        )
        info.update(ipv4_info)

        ipv6_info = self.get_node_network_state_interface_ipv6_info(
            interface_mo
        )
        info.update(ipv6_info)

        info['address'] = info['v4address'] + info['v6address']

        lacp_info = self.get_node_network_state_interface_lacp_info(
            interface_mo
        )
        info.update(lacp_info)

        lldp_info = self.get_node_network_state_interface_lldp_info(
            interface_mo
        )
        info.update(lldp_info)

        bridge_info = self.get_node_network_state_interface_bridge_info(
            interface_mo
        )
        info.update(bridge_info)

        ethernet_info = self.get_node_network_state_interface_ethernet_info(
            interface_mo
        )
        info.update(ethernet_info)

        if 'ethernet_sriov_enabled' in ethernet_info:
            if ethernet_info['ethernet_sriov_enabled']:
                info['ethernet_sriov_enabledTick'] = '\u2713'
            else:
                info['ethernet_sriov_enabledTick'] = '\u2717'

        if 'ethernet_auto' in ethernet_info:
            if ethernet_info['ethernet_auto']:
                info['ethernet_autoTick'] = '\u2713'
            else:
                info['ethernet_autoTick'] = '\u2717'

        vlan_info = self.get_node_network_state_interface_vlan_info(
            interface_mo
        )
        info.update(vlan_info)

        return info

    def get_node_network_state_interfaces_bond_info(self, node_name, interfaces):
        bond = []
        for interface in interfaces:
            if interface['type'] != 'bond':
                continue

            interface['node_name'] = node_name

            interface['ipv4'] = []
            if interface['v4enabled']:
                interface['ipv4'].append('Enabled')
                if interface['v4dhcp']:
                    interface['ipv4'].append('DHCPv4: yes')
                else:
                    interface['ipv4'].append('DHCPv4: no')
                interface['ipv4'] = interface['ipv4'] + interface['v4address']
            if len(interface['ipv4']) == 0:
                interface['ipv4'] = ['--']

            interface['ipv6'] = []
            if interface['v4enabled']:
                interface['ipv6'].append('Enabled')
                if interface['v6dhcp']:
                    interface['ipv6'].append('DHCPv6: yes')
                else:
                    interface['ipv6'].append('DHCPv6: no')
                interface['ipv6'] = interface['ipv6'] + interface['v6address']
            if len(interface['ipv6']) == 0:
                interface['ipv6'] = ['--']

            interface['ethtoolT'] = []
            for key in interface['ethtool']:
                interface['ethtoolT'].append(
                    '%s = %s' % (
                        key,
                        interface['ethtool'][key]
                    )
                )

            interface['lacp_optionT'] = []
            for key in interface['lacp_option']:
                interface['lacp_optionT'].append(
                    '%s = %s' % (
                        key,
                        interface['lacp_option'][key]
                    )
                )

            bond.append(
                interface
            )

        bond = sorted(
            bond,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        return bond
    
    def get_node_network_state_interfaces_ethernet_info(self, node_name, interfaces):
        ethernet = []
        for interface in interfaces:
            if interface['type'] != 'ethernet':
                continue

            if interface['state'] == 'ignore':
                continue

            interface['node_name'] = node_name

            if interface['ethernet_duplex'] is None:
                interface['ethernet_duplex'] = '--'

            if interface['ethernet_speed'] is None:
                interface['ethernet_speed'] = '--'

            if interface['lacp_parent'] is None:
                interface['lacp_parent'] = '--'

            if interface['bridge'] is None:
                interface['bridge'] = '--'

            interface['ipv4'] = []
            if interface['v4enabled']:
                interface['ipv4'].append('Enabled')
                if interface['v4dhcp']:
                    interface['ipv4'].append('DHCPv4: yes')
                else:
                    interface['ipv4'].append('DHCPv4: no')
                interface['ipv4'] = interface['ipv4'] + interface['v4address']
            if len(interface['ipv4']) == 0:
                interface['ipv4'] = ['--']

            interface['ipv6'] = []
            if interface['v4enabled']:
                interface['ipv6'].append('Enabled')
                if interface['v6dhcp']:
                    interface['ipv6'].append('DHCPv6: yes')
                else:
                    interface['ipv6'].append('DHCPv6: no')
                interface['ipv6'] = interface['ipv6'] + interface['v6address']
            if len(interface['ipv6']) == 0:
                interface['ipv6'] = ['--']

            interface['ethtoolT'] = []
            for key in interface['ethtool']:
                interface['ethtoolT'].append(
                    '%s = %s' % (
                        key,
                        interface['ethtool'][key]
                    )
                )

            ethernet.append(
                interface
            )

        ethernet = sorted(
            ethernet,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        return ethernet

    def get_node_network_state_interfaces_vlan_info(self, node_name, interfaces):
        vlan = []
        for interface in interfaces:
            if interface['type'] != 'vlan':
                continue

            interface['node_name'] = node_name

            interface['ipv4'] = []
            if interface['v4enabled']:
                interface['ipv4'].append('Enabled')
                if interface['v4dhcp']:
                    interface['ipv4'].append('DHCPv4: yes')
                else:
                    interface['ipv4'].append('DHCPv4: no')
                interface['ipv4'] = interface['ipv4'] + interface['v4address']
            if len(interface['ipv4']) == 0:
                interface['ipv4'] = ['--']

            interface['ipv6'] = []
            if interface['v4enabled']:
                interface['ipv6'].append('Enabled')
                if interface['v6dhcp']:
                    interface['ipv6'].append('DHCPv6: yes')
                else:
                    interface['ipv6'].append('DHCPv6: no')
                interface['ipv6'] = interface['ipv6'] + interface['v6address']
            if len(interface['ipv6']) == 0:
                interface['ipv6'] = ['--']

            interface['ethtoolT'] = []
            for key in interface['ethtool']:
                interface['ethtoolT'].append(
                    '%s = %s' % (
                        key,
                        interface['ethtool'][key]
                    )
                )

            vlan.append(
                interface
            )

        vlan = sorted(
            vlan,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        return vlan

    def get_node_network_state_interfaces_vlan_info(self, node_name, interfaces):
        vlan = []
        for interface in interfaces:
            if interface['type'] != 'vlan':
                continue

            interface['node_name'] = node_name

            interface['ipv4'] = []
            if interface['v4enabled']:
                interface['ipv4'].append('Enabled')
                if interface['v4dhcp']:
                    interface['ipv4'].append('DHCPv4: yes')
                else:
                    interface['ipv4'].append('DHCPv4: no')
                interface['ipv4'] = interface['ipv4'] + interface['v4address']
            if len(interface['ipv4']) == 0:
                interface['ipv4'] = ['--']

            interface['ipv6'] = []
            if interface['v4enabled']:
                interface['ipv6'].append('Enabled')
                if interface['v6dhcp']:
                    interface['ipv6'].append('DHCPv6: yes')
                else:
                    interface['ipv6'].append('DHCPv6: no')
                interface['ipv6'] = interface['ipv6'] + interface['v6address']
            if len(interface['ipv6']) == 0:
                interface['ipv6'] = ['--']

            interface['ethtoolT'] = []
            for key in interface['ethtool']:
                interface['ethtoolT'].append(
                    '%s = %s' % (
                        key,
                        interface['ethtool'][key]
                    )
                )

            vlan.append(
                interface
            )

        vlan = sorted(
            vlan,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        return vlan

    def get_node_network_state_interfaces_lb_info(self, node_name, interfaces):
        lb = []
        for interface in interfaces:
            if interface['type'] != 'linux-bridge':
                continue

            interface['node_name'] = node_name

            interface['ipv4'] = []
            if interface['v4enabled']:
                interface['ipv4'].append('Enabled')
                if interface['v4dhcp']:
                    interface['ipv4'].append('DHCPv4: yes')
                else:
                    interface['ipv4'].append('DHCPv4: no')
                interface['ipv4'] = interface['ipv4'] + interface['v4address']
            if len(interface['ipv4']) == 0:
                interface['ipv4'] = ['--']

            interface['ipv6'] = []
            if interface['v4enabled']:
                interface['ipv6'].append('Enabled')
                if interface['v6dhcp']:
                    interface['ipv6'].append('DHCPv6: yes')
                else:
                    interface['ipv6'].append('DHCPv6: no')
                interface['ipv6'] = interface['ipv6'] + interface['v6address']
            if len(interface['ipv6']) == 0:
                interface['ipv6'] = ['--']

            interface['ethtoolT'] = []
            for key in interface['ethtool']:
                interface['ethtoolT'].append(
                    '%s = %s' % (
                        key,
                        interface['ethtool'][key]
                    )
                )

            interface['bridge_optionT'] = []
            for key in interface['bridge_option']:
                interface['bridge_optionT'].append(
                    '%s = %s' % (
                        key,
                        interface['bridge_option'][key]
                    )
                )

            if len(interface['bridge_port']) == 0:
                interface['bridge_port'].append(dict(name='--'))

            lb.append(
                interface
            )

        lb = sorted(
            lb,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        return lb

    def get_node_network_state_interfaces_ovs_info(self, node_name, interfaces, bridge_mappings):
        ovs = []
        for item in interfaces:
            if item['type'] != 'ovs-bridge':
                continue

            item['node_name'] = node_name

            item['bridge_optionT'] = []
            if item['bridge_enabled']:
                for key in item['bridge_option']:
                    item['bridge_optionT'].append(
                        '%s = %s' % (
                            key,
                            item['bridge_option'][key]
                        )
                    )

            if len(item['bridge_port']) == 0:
                item['bridge_port'].append(dict(name='--'))

            item['localnet'] = []
            for brm in bridge_mappings:
                if brm['bridge'] == item['name']:
                    localnet = self.get(brm, 'localnet')
                    if localnet is not None:
                        item['localnet'].append(localnet)

            ovs.append(
                item
            )

        ovs = sorted(
            ovs,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        return ovs

    def get_node_network_state_interfaces_vf_info(self, node_name, interfaces):
        vfs = []
        for interface in interfaces:
            if interface['type'] != 'vf':
                continue

            interface['node_name'] = node_name

            if interface['ethernet_duplex'] is None:
                interface['ethernet_duplex'] = '--'

            if interface['ethernet_speed'] is None:
                interface['ethernet_speed'] = '--'

            interface['ipv4'] = []
            if interface['v4enabled']:
                interface['ipv4'].append('Enabled')
                if interface['v4dhcp']:
                    interface['ipv4'].append('DHCPv4: yes')
                else:
                    interface['ipv4'].append('DHCPv4: no')
                interface['ipv4'] = interface['ipv4'] + interface['v4address']
            if len(interface['ipv4']) == 0:
                interface['ipv4'] = ['--']

            interface['ipv6'] = []
            if interface['v4enabled']:
                interface['ipv6'].append('Enabled')
                if interface['v6dhcp']:
                    interface['ipv6'].append('DHCPv6: yes')
                else:
                    interface['ipv6'].append('DHCPv6: no')
                interface['ipv6'] = interface['ipv6'] + interface['v6address']
            if len(interface['ipv6']) == 0:
                interface['ipv6'] = ['--']

            interface['ethtoolT'] = []
            for key in interface['ethtool']:
                interface['ethtoolT'].append(
                    '%s = %s' % (
                        key,
                        interface['ethtool'][key]
                    )
                )

            vfs.append(
                interface
            )

        vfs = sorted(
            vfs,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        return vfs
    
    def get_node_network_state_interfaces_info(self, managed_object):
        node_name = self.get(managed_object, 'metadata:name')
        interfaces_mo = self.get(managed_object, 'status:currentState:interfaces')

        interfaces_info = []
        for interface_mo in interfaces_mo:
            interface_info = self.get_node_network_state_interface_info(node_name, interface_mo)
            if interface_info is not None:
                interfaces_info.append(
                    interface_info
                )

        bridge_interface_names = {}
        for interface_info in interfaces_info:
            if interface_info['type'] == 'linux-bridge':
                if 'bridge_port' in interface_info:
                    for port_info in interface_info['bridge_port']:
                        bridge_interface_names[port_info['name']] = interface_info['name']

        ovs_interface_names = {}
        for interface_info in interfaces_info:
            if interface_info['type'] == 'ovs-bridge':
                if 'bridge_port' in interface_info:
                    for port_info in interface_info['bridge_port']:
                        ovs_interface_names[port_info['name']] = interface_info['name']

        vlan_interface_names = {}
        for interface_info in interfaces_info:
            if interface_info['type'] == 'vlan':
                vlan_interface_names[interface_info['vlan_base']] = True
                if interface_info['name'] in bridge_interface_names:
                    bridge_interface_names[interface_info['vlan_base']] = bridge_interface_names[interface_info['name']]
                if interface_info['name'] in ovs_interface_names:
                    ovs_interface_names[interface_info['vlan_base']] = ovs_interface_names[interface_info['name']]

        vf_interface_names = []
        vf_interface_state = {}
        for interface_info in interfaces_info:
            if interface_info['type'] == 'ethernet':
                if 'ethernet_sriov_enabled' in interface_info and interface_info['ethernet_sriov_enabled']:
                    for vf_info in interface_info['ethernet_sriov_vfs']:
                        if 'iface-name' in vf_info:
                            if vf_info['iface-name'] is not None:
                                if vf_info['iface-name'] not in vf_interface_names:
                                    vf_interface_names.append(
                                        vf_info['iface-name']
                                    )
                                    vf_interface_state[vf_info['iface-name']] = vf_info

        bond_interface_names = {}
        for interface_info in interfaces_info:
            if interface_info['type'] == 'bond':
                interface_info['vlan'] = False
                interface_info['vlanTick'] = '\u2717'
                if interface_info['name'] in vlan_interface_names:
                    interface_info['vlan'] = True
                    interface_info['vlanTick'] = '\u2713'

                for port_name in interface_info['lacp_port']:
                    bond_interface_names[port_name] = interface_info['name']

        for interface_info in interfaces_info:
            if interface_info['type'] == 'ethernet':
                if interface_info['name'] in vf_interface_names:
                    interface_info['type'] = 'vf'
                    interface_info['vf'] = vf_interface_state[interface_info['name']]
                    continue

                interface_info['lacp_parent'] = None
                if interface_info['name'] in bond_interface_names:
                    interface_info['lacp_parent'] = bond_interface_names[interface_info['name']]

                interface_info['bridge'] = None
                if interface_info['name'] in bridge_interface_names:
                    interface_info['bridge'] = bridge_interface_names[interface_info['name']]
                if interface_info['lacp_parent'] is not None and interface_info['lacp_parent'] in bridge_interface_names:
                    interface_info['bridge'] = bridge_interface_names[interface_info['lacp_parent']]

                interface_info['ovs'] = False
                interface_info['ovsTick'] = '\u2717'
                interface_info['__Output']['ovsTick'] = 'Red'
                if interface_info['name'] in ovs_interface_names:
                    interface_info['ovs'] = True
                    interface_info['ovsTick'] = '\u2713'
                    interface_info['__Output']['ovsTick'] = 'Green'
                if interface_info['lacp_parent'] is not None and interface_info['lacp_parent'] in ovs_interface_names:
                    interface_info['ovs'] = True
                    interface_info['ovsTick'] = '\u2713'
                    interface_info['__Output']['ovsTick'] = 'Green'

                interface_info['vlan'] = False
                interface_info['vlanTick'] = '\u2717'
                interface_info['__Output']['vlanTick'] = 'Red'
                if interface_info['name'] in vlan_interface_names:
                    interface_info['vlan'] = True
                    interface_info['vlanTick'] = '\u2713'
                    interface_info['__Output']['vlanTick'] = 'Green'
                if interface_info['lacp_parent'] is not None and interface_info['lacp_parent'] in vlan_interface_names:
                    interface_info['vlan'] = True
                    interface_info['vlanTick'] = '\u2713'
                    interface_info['__Output']['vlanTick'] = 'Green'

        interfaces_info = sorted(
            interfaces_info,
            key=lambda i: i['name']
        )

        info = {}
        info['interface'] = interfaces_info
        info['bond'] = self.get_node_network_state_interfaces_bond_info(node_name, interfaces_info)
        info['ethernet'] = self.get_node_network_state_interfaces_ethernet_info(node_name, interfaces_info)
        info['vlan'] = self.get_node_network_state_interfaces_vlan_info(node_name, interfaces_info)
        info['lb'] = self.get_node_network_state_interfaces_lb_info(node_name, interfaces_info)
        info['ovs'] = self.get_node_network_state_interfaces_ovs_info(
            node_name, 
            interfaces_info,
            self.get(managed_object, 'status:currentState:ovn:bridge-mappings', on_error=[], on_none=[])
        )
        info['vf'] = self.get_node_network_state_interfaces_vf_info(node_name, interfaces_info)
        return info