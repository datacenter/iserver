class InterfacePhyOutput():
    def __init__(self):
        pass

    def print_interfaces_phy_state(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'portName',
            'adminSt',
            'switchingSt',
            'stats.operSt',
            'stats.operStQual',
            'portT',
            'layerT',
            'stats.bundleIndex',
            'stats.backplaneMac',
            'stats.operMode',
            'stats.operSpeed',
            'stats.operDuplex',
            'mtu',
            'stats.operFecMode'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Admin',
            'Switching',
            'Oper',
            'Reason',
            'Type',
            'Layer',
            'PC',
            'MAC',
            'Mode',
            'Speed',
            'Duplex',
            'MTU',
            'FEC'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_phy_ether(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'portName',
            'stats.operSt',
            'ether_stats.pkts',
            'ether_stats.broadcastPkts',
            'ether_stats.multicastPkts',
            'ether_stats.rXNoErrors',
            'ether_stats.tXNoErrors',
            'ether_stats.pkts64Octets',
            'ether_stats.pkts65to127Octets',
            'ether_stats.pkts128to255Octets',
            'ether_stats.pkts256to511Octets',
            'ether_stats.pkts512to1023Octets',
            'ether_stats.pkts1024to1518Octets'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Oper',
            'Packets',
            'Broadcast',
            'Multicast',
            'Rx',
            'Tx',
            'Size up to 64B',
            'Size 65-1270B',
            'Size 128-255B',
            'Size 256-511B',
            'Size 512-1023',
            'Size 1024-1518'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_phy_err(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'portName',
            'stats.operSt',
            'ether_stats.oversizePkts',
            'ether_stats.undersizePkts',
            'ether_stats.rxGiantPkts',
            'ether_stats.rxOversizePkts',
            'ether_stats.txGiantPkts',
            'ether_stats.txOversizePkts',
            'ether_stats.collisions',
            'ether_stats.cRCAlignErrors',
            'ether_stats.dropEvents'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Oper',
            'Oversize',
            'Undersize',
            'Rx giant',
            'Rx oversize',
            'Tx giant',
            'Tx oversize',
            'Collisions',
            'CRC errors',
            'Drops'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_phy_trans(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'portName',
            'stats.operSt',
            'fc_stats.isFcotPresent',
            'fc_stats.state',
            'fc_stats.type',
            'fc_stats.guiName',
            'fc_stats.guiCiscoPID',
            'fc_stats.guiPN',
            'fc_stats.guiRev',
            'fc_stats.guiSN'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Oper',
            'Present',
            'State',
            'Optics',
            'Name',
            'Type',
            'PN',
            'Rev',
            'SN'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_phy_vlan(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'portName',
            'stats.operSt',
            'stats.nativeVlan',
            'stats.primaryVlan',
            'stats.operVlans',
            'epg_stats.nameApTenant',
            'epg_stats.vlan.id',
            'epg_stats.vlan.encap',
            'epg_stats.vlan.fabEncap',
            'epg_stats.vlan.operSt'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Oper',
            'Native',
            'Primary',
            'Oper Vlans',
            'EPG',
            'Internal VLAN',
            'Encap VLAN',
            'Fabric VxLAN',
            'VLAN Oper State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                ['epg_stats']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_phy_epg(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'portName',
            'stats.operSt',
            'epg_stats.nameApTenant',
            'epg_stats.fvBD.nameTenant',
            'epg_stats.fvBD.fvSubnets'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Oper',
            'EPG',
            'Bridge Domain',
            'Subnets'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                ['epg_stats']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_phy_load(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'portName',
            'stats.operSt',
            'load.loadIntvl1',
            'load.loadIntvl2',
            'load.loadIntvl3'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Oper',
            'Load Interval 1',
            'Load Interval 2',
            'Load Interval 3'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_phy_eee(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'portName',
            'stats.operSt',
            'eee.eeeLat',
            'eee.eeeLpi',
            'eee.eeeState'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Oper',
            'Eee Lat',
            'Eee Lpi',
            'Eee State'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_phy_nei(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'portName',
            'stats.operSt',
            'cdp.sysName',
            'cdp.platId',
            'cdp.portId',
            'lldp.sysName',
            'lldp.portIdV'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Oper',
            'CDP System Name',
            'CDP Platform',
            'CDP Port ID',
            'LLDP System Name',
            'LLDP Port ID'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                ['cdp', 'lldp']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_phy_cdp(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'portName',
            'stats.operSt',
            'cdp.sysName',
            'cdp.platId',
            'cdp.portId',
            'cdp.cap',
            'cdp.stQual'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Oper',
            'CDP System Name',
            'Platform',
            'Port ID',
            'Capability',
            'State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                ['cdp']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_phy_lldp(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'portName',
            'stats.operSt',
            'lldp.sysName',
            'lldp.portIdV',
            'lldp.capability',
            'lldp.mgmtIp',
            'lldp.mgmtPortMac',
            'lldp.stQual'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Oper',
            'LLDP System Name',
            'Port ID',
            'Capability',
            'Mgmt IP',
            'Mgmt MAC',
            'State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                ['cdp', 'lldp']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_phy_policy(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'portName',
            'stats.operSt',
            'portT',
            'policy_selector.policy_group_type',
            'policy_selector.policy_group_name',
            'policy_selector.policy_group_info.policy.infraRsHIfPol',
            'policy_selector.policy_group_info.policy.infraRsLinkFlapPol',
            'policy_selector.policy_group_info.policy.infraRsCdpIfPol',
            'policy_selector.policy_group_info.policy.infraRsMcpIfPol',
            'policy_selector.policy_group_info.policy.infraRsLldpIfPol',
            'policy_selector.policy_group_info.policy.infraRsStpIfPol'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Oper',
            'Type',
            'Policy Group Type',
            'Policy Group Name',
            'Link Level',
            'Link Flap',
            'CDP',
            'MCP',
            'LLDP',
            'STP'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_phy_policy_group(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'portName',
            'stats.operSt',
            'portT',
            'policy_selector.profile',
            'policy_selector.name',
            'policy_selector.policy_group_type_name',
            'policy_selector.policy_group_name',
            'policy_selector.policy_group_info.aaep_name'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Oper',
            'Type',
            'Leaf Interface Profile',
            'Interface Selector',
            'Policy Group Type',
            'Policy Group Name',
            'Attached Entity Profile'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interfaces_phy_aaep(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        for item in interfaces:
            try:
                item['infraRsDomP'] = item['policy_selector']['policy_group_info']['aaep']['infraRsDomP']
            except BaseException:
                item['infraRsDomP'] = None

        order = order + [
            'pod_node_name',
            'portName',
            'stats.operSt',
            'portT',
            'policy_selector.policy_group_name',
            'policy_selector.policy_group_info.aaep_name',
            'infraRsDomP.domainType',
            'infraRsDomP.domainName'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Oper',
            'Type',
            'Policy Group Name',
            'Attached Entity Profile',
            'Domain Type',
            'Domain Name'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                ['infraRsDomP']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_interfaces_phy_qos(self, interfaces, stream='default'):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'adminSt',
            'stats.operSt',
            'qos.id',
            'qos.RxAdmitBytesCount',
            'qos.RxAdmitPacketsCount',
            'qos.RxDropBytesCount',
            'qos.RxDropPacketsCount',
            'qos.TxAdmitBytesCount',
            'qos.TxAdmitPacketsCount',
            'qos.TxDropBytesCount',
            'qos.TxDropPacketsCount'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'Interface',
            'Admin',
            'Oper',
            'Class',
            'Rx Admit [B]',
            'Rx Admin',
            'Rx Drop [B]',
            'Rx Drop',
            'Tx Admit [B]',
            'Tx Admin',
            'Tx Drop [B]',
            'Tx Drop'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                interfaces,
                order,
                ['qos']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            stream=stream
        )

    def print_interface_phy(self, port):
        order = [
            'pod_node_name',
            'id',
            'adminSt',
            'usage',
            'stats.operSpeed',
            'stats.operSt',
            'stats.operStQual',
            'stats.backplaneMac',
            'stats.lastLinkStChg',
            'stats.operRouterMac',
            'stats.operMdix',
            'stats.operMode',
            'stats.accessVlan',
            'stats.nativeVlan',
            'stats.resetCtr',
            'stats.operVlans',
            'stats.allowedVlans',
            'stats.bundleIndex',
            'bw',
            'delay',
            'mdix',
            'medium',
            'mtu',
            'routerMac',
            'speed',
            'fecMode',
            'autoNeg',
            'linkDebounce',
            'dot1qEtherType',
            'layerT',
            'mode',
            'switchingSt',
            'spanMode'
        ]

        headers = [
            'Node',
            'Port',
            'Admin State',
            'Usage',
            'Oper Speed',
            'Oper State',
            'Oper State Reason',
            'Backplane Mac',
            'Last Link State Change',
            'Oper Router Mac',
            'Oper Mdix',
            'Oper Mode',
            'Access VLAN',
            'Native VLAN',
            'Reset Counter',
            'Operational VLANs',
            'Allowed VLANs',
            'Port Channel',
            'Bandwidth (kb)',
            'Delay (usec)',
            'Mdix',
            'Medium',
            'MTU',
            'Router Mac',
            'Speed',
            'Forward Error Correction',
            'Auto Negotiation',
            'Link Debounce Interval (msec)',
            'Dot1Q Ether Type',
            'Layer',
            'Mode',
            'Switching State',
            'Destination SPAN Mode'
        ]

        if 'load_interval' in port:
            order = order + [
                'load_interval.loadIntvl1',
                'load_interval.loadIntvl2',
                'load_interval.loadIntvl3'
            ]

            headers = headers + [
                'Load Interval 1',
                'Load Interval 2',
                'Load Interval 3'
            ]

        if 'eee' in port:
            order = order + [
                'eee.eeeLat',
                'eee.eeeLpi',
                'eee.eeeState'
            ]

            headers = headers + [
                'Eee Lat',
                'Eee Lpi',
                'Eee State'
            ]

        if 'capability' in port:
            order = order + [
                'capability.speed',
                'capability.mdix'
            ]

            headers = headers + [
                'Capability Speed',
                'Capability Mdix'
            ]

        if 'pc' in port:
            order = order + [
                'pc.channelingSt'
            ]

            headers = headers + [
                'Channeling State'
            ]

        if 'fc_stats' in port:
            order = order + [
                'fc_stats.isFcotPresent',
                'fc_stats.typeName',
                'fc_stats.actualType',
                'fc_stats.guiName',
                'fc_stats.guiPN',
                'fc_stats.guiRev',
                'fc_stats.guiSN'
            ]

            headers = headers + [
                'Transceiver Present',
                'Transceiver Type',
                'Transceiver Actual Type',
                'Transceiver Name',
                'Transceiver Part Number',
                'Transceiver Revision',
                'Transceiver Serial Number'
            ]

        self.my_output.dictionary(
            port,
            title='Fabric Port Details',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

        self.print_interface_phy_cdp_adjacency(port)
        self.print_interface_phy_lldp_adjacency(port)
        self.print_interface_phy_epg_stats(port)
        self.print_interface_phy_vlan(port)
        self.print_interface_phy_ether_stats(port)
        self.print_interface_phy_qos_stats(port)

    def print_interface_phy_cdp_adjacency(self, port):
        if 'cdp' in port and len(port['cdp']) > 0:
            for lldp_info in port['cdp']:
                order = [
                    'sysName',
                    'ver',
                    'platId',
                    'portId',
                    'cap',
                    'stQual'
                ]

                headers = [
                    'System Name',
                    'System Version',
                    'Platform',
                    'Port ID',
                    'Capability',
                    'State'
                ]

                self.my_output.dictionary(
                    lldp_info,
                    title='CDP',
                    underline=True,
                    prefix="- ",
                    justify=True,
                    keys=order,
                    title_keys=headers
                )

    def print_interface_phy_lldp_adjacency(self, port):
        if 'lldp' in port and len(port['lldp']) > 0:
            for lldp_info in port['lldp']:
                order = [
                    'sysName',
                    'sysDesc',
                    'portDesc',
                    'portIdT',
                    'portIdV',
                    'capability'
                ]

                headers = [
                    'System Name',
                    'System Description',
                    'Port Description',
                    'Port Id Type',
                    'Port Id Value',
                    'Capability'
                ]

                self.my_output.dictionary(
                    lldp_info,
                    title='LLDP',
                    underline=True,
                    prefix="- ",
                    justify=True,
                    keys=order,
                    title_keys=headers
                )

    def print_interface_phy_epg_stats(self, port):
        if 'epg_stats' not in port or port['epg_stats'] is None:
            return

        self.print_epgs_properties(
            port['epg_stats']
        )

    def print_interface_phy_vlan(self, port):
        if 'epg_stats' not in port or port['epg_stats'] is None:
            return

        order = [
            'epg_stats.nameApTenant',
            'epg_stats.vlan.id',
            'epg_stats.vlan.encap',
            'epg_stats.vlan.fabEncap',
            'epg_stats.vlan.operSt'
        ]

        headers = [
            'EPG',
            'Internal VLAN',
            'Encap VLAN',
            'Fabric VxLAN',
            'VLAN Oper State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                [port],
                order,
                ['epg_stats']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_interface_phy_ether_stats(self, port):
        if 'ether_stats' in port:
            order = [
                'pkts',
                'broadcastPkts',
                'multicastPkts',
                'pkts64Octets',
                'pkts65to127Octets',
                'pkts128to255Octets',
                'pkts256to511Octets',
                'pkts512to1023Octets',
                'pkts1024to1518Octets',
                'oversizePkts',
                'undersizePkts',
                'rXNoErrors',
                'rxGiantPkts',
                'rxOversizePkts',
                'tXNoErrors',
                'txGiantPkts',
                'txOversizePkts',
                'collisions',
                'cRCAlignErrors',
                'dropEvents'
            ]

            headers = [
                'Packets with no errors',
                'Broadcast',
                'Multicast',
                'Size up to 64B',
                'Size 65-1270B',
                'Size 128-255B',
                'Size 256-511B',
                'Size 512-1023',
                'Size 1024-1518',
                'Oversize',
                'Undersize',
                'Rx with no errors',
                'Rx giant',
                'Rx oversize',
                'Tx with no errors',
                'Tx giant',
                'Tx oversize',
                'Collisions',
                'CRC errors',
                'Drops'
            ]

            self.my_output.dictionary(
                port['ether_stats'],
                title='Ethernet Packets Statistics',
                underline=True,
                prefix="- ",
                justify=True,
                keys=order,
                title_keys=headers
            )

    def print_interface_phy_qos_stats(self, port):
        if 'qos' not in port or port['qos'] is None:
            return

        order = [
            'id',
            'RxAdmitBytesCount',
            'RxAdmitPacketsCount',
            'RxDropBytesCount',
            'RxDropPacketsCount',
            'TxAdmitBytesCount',
            'TxAdmitPacketsCount',
            'TxDropBytesCount',
            'TxDropPacketsCount'
        ]

        headers = [
            'Class',
            'Rx Admit [B]',
            'Rx Admin',
            'Rx Drop [B]',
            'Rx Drop',
            'Tx Admit [B]',
            'Tx Admin',
            'Tx Drop [B]',
            'Tx Drop'
        ]

        self.my_output.my_table(
            port['qos'],
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
