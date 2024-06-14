import copy


class K8sNodeNetworkStateOutput():
    def __init__(self):
        pass

    def print_node_network_state(self, info, title=False):
        if title:
            self.my_output.default(
                'Node Network State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

    def print_node_network_state_dns(self, state, title=False):
        if title:
            self.my_output.default(
                'Node Network State - DNS [#%s]' % (len(state)),
                underline=True,
                before_newline=True
            )

        order = [
            'name',
            'dns.search',
            'dns.server'
        ]

        headers = [
            'Node',
            'Search',
            'Server'
        ]

        self.my_output.my_table(
            state,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_node_network_state_route(self, state, title=False):
        if title:
            self.my_output.default(
                'Node Network State - Route [#%s]' % (len(state)),
                underline=True,
                before_newline=True
            )

        order = [
            'name',
            'route.destination',
            'route.next-hop-address',
            'route.next-hop-interface',
            'route.metric',
            'route.table-id'
        ]

        headers = [
            'Node',
            'Destination',
            'NH',
            'Interface',
            'Metric',
            'Table'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                state,
                order,
                ['route']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_node_network_state_bond(self, state, options=False, ethtool=False, title=False):
        interfaces = []

        info = copy.deepcopy(state)
        for item in info:
            for interface in item['interface']:
                if interface['type'] != 'bond':
                    continue

                interface['node_name'] = item['name']

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

                interfaces.append(
                    interface
                )

        interfaces = sorted(
            interfaces,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        if title:
            self.my_output.default(
                'Node Network State - Bond Interface [#%s]' % (len(interfaces)),
                underline=True,
                before_newline=True
            )

        order = [
            'node_name',
            'name',
            'stateTick',
            'mtu',
            'mac',
            'lacp_mode',
            'lacp_port',
            'lldp_enabledTick',
            'vlanTick',
            'ipv4',
            'ipv6'
        ]

        headers = [
            'Node',
            'Interface',
            'State',
            'MTU',
            'MAC',
            'Mode',
            'Port',
            'LLDP',
            'VLAN',
            'IPv4',
            'IPv6'
        ]

        to_expand = ['ipv4', 'ipv6', 'lacp_port']

        if options:
            order.append('lacp_optionT')
            headers.append('LACP Options')
            to_expand.append('lacp_optionT')

        if ethtool:
            order.append('ethtoolT')
            headers.append('Ethtool')
            to_expand.append('ethtoolT')

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                to_expand
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_node_network_state_ethernet(self, state, ethtool=False, title=False):
        interfaces = []

        info = copy.deepcopy(state)
        for item in info:
            for interface in item['interface']:
                if interface['type'] != 'ethernet':
                    continue

                interface['node_name'] = item['name']

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

                interfaces.append(
                    interface
                )

        interfaces = sorted(
            interfaces,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        if title:
            self.my_output.default(
                'Node Network State - Ethernet Interface [#%s]' % (len(interfaces)),
                underline=True,
                before_newline=True
            )

        order = [
            'node_name',
            'name',
            'stateTick',
            'mtu',
            'mac',
            'ethernet_autoTick',
            'ethernet_duplex',
            'ethernet_speed',
            'ethernet_sriov_vfs_summary',
            'lldp_enabledTick',
            'lacp_parent',
            'vlanTick',
            'ovsTick',
            'bridge',
            'ipv4',
            'ipv6'
        ]

        headers = [
            'Node',
            'Interface',
            'State',
            'MTU',
            'MAC',
            'Auto',
            'Duplex',
            'Speed',
            'SR-IOV',
            'LLDP',
            'LACP',
            'VLAN',
            'OVS',
            'LB',
            'IPv4',
            'IPv6'
        ]

        to_expand = ['ipv4', 'ipv6']
        if ethtool:
            order.append('ethtoolT')
            headers.append('Ethtool')
            to_expand.append('ethtoolT')

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                to_expand
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_node_network_state_vf(self, state, ethtool=False, title=False):
        interfaces = []

        info = copy.deepcopy(state)
        for item in info:
            for interface in item['interface']:
                if interface['type'] != 'vf':
                    continue

                interface['node_name'] = item['name']

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

                interfaces.append(
                    interface
                )

        interfaces = sorted(
            interfaces,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        if title:
            self.my_output.default(
                'Node Network State - SR-IOV VF [#%s]' % (len(interfaces)),
                underline=True,
                before_newline=True
            )

        if len(interfaces) == 0:
            self.my_output.default('None')
            return

        order = [
            'node_name',
            'name',
            'stateTick',
            'mtu',
            'mac',
            'ethernet_autoTick',
            'ethernet_duplex',
            'ethernet_speed',
            'ipv4',
            'ipv6',
            'vf.spoof-check',
            'vf.trust',
            'vf.vlan-id'
        ]

        headers = [
            'Node',
            'Interface',
            'State',
            'MTU',
            'MAC',
            'Auto',
            'Duplex',
            'Speed',
            'IPv4',
            'IPv6',
            'Spoof',
            'Trust',
            'VLAN'
        ]

        to_expand = ['ipv4', 'ipv6']
        if ethtool:
            order.append('ethtoolT')
            headers.append('Ethtool')
            to_expand.append('ethtoolT')

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                to_expand
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_node_network_state_vlan(self, state, ethtool=False, title=False):
        interfaces = []

        info = copy.deepcopy(state)
        for item in info:
            for interface in item['interface']:
                if interface['type'] != 'vlan':
                    continue

                interface['node_name'] = item['name']

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

                interfaces.append(
                    interface
                )

        interfaces = sorted(
            interfaces,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        if title:
            self.my_output.default(
                'Node Network State - VLAN Interface [#%s]' % (len(interfaces)),
                underline=True,
                before_newline=True
            )

        if len(interfaces) == 0:
            self.my_output.default('None')
            return

        order = [
            'node_name',
            'name',
            'stateTick',
            'mtu',
            'mac',
            'ipv4',
            'ipv6',
            'vlan_base',
            'vlan_id'
        ]

        headers = [
            'Node',
            'Interface',
            'State',
            'MTU',
            'MAC',
            'IPv4',
            'IPv6',
            'Base Intf',
            'VLAN ID'
        ]

        to_expand = ['ipv4', 'ipv6']
        if ethtool:
            order.append('ethtoolT')
            headers.append('Ethtool')
            to_expand.append('ethtoolT')

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                to_expand
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_node_network_state_lb(self, state, options=False, ethtool=False, title=False):
        interfaces = []

        info = copy.deepcopy(state)
        for item in info:
            for interface in item['interface']:
                if interface['type'] != 'linux-bridge':
                    continue

                interface['node_name'] = item['name']

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

                interfaces.append(
                    interface
                )

        interfaces = sorted(
            interfaces,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        if title:
            self.my_output.default(
                'Node Network State - Linux Bridge [#%s]' % (len(interfaces)),
                underline=True,
                before_newline=True
            )

        if len(interfaces) == 0:
            self.my_output.default('None')
            return

        order = [
            'node_name',
            'name',
            'stateTick',
            'mtu',
            'mac',
            'bridge_port.name',
            'lldp_enabledTick',
            'ipv4',
            'ipv6'
        ]

        headers = [
            'Node',
            'Bridge',
            'State',
            'MTU',
            'MAC',
            'Interface',
            'LLDP',
            'IPv4',
            'IPv6'
        ]

        to_expand = ['ipv4', 'ipv6', 'bridge_port']

        if options:
            order.append('bridge_optionT')
            headers.append('Bridge Options')
            to_expand.append('bridge_optionT')

        if ethtool:
            order.append('ethtoolT')
            headers.append('Ethtool')
            to_expand.append('ethtoolT')

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                to_expand
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_node_network_state_lb_interfaces(self, state):
        ports = []

        info = copy.deepcopy(state)
        for item in info:
            for interface in item['interface']:
                if interface['type'] != 'linux-bridge':
                    continue

                for lb_port_info in interface['bridge_port']:
                    port_info = lb_port_info
                    port_info['node_name'] = item['name']
                    port_info['lb_name'] = interface['name']
                    port_info['vlan_rangeT'] = '--'
                    if 'vlan_range' in port_info:
                        port_info['vlan_rangeT'] = ','.join(port_info['vlan_range'])

                    ports.append(
                        port_info
                    )

        ports = sorted(
            ports,
            key=lambda i: (
                i['node_name'].lower(),
                i['lb_name'].lower(),
                i['name'].lower()
            )
        )

        if len(ports) == 0:
            return

        order = [
            'node_name',
            'lb_name',
            'name',
            'stp-hairpin-mode',
            'stp-path-cost',
            'stp-priority',
            'vlan_enabled',
            'vlan_native',
            'vlan_mode',
            'vlan_rangeT'
        ]

        headers = [
            'Node',
            'Bridge',
            'Interface',
            'STP Hairpin',
            'STP Cost',
            'STP Prio',
            'VLAN',
            'Native',
            'Mode',
            'Range'
        ]

        self.my_output.my_table(
            ports,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_node_network_state_ovs(self, state, options=False, ethtool=False, title=False):
        interfaces = []

        info = copy.deepcopy(state)
        for item in info:
            for interface in item['interface']:
                if interface['type'] != 'ovs-bridge':
                    continue

                interface['node_name'] = item['name']

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

                interfaces.append(
                    interface
                )

        interfaces = sorted(
            interfaces,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        if title:
            self.my_output.default(
                'Node Network State - OVS [#%s]' % (len(interfaces)),
                underline=True,
                before_newline=True
            )

        if len(interfaces) == 0:
            self.my_output.default('None')
            return

        order = [
            'node_name',
            'name',
            'state',
            'bridge_port.name',
            'lldp_enabledTick'
        ]

        headers = [
            'Node',
            'Bridge',
            'State',
            'Interface',
            'LLDP'
        ]

        to_expand = ['bridge_port']

        if options:
            order.append('bridge_optionT')
            headers.append('Bridge Options')
            to_expand.append('bridge_optionT')

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                to_expand
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_node_network_state_ovs_interfaces(self, state, ethtool=False):
        interfaces = []

        info = copy.deepcopy(state)
        for item in info:
            for interface in item['interface']:
                if interface['type'] != 'ovs-interface':
                    continue

                interface['node_name'] = item['name']

                if interface['mtu'] is None:
                    interface['mtu'] = '--'

                if interface['mac'] is None:
                    interface['mac'] = '--'

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

                interfaces.append(
                    interface
                )

        interfaces = sorted(
            interfaces,
            key=lambda i: (
                i['node_name'].lower(),
                i['name'].lower()
            )
        )

        if len(interfaces) == 0:
            return

        order = [
            'node_name',
            'name',
            'stateTick',
            'mtu',
            'mac',
            'ipv4',
            'ipv6'
        ]

        headers = [
            'Node',
            'Interface',
            'State',
            'MTU',
            'MAC',
            'IPv4',
            'IPv6'
        ]

        to_expand = ['ipv4', 'ipv6']

        if ethtool:
            order.append('ethtoolT')
            headers.append('Ethtool')
            to_expand.append('ethtoolT')

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                to_expand
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
