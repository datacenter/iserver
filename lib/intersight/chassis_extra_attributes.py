from lib import log_helper
from lib.intersight import cache as intersight_cache
from lib.intersight.adapter_unit import main as adapter_unit
from lib.intersight.adapter_ext_eth_interface import main as adapter_ext_eth_interface
from lib.intersight.asset_device_contract_information import main as asset_device_contract_information
from lib.intersight.chassis_profile import main as chassis_profile
from lib.intersight.compute_blade import main as compute_blade
from lib.intersight.cond_alarm import main as cond_alarm
from lib.intersight.equipment_expander_module import main as equipment_expander_module
from lib.intersight.equipment_fan_module import main as equipment_fan_module
from lib.intersight.equipment_fan import main as equipment_fan
from lib.intersight.equipment_fan_control import main as equipment_fan_control
from lib.intersight.equipment_iocard import main as equipment_iocard
from lib.intersight.equipment_psu import main as equipment_psu
from lib.intersight.equipment_psu_control import main as equipment_psu_control
from lib.intersight.ethernet_host_port import main as ethernet_host_port
from lib.intersight.ethernet_network_port import main as ethernet_network_port
from lib.intersight.ethernet_physical_port import main as ethernet_physical_port
from lib.intersight.network_element_summary import main as network_element_summary
from lib.intersight.power_control_state import main as power_control_state
from lib.intersight.tam_advisory_instance import main as tam_advisory_instance


