from lib import filter_helper


class K8sNodeNetworkStateInfo():
    def __init__(self):
        self.node_network_state = None

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
            if key not in ['feature', 'coalesce', 'pause', 'ring']:
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

        return info

    def get_node_network_state_interface_bridge_info(self, interface_mo):
        info = {}
        bridge_mo = self.get(interface_mo, 'bridge', on_error=None, on_none=None)
        if bridge_mo is None:
            info['bridge_enabled'] = False
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
                    if vf_info['_vf_iface_name'] is not None:
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

    def get_node_network_state_interface_info(self, interface_mo):
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

    def get_node_network_state_interfaces_info(self, interfaces_mo):
        interfaces_info = []
        for interface_mo in interfaces_mo:
            interface_info = self.get_node_network_state_interface_info(interface_mo)
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
            if interface_info['type'] == 'ethernet' and interface_info['ethernet_sriov_enabled']:
                for vf_info in interface_info['ethernet_sriov_vfs']:
                    if vf_info['_vf_iface_name'] is not None:
                        if vf_info['_vf_iface_name'] not in vf_interface_names:
                            vf_interface_names.append(
                                vf_info['_vf_iface_name']
                            )
                            vf_interface_state[vf_info['_vf_iface_name']] = vf_info

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

        return interfaces_info

    def get_node_network_state_info(self, node_network_state_mo):
        if node_network_state_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            node_network_state_mo
        )
        info.update(metadata_info)

        info['interface'] = self.get_node_network_state_interfaces_info(
            self.get(
                node_network_state_mo,
                'status:currentState:interfaces'
            )
        )

        info['dns'] = {}
        info['dns']['search'] = self.get(
            node_network_state_mo,
            'status:currentState:dns-resolver:running:search'
        )
        info['dns']['server'] = self.get(
            node_network_state_mo,
            'status:currentState:dns-resolver:running:server'
        )

        info['route'] = []
        routes_mo = self.get(
            node_network_state_mo,
            'status:currentState:routes:running'
        )
        for route_mo in routes_mo:
            route_info = {}
            for key in route_mo:
                route_info[key] = route_mo[key]
            info['route'].append(
                route_info
            )

        return info

    def get_node_network_states_info(self, cache_enabled=True):
        if cache_enabled:
            if self.node_network_state is not None:
                return self.node_network_state

        managed_objects = self.get_node_network_state_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.node_network_state = []
        for managed_object in managed_objects:
            node_network_state_info = {}
            node_network_state_info['info'] = self.get_node_network_state_info(
                managed_object
            )
            node_network_state_info['mo'] = managed_object
            self.node_network_state.append(
                node_network_state_info
            )

        return self.node_network_state

    def match_node_network_state(self, node_network_state_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, node_network_state_info['name']):
                    return False

            if key.startswith('interface-'):
                key_found = True

            if not key_found:
                self.log.error(
                    'match_node_network_state',
                    'Unsupported key: %s' % (key)
                )

        return True

    def match_node_network_state_interface(self, node_network_state_interface_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True

            if key == 'interface-type':
                key_found = True
                if not filter_helper.match_string(value, node_network_state_interface_info['interface']):
                    return False

            if not key_found:
                self.log.error(
                    'match_node_network_state_interface',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_node_network_states(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_node_network_states = self.get_node_network_states_info(cache_enabled=cache_enabled)
        if all_node_network_states is None:
            return None

        node_network_states = []

        for node_network_state_info in all_node_network_states:
            if not self.match_node_network_state(node_network_state_info['info'], object_filter):
                continue

            if return_mo:
                node_network_states.append(
                    node_network_state_info['mo']
                )
                continue

            interfaces_info = []
            for node_network_state_interface_info in node_network_state_info['info']['interface']:
                if not self.match_node_network_state_interface(node_network_state_interface_info, object_filter):
                    continue

                interfaces_info.append(
                    node_network_state_interface_info
                )

            node_network_state_info['info']['interface'] = interfaces_info

            node_network_states.append(
                node_network_state_info['info']
            )

        return node_network_states

    def is_node_network_state(self, name, cache_enabled=True):
        if self.get_node_network_state(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_node_network_state(self, node_name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (node_name)
        )
        node_network_states = self.get_node_network_states(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if node_network_states is None:
            return None

        if len(node_network_states) == 1:
            return node_network_states[0]

        return None
