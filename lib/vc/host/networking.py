import time

# pylint: disable=no-name-in-module
from pyVmomi import vim

from lib import ip_helper


class VcHostNetworking():
    def __init__(self):
        pass

    def get_host_pnic_info(self, pnic_obj):
        # (vim.host.PhysicalNic) {
        #     dynamicType = <unset>,
        #     dynamicProperty = (vmodl.DynamicProperty) [],
        #     key = 'key-vim.host.PhysicalNic-vmnic0',
        #     device = 'vmnic0',
        #     pci = '0000:0c:00.0',
        #     driver = 'i40en',
        #     linkSpeed = (vim.host.PhysicalNic.LinkSpeedDuplex) {
        #        dynamicType = <unset>,
        #        dynamicProperty = (vmodl.DynamicProperty) [],
        #        speedMb = 10000,
        #        duplex = true
        #     },

        #     validLinkSpecification = (vim.host.PhysicalNic.LinkSpeedDuplex) [
        #        (vim.host.PhysicalNic.LinkSpeedDuplex) {
        #           dynamicType = <unset>,
        #           dynamicProperty = (vmodl.DynamicProperty) [],
        #           speedMb = 10000,
        #           duplex = true
        #        }
        #     ],
        #     spec = (vim.host.PhysicalNic.Specification) {
        #        dynamicType = <unset>,
        #        dynamicProperty = (vmodl.DynamicProperty) [],
        #        ip = (vim.host.IpConfig) {
        #           dynamicType = <unset>,
        #           dynamicProperty = (vmodl.DynamicProperty) [],
        #           dhcp = false,
        #           ipAddress = '',
        #           subnetMask = '',
        #           ipV6Config = <unset>
        #        },
        #        linkSpeed = <unset>,
        #        enableEnhancedNetworkingStack = false,
        #        ensInterruptEnabled = false
        #     },
        #     wakeOnLanSupported = false,
        #     mac = '40:a6:b7:0b:e5:50',
        #     fcoeConfiguration = (vim.host.FcoeConfig) {
        #        dynamicType = <unset>,
        #        dynamicProperty = (vmodl.DynamicProperty) [],
        #        priorityClass = 3,
        #        sourceMac = '40:a6:b7:0b:e5:50',
        #        vlanRange = (vim.host.FcoeConfig.VlanRange) [
        #           (vim.host.FcoeConfig.VlanRange) {
        #              dynamicType = <unset>,
        #              dynamicProperty = (vmodl.DynamicProperty) [],
        #              vlanLow = 0,
        #              vlanHigh = 0
        #           }
        #        ],
        #        capabilities = (vim.host.FcoeConfig.FcoeCapabilities) {
        #           dynamicType = <unset>,
        #           dynamicProperty = (vmodl.DynamicProperty) [],
        #           priorityClass = false,
        #           sourceMacAddress = false,
        #           vlanRange = false
        #        },
        #        fcoeActive = false
        #     },
        #     vmDirectPathGen2Supported = false,
        #     vmDirectPathGen2SupportedMode = <unset>,
        #     resourcePoolSchedulerAllowed = true,
        #     resourcePoolSchedulerDisallowedReason = (str) [],
        #     autoNegotiateSupported = true,
        #     enhancedNetworkingStackSupported = true,
        #     ensInterruptSupported = true,
        #     rdmaDevice = <unset>
        # },

        info = {}

        info['key'] = pnic_obj.key
        info['device'] = pnic_obj.device
        info['pci'] = pnic_obj.pci
        info['driver'] = pnic_obj.driver

        link_speed_obj = pnic_obj.linkSpeed
        if link_speed_obj is not None:
            info['speedMb'] = link_speed_obj.speedMb
            info['speedUnit'] = self.convert_speed(
                info['speedMb'] * 1000 * 1000
            )
            info['duplex'] = link_speed_obj.duplex

        info['mac'] = pnic_obj.mac
        info['wakeOnLanSupported'] = pnic_obj.wakeOnLanSupported

        return info

    def get_host_vnic_info(self, vnic_obj, port_group_info):
        # (vim.host.VirtualNic) {
        #     dynamicType = <unset>,
        #     dynamicProperty = (vmodl.DynamicProperty) [],
        #     device = 'vmk0',
        #     key = 'key-vim.host.VirtualNic-vmk0',
        #     portgroup = 'Management Network',
        #     spec = (vim.host.VirtualNic.Specification) {
        #        dynamicType = <unset>,
        #        dynamicProperty = (vmodl.DynamicProperty) [],
        #        ip = (vim.host.IpConfig) {
        #           dynamicType = <unset>,
        #           dynamicProperty = (vmodl.DynamicProperty) [],
        #           dhcp = false,
        #           ipAddress = '<ip>',
        #           subnetMask = '<ip>',
        #           ipV6Config = <unset>
        #        },
        #        mac = '3c:fd:fe:cb:f7:c0',
        #        distributedVirtualPort = <unset>,
        #        portgroup = 'Management Network',
        #        mtu = 1500,
        #        tsoEnabled = true,
        #        netStackInstanceKey = 'defaultTcpipStack',
        #        opaqueNetwork = <unset>,
        #        externalId = <unset>,
        #        pinnedPnic = <unset>,
        #        ipRouteSpec = (vim.host.VirtualNic.IpRouteSpec) {
        #           dynamicType = <unset>,
        #           dynamicProperty = (vmodl.DynamicProperty) [],
        #           ipRouteConfig = (vim.host.IpRouteConfig) {
        #              dynamicType = <unset>,
        #              dynamicProperty = (vmodl.DynamicProperty) [],
        #              defaultGateway = '<ip>',
        #              gatewayDevice = <unset>,
        #              ipV6DefaultGateway = <unset>,
        #              ipV6GatewayDevice = <unset>
        #           }
        #        },
        #        systemOwned = <unset>
        #     },
        #     port = 'key-vim.host.PortGroup.Port-234881068'
        # },

        info = {}
        info['key'] = vnic_obj.key
        info['device'] = vnic_obj.device
        info['portgroup'] = vnic_obj.portgroup
        info['mac'] = vnic_obj.spec.mac
        info['mtu'] = vnic_obj.spec.mtu
        info['ip'] = vnic_obj.spec.ip.ipAddress
        info['mask'] = vnic_obj.spec.ip.subnetMask
        info['prefix'] = ip_helper.netmask_to_prefix(vnic_obj.spec.ip.subnetMask)
        info['cidr'] = '%s/%s' % (
            info['ip'],
            info['prefix']
        )

        info['gateway'] = None
        ip_route_spec = vnic_obj.spec.ipRouteSpec
        if ip_route_spec is not None:
            info['gateway'] = ip_route_spec.ipRouteConfig.defaultGateway

        info['port_key'] = vnic_obj.port
        info['vswitch'] = None
        info['vlan'] = None
        for port_group in port_group_info:
            for port in port_group['ports']:
                if port['key'] == info['port_key']:
                    info['vswitch'] = port_group['vswitch']
                    info['vlan'] = port_group['vlan']

        return info

    def get_host_vnic_services(self, services_obj):
        services = {}
        for net_config in services_obj.netConfig:
            if len(net_config.selectedVnic) == 0:
                continue

            services[net_config.nicType] = []
            for nic_key in net_config.selectedVnic:
                for nic_candidate in net_config.candidateVnic:
                    if nic_candidate.key == nic_key:
                        services[net_config.nicType].append(
                            nic_candidate.device
                        )

        return services

    def get_host_port_group_config_info(self, port_group_obj):
        # (vim.host.PortGroup) {
        #     dynamicType = <unset>,
        #     dynamicProperty = (vmodl.DynamicProperty) [],
        #     key = 'key-vim.host.PortGroup-iscsi-B',
        #     port = (vim.host.PortGroup.Port) [
        #         (vim.host.PortGroup.Port) {
        #             dynamicType = <unset>,
        #             dynamicProperty = (vmodl.DynamicProperty) [],
        #             key = 'key-vim.host.PortGroup.Port-234881072',
        #             mac = (str) [
        #                 '00:50:56:65:15:68'
        #             ],
        #             type = 'host'
        #         }
        #     ],
        #     vswitch = 'key-vim.host.VirtualSwitch-vSwitch0',
        #     computedPolicy = (vim.host.NetworkPolicy) {
        #         dynamicType = <unset>,
        #         dynamicProperty = (vmodl.DynamicProperty) [],
        #         security = (vim.host.NetworkPolicy.SecurityPolicy) {
        #             dynamicType = <unset>,
        #             dynamicProperty = (vmodl.DynamicProperty) [],
        #             allowPromiscuous = false,
        #             macChanges = true,
        #             forgedTransmits = true
        #         },
        #         nicTeaming = (vim.host.NetworkPolicy.NicTeamingPolicy) {
        #             dynamicType = <unset>,
        #             dynamicProperty = (vmodl.DynamicProperty) [],
        #             policy = 'loadbalance_srcid',
        #             reversePolicy = true,
        #             notifySwitches = true,
        #             rollingOrder = false,
        #             failureCriteria = (vim.host.NetworkPolicy.NicFailureCriteria) {
        #                 dynamicType = <unset>,
        #                 dynamicProperty = (vmodl.DynamicProperty) [],
        #                 checkSpeed = 'minimum',
        #                 speed = 10,
        #                 checkDuplex = false,
        #                 fullDuplex = false,
        #                 checkErrorPercent = false,
        #                 percentage = 0,
        #                 checkBeacon = false
        #             },
        #             nicOrder = (vim.host.NetworkPolicy.NicOrderPolicy) {
        #                 dynamicType = <unset>,
        #                 dynamicProperty = (vmodl.DynamicProperty) [],
        #                 activeNic = (str) [
        #                 'vmnic1'
        #                 ],
        #                 standbyNic = (str) []
        #             }
        #         },
        #         offloadPolicy = (vim.host.NetOffloadCapabilities) {
        #             dynamicType = <unset>,
        #             dynamicProperty = (vmodl.DynamicProperty) [],
        #             csumOffload = true,
        #             tcpSegmentation = true,
        #             zeroCopyXmit = true
        #         },
        #         shapingPolicy = (vim.host.NetworkPolicy.TrafficShapingPolicy) {
        #             dynamicType = <unset>,
        #             dynamicProperty = (vmodl.DynamicProperty) [],
        #             enabled = false,
        #             averageBandwidth = <unset>,
        #             peakBandwidth = <unset>,
        #             burstSize = <unset>
        #         }
        #     },
        #     spec = (vim.host.PortGroup.Specification) {
        #         dynamicType = <unset>,
        #         dynamicProperty = (vmodl.DynamicProperty) [],
        #         name = 'iscsi-B',
        #         vlanId = 19,
        #         vswitchName = 'vSwitch0',

        #         policy = (vim.host.NetworkPolicy) {
        #             dynamicType = <unset>,
        #             dynamicProperty = (vmodl.DynamicProperty) [],
        #             security = (vim.host.NetworkPolicy.SecurityPolicy) {
        #                 dynamicType = <unset>,
        #                 dynamicProperty = (vmodl.DynamicProperty) [],
        #                 allowPromiscuous = <unset>,
        #                 macChanges = <unset>,
        #                 forgedTransmits = <unset>
        #             },
        #             nicTeaming = (vim.host.NetworkPolicy.NicTeamingPolicy) {
        #                 dynamicType = <unset>,
        #                 dynamicProperty = (vmodl.DynamicProperty) [],
        #                 policy = <unset>,
        #                 reversePolicy = <unset>,
        #                 notifySwitches = <unset>,
        #                 rollingOrder = <unset>,
        #                 failureCriteria = (vim.host.NetworkPolicy.NicFailureCriteria) {
        #                 dynamicType = <unset>,
        #                 dynamicProperty = (vmodl.DynamicProperty) [],
        #                 checkSpeed = <unset>,
        #                 speed = <unset>,
        #                 checkDuplex = <unset>,
        #                 fullDuplex = <unset>,
        #                 checkErrorPercent = <unset>,
        #                 percentage = <unset>,
        #                 checkBeacon = <unset>
        #                 },
        #                 nicOrder = (vim.host.NetworkPolicy.NicOrderPolicy) {
        #                 dynamicType = <unset>,
        #                 dynamicProperty = (vmodl.DynamicProperty) [],
        #                 activeNic = (str) [
        #                     'vmnic1'
        #                 ],
        #                 standbyNic = (str) []
        #                 }
        #             },
        #             offloadPolicy = (vim.host.NetOffloadCapabilities) {
        #                 dynamicType = <unset>,
        #                 dynamicProperty = (vmodl.DynamicProperty) [],
        #                 csumOffload = <unset>,
        #                 tcpSegmentation = <unset>,
        #                 zeroCopyXmit = <unset>
        #             },
        #             shapingPolicy = (vim.host.NetworkPolicy.TrafficShapingPolicy) {
        #                 dynamicType = <unset>,
        #                 dynamicProperty = (vmodl.DynamicProperty) [],
        #                 enabled = <unset>,
        #                 averageBandwidth = <unset>,
        #                 peakBandwidth = <unset>,
        #                 burstSize = <unset>
        #             }
        #         }
        #     }
        # },

        info = {}
        info['key'] = getattr(port_group_obj, 'key')
        info['ports'] = []
        port_objs = getattr(port_group_obj, 'port', None)
        if port_objs is not None:
            for port_obj in port_objs:
                port_info = {}
                port_info['key'] = getattr(port_obj, 'key')
                port_info['type'] = getattr(port_obj, 'type')
                port_info['mac'] = []
                macs = getattr(port_obj, 'mac', None)
                if macs is not None:
                    for mac in macs:
                        port_info['mac'].append(mac)
                info['ports'].append(port_info)

        info['vswitch_key'] = getattr(port_group_obj, 'vswitch', None)

        security = getattr(
            getattr(port_group_obj, 'computedPolicy'),
            'security'
        )

        info['allowPromiscuous'] = getattr(security, 'allowPromiscuous')
        info['macChanges'] = getattr(security, 'macChanges')
        info['forgedTransmits'] = getattr(security, 'forgedTransmits')

        spec = getattr(port_group_obj, 'spec')
        info['name'] = getattr(spec, 'name')
        info['vswitch'] = getattr(spec, 'vswitchName')
        info['vlan'] = getattr(spec, 'vlanId')

        return info

    def get_host_vswitch_config_info(self, vswitch_obj):
        info = {}
        info['name'] = vswitch_obj.name
        info['mtu'] = vswitch_obj.mtu
        info['portgroup'] = []
        for port_group_key in vswitch_obj.portgroup:
            item = {}
            item['key'] = port_group_key
            info['portgroup'].append(item)

        info['pnic'] = []
        for pnic_key in vswitch_obj.pnic:
            item = {}
            item['key'] = pnic_key
            info['pnic'].append(item)

        spec = getattr(vswitch_obj, 'spec')
        info['discoveryProtocol'] = spec.bridge.linkDiscoveryProtocolConfig.protocol

        return info

    def get_host_dvswitch_config_info(self, dvswitch_obj):
        info = {}
        info['name'] = dvswitch_obj.dvsName
        info['mtu'] = dvswitch_obj.mtu

        info['pnic'] = []
        for pnic_key in dvswitch_obj.spec.backing.pnicSpec:
            item = {}
            item['device'] = pnic_key.pnicDevice
            item['uplink'] = pnic_key.uplinkPortKey
            info['pnic'].append(item)

        return info

    def get_host_pci_pt(self, pci_pt_obj):
        info = []

        for pci_pt_device in pci_pt_obj:
            if isinstance(pci_pt_device, vim.Host.PciPassthruInfo):
                keys = [
                    'id',
                    'passthruEnabled',
                    'passthruCapable',
                    'passthruActive'
                ]
                item = {}
                for key in keys:
                    item[key] = getattr(pci_pt_device, key)
                info.append(item)

        return info

    def get_host_sriov(self, pci_pt_obj):
        info = []

        if pci_pt_obj is None:
            return info

        for pci_pt_device in pci_pt_obj:
            if isinstance(pci_pt_device, vim.host.SriovInfo):
                keys = [
                    'id',
                    'passthruEnabled',
                    'passthruCapable',
                    'passthruActive',
                    'sriovEnabled',
                    'sriovCapable',
                    'sriovActive',
                    'numVirtualFunctionRequested',
                    'numVirtualFunction',
                    'maxVirtualFunctionSupported'
                ]
                item = {}
                for key in keys:
                    item[key] = getattr(pci_pt_device, key)

                item['vf'] = '%s/%s/%s' % (
                    item['numVirtualFunctionRequested'],
                    item['numVirtualFunction'],
                    item['maxVirtualFunctionSupported']
                )
                info.append(item)

        return info

    def get_host_networking_hint_cdp_info(self, cdp_obj):
        info = {}
        info['switch_device_id'] = cdp_obj.devId
        info['switch_system_name'] = cdp_obj.systemName
        info['switch_hw'] = cdp_obj.hardwarePlatform
        info['switch_sw'] = cdp_obj.softwareVersion
        info['switch_mgmt_ip'] = cdp_obj.mgmtAddr
        info['switch_port'] = cdp_obj.portId
        return info

    def get_host_networking_hint_lldp_info(self, lldp_obj):
        info = {}
        for paremeter_obj in lldp_obj.parameter:
            if paremeter_obj.key == 'Management Address':
                info['switch_mgmt_ip'] = paremeter_obj.value

            if paremeter_obj.key == 'System Name':
                info['switch_system_name'] = paremeter_obj.value

            if paremeter_obj.key == 'System Description':
                info['switch_device_id'] = paremeter_obj.value

        info['switch_hw'] = ''
        info['switch_sw'] = ''
        info['switch_port'] = lldp_obj.portId

        return info

    def get_host_networking_hint_info(self, hint_obj):
        info = {}
        info['device'] = hint_obj.device

        cdp_obj = getattr(hint_obj, 'connectedSwitchPort', None)
        lldp_obj = getattr(hint_obj, 'lldpInfo', None)

        nei_info = None
        info['switch_source'] = None

        if cdp_obj is not None:
            info['switch_source'] = 'cdp'
            nei_info = self.get_host_networking_hint_cdp_info(cdp_obj)

        if lldp_obj is not None:
            info['switch_source'] = 'lldp'
            nei_info = self.get_host_networking_hint_lldp_info(lldp_obj)

        if nei_info is not None:
            for key in nei_info:
                info[key] = nei_info[key]

        return info

    def get_host_networking_hints(self, host_obj):
        hints = []
        network_system = host_obj.configManager.networkSystem
        if network_system is not None:
            if network_system.capabilities.supportsNetworkHints:
                for hint_obj in network_system.QueryNetworkHint():
                    hints.append(
                        self.get_host_networking_hint_info(
                            hint_obj
                        )
                    )

        return hints

    def get_host_networking(self, host_obj):
        network_config = host_obj.config.network

        start_time = int(time.time() * 1000)

        info = {}

        info['vswitch'] = []
        for vswitch_obj in network_config.vswitch:
            info['vswitch'].append(
                self.get_host_vswitch_config_info(
                    vswitch_obj
                )
            )

        info['dvswitch'] = []
        for dvswitch_obj in network_config.proxySwitch:
            info['dvswitch'].append(
                self.get_host_dvswitch_config_info(
                    dvswitch_obj
                )
            )

        info['port_group'] = []
        for port_group_obj in network_config.portgroup:
            info['port_group'].append(
                self.get_host_port_group_config_info(
                    port_group_obj
                )
            )

        info['pnic'] = []
        for pnic_obj in network_config.pnic:
            info['pnic'].append(
                self.get_host_pnic_info(
                    pnic_obj
                )
            )

        info['pnic'] = sorted(
            info['pnic'],
            key=lambda i: i['device']
        )

        sriovs = self.get_host_sriov(
            host_obj.config.pciPassthruInfo
        )

        hints = self.get_host_networking_hints(
            host_obj
        )

        for pnic in info['pnic']:
            pnic['sriov'] = {}
            pnic['sriov']['sriovCapable'] = False
            for sriov in sriovs:
                if pnic['pci'] == sriov['id']:
                    pnic['sriov'] = sriov

            pnic['uplink'] = None
            for vswitch in info['vswitch']:
                for vswitch_pnic in vswitch['pnic']:
                    if vswitch_pnic['key'] == pnic['key']:
                        pnic['uplink'] = vswitch['name']

            for dvswitch in info['dvswitch']:
                for dvswitch_pnic in dvswitch['pnic']:
                    if dvswitch_pnic['device'] == pnic['device']:
                        pnic['uplink'] = dvswitch['name']

            for hint in hints:
                if hint['device'] == pnic['device']:
                    for key in hint:
                        if key != 'device':
                            pnic[key] = hint[key]

        info['vnic'] = []
        for vnic_obj in network_config.vnic:
            info['vnic'].append(
                self.get_host_vnic_info(
                    vnic_obj,
                    info['port_group']
                )
            )

        info['vnic'] = sorted(
            info['vnic'],
            key=lambda i: i['device']
        )

        info['vnic_services'] = self.get_host_vnic_services(
            host_obj.config.virtualNicManagerInfo
        )
        for vnic in info['vnic']:
            vnic['services'] = []
            for vnic_service in info['vnic_services']:
                for vnic_device in info['vnic_services'][vnic_service]:
                    if vnic['device'] == vnic_device:
                        vnic['services'].append(vnic_service)

        duration = int(time.time() * 1000) - start_time
        self.log.vcenter(
            'get',
            'get_host_net',
            True,
            duration
        )

        return info

    def print_host_networking_vmkernel(self, info):
        order = [
            'device',
            'portgroup',
            'vswitch',
            'vlan',
            'cidr',
            'gateway',
            'services'
        ]

        headers = [
            'VMkernel Adapter Device',
            'Network Label',
            'Switch',
            'VLAN',
            'IP',
            'Gateway',
            'Services'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info['vnic'],
                order,
                ['services']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_host_networking_pnic(self, info):
        order = [
            'device',
            'pci',
            'driver',
            'speedUnit',
            'duplex',
            'mac',
            'wakeOnLanSupported',
            'sriov.sriovCapable',
            'sriov.sriovActive',
            'sriov.vf',
            'uplink'
        ]

        headers = [
            'Physical Adapter',
            'PCI',
            'Driver',
            'Speed',
            'Duplex',
            'MAC',
            'Wake On LAN',
            'SRIOV Capable',
            'SRIOV Active',
            'VF (req/act/max)',
            'vSwitch Uplink'
        ]

        self.my_output.my_table(
            info['pnic'],
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_host_networking_pnic_switch(self, info):
        order = [
            'device',
            'switch_source',
            'switch_system_name',
            'switch_port',
            'switch_hw',
            'switch_sw',
            'switch_mgmt_ip'
        ]

        headers = [
            'Physical Adapter',
            'Source',
            'Switch Name',
            'Port',
            'Hardware',
            'Software',
            'Management IP'
        ]

        self.my_output.my_table(
            info['pnic'],
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_host_networking(self, info):
        self.print_host_networking_vmkernel(info)
        self.print_host_networking_pnic(info)
        self.print_host_networking_pnic_switch(info)

    def print_host_phy_networking(self, info):
        self.print_host_networking_pnic(info)
        self.print_host_networking_pnic_switch(info)
