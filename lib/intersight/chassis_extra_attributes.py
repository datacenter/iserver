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
    def __init__(self, iaccount, settings, log_id=None):
        self.settings = settings
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
        self.chassis_info['Chassis'] = {}

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
                self.chassis_info['Chassis'][key] = self.chassis[key].strip()
                continue

            self.chassis_info['Chassis'][key] = self.chassis[key]

        if self.chassis['AlarmSummary']['Warning'] == 0 and self.chassis['AlarmSummary']['Critical'] == 0:
            self.chassis_info['Chassis']['Health'] = 'Healthy'
            self.chassis_info['Chassis']['HealthSummary'] = 'Healthy'
        if self.chassis['AlarmSummary']['Warning'] > 0 and self.chassis['AlarmSummary']['Critical'] == 0:
            self.chassis_info['Chassis']['Health'] = 'Warnings'
            self.chassis_info['Chassis']['HealthSummary'] = 'Warnings (%s)' % (self.chassis['AlarmSummary']['Warning'])
        if self.chassis['AlarmSummary']['Critical'] > 0:
            self.chassis_info['Chassis']['Health'] = 'Critical'
            self.chassis_info['Chassis']['HealthSummary'] = 'Critical (%s)' % (self.chassis['AlarmSummary']['Critical'])

        self.chassis_info['Chassis']['AlarmWarning'] = self.chassis['AlarmSummary']['Warning']
        self.chassis_info['Chassis']['AlarmCritical'] = self.chassis['AlarmSummary']['Critical']

        self.chassis_info['Chassis']['ConnectionSummary'] = '%s / %s' % (
            self.chassis_info['Chassis']['ConnectionPath'],
            self.chassis_info['Chassis']['ConnectionStatus']
        )

        self.chassis_info['Chassis']['NodeMax'] = None
        self.chassis_info['Chassis']['IfmMax'] = None
        self.chassis_info['Chassis']['FanModuleMax'] = None
        self.chassis_info['Chassis']['FanMax'] = None
        self.chassis_info['Chassis']['PsuMax'] = None

        if self.chassis_info['Chassis']['Model'] == 'UCSX-9508':
            self.chassis_info['Chassis']['NodeMax'] = 8
            self.chassis_info['Chassis']['IfmMax'] = 2
            self.chassis_info['Chassis']['FanModuleMax'] = 4
            self.chassis_info['Chassis']['FanMax'] = 8
            self.chassis_info['Chassis']['PsuMax'] = 6

    def add_chassis_alarms_attributes(self):
        # Dependencies
        # - only base chassis object required

        self.cond_alarm_handler.set_get_filter(
            "AncestorMoId eq '%s'" % (self.chassis['Moid'])
        )

        self.chassis_info['Chassis']['Alarms'] = []

        for alarm_item in self.cond_alarm_handler.get_all():
            self.chassis_info['Chassis']['Alarms'].append(
                self.cond_alarm_handler.get_info(
                    alarm_item['Moid']
                )
            )

    def add_chassis_advisory_attributes(self):
        # Dependencies
        # - only base chassis object required

        self.tam_advisory_instance_handler.set_get_filter(
            "AffectedObjectMoid eq '%s'" % (self.chassis['Moid'])
        )

        self.chassis_info['Chassis']['Advisory'] = []

        for advisory_item in self.tam_advisory_instance_handler.get_all():
            self.chassis_info['Chassis']['Advisory'].append(
                self.cond_alarm_handler.get_info(
                    advisory_item['Moid']
                )
            )

        self.chassis_info['Chassis']['AdvisoryCount'] = len(
            self.chassis_info['Chassis']['Advisory']
        )

    def add_chassis_contract_attributes(self):
        # Dependencies
        # - only base chassis object required

        self.asset_device_contract_information_handler.set_get_filter(
            "DeviceId eq '%s'" % (self.chassis['Serial'])
        )

        contracts = self.asset_device_contract_information_handler.get_all()
        if len(contracts) == 0:
            self.chassis_info['Chassis']['Contract'] = None

        if len(contracts) > 0:
            self.chassis_info['Chassis']['Contract'] = self.asset_device_contract_information_handler.get_info(
                contracts[0]['Moid']
            )

    def add_chassis_profile_attributes(self):
        # Dependencies
        # - only base chassis object required

        self.chassis_profile_handler.set_get_filter(
            "AssignedChassis/Moid eq '%s'" % (self.chassis['Moid'])
        )

        profiles = self.chassis_profile_handler.get_all()
        if len(profiles) == 0:
            self.chassis_info['Chassis']['Profile'] = None

        if len(profiles) > 0:
            self.chassis_info['Chassis']['Profile'] = self.chassis_profile_handler.get_info(
                profiles[0]['Moid']
            )

    def add_chassis_domain_attributes(self):
        self.chassis_info['Domain'] = {}
        self.chassis_info['Domain']['Name'] = self.chassis['RegisteredDevice']['DeviceHostname'][0]

        self.network_element_summary_handler.set_get_filter(
            "DeviceMoId eq '%s'" % (self.chassis['DeviceMoId'])
        )

        domain_switches = self.network_element_summary_handler.get_all()
        self.chassis_info['Domain']['Switch'] = []
        for domain_switch in domain_switches:
            self.chassis_info['Domain']['Switch'].append(
                self.network_element_summary_handler.get_info(
                    domain_switch['Moid']
                )
            )

        self.chassis_info['Domain']['Switch'] = sorted(
            self.chassis_info['Domain']['Switch'],
            key=lambda k: (k['Name'])
        )

    def add_node_attributes(self):
        # Dependencies
        # - only base chassis object required

        # Limit the scope of isctl get query

        self.compute_blade_handler.set_get_filter(
            "EquipmentChassis/Moid eq '%s'" % (self.chassis['Moid'])
        )

        self.chassis_info['NodeInfo'] = []
        for blade in self.chassis['Blades']:
            blade_info = self.compute_blade_handler.get_info(
                blade['Moid']
            )
            self.chassis_info['NodeInfo'].append(
                blade_info
            )

        # Sort for nice display
        self.chassis_info['NodeInfo'] = sorted(
            self.chassis_info['NodeInfo'],
            key=lambda k: (k['SlotId'])
        )

        # Summaries

        self.chassis_info['Chassis']['NodePowerOn'] = 0
        for blade_info in self.chassis_info['NodeInfo']:
            if blade_info['PowerOn']:
                self.chassis_info['Chassis']['NodePowerOn'] = self.chassis_info['Chassis']['NodePowerOn'] + 1

        self.chassis_info['Chassis']['NodeCount'] = len(
            self.chassis_info['NodeInfo']
        )

        if self.chassis_info['Chassis']['NodeMax'] is None:
            self.chassis_info['Chassis']['NodeSummary'] = '%s/%s' % (
                self.chassis_info['Chassis']['NodePowerOn'],
                self.chassis_info['Chassis']['NodeCount']
            )
        else:
            self.chassis_info['Chassis']['NodeSummary'] = '%s/%s/%s' % (
                self.chassis_info['Chassis']['NodePowerOn'],
                self.chassis_info['Chassis']['NodeCount'],
                self.chassis_info['Chassis']['NodeMax']
            )

    def add_adapter_unit_attributes(self):
        # Dependencies
        # - nodes information required

        blade_ids = []
        for blade in self.chassis['Blades']:
            blade_ids.append('\'%s\'' % (blade['Moid']))
        self.adapter_unit_handler.set_get_filter(
            "Parent/Moid in (%s)" % (', '.join(blade_ids))
        )

        self.chassis_helper['AdapterUnitIds'] = []
        self.chassis_info['AdapterUnitInfo'] = []

        for adapter_unit_item in self.adapter_unit_handler.get_all():
            self.chassis_helper['AdapterUnitIds'].append(
                adapter_unit_item['Moid']
            )

            adapter_unit_info = self.adapter_unit_handler.get_info(
                adapter_unit_item['Moid']
            )
            self.chassis_info['AdapterUnitInfo'].append(
                adapter_unit_info
            )

            for node_info in self.chassis_info['NodeInfo']:
                if adapter_unit_info['ComputeNodeMoid'] == node_info['Moid']:
                    adapter_unit_info['ComputeNodeId'] = node_info['SlotId']
                    adapter_unit_info['ComputeNodePowerOn'] = node_info['PowerOn']

    def add_adapter_ext_eth_interface_attributes(self):
        # Dependencies
        # - must run after adaptor unit collection

        adapter_unit_ids = []
        for adapter_unit_id in self.chassis_helper['AdapterUnitIds']:
            adapter_unit_ids.append('\'%s\'' % (adapter_unit_id))
        self.adapter_ext_eth_interface_handler.set_get_filter(
            "Parent/Moid in (%s)" % (', '.join(adapter_unit_ids))
        )

        self.chassis_info['AdapterExtEthInterfaceInfo'] = []

        for adapter_ext_eth_interface_item in self.adapter_ext_eth_interface_handler.get_all():
            adapter_ext_eth_interface_info = self.adapter_ext_eth_interface_handler.get_info(
                adapter_ext_eth_interface_item['Moid']
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
        # Dependencies
        # - self.chassis (original chassis object)

        # Limit the scope of isctl get query
        self.iocard_handler.set_get_filter(
            "Parent/Moid eq '%s'" % (self.chassis['Moid'])
        )

        self.chassis_helper['IfmIds'] = []
        self.chassis_info['IfmInfo'] = []

        # Get io module info
        for io_module in self.chassis['Ioms']:
            self.chassis_helper['IfmIds'].append(
                io_module['Moid']
            )

            io_module_info = self.iocard_handler.get_info(
                io_module['Moid']
            )
            self.chassis_info['IfmInfo'].append(
                io_module_info
            )

        # Sort for nice display
        self.chassis_info['IfmInfo'] = sorted(
            self.chassis_info['IfmInfo'],
            key=lambda k: (k['ModuleId'])
        )

        # Summaries

        self.chassis_info['Chassis']['IfmOn'] = 0
        for io_module in self.chassis_info['IfmInfo']:
            if io_module['On']:
                self.chassis_info['Chassis']['IfmOn'] = self.chassis_info['Chassis']['IfmOn'] + 1

        self.chassis_info['Chassis']['IfmCount'] = len(
            self.chassis_info['IfmInfo']
        )

        if self.chassis_info['Chassis']['IfmMax'] is None:
            self.chassis_info['Chassis']['IfmSummary'] = '%s/%s' % (
                self.chassis_info['Chassis']['IfmOn'],
                self.chassis_info['Chassis']['IfmCount']
            )
        else:
            self.chassis_info['Chassis']['IfmSummary'] = '%s/%s/%s' % (
                self.chassis_info['Chassis']['IfmOn'],
                self.chassis_info['Chassis']['IfmCount'],
                self.chassis_info['Chassis']['IfmMax']
            )

    def get_io_modules_filter(self):
        io_module_ids = []
        for io_module_id in self.chassis_helper['IfmIds']:
            io_module_ids.append('\'%s\'' % (io_module_id))
        return ', '.join(io_module_ids)

    def add_host_port_attributes(self):
        # Dependencies
        # - must run after base io module attributes

        io_module_ids_filter = self.get_io_modules_filter()
        self.ether_host_port_handler.set_get_filter(
            'EquipmentIoCardBase/Moid in (%s)' % (io_module_ids_filter)
        )

        self.chassis_info['HostPortInfo'] = []
        for host_port in self.ether_host_port_handler.get_all():
            # Base object info
            host_port_info = self.ether_host_port_handler.get_info(
                host_port['Moid']
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

        self.chassis_info['Chassis']['HostPortCount'] = 0
        self.chassis_info['Chassis']['HostPortUp'] = 0

        for io_module_info in self.chassis_info['IfmInfo']:
            self.chassis_info['Chassis']['HostPortCount'] = self.chassis_info['Chassis']['HostPortCount'] + io_module_info['HostPortCount']
            self.chassis_info['Chassis']['HostPortUp'] = self.chassis_info['Chassis']['HostPortUp'] + io_module_info['HostPortUp']

        self.chassis_info['Chassis']['HostPortSummary'] = '%s/%s' % (
            self.chassis_info['Chassis']['HostPortUp'],
            self.chassis_info['Chassis']['HostPortCount']
        )

    def add_network_port_attributes(self):
        # Dependencies
        # - must run after base io module attributes

        io_module_ids_filter = self.get_io_modules_filter()
        self.ether_network_port_handler.set_get_filter(
            'EquipmentIoCardBase/Moid in (%s)' % (io_module_ids_filter)
        )

        self.chassis_helper['PhysicalPortIds'] = []
        self.chassis_info['NetworkPortInfo'] = []

        for network_port in self.ether_network_port_handler.get_all():
            # Base object info
            network_port_info = self.ether_network_port_handler.get_info(
                network_port['Moid']
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

        self.chassis_info['Chassis']['NetworkPortUp'] = 0
        self.chassis_info['Chassis']['NetworkPortCount'] = 0
        self.chassis_info['Chassis']['NetworkPortMax'] = 0

        for io_module_info in self.chassis_info['IfmInfo']:
            if io_module_info['NetworkPortMax'] is not None:
                self.chassis_info['Chassis']['NetworkPortMax'] = self.chassis_info['Chassis']['NetworkPortMax'] + io_module_info['NetworkPortMax']

            self.chassis_info['Chassis']['NetworkPortCount'] = self.chassis_info['Chassis']['NetworkPortCount'] + io_module_info['NetworkPortCount']
            self.chassis_info['Chassis']['NetworkPortUp'] = self.chassis_info['Chassis']['NetworkPortUp'] + io_module_info['NetworkPortUp']

        if self.chassis_info['Chassis']['NetworkPortMax'] == 0:
            self.chassis_info['Chassis']['NetworkPortSummary'] = '%s/%s' % (
                self.chassis_info['Chassis']['NetworkPortUp'],
                self.chassis_info['Chassis']['NetworkPortCount']
            )
        else:
            self.chassis_info['Chassis']['NetworkPortSummary'] = '%s/%s/%s' % (
                self.chassis_info['Chassis']['NetworkPortUp'],
                self.chassis_info['Chassis']['NetworkPortCount'],
                self.chassis_info['Chassis']['NetworkPortMax']
            )

    def get_physical_port_ids_filter(self):
        # Dependencies
        # - must run after network port collection to populate physial port ids

        physical_port_ids = []
        if len(self.chassis_helper['PhysicalPortIds']) == 0:
            return physical_port_ids

        for physical_port_id in self.chassis_helper['PhysicalPortIds']:
            physical_port_ids.append('\'%s\'' % (physical_port_id))

        return ', '.join(physical_port_ids)

    def add_physical_port_attributes(self):
        # Dependencies
        # - must run after network port collection to populate physial port ids

        self.chassis_info['PhysicalPortInfo'] = []

        if len(self.chassis_helper['PhysicalPortIds']) > 0:
            physical_port_ids_filter = self.get_physical_port_ids_filter()
            self.ether_physical_port_handler.set_get_filter(
                'Moid in (%s)' % (physical_port_ids_filter)
            )

            for physical_port in self.ether_physical_port_handler.get_all():
                physical_port_info = self.ether_physical_port_handler.get_info(physical_port['Moid'])
                self.chassis_info['PhysicalPortInfo'].append(
                    physical_port_info
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
        # Dependencies
        # - self.chassis (original chassis object)

        self.chassis_info['FanControlInfo'] = self.fan_control_handler.get_info(
            self.chassis['FanControl']['Moid']
        )

    def add_fan_module_attributes(self):
        # Dependencies
        # - self.chassis (original chassis object)

        # Limit the scope of isctl get query
        self.fan_module_handler.set_get_filter(
            "Parent/Moid eq '%s'" % (self.chassis['Moid'])
        )

        # Get fan modules state
        self.chassis_helper['FanModuleIds'] = []
        self.chassis_info['FanModuleInfo'] = []

        for fan_module in self.chassis['Fanmodules']:
            self.chassis_helper['FanModuleIds'].append(
                fan_module['Moid']
            )

            self.chassis_info['FanModuleInfo'].append(
                self.fan_module_handler.get_fan_info(fan_module['Moid'])
            )

        # Sort for nice display
        self.chassis_info['FanModuleInfo'] = sorted(
            self.chassis_info['FanModuleInfo'],
            key=lambda i: i['ModuleId']
        )

        # Summaries

        self.chassis_info['Chassis']['FanModulesOn'] = 0
        for fan_module in self.chassis_info['FanModuleInfo']:
            if fan_module['On']:
                self.chassis_info['Chassis']['FanModulesOn'] = self.chassis_info['Chassis']['FanModulesOn'] + 1

        self.chassis_info['Chassis']['FanModuleCount'] = len(self.chassis_info['FanModuleInfo'])

        if self.chassis_info['Chassis']['FanModuleMax'] is None:
            self.chassis_info['Chassis']['FanModuleSummary'] = '%s/%s' % (
                self.chassis_info['Chassis']['FanModulesOn'],
                self.chassis_info['Chassis']['FanModuleCount']
            )
        else:
            self.chassis_info['Chassis']['FanModuleSummary'] = '%s/%s/%s' % (
                self.chassis_info['Chassis']['FanModulesOn'],
                self.chassis_info['Chassis']['FanModuleCount'],
                self.chassis_info['Chassis']['FanModuleMax']
            )

    def add_fan_attributes(self):
        # Dependencies
        # - self.chassis (original chassis object)
        # - must run after fan module state collection

        # Limit the scope of isctl get query
        fan_module_ids = []
        for fan_module_id in self.chassis_helper['FanModuleIds']:
            fan_module_ids.append('\'%s\'' % (fan_module_id))

        self.fan_handler.set_get_filter(
            "Parent/Moid in (%s)" % (', '.join(fan_module_ids))
        )

        # Get fan info based on the fans in fan module
        self.chassis_info['FanInfo'] = []
        for fan_module in self.chassis_info['FanModuleInfo']:
            for fan_moid in fan_module['FanMoids']:
                self.chassis_info['FanInfo'].append(
                    self.fan_handler.get_info(fan_moid)
                )

        # Sort for nice display
        self.chassis_info['FanInfo'] = sorted(
            self.chassis_info['FanInfo'],
            key=lambda i: i['ModuleId']
        )

        # Summaries

        self.chassis_info['Chassis']['FanOn'] = 0
        for fan in self.chassis_info['FanInfo']:
            if fan['On']:
                self.chassis_info['Chassis']['FanOn'] = self.chassis_info['Chassis']['FanOn'] + 1

        self.chassis_info['Chassis']['FanCount'] = len(
            self.chassis_info['FanInfo']
        )

        if self.chassis_info['Chassis']['FanMax'] is None:
            self.chassis_info['Chassis']['FanSummary'] = '%s/%s' % (
                self.chassis_info['Chassis']['FanOn'],
                self.chassis_info['Chassis']['FanCount']
            )
        else:
            self.chassis_info['Chassis']['FanSummary'] = '%s/%s/%s' % (
                self.chassis_info['Chassis']['FanOn'],
                self.chassis_info['Chassis']['FanCount'],
                self.chassis_info['Chassis']['FanMax']
            )

    def add_psu_control_attributes(self):
        # Dependencies
        # - self.chassis (original chassis object)

        # Limit the scope of isctl get query
        self.psu_control_handler.set_get_filter(
            "Parent/Moid eq '%s'" % (self.chassis['Moid'])
        )

        self.chassis_info['PsuControlStateInfo'] = None

        items = self.psu_control_handler.get_all()
        if len(items) == 1:
            self.chassis_info['PsuControlStateInfo'] = self.psu_control_handler.get_info(
                items[0]['Moid']
            )

    def add_power_control_attributes(self):
        # Dependencies
        # - self.chassis (original chassis object)

        # Get power control state
        self.chassis_info['PowerControlStateInfo'] = self.power_control_state_handler.get_info(
            self.chassis['PowerControlState']['Moid'],
            cache=False
        )

    def add_psu_attributes(self):
        # Dependencies
        # - self.chassis (original chassis object)

        # Limit the scope of isctl get query
        self.psu_handler.set_get_filter(
            "Parent/Moid eq '%s'" % (self.chassis['Moid'])
        )

        # Get power supply units info
        self.chassis_info['PsuInfo'] = []
        for psu in self.chassis['Psus']:
            self.chassis_info['PsuInfo'].append(
                self.psu_handler.get_psu_info(
                    psu['Moid']
                )
            )

        # Sort psu info for nice display
        self.chassis_info['PsuInfo'] = sorted(
            self.chassis_info['PsuInfo'],
            key=lambda i: i['Dn']
        )

        # Summaries

        self.chassis_info['Chassis']['PsuCount'] = len(
            self.chassis_info['PsuInfo']
        )

        self.chassis_info['Chassis']['PsuOn'] = 0
        for psu_info in self.chassis_info['PsuInfo']:
            if psu_info['On']:
                self.chassis_info['Chassis']['PsuOn'] = self.chassis_info['Chassis']['PsuOn'] + 1

        if self.chassis_info['Chassis']['PsuMax'] is None:
            self.chassis_info['Chassis']['PsuSummary'] = '%s/%s' % (
                self.chassis_info['Chassis']['PsuOn'],
                self.chassis_info['Chassis']['PsuCount']
            )
        else:
            self.chassis_info['Chassis']['PsuSummary'] = '%s/%s/%s' % (
                self.chassis_info['Chassis']['PsuOn'],
                self.chassis_info['Chassis']['PsuCount'],
                self.chassis_info['Chassis']['PsuMax']
            )

    def add_chassis_attributes(self):
        self.add_common_attributes()

        if self.settings['summary']['enabled'] or self.settings['module']['enabled']:
            self.add_io_module_attributes()
            self.add_host_port_attributes()
            self.add_network_port_attributes()

        if self.settings['summary']['enabled'] or self.settings['node']['enabled']:
            self.add_node_attributes()

        if self.settings['summary']['enabled']:
            self.add_chassis_domain_attributes()
            self.add_chassis_alarms_attributes()
            self.add_chassis_advisory_attributes()
            self.add_chassis_contract_attributes()
            self.add_chassis_profile_attributes()
            self.add_psu_control_attributes()

        if self.settings['port']['enabled']:
            if self.settings['port']['type'] is None or self.settings['port']['type'] == 'host':
                if not self.settings['module']['enabled']:
                    self.add_io_module_attributes()
                    self.add_host_port_attributes()
                if not self.settings['node']['enabled']:
                    self.add_node_attributes()
                self.add_adapter_unit_attributes()
                self.add_adapter_ext_eth_interface_attributes()

            if self.settings['port']['type'] is None or self.settings['port']['type'] == 'net':
                if not self.settings['module']['enabled']:
                    self.add_io_module_attributes()
                    self.add_network_port_attributes()
                self.add_physical_port_attributes()

        if self.settings['fan']['enabled']:
            self.add_fan_control_attributes()

        if self.settings['summary']['enabled'] or self.settings['fan']['enabled']:
            self.add_fan_module_attributes()
            self.add_fan_attributes()

        if self.settings['power']['enabled']:
            self.add_power_control_attributes()

        if self.settings['summary']['enabled'] or self.settings['power']['enabled']:
            self.add_psu_control_attributes()
            self.add_psu_attributes()
