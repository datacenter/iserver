from lib import log_helper
from lib.intersight import cache as intersight_cache
from lib.intersight import equipment_fan_module
from lib.intersight import equipment_fan
from lib.intersight import equipment_fan_control
from lib.intersight import equipment_psu
from lib.intersight import equipment_psu_control
from lib.intersight import power_control_state
from lib.intersight import equipment_iocard
from lib.intersight import ethernet_host_port
from lib.intersight import ethernet_network_port
from lib.intersight import ethernet_physical_port
from lib.intersight import compute_blade
from lib.intersight import adapter_unit
from lib.intersight import adapter_ext_eth_interface
from lib.intersight import cond_alarm
from lib.intersight import tam_advisory_instance
from lib.intersight import asset_device_contract_information
from lib.intersight import chassis_profile
from lib.intersight import network_element_summary


class ChassisExtraAttributes():
    """Class for chassis object extra attributes
    """
    def __init__(self, iaccount, log_id=None):
        self.chassis = None
        self.chassis_info = {}
        self.chassis_helper = {}
        self.settings = None

        self.log_handler = log_helper.Log(log_id=log_id)

        self.cache_handler = intersight_cache.IntersightCache(
            iaccount,
            log_id=log_id
        )

        self.iocard_handler = equipment_iocard.EquipmentIoCard(iaccount, log_id=log_id)
        self.ether_host_port_handler = ethernet_host_port.EthernetHostPort(iaccount, log_id=log_id)
        self.ether_network_port_handler = ethernet_network_port.EthernetNetworkPort(iaccount, log_id=log_id)
        self.ether_physical_port_handler = ethernet_physical_port.EthernetPhysicalPort(iaccount, log_id=log_id)

        self.fan_module_handler = equipment_fan_module.EquipmentFanModule(iaccount, log_id=log_id)
        self.fan_handler = equipment_fan.EquipmentFan(iaccount, log_id=log_id)
        self.fan_control_handler = equipment_fan_control.EquipmentFanControl(iaccount, log_id=log_id)
        self.psu_handler = equipment_psu.EquipmentPsu(iaccount, log_id=log_id)
        self.psu_control_handler = equipment_psu_control.EquipmentPsuControl(iaccount, log_id=log_id)
        self.power_control_state_handler = power_control_state.PowerControlState(iaccount, log_id=log_id)

        self.compute_blade_handler = compute_blade.ComputeBlade(iaccount, log_id=log_id)
        self.adapter_unit_handler = adapter_unit.AdapterUnit(iaccount, log_id=log_id)
        self.adapter_ext_eth_interface_handler = adapter_ext_eth_interface.AdapterExtEthInterface(iaccount, log_id=log_id)
        self.cond_alarm_handler = cond_alarm.CondAlarm(iaccount, log_id=log_id)
        self.tam_advisory_instance_handler = tam_advisory_instance.TamAdvisoryInstance(iaccount, log_id=log_id)
        self.asset_device_contract_information_handler = asset_device_contract_information.AssetDeviceContractInformation(iaccount, log_id=log_id)
        self.chassis_profile_handler = chassis_profile.ChassisProfile(iaccount, log_id=log_id)
        self.network_element_summary_handler = network_element_summary.NetworkElementSummary(iaccount, log_id=log_id)

    def add_common_attributes(self):
        keys = [
            'ConnectionPath',
            'ConnectionStatus',
            'Description',
            'Dn',
            'DeviceMoId',
            'Moid',
            'Model',
            'Name',
            'OperState',
            'PartNumber',
            'Pid',
            'ProductName',
            'Serial',
            'Sku',
            'Vendor'
        ]

        for key in keys:
            if isinstance(self.chassis[key], str):
                self.chassis_info[key] = self.chassis[key].strip()
                continue

            self.chassis_info[key] = self.chassis[key]

        if self.chassis['AlarmSummary']['Warning'] == 0 and self.chassis['AlarmSummary']['Critical'] == 0:
            self.chassis_info['Health'] = 'Healthy'
            self.chassis_info['HealthSummary'] = 'Healthy'
        if self.chassis['AlarmSummary']['Warning'] > 0 and self.chassis['AlarmSummary']['Critical'] == 0:
            self.chassis_info['Health'] = 'Warnings'
            self.chassis_info['HealthSummary'] = 'Warnings (%s)' % (self.chassis['AlarmSummary']['Warning'])
        if self.chassis['AlarmSummary']['Critical'] > 0:
            self.chassis_info['Health'] = 'Critical'
            self.chassis_info['HealthSummary'] = 'Critical (%s)' % (self.chassis['AlarmSummary']['Critical'])

        self.chassis_info['AlarmWarning'] = self.chassis['AlarmSummary']['Warning']
        self.chassis_info['AlarmCritical'] = self.chassis['AlarmSummary']['Critical']

        self.chassis_info['ConnectionSummary'] = '%s / %s' % (
            self.chassis_info['ConnectionPath'],
            self.chassis_info['ConnectionStatus']
        )

        self.chassis_info['NodeMax'] = None
        self.chassis_info['IfmMax'] = None
        self.chassis_info['FanModuleMax'] = None
        self.chassis_info['FanMax'] = None
        self.chassis_info['PsuMax'] = None

        if self.chassis_info['Model'] == 'UCSX-9508':
            self.chassis_info['NodeMax'] = 8
            self.chassis_info['IfmMax'] = 2
            self.chassis_info['FanModuleMax'] = 4
            self.chassis_info['FanMax'] = 8
            self.chassis_info['PsuMax'] = 6

    def add_chassis_alarms_attributes(self):
        self.chassis_info['Alarms'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'alarm',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_chassis_alarms_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.chassis_info['Alarms'].append(
                    self.cond_alarm_handler.get_info(
                        managed_object
                    )
                )

    def add_chassis_advisory_attributes(self):
        self.chassis_info['Advisory'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'advisory',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_chassis_advisory_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.chassis_info['Advisory'].append(
                    self.tam_advisory_instance_handler.get_info(
                        managed_object
                    )
                )

        self.chassis_info['AdvisoryCount'] = len(
            self.chassis_info['Advisory']
        )

    def add_chassis_contract_attributes(self):
        self.chassis_info['Contract'] = None

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'contract',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_chassis_contract_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
            return

        if len(managed_objects) == 0:
            return

        if len(managed_objects) > 1:
            self.log_handler.error(
                'add_chassis_contract_attributes',
                'Unexpected contract count: %s' % (self.chassis['Moid'])
            )
            return

        self.chassis_info['Contract'] = self.asset_device_contract_information_handler.get_info(
            managed_objects[0]
        )

    def add_chassis_profile_attributes(self):
        self.chassis_info['Profile'] = None

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'profile',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_chassis_profile_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
            return

        if len(managed_objects) == 0:
            return

        if len(managed_objects) > 1:
            self.log_handler.error(
                'add_chassis_profile_attributes',
                'Unexpected profile count: %s' % (self.chassis['Moid'])
            )
            return

        self.chassis_info['Profile'] = self.chassis_profile_handler.get_info(
            managed_objects[0]
        )

    def add_chassis_domain_attributes(self):
        self.chassis_info['Domain'] = {}
        self.chassis_info['Domain']['Name'] = self.chassis['RegisteredDevice']['DeviceHostname'][0]

        self.chassis_info['Domain']['Switch'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'network',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_chassis_domain_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.chassis_info['Domain']['Switch'].append(
                    self.network_element_summary_handler.get_info(
                        managed_object
                    )
                )

        self.chassis_info['Domain']['Switch'] = sorted(
            self.chassis_info['Domain']['Switch'],
            key=lambda k: (k['Name'])
        )

    def add_node_attributes(self):
        self.chassis_info['NodeInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'blade',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_node_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.chassis_info['NodeInfo'].append(
                    self.compute_blade_handler.get_info(
                        managed_object
                    )
                )

        # Sort for nice display
        self.chassis_info['NodeInfo'] = sorted(
            self.chassis_info['NodeInfo'],
            key=lambda k: (k['SlotId'])
        )

        # Summaries

        self.chassis_info['NodePowerOn'] = 0
        for blade_info in self.chassis_info['NodeInfo']:
            if blade_info['PowerOn']:
                self.chassis_info['NodePowerOn'] = self.chassis_info['NodePowerOn'] + 1

        self.chassis_info['NodeCount'] = len(
            self.chassis_info['NodeInfo']
        )

        if self.chassis_info['NodeMax'] is None:
            self.chassis_info['NodeSummary'] = '%s/%s' % (
                self.chassis_info['NodePowerOn'],
                self.chassis_info['NodeCount']
            )
        else:
            self.chassis_info['NodeSummary'] = '%s/%s/%s' % (
                self.chassis_info['NodePowerOn'],
                self.chassis_info['NodeCount'],
                self.chassis_info['NodeMax']
            )

    def add_adapter_unit_attributes(self):
        self.chassis_helper['AdapterUnitIds'] = []
        self.chassis_info['AdapterUnitInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'adapter',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_adapter_unit_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
            return

        for managed_object in managed_objects:
            self.chassis_helper['AdapterUnitIds'].append(
                managed_object['Moid']
            )

            adapter_unit_info = self.adapter_unit_handler.get_info(
                managed_object
            )
            self.chassis_info['AdapterUnitInfo'].append(
                adapter_unit_info
            )

            for node_info in self.chassis_info['NodeInfo']:
                if adapter_unit_info['ComputeNodeMoid'] == node_info['Moid']:
                    adapter_unit_info['ComputeNodeId'] = node_info['SlotId']
                    adapter_unit_info['ComputeNodePowerOn'] = node_info['PowerOn']

    def add_adapter_ext_eth_interface_attributes(self):
        self.chassis_info['AdapterExtEthInterfaceInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'interface',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_adapter_ext_eth_interface_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
            return

        for managed_object in managed_objects:
            adapter_ext_eth_interface_info = self.adapter_ext_eth_interface_handler.get_info(
                managed_object
            )

            for adapter_unit_info in self.chassis_info['AdapterUnitInfo']:
                if adapter_ext_eth_interface_info['AdapterUnitId'] == adapter_unit_info['Moid']:
                    adapter_ext_eth_interface_info['ComputeNodeMoid'] = adapter_unit_info['ComputeNodeMoid']
                    adapter_ext_eth_interface_info['ComputeNodeId'] = adapter_unit_info['ComputeNodeId']
                    adapter_ext_eth_interface_info['ComputeNodePowerOn'] = adapter_unit_info['ComputeNodePowerOn']
                    adapter_ext_eth_interface_info['ComputeNodeSlot'] = adapter_unit_info['PciSlot']
                    adapter_ext_eth_interface_info['AdepterModel'] = adapter_unit_info['Model']
                    adapter_ext_eth_interface_info['AdepterOperState'] = adapter_unit_info['OperState']
                    adapter_ext_eth_interface_info['AdepterPresence'] = adapter_unit_info['Presence']
                    adapter_ext_eth_interface_info['AdepterSerial'] = adapter_unit_info['Serial']

            if adapter_ext_eth_interface_info['ComputeNodePowerOn']:
                adapter_ext_eth_interface_info['PeerInfo'] = 'Node #%s (P+) %s %s' % (
                    adapter_ext_eth_interface_info['ComputeNodeId'],
                    adapter_ext_eth_interface_info['ComputeNodeSlot'],
                    adapter_ext_eth_interface_info['AdepterModel']
                )

            if not adapter_ext_eth_interface_info['ComputeNodePowerOn']:
                adapter_ext_eth_interface_info['PeerInfo'] = 'Node #%s (P-) %s %s' % (
                    adapter_ext_eth_interface_info['ComputeNodeId'],
                    adapter_ext_eth_interface_info['ComputeNodeSlot'],
                    adapter_ext_eth_interface_info['AdepterModel']
                )

            self.chassis_info['AdapterExtEthInterfaceInfo'].append(
                adapter_ext_eth_interface_info
            )

        for host_port in self.chassis_info['HostPortInfo']:
            host_port['PeerInfo'] = ''
            host_port['PeerNodeId'] = None

            if host_port['PeerInterfaceType'] is not None:
                if host_port['PeerInterfaceType'] == 'adapter.ExtEthInterface':
                    for ext_eth_interface_info in self.chassis_info['AdapterExtEthInterfaceInfo']:
                        if host_port['PeerInterfaceId'] == ext_eth_interface_info['Moid']:
                            host_port['PeerNodeId'] = ext_eth_interface_info['ComputeNodeId']
                            host_port['PeerInfo'] = ext_eth_interface_info['PeerInfo']

    def add_io_module_attributes(self):
        self.chassis_info['IfmInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'iocard',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_io_module_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.chassis_info['IfmInfo'].append(
                    self.iocard_handler.get_info(
                        managed_object
                    )
                )

        self.chassis_info['IfmInfo'] = sorted(
            self.chassis_info['IfmInfo'],
            key=lambda k: (k['ModuleId'])
        )

        # Summaries

        self.chassis_info['IfmOn'] = 0
        for io_module in self.chassis_info['IfmInfo']:
            if io_module['On']:
                self.chassis_info['IfmOn'] = self.chassis_info['IfmOn'] + 1

        self.chassis_info['IfmCount'] = len(
            self.chassis_info['IfmInfo']
        )

        if self.chassis_info['IfmMax'] is None:
            self.chassis_info['IfmSummary'] = '%s/%s' % (
                self.chassis_info['IfmOn'],
                self.chassis_info['IfmCount']
            )
        else:
            self.chassis_info['IfmSummary'] = '%s/%s/%s' % (
                self.chassis_info['IfmOn'],
                self.chassis_info['IfmCount'],
                self.chassis_info['IfmMax']
            )

    def add_host_port_attributes(self):
        self.chassis_info['HostPortInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'ether_host_port',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_host_port_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
        else:
            for managed_object in managed_objects:
                host_port_info = self.ether_host_port_handler.get_info(
                    managed_object
                )

                # Enrich with module info
                for io_module in self.chassis_info['IfmInfo']:
                    if io_module['Moid'] == host_port_info['IoModuleId']:
                        host_port_info['IfmDn'] = io_module['Dn']
                        host_port_info['IfmName'] = io_module['Name']
                        host_port_info['IfmId'] = io_module['ModuleId']

                self.chassis_info['HostPortInfo'].append(
                    host_port_info
                )

        # Sort for nice display
        self.chassis_info['HostPortInfo'] = sorted(
            self.chassis_info['HostPortInfo'],
            key=lambda k: (
                k['IfmName'],
                k['ModuleId'],
                k['SlotId'],
                k['PortId']
            )
        )

        # Module Host Port Summaries

        for io_module_info in self.chassis_info['IfmInfo']:
            io_module_info['HostPortCount'] = len(
                io_module_info['HostPorts']
            )

            io_module_info['HostPortUp'] = 0
            for host_port_moid in io_module_info['HostPorts']:
                for host_port_info in self.chassis_info['HostPortInfo']:
                    if host_port_moid == host_port_info['Moid']:
                        if host_port_info['Up']:
                            io_module_info['HostPortUp'] = io_module_info['HostPortUp'] + 1

            io_module_info['HostPortSummary'] = '%s/%s' % (
                io_module_info['HostPortUp'],
                io_module_info['HostPortCount']
            )

        # Global Summaries

        self.chassis_info['HostPortCount'] = 0
        self.chassis_info['HostPortUp'] = 0

        for io_module_info in self.chassis_info['IfmInfo']:
            self.chassis_info['HostPortCount'] = self.chassis_info['HostPortCount'] + io_module_info['HostPortCount']
            self.chassis_info['HostPortUp'] = self.chassis_info['HostPortUp'] + io_module_info['HostPortUp']

        self.chassis_info['HostPortSummary'] = '%s/%s' % (
            self.chassis_info['HostPortUp'],
            self.chassis_info['HostPortCount']
        )

    def add_network_port_attributes(self):
        self.chassis_helper['PhysicalPortIds'] = []
        self.chassis_info['NetworkPortInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'ether_network_port',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_network_port_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
        else:
            for managed_object in managed_objects:
                network_port_info = self.ether_network_port_handler.get_info(
                    managed_object
                )

                # Enrich with module info
                for io_module in self.chassis_info['IfmInfo']:
                    if io_module['Moid'] == network_port_info['IoModuleId']:
                        network_port_info['IfmDn'] = io_module['Dn']
                        network_port_info['IfmName'] = io_module['Name']
                        network_port_info['IfmId'] = io_module['ModuleId']

                self.chassis_info['NetworkPortInfo'].append(
                    network_port_info
                )

                # Populate physical port ids for later use
                if network_port_info['PeerInterfaceType'] is not None:
                    if network_port_info['PeerInterfaceType'] == 'ether.PhysicalPort':
                        self.chassis_helper['PhysicalPortIds'].append(
                            network_port_info['PeerInterfaceId']
                        )

        # Sort for nice display
        self.chassis_info['NetworkPortInfo'] = sorted(
            self.chassis_info['NetworkPortInfo'],
            key=lambda k: (
                k['IfmDn'],
                k['PortId']
            )
        )

        # Module Host Port Summaries

        for io_module_info in self.chassis_info['IfmInfo']:
            io_module_info['NetworkPortCount'] = len(
                io_module_info['NetworkPorts']
            )

            io_module_info['NetworkPortUp'] = 0
            for network_port_moid in io_module_info['NetworkPorts']:
                for network_port_info in self.chassis_info['NetworkPortInfo']:
                    if network_port_moid == network_port_info['Moid']:
                        if network_port_info['Up']:
                            io_module_info['NetworkPortUp'] = io_module_info['NetworkPortUp'] + 1

            if io_module_info['NetworkPortMax'] is None:
                io_module_info['NetworkPortSummary'] = '%s/%s' % (
                    io_module_info['NetworkPortUp'],
                    io_module_info['NetworkPortCount']
                )
            else:
                io_module_info['NetworkPortSummary'] = '%s/%s/%s' % (
                    io_module_info['NetworkPortUp'],
                    io_module_info['NetworkPortCount'],
                    io_module_info['NetworkPortMax']
                )

        # Global Summaries

        self.chassis_info['NetworkPortUp'] = 0
        self.chassis_info['NetworkPortCount'] = 0
        self.chassis_info['NetworkPortMax'] = 0

        for io_module_info in self.chassis_info['IfmInfo']:
            if io_module_info['NetworkPortMax'] is not None:
                self.chassis_info['NetworkPortMax'] = self.chassis_info['NetworkPortMax'] + io_module_info['NetworkPortMax']

            self.chassis_info['NetworkPortCount'] = self.chassis_info['NetworkPortCount'] + io_module_info['NetworkPortCount']
            self.chassis_info['NetworkPortUp'] = self.chassis_info['NetworkPortUp'] + io_module_info['NetworkPortUp']

        if self.chassis_info['NetworkPortMax'] == 0:
            self.chassis_info['NetworkPortSummary'] = '%s/%s' % (
                self.chassis_info['NetworkPortUp'],
                self.chassis_info['NetworkPortCount']
            )
        else:
            self.chassis_info['NetworkPortSummary'] = '%s/%s/%s' % (
                self.chassis_info['NetworkPortUp'],
                self.chassis_info['NetworkPortCount'],
                self.chassis_info['NetworkPortMax']
            )

    def add_physical_port_attributes(self):
        self.chassis_info['PhysicalPortInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'ether_physical_port',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_physical_port_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.chassis_info['PhysicalPortInfo'].append(
                    self.ether_physical_port_handler.get_info(
                        managed_object
                    )
                )

        for network_port in self.chassis_info['NetworkPortInfo']:
            if network_port['PeerInterfaceType'] is not None:
                if network_port['PeerInterfaceType'] == 'ether.PhysicalPort':
                    for physical_port_info in self.chassis_info['PhysicalPortInfo']:
                        if network_port['PeerInterfaceId'] == physical_port_info['Moid']:
                            network_port['PeerSwitchId'] = physical_port_info['SwitchId']
                            network_port['PeerPortName'] = physical_port_info['Name']
                            network_port['PeerPortChannelId'] = physical_port_info['PortChannelId']
                            network_port['PeerPortTransceiverType'] = physical_port_info['TransceiverType']
                            network_port['PeerOperSpeed'] = physical_port_info['OperSpeed']

    def add_fan_control_attributes(self):
        self.chassis_info['FanControlInfo'] = None

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'fan_control',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_fan_control_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
            return

        if len(managed_objects) == 0:
            return

        if len(managed_objects) > 1:
            self.log_handler.error(
                'add_fan_control_attributes',
                'Unexpected fan control count: %s' % (self.chassis['Moid'])
            )
            return

        self.chassis_info['FanControlInfo'] = self.fan_control_handler.get_info(
            managed_objects[0]
        )

    def add_fan_module_attributes(self):
        self.chassis_helper['FanModuleIds'] = []
        self.chassis_info['FanModuleInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'fan_module',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_fan_module_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.chassis_info['FanModuleInfo'].append(
                    self.fan_module_handler.get_info(
                        managed_object
                    )
                )

        # Sort for nice display
        self.chassis_info['FanModuleInfo'] = sorted(
            self.chassis_info['FanModuleInfo'],
            key=lambda i: i['ModuleId']
        )

        # Summaries

        self.chassis_info['FanModulesOn'] = 0
        for fan_module in self.chassis_info['FanModuleInfo']:
            if fan_module['On']:
                self.chassis_info['FanModulesOn'] = self.chassis_info['FanModulesOn'] + 1

        self.chassis_info['FanModuleCount'] = len(self.chassis_info['FanModuleInfo'])

        if self.chassis_info['FanModuleMax'] is None:
            self.chassis_info['FanModuleSummary'] = '%s/%s' % (
                self.chassis_info['FanModulesOn'],
                self.chassis_info['FanModuleCount']
            )
        else:
            self.chassis_info['FanModuleSummary'] = '%s/%s/%s' % (
                self.chassis_info['FanModulesOn'],
                self.chassis_info['FanModuleCount'],
                self.chassis_info['FanModuleMax']
            )

    def add_fan_attributes(self):
        self.chassis_info['FanInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'fan',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_fan_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.chassis_info['FanInfo'].append(
                    self.fan_handler.get_info(
                        managed_object
                    )
                )

        # Sort for nice display
        self.chassis_info['FanInfo'] = sorted(
            self.chassis_info['FanInfo'],
            key=lambda i: i['ModuleId']
        )

        # Summaries

        self.chassis_info['FanOn'] = 0
        for fan in self.chassis_info['FanInfo']:
            if fan['On']:
                self.chassis_info['FanOn'] = self.chassis_info['FanOn'] + 1

        self.chassis_info['FanCount'] = len(
            self.chassis_info['FanInfo']
        )

        if self.chassis_info['FanMax'] is None:
            self.chassis_info['FanSummary'] = '%s/%s' % (
                self.chassis_info['FanOn'],
                self.chassis_info['FanCount']
            )
        else:
            self.chassis_info['FanSummary'] = '%s/%s/%s' % (
                self.chassis_info['FanOn'],
                self.chassis_info['FanCount'],
                self.chassis_info['FanMax']
            )

    def add_psu_control_attributes(self):
        self.chassis_info['PsuControlStateInfo'] = None

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'psu_control',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_psu_control_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
            return

        if len(managed_objects) == 0:
            return

        if len(managed_objects) > 1:
            self.log_handler.error(
                'add_psu_control_attributes',
                'Unexpected psu control count: %s' % (self.chassis['Moid'])
            )
            return

        self.chassis_info['PsuControlStateInfo'] = self.psu_control_handler.get_info(
            managed_objects[0]
        )

    def add_power_control_attributes(self):
        self.chassis_info['PowerControlStateInfo'] = None

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'power_control',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_power_control_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
            return

        if len(managed_objects) == 0:
            return

        if len(managed_objects) > 1:
            self.log_handler.error(
                'add_power_control_attributes',
                'Unexpected psu control count: %s' % (self.chassis['Moid'])
            )
            return

        self.chassis_info['PowerControlStateInfo'] = self.power_control_state_handler.get_info(
            managed_objects[0]
        )

    def add_psu_attributes(self):
        self.chassis_info['PsuInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'psu',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_psu_attributes',
                'No cache:%s' % (self.chassis['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.chassis_info['PsuInfo'].append(
                    self.psu_handler.get_info(
                        managed_object
                    )
                )

        # Sort psu info for nice display
        self.chassis_info['PsuInfo'] = sorted(
            self.chassis_info['PsuInfo'],
            key=lambda i: i['Dn']
        )

        # Summaries

        self.chassis_info['PsuCount'] = len(
            self.chassis_info['PsuInfo']
        )

        self.chassis_info['PsuOn'] = 0
        for psu_info in self.chassis_info['PsuInfo']:
            if psu_info['On']:
                self.chassis_info['PsuOn'] = self.chassis_info['PsuOn'] + 1

        if self.chassis_info['PsuMax'] is None:
            self.chassis_info['PsuSummary'] = '%s/%s' % (
                self.chassis_info['PsuOn'],
                self.chassis_info['PsuCount']
            )
        else:
            self.chassis_info['PsuSummary'] = '%s/%s/%s' % (
                self.chassis_info['PsuOn'],
                self.chassis_info['PsuCount'],
                self.chassis_info['PsuMax']
            )

    def add_chassis_attributes(self, chassis_mo, settings):
        self.chassis = chassis_mo
        self.chassis_info = {}
        self.settings = settings

        self.add_common_attributes()
        self.add_node_attributes()

        self.add_io_module_attributes()
        self.add_host_port_attributes()
        self.add_network_port_attributes()
        self.add_physical_port_attributes()

        self.add_adapter_unit_attributes()
        self.add_adapter_ext_eth_interface_attributes()

        self.add_chassis_domain_attributes()
        self.add_chassis_alarms_attributes()
        self.add_chassis_advisory_attributes()
        self.add_chassis_contract_attributes()
        self.add_chassis_profile_attributes()

        self.add_fan_control_attributes()
        self.add_fan_module_attributes()
        self.add_fan_attributes()

        self.add_power_control_attributes()
        self.add_psu_control_attributes()
        self.add_psu_attributes()

        self.log_handler.set_log(
            'chassis_info.%s' % (chassis_mo['Moid']),
            self.chassis_info,
            json_conversion=True
        )

        return self.chassis_info
