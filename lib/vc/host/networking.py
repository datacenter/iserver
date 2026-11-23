import time
from lib.vc import helper as vc_helper

# pylint: disable=no-name-in-module
from pyVmomi import vim

from lib import ip_helper


class VcHostNetworking():
    def __init__(self):
        pass

    def get_host_pnic_info(self, pnic_obj):
        info = {}

        info['key'] = pnic_obj.key
        info['device'] = pnic_obj.device
        info['_index'] = 0
        if len(info['device'].split('vmnic')) == 2:
            info['_index'] = int(info['device'].split('vmnic')[1])

        info['pci'] = pnic_obj.pci
        info['driver'] = pnic_obj.driver

        link_speed_obj = pnic_obj.linkSpeed
        info['up'] = False
        info['speedMb'] = None
        info['speedUnit'] = None
        info['duplex'] = None
        if link_speed_obj is not None:
            info['up'] = True
            info['speedMb'] = link_speed_obj.speedMb
            info['speedUnit'] = vc_helper.convert_speed(
                info['speedMb'] * 1000 * 1000
            )
            info['duplex'] = link_speed_obj.duplex

        info['mac'] = pnic_obj.mac
        info['wakeOnLanSupported'] = pnic_obj.wakeOnLanSupported

        info['autoNegotiateSupported'] = pnic_obj.autoNegotiateSupported
        info['dpuId'] = pnic_obj.dpuId
        info['driverVersion'] = pnic_obj.driverVersion
        info['enhancedNetworkingStackSupported'] = pnic_obj.enhancedNetworkingStackSupported
        info['ensInterruptSupported'] = pnic_obj.ensInterruptSupported
        info['firmwareVersion'] = str(pnic_obj.firmwareVersion)
        info['rdmaDevice'] = pnic_obj.rdmaDevice
        info['resourcePoolSchedulerAllowed'] = pnic_obj.resourcePoolSchedulerAllowed

        return info

    def get_host_vnic_info(self, vnic_obj, port_group_info):
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
        try:
            info['discoveryProtocol'] = spec.bridge.linkDiscoveryProtocolConfig.protocol
        except BaseException:
            info['discoveryProtocol'] = None

        return info

    def normalize_dvswitch_uplink_name(self, name):
        if 'uplink' in name.lower():
            return name.lower().replace(' ', '')
        return name

    def get_host_dvswitch_config_info(self, dvswitch_obj):
        info = {}
        info['name'] = dvswitch_obj.dvsName
        info['key'] = dvswitch_obj.key
        info['mtu'] = dvswitch_obj.mtu
        info['configNumPorts'] = dvswitch_obj.configNumPorts
        info['numPorts'] = dvswitch_obj.numPorts
        info['numPortsAvailable'] = dvswitch_obj.numPortsAvailable

        keys = {}
        for obj in dvswitch_obj.uplinkPort:
            keys[obj.key] = self.normalize_dvswitch_uplink_name(obj.value)

        info['pnic'] = []
        for pnic_key in dvswitch_obj.spec.backing.pnicSpec:
            item = {}
            item['device'] = pnic_key.pnicDevice
            item['uplink'] = keys[pnic_key.uplinkPortKey]
            item['uplinkId'] = 0
            if 'uplink' in item['uplink']:
                item['uplinkId'] = int(item['uplink'].split('uplink')[1])
            item['uplinkPortGroup'] = pnic_key.uplinkPortgroupKey
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

    def get_host_networking_hint_cdp_switch_info(self, cdp_obj):
        info = {}
        info['switch_device_id'] = cdp_obj.devId
        info['switch_system_name'] = cdp_obj.systemName
        info['switch_hw'] = cdp_obj.hardwarePlatform
        info['switch_sw'] = cdp_obj.softwareVersion
        info['switch_mgmt_ip'] = cdp_obj.mgmtAddr
        info['switch_port'] = cdp_obj.portId
        return info

    def get_host_networking_hint_cdp_info(self, cdp_obj):
        info = {}
        info['address'] = cdp_obj.address
        info['cdpVersion'] = cdp_obj.cdpVersion
        info['devId'] = cdp_obj.devId
        info['deviceCapability'] = {}
        if cdp_obj.deviceCapability is not None:
            info['deviceCapability']['router'] = cdp_obj.deviceCapability.router
            info['deviceCapability']['transparentBridge'] = cdp_obj.deviceCapability.transparentBridge
            info['deviceCapability']['sourceRouteBridge'] = cdp_obj.deviceCapability.sourceRouteBridge
            info['deviceCapability']['networkSwitch'] = cdp_obj.deviceCapability.networkSwitch
            info['deviceCapability']['igmpEnabled'] = cdp_obj.deviceCapability.igmpEnabled
            info['deviceCapability']['repeater'] = cdp_obj.deviceCapability.repeater

        info['fullDuplex'] = cdp_obj.fullDuplex
        info['hardwarePlatform'] = cdp_obj.hardwarePlatform
        info['ipPrefix'] = cdp_obj.ipPrefix
        info['ipPrefixLen'] = cdp_obj.ipPrefixLen
        info['location'] = cdp_obj.location
        info['mgmtAddr'] = cdp_obj.mgmtAddr
        info['mtu'] = cdp_obj.mtu
        info['portId'] = cdp_obj.portId
        info['softwareVersion'] = cdp_obj.softwareVersion
        info['systemName'] = cdp_obj.systemName
        info['timeout'] = cdp_obj.timeout
        info['ttl'] = cdp_obj.ttl
        info['vlan'] = cdp_obj.vlan

        return info

    def get_host_networking_hint_lldp_switch_info(self, lldp_obj):
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

    def get_host_networking_hint_lldp_info(self, lldp_obj):
        info = {}
        info['chassisId'] = lldp_obj.chassisId
        info['portId'] = lldp_obj.portId
        info['timeToLive'] = lldp_obj.timeToLive
        for paremeter_obj in lldp_obj.parameter:
            if paremeter_obj.key == 'Management Address':
                value = paremeter_obj.value
                if ip_helper.is_mac_address(value):
                    info['managementMac'] = paremeter_obj.value
                if ip_helper.is_valid_ipv4_address(value):
                    info['managementIPv4'] = paremeter_obj.value

            if paremeter_obj.key == 'System Name':
                info['systemName'] = paremeter_obj.value

            if paremeter_obj.key == 'System Description':
                info['systemDescription'] = paremeter_obj.value

            if paremeter_obj.key == 'Port Description':
                info['portDescription'] = paremeter_obj.value

            if paremeter_obj.key == 'TimeOut':
                info['timeOut'] = paremeter_obj.value

            if paremeter_obj.key == 'Vlan ID':
                info['vlan'] = paremeter_obj.value

            if paremeter_obj.key == 'Enabled Capabilities':
                info['deviceCapability'] = {}
                cap_obj = paremeter_obj.value
                if cap_obj is not None:
                    info['deviceCapability']['router'] = cap_obj.router
                    info['deviceCapability']['transparentBridge'] = cap_obj.transparentBridge
                    info['deviceCapability']['sourceRouteBridge'] = cap_obj.sourceRouteBridge
                    info['deviceCapability']['networkSwitch'] = cap_obj.networkSwitch
                    info['deviceCapability']['igmpEnabled'] = cap_obj.igmpEnabled
                    info['deviceCapability']['repeater'] = cap_obj.repeater

        return info

    def get_host_networking_hint_ip_network(self, hint_objs):
        info = []

        for hint_obj in hint_objs:
            item = {}
            item['vlan'] = hint_obj.vlanId
            item['subnet'] = hint_obj.ipSubnet
            info.append(
                item
            )

        return info

    def get_host_networking_hint_info(self, hint_obj):
        info = {}
        info['device'] = hint_obj.device

        cdp_obj = getattr(hint_obj, 'connectedSwitchPort', None)
        lldp_obj = getattr(hint_obj, 'lldpInfo', None)

        info['hintNetwork'] = self.get_host_networking_hint_ip_network(hint_obj.subnet)

        nei_info = None
        info['switch_source'] = None

        info['cdp'] = None
        if cdp_obj is not None:
            info['cdp'] = self.get_host_networking_hint_cdp_info(cdp_obj)
            info['switch_source'] = 'cdp'
            nei_info = self.get_host_networking_hint_cdp_switch_info(cdp_obj)

        info['lldp'] = None
        if lldp_obj is not None:
            info['lldp'] = self.get_host_networking_hint_lldp_info(lldp_obj)
            info['switch_source'] = 'lldp'
            nei_info = self.get_host_networking_hint_lldp_switch_info(lldp_obj)

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
            key=lambda i: i['_index']
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
