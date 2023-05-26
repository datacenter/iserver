import json

from lib.intersight.chassis_extra_attributes import ChassisExtraAttributes
from lib.intersight import equipment_chassis
from lib import log_helper
from lib import output_helper


class ChassisInfo(ChassisExtraAttributes):
    """Class for intersight chassis objects
    """
    def __init__(self, iaccount, settings=None, log_id=None):
        self.settings = settings
        if settings is None:
            self.settings = self.get_default_settings()

        ChassisExtraAttributes.__init__(self, iaccount, self.settings)
        self.chassis_handler = equipment_chassis.EquipmentChassis(iaccount, log_id=log_id)
        self.my_output = output_helper.OutputHelper(log_id=log_id)
        self.log = log_helper.Log(log_id=log_id)

        self.chassis = None
        self.chassis_info = {}
        self.chassis_helper = {}

    def get_default_settings(self):
        settings = {}
        settings['summary'] = {}
        settings['summary']['enabled'] = True
        settings['power'] = {}
        settings['power']['enabled'] = False
        settings['fan'] = {}
        settings['fan']['enabled'] = False
        settings['module'] = {}
        settings['module']['enabled'] = False
        settings['port'] = {}
        settings['port']['enabled'] = False
        settings['node'] = {}
        settings['node']['enabled'] = False

        return settings

    def get(self, moid=None, chassis=None, extra_attributes_enabled=True):
        if moid is None and chassis is None:
            return None

        if chassis is not None:
            self.chassis = chassis
            command = 'isctl get %s moid %s' % (
                self.chassis_handler.iobject,
                self.chassis['Moid']
            )
            self.log.api(command, self.chassis)

        if moid is not None:
            self.chassis_handler.set_get_expand('RegisteredDevice')
            self.chassis = self.chassis_handler.get(moid)
            command = 'isctl get %s moid %s' % (
                self.chassis_handler.iobject,
                moid
            )
            self.log.api(command, self.chassis)

        if self.chassis is None:
            return None

        if extra_attributes_enabled:
            self.add_chassis_attributes()

        self.log.debug('chassis_info.get', json.dumps(self.chassis_info, indent=4))
        return self.chassis_info

    def print_chassis_identity(self):
        keys = [
            'Moid',
            'Name',
            'Type',
            'Model',
            'Serial',
            'PartNumber'
        ]

        headers = [
            'Chassis Moid',
            'Name',
            'Type',
            'Model',
            'Serial',
            'Part Number'
        ]

        self.my_output.dictionary(
            self.chassis_info['Chassis'],
            title='Identity',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_chassis_domain(self):
        self.my_output.default('UCS Domain', underline=True)
        self.my_output.default('- Name : %s\n' % self.chassis_info['Domain']['Name'])

        if len(self.chassis_info['Domain']['Switch']) > 0:
            order = [
                'Name',
                'HealthSummary',
                'ConnectionStatus',
                'SwitchId',
                'Model',
                'Serial',
                'OutOfBandIpAddress',
                'NumEtherPortsSummary',
                'Version'
            ]

            headers = [
                'Name',
                'Health',
                'Status',
                'Id',
                'Model',
                'Serial',
                'Management IP',
                'Ports',
                'Version'
            ]

            self.my_output.my_table(
                self.chassis_info['Domain']['Switch'],
                order=order,
                headers=headers,
                underline=True,
                table=True
            )

    def print_chassis_health(self):
        keys = [
            'Health',
            'AlarmWarning',
            'AlarmCritical',
            'AdvisoryCount'
        ]

        headers = [
            'State',
            'Warnings',
            'Critical',
            'Advisories'
        ]

        self.my_output.dictionary(
            self.chassis_info['Chassis'],
            title='Health',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

        if len(self.chassis_info['Chassis']['Alarms']) > 0:
            order = [
                'Severity',
                'CreateTime',
                'Name',
                'Description'
            ]

            headers = [
                'Severity',
                'CreateTime',
                'Name',
                'Description'
            ]

            self.my_output.my_table(
                self.chassis_info['Chassis']['Alarms'],
                order=order,
                headers=headers,
                underline=True,
                table=True
            )

    def print_chassis_profile(self):
        if self.chassis_info['Chassis']['Profile'] is None:
            self.my_output.default('Profile', underline=True)
            self.my_output.default('No chassis profile assigned\n')

        if self.chassis_info['Chassis']['Profile'] is not None:
            keys = [
                'Moid'
            ]

            headers = [
                'Chassis Moid'
            ]

            self.my_output.dictionary(
                self.chassis_info['Chassis'],
                title='Profile',
                underline=True,
                prefix="- ",
                justify=True,
                keys=keys,
                title_keys=headers
            )

    def print_chassis_contract(self):
        if self.chassis_info['Chassis']['Contract'] is None:
            self.my_output.default('Contract', underline=True)
            self.my_output.default('No contract found\n')

        if self.chassis_info['Chassis']['Contract'] is not None:
            keys = [
                'ContractStatus',
                'ContractNumber',
                'ServiceStartDate',
                'ServiceEndDate',
                'ContractUpdatedTime',
                'ServiceLevel',
                'ServiceSku'
            ]

            headers = [
                'Status',
                'Number',
                'Start Date',
                'End Date',
                'Last Updated',
                'Service Level',
                'Type'
            ]

            self.my_output.dictionary(
                self.chassis_info['Chassis']['Contract'],
                title='Contract',
                underline=True,
                prefix="- ",
                justify=True,
                keys=keys,
                title_keys=headers
            )

    def print_chassis_inventory(self):
        keys = [
            'NodeSummary',
            'IfmSummary',
            'NetworkPortSummary',
            'HostPortSummary',
            'FanModuleSummary',
            'FanSummary',
            'PsuSummary'
        ]

        headers = [
            'Node',
            'IFM',
            'Network Ports',
            'Host Ports',
            'Fan Module',
            'Fan',
            'Psu'
        ]

        self.my_output.dictionary(
            self.chassis_info['Chassis'],
            title='Inventory',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_summary(self):
        if self.settings['summary']['enabled']:
            self.print_chassis_identity()
            self.print_chassis_domain()
            self.print_psu_control_state_info()
            self.print_chassis_health()
            self.print_chassis_profile()
            self.print_chassis_contract()
            self.print_chassis_inventory()

    def print_node(self):
        if self.settings['node']['enabled']:
            order = [
                'SlotId',
                'Name',
                'Health',
                'OperPowerState',
                'Model',
                'Serial',
                'CpuSummary',
                'TotalMemoryUnit'
            ]

            headers = [
                'Slot',
                'Name',
                'Health',
                'Power',
                'Model',
                'Serial',
                'CPU',
                'Memory'
            ]

            self.my_output.my_table(
                self.chassis_info['NodeInfo'],
                order=order,
                headers=headers,
                underline=True,
                table=True
            )

    def print_io_module_info(self, io_module_info):
        keys = [
            'Name',
            'ConnectionPath',
            'On',
            'OperState',
            'Model',
            'Serial',
            'PartNumber',
            'Version',
            'HostPortSummary',
            'NetworkPortSummary',
            'ManagementCidr',
            'ManagementGateway',
            'ManagementVlan'
        ]

        headers = [
            'I/O Module',
            'Path',
            'Presence',
            'OperState',
            'Model',
            'Serial',
            'P/N',
            'Version',
            'Host Ports',
            'Network Ports',
            'Management IP',
            'Gateway',
            'VLAN'
        ]

        self.my_output.dictionary(
            io_module_info,
            title='I/O Module State',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_io_modules_info(self, io_modules_info):
        order = [
            'Name',
            'ConnectionPath',
            'On',
            'OperState',
            'Model',
            'Serial',
            'PartNumber',
            'Version',
            'HostPortSummary',
            'NetworkPortSummary'
        ]

        headers = [
            'I/O Module',
            'Path',
            'Presence',
            'OperState',
            'Model',
            'Serial',
            'P/N',
            'Version',
            'Host Ports',
            'Network Ports'
        ]

        self.my_output.my_table(
            io_modules_info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_io_modules_management(self, io_modules_info):
        order = [
            'Name',
            'ManagementCidr',
            'ManagementGateway',
            'ManagementVlan'
        ]

        headers = [
            'I/O Module',
            'Management IP',
            'Gateway',
            'VLAN'
        ]

        self.my_output.my_table(
            io_modules_info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def filter_io_modules(self):
        io_modules = []
        for io_module_info in self.chassis_info['IfmInfo']:
            if self.settings['module']['path'] is None and self.settings['module']['id'] is None:
                io_modules.append(io_module_info)
                continue

            if self.settings['module']['path'] is not None:
                if self.settings['module']['path'].lower() == io_module_info['ConnectionPath'].lower():
                    io_modules.append(io_module_info)
                    continue

            if self.settings['module']['id'] is not None:
                if self.settings['module']['id'] == io_module_info['ModuleId']:
                    io_modules.append(io_module_info)
                    continue

        return io_modules

    def print_io_modules(self):
        if self.settings['module']['enabled']:
            filtered_io_modules = self.filter_io_modules()
            if len(filtered_io_modules) == 1:
                self.print_io_module_info(
                    filtered_io_modules[0]
                )

            if len(filtered_io_modules) > 1:
                self.print_io_modules_info(
                    filtered_io_modules
                )
                self.print_io_modules_management(
                    filtered_io_modules
                )

    def print_network_port(self, network_port_info):
        order = [
            'IfmName',
            'Name',
            'Speed',
            'PeerSwitchId',
            'PeerPortName',
            'PeerPortChannelId',
            'PeerPortTransceiverType',
            'PeerOperSpeed'
        ]

        headers = [
            'I/O Module',
            'Network Port',
            'Speed',
            'Switch ID',
            'Switch Port',
            'Switch Port Channel',
            'Switch Transceiver',
            'Switch Port Speed'
        ]

        self.my_output.my_table(
            network_port_info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_host_port(self, host_port_info):
        order = [
            'IfmName',
            'SwitchId',
            'Name',
            'Mode',
            'OperSpeed',
            'OperState',
            'OperStateQual',
            'PortChannelId',
            'PeerInfo'
        ]

        headers = [
            'I/O Module',
            'Path',
            'Host Port',
            'Mode',
            'Speed',
            'State',
            'State Qual',
            'Port Channel',
            'Peer Info'
        ]

        self.my_output.my_table(
            host_port_info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def filter_host_ports(self):
        filtered_host_ports = []
        for host_port_info in self.chassis_info['HostPortInfo']:
            if self.settings['port']['state'] is not None:
                if self.settings['port']['state'] == 'up' and not host_port_info['Up']:
                    continue
                if self.settings['port']['state'] == 'down' and host_port_info['Up']:
                    continue

            if self.settings['port']['module'] is not None:
                if self.settings['port']['module'] == 'a' and host_port_info['SwitchId'].lower() != 'a':
                    continue

                if self.settings['port']['module'] == 'b' and host_port_info['SwitchId'].lower() != 'b':
                    continue

                if self.settings['port']['module'] == '1' and host_port_info['IfmId'] != 1:
                    continue

                if self.settings['port']['module'] == '2' and host_port_info['IfmId'] != 2:
                    continue

            if self.settings['port']['node'] is not None:
                if self.settings['port']['node'] < 1:
                    if host_port_info['PeerInfo'] == '':
                        continue

                if self.settings['port']['node'] > 0:
                    if host_port_info['PeerInfo'] == '':
                        continue
                    if self.settings['port']['node'] != host_port_info['PeerNodeId']:
                        continue

            filtered_host_ports.append(host_port_info)

        return filtered_host_ports

    def print_ports(self):
        if self.settings['port']['enabled']:
            self.log.debug(
                'chassis_info.print_ports',
                json.dumps(self.settings['port'], indent=4)
            )

            if self.settings['port']['type'] is None or self.settings['port']['type'] == 'host':
                filtered_host_ports = self.filter_host_ports()
                if filtered_host_ports is not None:
                    if len(filtered_host_ports) == 0:
                        self.my_output.default('No host ports matching selection criteria')
                    if len(filtered_host_ports) > 0:
                        self.print_host_port(
                            filtered_host_ports
                        )

            if self.settings['port']['type'] is None or self.settings['port']['type'] == 'net':
                self.print_network_port(self.chassis_info['NetworkPortInfo'])

    def print_fan_summary(self):
        keys = [
            'FanModuleSummary',
            'FanSummary'
        ]

        headers = [
            'Fan Module',
            'Fan'
        ]

        self.my_output.dictionary(
            self.chassis_info['Chassis'],
            title='Fan State Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_fan_control_state_info(self):
        keys = [
            'Mode'
        ]

        headers = [
            'Mode'
        ]

        self.my_output.dictionary(
            self.chassis_info['FanControlInfo'],
            title='Fan Control Configuration',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_fan_module(self):
        order = [
            'Name',
            'ModuleId',
            'Presence',
            'OperState',
            'FanCount'
        ]

        headers = [
            'Fan Module',
            'Module Id',
            'Presence',
            'Operational State',
            'Fans'
        ]

        self.my_output.my_table(
            self.chassis_info['FanModuleInfo'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_fan(self):
        order = [
            'Name',
            'ModuleId',
            'FanId',
            'Presence',
            'OperState',
            'Model',
            'Serial',
            'PartNumber'
        ]

        headers = [
            'Fan',
            'Module Id',
            'Fan Id',
            'Presence',
            'Operational State',
            'Model',
            'Serial',
            'Part Number'
        ]

        self.my_output.my_table(
            self.chassis_info['FanInfo'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_fans(self):
        if self.settings['fan']['enabled']:
            self.print_fan_summary()
            self.print_fan_control_state_info()
            self.print_fan_module()
            self.print_fan()

    def print_psu_summary(self):
        keys = [
            'PsuSummary'
        ]

        headers = [
            'Psu'
        ]

        self.my_output.dictionary(
            self.chassis_info['Chassis'],
            title='Psu State Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_power_control_state_info(self):
        keys = [
            'PowerSaveMode',
            'ExtendedPowerCapacity',
            'PowerRebalancing',
            'AllocatedBudget',
            'MaxRequiredPowerUnit',
            'MinRequiredPowerUnit',
            'NonRedundantMaxPowerUnit',
            'GridMaxPowerUnit',
            'N1MaxPowerUnit',
            'N2MaxPowerUnit'
        ]

        headers = [
            'Power Save Mode',
            'Extended Power Capacity',
            'Dynamic Power Rebalancing',
            'Allocated Budget',
            'Maximum Required Power',
            'Minimum Required Power',
            'Maximum Available Non-Redundant Power (N)',
            'Maximum Available Grid Power (N+N)',
            'Maximum Available N1 Power (N+1)',
            'Maximum Available N2 Power (N+2)'
        ]

        self.my_output.dictionary(
            self.chassis_info['PowerControlStateInfo'],
            title='Power Control Configuration',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_psu_control_state_info(self):
        keys = [
            'InputPowerState',
            'OutputPowerState',
            'OperState',
            'Redundancy'
        ]

        headers = [
            'Input Power Health',
            'Output Power Health',
            'Redundancy Health',
            'Redundancy Mode'
        ]

        self.my_output.dictionary(
            self.chassis_info['PsuControlStateInfo'],
            title='Psu Control State',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_psu(self):
        order = [
            'Dn',
            'On',
            'Voltage',
            'Model',
            'Serial'
        ]

        headers = [
            'Chassis PSU',
            'On',
            'Voltage',
            'Model',
            'Serial'
        ]

        self.my_output.my_table(
            self.chassis_info['PsuInfo'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_power(self):
        if self.settings['power']['enabled']:
            self.print_power_control_state_info()
            self.print_psu_control_state_info()
            self.print_psu_summary()
            self.print_psu()

    def print(self):
        self.print_summary()
        self.print_node()
        self.print_io_modules()
        self.print_ports()
        self.print_fans()
        self.print_power()