class ChassisExtraAttributes():
    """Class for chassis object extra attributes
    """
    def __init__(self, iaccount, log_id=None):
        self.chassis_info = {}
        self.chassis_helper = {}

        self.log_handler = log_helper.Log(log_id=log_id)

        self.cache_handler = intersight_cache.IntersightCache(
            iaccount,
            log_id=log_id
        )

        self.iocard_handler = equipment_iocard.EquipmentIoCard(iaccount, log_id=log_id)
        self.expander_module_handler = equipment_expander_module.EquipmentExpanderModule(iaccount, log_id=log_id)
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

    def add_common_attributes(self, chassis_mo):
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
            if isinstance(chassis_mo[key], str):
                self.chassis_info[key] = chassis_mo[key].strip()
                continue

            self.chassis_info[key] = chassis_mo[key]

        self.chassis_info['AlarmSummary'] = {}
        self.chassis_info['AlarmSummary']['__Output'] = {}
        self.chassis_info['AlarmSummary']['__Output']['Critical'] = 'Red'
        self.chassis_info['AlarmSummary']['__Output']['Warning'] = 'Yellow'
        self.chassis_info['AlarmSummary']['__Output']['Info'] = 'Blue'
        self.chassis_info['AlarmSummary']['__Output']['Cleared'] = 'Green'

        for key in ['Critical', 'Warning', 'Info', 'Cleared']:
            if key in chassis_mo['AlarmSummary']:
                self.chassis_info['AlarmSummary'][key] = chassis_mo['AlarmSummary'][key]

        self.chassis_info['Health'] = 'Healthy'
        self.chassis_info['__Output']['Health'] = 'Green'

        if self.chassis_info['AlarmSummary']['Warning'] == 0 and self.chassis_info['AlarmSummary']['Critical'] == 0:
            if 'Info' in self.chassis_info['AlarmSummary'] and self.chassis_info['AlarmSummary']['Info'] > 0:
                self.chassis_info['Health'] = 'Healthy (%s)' % (
                    self.chassis_info['AlarmSummary']['Info']
                )
                self.chassis_info['__Output']['Health'] = 'Blue'

        if self.chassis_info['AlarmSummary']['Warning'] > 0 and self.chassis_info['AlarmSummary']['Critical'] == 0:
            self.chassis_info['Health'] = 'Warnings (%s)' % (
                self.chassis_info['AlarmSummary']['Warning']
            )
            self.chassis_info['__Output']['Health'] = 'Yellow'

        if self.chassis_info['AlarmSummary']['Critical'] > 0:
            self.chassis_info['Health'] = 'Critical (%s)' % (
                self.chassis_info['AlarmSummary']['Critical']
            )
            self.chassis_info['__Output']['Health'] = 'Red'

        if self.chassis_info['OperState'] == '':
            self.chassis_info['OperStateTick'] = '--'
        else:
            if self.chassis_info['OperState'].lower() in ['ok', 'operable']:
                self.chassis_info['OperStateTick'] = '\u2713'
                self.chassis_info['__Output']['OperStateTick'] = 'Green'
            else:
                self.chassis_info['OperStateTick'] = '\u2717'
                self.chassis_info['__Output']['OperStateTick'] = 'Red'

        self.chassis_info['NodeCount'] = len(
            chassis_mo['Blades']
        )

        self.chassis_info['FanModuleCount'] = len(
            chassis_mo['Fanmodules']
        )

        self.chassis_info['IoCount'] = len(
            chassis_mo['Ioms']
        )

        self.chassis_info['ExpanderModuleCount'] = len(
            chassis_mo['ExpanderModules']
        )

        self.chassis_info['PsuCount'] = len(
            chassis_mo['Psus']
        )

    def add_alarm_info(self, include_cleared=False, include_acknowledged=False):
        self.chassis_info['AlarmInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'alarm',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_alarm_info',
                'No cache:%s' % (self.chassis['Moid'])
            )
            return

        critical_count = 0
        warning_count = 0
        info_count = 0

        for managed_object in managed_objects:
            alarm_info = self.cond_alarm_handler.get_info(
                managed_object
            )
            if alarm_info['Severity'] == 'Cleared' and not include_cleared:
                continue

            if alarm_info['Acknowledge'] == 'Acknowledge' and not include_acknowledged:
                continue

            if alarm_info['AncestorMoId'] != self.chassis_info['Moid']:
                continue

            if alarm_info['Severity'] == 'Critical':
                critical_count = critical_count + 1

            if alarm_info['Severity'] == 'Warning':
                warning_count = warning_count + 1

            if alarm_info['Severity'] == 'Info':
                info_count = info_count + 1

            self.chassis_info['AlarmInfo'].append(
                alarm_info
            )

        if critical_count != self.chassis_info['AlarmSummary']['Critical']:
            self.log.error(
                'add_alarm_info',
                'Critical alarms do not match count: %s' % (self.chassis_info['Moid'])
            )

        if warning_count != self.chassis_info['AlarmSummary']['Warning']:
            self.log.error(
                'add_alarm_info',
                'Warning alarms do not match count: %s' % (self.chassis_info['Moid'])
            )

        if info_count != self.chassis_info['AlarmSummary']['Info']:
            self.log.error(
                'add_alarm_info',
                'Info alarms do not match count: %s' % (self.chassis_info['Moid'])
            )

    def add_advisory_info(self):
        self.chassis_info['AdvisoryInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'advisory',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_advisory_info',
                'No cache:%s' % (self.chassis['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.chassis_info['AdvisoryInfo'].append(
                    self.tam_advisory_instance_handler.get_info(
                        managed_object
                    )
                )

    def add_contract_info(self):
        self.chassis_info['ContractInfo'] = None

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'contract',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_contract_info',
                'No cache:%s' % (self.chassis['Moid'])
            )
            return

        if len(managed_objects) == 0:
            return

        if len(managed_objects) > 1:
            self.log_handler.error(
                'add_contract_info',
                'Unexpected contract count: %s' % (self.chassis['Moid'])
            )
            return

        self.chassis_info['ContractInfo'] = self.asset_device_contract_information_handler.get_info(
            managed_objects[0]
        )

    def add_profile_info(self):
        self.chassis_info['ProfileInfo'] = None

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'profile',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_profile_info',
                'No cache:%s' % (self.chassis['Moid'])
            )
            return

        if len(managed_objects) == 0:
            return

        if len(managed_objects) > 1:
            self.log_handler.error(
                'add_profile_info',
                'Unexpected profile count: %s' % (self.chassis['Moid'])
            )
            return

        self.chassis_info['ProfileInfo'] = self.chassis_profile_handler.get_info(
            managed_objects[0]
        )

    def add_domain_info(self, chassis_mo):
        self.chassis_info['Domain'] = {}
        self.chassis_info['Domain']['Name'] = chassis_mo['RegisteredDevice']['DeviceHostname'][0]

        self.chassis_info['Domain']['Switch'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'network',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_domain_info',
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

    def add_node_info(self):
        self.chassis_info['NodeInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'blade',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_node_info',
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
            key=lambda i: (
                i['SlotId']
            )
        )

        for node_info in self.chassis_info['NodeInfo']:
            if node_info['Presence'] == 'equipped':
                inventory_info = {}
                inventory_info['Order'] = 2
                inventory_info['SubOrder'] = node_info['SlotId']
                inventory_info['Type'] = 'Node'
                inventory_info['Name'] = node_info['ServerName']
                for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                    inventory_info[key] = ''
                    if key in node_info:
                        inventory_info[key] = node_info[key]
                        if inventory_info[key] is None:
                                inventory_info[key] = ''

                inventory_info['ChassisMoid'] = self.chassis_info['Moid']
                inventory_info['ServerType'] = 'N/A'
                inventory_info['ServerPid'] = 'N/A'
                inventory_info['ServerSerial'] = 'N/A'

                self.chassis_info['Inventory'].append(
                    inventory_info
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

            adapter_unit_info['ComputeNodeId'] = None
            adapter_unit_info['ComputeNodePowerOn'] = None
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

    def add_io_info(self):
        self.chassis_info['IfmInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'iocard',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_io_info',
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
            key=lambda i: (
                i['ModuleId']
            )
        )

        # Inventory

        for ifm_info in self.chassis_info['IfmInfo']:
            if ifm_info['Presence'] == 'equipped':
                inventory_info = {}
                inventory_info['Order'] = 3
                inventory_info['SubOrder'] = ifm_info['ModuleId']
                inventory_info['Type'] = 'IO'
                inventory_info['Name'] = ifm_info['Name']
                for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                    inventory_info[key] = ''
                    if key in ifm_info:
                        inventory_info[key] = ifm_info[key]
                        if inventory_info[key] is None:
                                inventory_info[key] = ''

                inventory_info['ChassisMoid'] = self.chassis_info['Moid']
                inventory_info['ServerType'] = 'N/A'
                inventory_info['ServerPid'] = 'N/A'
                inventory_info['ServerSerial'] = 'N/A'

                self.chassis_info['Inventory'].append(
                    inventory_info
                )

    def add_expander_module_info(self):
        self.chassis_info['ExpanderModuleInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'expander_module',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_expander_module_info',
                'No cache:%s' % (self.chassis['Moid'])
            )
        else:
            for managed_object in managed_objects:
                self.chassis_info['ExpanderModuleInfo'].append(
                    self.expander_module_handler.get_info(
                        managed_object
                    )
                )

        self.chassis_info['ExpanderModuleInfo'] = sorted(
            self.chassis_info['ExpanderModuleInfo'],
            key=lambda i: (
                i['ModuleId']
            )
        )

        # Inventory

        for expander_info in self.chassis_info['ExpanderModuleInfo']:
            if expander_info['Presence'] == 'equipped':
                inventory_info = {}
                inventory_info['Order'] = 4
                inventory_info['SubOrder'] = expander_info['ModuleId']
                inventory_info['Type'] = 'Expander'
                inventory_info['Name'] = expander_info['Name']
                for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                    inventory_info[key] = ''
                    if key in expander_info:
                        inventory_info[key] = expander_info[key]
                        if inventory_info[key] is None:
                                inventory_info[key] = ''

                inventory_info['ChassisMoid'] = self.chassis_info['Moid']
                inventory_info['ServerType'] = 'N/A'
                inventory_info['ServerPid'] = 'N/A'
                inventory_info['ServerSerial'] = 'N/A'

                self.chassis_info['Inventory'].append(
                    inventory_info
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

    def add_fan_control_info(self):
        self.chassis_info['FanControlInfo'] = None

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'fan_control',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_fan_control_info',
                'No cache:%s' % (self.chassis['Moid'])
            )
            return

        if len(managed_objects) == 0:
            return

        if len(managed_objects) > 1:
            self.log_handler.error(
                'add_fan_control_info',
                'Unexpected fan control count: %s' % (self.chassis['Moid'])
            )
            return

        self.chassis_info['FanControlInfo'] = self.fan_control_handler.get_info(
            managed_objects[0]
        )

    def add_fan_module_info(self):
        self.chassis_helper['FanModuleIds'] = []
        self.chassis_info['FanModuleInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'fan_module',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_fan_module_info',
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

    def add_fan_info(self):
        self.chassis_info['FanInfo'] = []

        managed_objects = self.cache_handler.get_intersight_cache_entry(
            'fan',
            subdirectory=self.chassis_info['Moid'],
            check_ttl=False
        )
        if managed_objects is None:
            self.log_handler.error(
                'add_fan_info',
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
            key=lambda i: (
                i['FanModuleId'],
                i['FanId']
            )
        )

        # Inventory

        for fan_info in self.chassis_info['FanInfo']:
            if fan_info['Presence'] == 'equipped':
                inventory_info = {}
                inventory_info['Order'] = 5
                inventory_info['SubOrder'] = (fan_info['FanModuleId'] + 1) * 10 + fan_info['FanId']
                inventory_info['Type'] = 'Fan'
                inventory_info['Name'] = fan_info['Name']
                for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                    inventory_info[key] = ''
                    if key in fan_info:
                        inventory_info[key] = fan_info[key]
                        if inventory_info[key] is None:
                            inventory_info[key] = ''

                inventory_info['ChassisMoid'] = self.chassis_info['Moid']
                inventory_info['ServerType'] = 'N/A'
                inventory_info['ServerPid'] = 'N/A'
                inventory_info['ServerSerial'] = 'N/A'

                self.chassis_info['Inventory'].append(
                    inventory_info
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

        # Inventory

        for psu_info in self.chassis_info['PsuInfo']:
            inventory_info = {}
            inventory_info['Order'] = 6
            inventory_info['SubOrder'] = psu_info['Id']
            inventory_info['Type'] = 'PSU'
            inventory_info['Id'] = psu_info['Id']
            inventory_info['Name'] = 'PSU #%s' % (psu_info['Id'])
            for key in ['Model', 'Vendor', 'Serial', 'Pid']:
                inventory_info[key] = ''
                if key in psu_info:
                    inventory_info[key] = psu_info[key]
                    if inventory_info[key] is None:
                        inventory_info[key] = ''

            inventory_info['ChassisMoid'] = self.chassis_info['Moid']
            inventory_info['ServerType'] = 'N/A'
            inventory_info['ServerPid'] = 'N/A'
            inventory_info['ServerSerial'] = 'N/A'

            self.chassis_info['Inventory'].append(
                inventory_info
            )

    def add_chassis_attributes(self, chassis_mo, settings):
        self.chassis_info = {}
        self.chassis_info['__Output'] = {}

        self.add_common_attributes(chassis_mo)

        self.chassis_info['Inventory'] = []
        inventory_info = {}
        inventory_info['Order'] = 1
        inventory_info['SubOrder'] = 1
        inventory_info['Type'] = 'Chassis'
        inventory_info['Name'] = self.chassis_info['Name']
        for key in ['Model', 'Vendor', 'Serial', 'Pid']:
            inventory_info[key] = ''
            if key in self.chassis_info:
                inventory_info[key] = self.chassis_info[key]
                if inventory_info[key] is None:
                    inventory_info[key] = ''

        if len(inventory_info['Pid']) == 0:
            inventory_info['Pid'] = inventory_info['Model']

        inventory_info['ChassisMoid'] = self.chassis_info['Moid']
        self.chassis_info['ChassisPid'] = inventory_info['Pid']
        self.chassis_info['ChassisSerial'] = inventory_info['Serial']

        inventory_info['ServerType'] = 'N/A'
        inventory_info['ServerPid'] = 'N/A'
        inventory_info['ServerSerial'] = 'N/A'

        self.chassis_info['Inventory'].append(
            inventory_info
        )

        if 'alarm' in settings and settings['alarm']:
            self.add_alarm_info()

        if 'advisory' in settings and settings['advisory']:
            self.add_advisory_info()

        if 'contract' in settings and settings['contract']:
            self.add_contract_info()

        if 'profile' in settings and settings['profile']:
            self.add_profile_info()

        if 'node' in settings and settings['node']:
            self.add_node_info()

        if 'io' in settings and settings['io']:
            self.add_io_info()

        if 'expander_module' in settings and settings['expander_module']:
            self.add_expander_module_info()

        if 'eth' in settings and settings['eth']:
            self.add_adapter_unit_attributes()

        if 'port' in settings and settings['port']:
            self.add_adapter_unit_attributes()
            self.add_host_port_attributes()
            self.add_network_port_attributes()
            self.add_physical_port_attributes()
            self.add_adapter_ext_eth_interface_attributes()

        if 'fi' in settings and settings['fi']:
            self.add_domain_info(chassis_mo)

        if 'fan' in settings and settings['fan']:
            self.add_fan_module_info()
            self.add_fan_info()

        if 'fan_control' in settings and settings['fan_control']:
            self.add_fan_control_info()

        if 'psu_control' in settings and settings['psu_control']:
            self.add_power_control_attributes()
            self.add_psu_control_attributes()

        if 'psu' in settings and settings['psu']:
            self.add_psu_attributes()

        self.chassis_info['Inventory'] = sorted(
            self.chassis_info['Inventory'],
            key=lambda i: (
                i['Order'],
                i['SubOrder']
            )
        )

        self.log_handler.set_log(
            'chassis_info.%s' % (chassis_mo['Moid']),
            self.chassis_info,
            json_conversion=True
        )

        return self.chassis_info
