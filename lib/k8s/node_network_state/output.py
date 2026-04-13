class K8sNodeNetworkStateOutput():
    def __init__(self):
        pass

    def print_node_network_states_dns(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Node', 'name'],
                ['DNS Search', 'dns.search'],
                ['DNS Server', 'dns.server']
            ]
        )

    def print_node_network_states_route(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Node', 'name'],
                ['Table', 'route.table-id'],
                ['Destination', 'route.destination'],
                ['Next Hop', 'route.next-hop-address'],
                ['Interface', 'route.next-hop-interface'],
                ['Metric', 'route.metric']
            ],
            remove_empty=['route.metric']
        )

    def print_node_network_states_bond(self, info):
        bonds = []
        for item in info:
            for bond in item['bond']:
                bonds.append(bond)

        self.my_output.my_table_ng(
            bonds,
            [
                ['Node', 'node_name'],
                ['Bond', 'name'],
                ['State', 'stateTick'],
                ['MTU', 'mtu'],
                ['MAC', 'mac'],
                ['Mode', 'lacp_mode'],
                ['Port', 'lacp_port'],
                ['LLDP', 'lldp_enabledTick'],
                ['VLAN', 'vlanTick'],
                ['IPv4', 'ipv4'],
                ['IPv6', 'ipv6'],
                ['LACP Options', 'lacp_optionT'],
                ['Ethtool', 'ethtoolT']
            ]
        )

    def print_node_network_states_eth(self, info, brief=False):
        ethernets = []
        for item in info:
            for ethernet in item['ethernet']:
                ethernets.append(ethernet)

        if brief:
            self.my_output.my_table_ng(
                ethernets,
                [
                    ['Node', 'node_name'],
                    ['Ethernet', 'name'],
                    ['State', 'stateTick'],
                    ['MTU', 'mtu'],
                    ['MAC', 'mac']
                ]
            )

        if not brief:
            self.my_output.my_table_ng(
                ethernets,
                [
                    ['Node', 'node_name'],
                    ['Ethernet', 'name'],
                    ['State', 'stateTick'],
                    ['MTU', 'mtu'],
                    ['MAC', 'mac'],
                    ['Auto', 'ethernet_autoTick'],
                    ['Duplex', 'ethernet_duplex'],
                    ['Speed', 'ethernet_speed'],
                    ['SR-IOV', 'ethernet_sriov_vfs_summary'],
                    ['LLDP', 'lldp_enabledTick'],
                    ['LACP', 'lacp_parent'],
                    ['VLAN', 'vlanTick'],
                    ['OVS', 'ovsTick'],
                    ['LB', 'bridge'],
                    ['IPv4', 'ipv4'],
                    ['IPv6', 'ipv6']
                ]
            )

    def print_node_network_states_lldp(self, info):
        ethernets = []
        for item in info:
            for ethernet in item['ethernet']:
                ethernets.append(ethernet)

        self.my_output.my_table_ng(
            ethernets,
            [
                ['Node', 'node_name'],
                ['Ethernet', 'name'],
                ['MAC', 'mac'],
                ['State', 'stateTick'],
                ['LLDP', 'lldp_enabledTick'],
                ['Nei System', 'lldp_neighbors.system'],
                ['Nei Interface', 'lldp_neighbors.interface']
            ],
            cast_zero=True
        )

    def print_node_network_states_vf(self, info):
        vfs = []
        for item in info:
            for vf in item['vf']:
                vfs.append(vf)

        self.my_output.my_table_ng(
            vfs,
            [
                ['Node', 'node_name'],
                ['VF', 'name'],
                ['State', 'stateTick'],
                ['MTU', 'mtu'],
                ['MAC', 'mac'],
                ['Auto', 'ethernet_autoTick'],
                ['Duplex', 'ethernet_duplex'],
                ['Speed', 'ethernet_speed'],
                ['IPv4', 'ipv4'],
                ['IPv6', 'ipv6'],
                ['Spoof', 'vf.spoof-check'],
                ['Trust', 'vf.trust'],
                ['VLAN', 'vf.vlan-id']
            ]
        )

    def print_node_network_states_vlan(self, info):
        vlans = []
        for item in info:
            for vlan in item['vlan']:
                vlans.append(vlan)

        self.my_output.my_table_ng(
            vlans,
            [
                ['Node', 'node_name'],
                ['VLAN', 'name'],
                ['State', 'stateTick'],
                ['MTU', 'mtu'],
                ['MAC', 'mac'],
                ['IPv4', 'ipv4'],
                ['IPv6', 'ipv6'],
                ['Base Intf', 'vlan_base'],
                ['VLAN ID', 'vlan_id']
            ]
        )

    def print_node_network_states_lb(self, info):
        lbs = []
        for item in info:
            for lb in item['lb']:
                lbs.append(lb)

        self.my_output.my_table_ng(
            lbs,
            [
                ['Node', 'node_name'],
                ['LB', 'name'],
                ['State', 'stateTick'],
                ['MTU', 'mtu'],
                ['MAC', 'mac'],
                ['Interface', 'bridge_port.name'],
                ['LLDP', 'lldp_enabledTick'],
                ['IPv4', 'ipv4'],
                ['IPv6', 'ipv6'],
                ['Bridge Options', 'bridge_optionT']
            ]
        )

    def print_node_network_states_ovs(self, info):
        ovses = []
        for item in info:
            for ovs in item['ovs']:
                ovses.append(ovs)

        self.my_output.my_table_ng(
            ovses,
            [
                ['Node', 'node_name'],
                ['OVS', 'name'],
                ['State', 'stateTick'],
                ['Interface', 'bridge_port.name'],
                ['Localnet', 'localnet'],
                ['LLDP', 'lldp_enabledTick'],
                ['Bridge Options', 'bridge_optionT']
            ]
        )

    def print_node_network_states_ethtool(self, info):
        interfaces = []
        for item in info:
            for interface in item['interface']:
                if 'ethtoolT' in interface:
                    interfaces.append(interface)

        self.my_output.my_table_ng(
            interfaces,
            [
                ['Node', 'node_name'],
                ['Interface', 'name'],
                ['Type', 'type'],
                ['Ethtool', 'ethtoolT']
            ]
        )

    def print_node_network_states_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Node', 'name'],
                ['Interface', 'interfaceT'],
                ['Bridge', 'bridgeT'],
                ['DNS', 'dnsT'],
                ['Route', 'routeT']
            ]
        )
