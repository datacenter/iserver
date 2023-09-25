from lib import filter_helper
from lib import output_helper


class ChassisOutput():
    def __init__(self, log_id):
        self.my_output = output_helper.OutputHelper(log_id=log_id)

    def print_summary(self, chassiz, title=False):
        if title:
            self.my_output.default(
                'Chassis Summary [#%s]' % (len(chassiz)),
                underline=True,
                before_newline=True
            )

        if len(chassiz) == 0:
            self.my_output.default('None')
            return

        order = [
            'Name',
            'Moid',
            'Model',
            'Serial',
            'PartNumber',
            'HealthSummary',
            'NodeMax',
            'IfmMax',
            'FanModuleMax',
            'FanMax',
            'PsuMax'
        ]

        headers = [
            'Name',
            'Moid',
            'Model',
            'Serial',
            'Part Number',
            'Health',
            'Node Max',
            'Ifm Max',
            'Fan Module Max',
            'Fan Max',
            'Psu Max'
        ]

        self.my_output.my_table(
            chassiz,
            order=order,
            headers=headers,
            table=True
        )

    def print_state(self, chassiz, title=False):
        if title:
            self.my_output.default(
                'Chassis State Summary [#%s]' % (len(chassiz)),
                underline=True,
                before_newline=True
            )

        if len(chassiz) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'Name',
            'NodeSummary',
            'IfmSummary',
            'NetworkPortSummary',
            'HostPortSummary',
            'FanModuleSummary',
            'FanSummary',
            'PsuSummary'
        ]

        headers = [
            'Chassis',
            'Node',
            'IFM',
            'Network Ports',
            'Host Ports',
            'Fan Module',
            'Fan',
            'Psu'
        ]

        self.my_output.my_table(
            chassiz,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_domain(self, chassiz, title=False):
        items = []
        for chassis in chassiz:
            for switch_info in chassis['Domain']['Switch']:
                item = switch_info
                switch_info['DomainName'] = chassis['Domain']['Name']
                switch_info['ChassisName'] = chassis['Name']
                items.append(
                    item
                )

        if title:
            self.my_output.default(
                'UCS Domain Switch [#%s]' % (len(items)),
                underline=True,
                before_newline=True
            )

        if len(items) == 0:
            self.my_output.default('None')
            return

        order = [
            'ChassisName',
            'DomainName',
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
            'Chassis',
            'Domain',
            'Switch',
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
            items,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_health(self, chassiz, title=False):
        if title:
            self.my_output.default(
                'Chassis Health [#%s]' % (len(chassiz)),
                underline=True,
                before_newline=True
            )

        if len(chassiz) == 0:
            self.my_output.default('None')
            return

        order = [
            'Name',
            'Health',
            'AlarmWarning',
            'AlarmCritical',
            'AdvisoryCount'
        ]

        headers = [
            'Chassis',
            'State',
            'Warnings',
            'Critical',
            'Advisories'
        ]

        self.my_output.my_table(
            chassiz,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

        items = []
        for chassis in chassiz:
            for alarm in chassis['Alarms']:
                item = alarm
                item['ChassisName'] = chassis['Name']
                item['DescriptionT'] = filter_helper.get_string_chunks(
                    item['Description'],
                    40,
                    separator=' '
                )
                items.append(
                    item
                )

        if title:
            self.my_output.default(
                'Chassis Alarms [#%s]' % (len(items)),
                underline=True,
                before_newline=True
            )

        if len(items) == 0:
            self.my_output.default('None')
            return

        order = [
            'ChassisName',
            'Severity',
            'CreateTime',
            'Name',
            'DescriptionT'
        ]

        headers = [
            'Chassis',
            'Severity',
            'CreateTime',
            'Name',
            'Description'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                items,
                order,
                ['DescriptionT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_profile(self, chassiz, title=False):
        info = []
        for chassis in chassiz:
            if chassis['Profile'] is not None:
                item = chassis['Profile']
                item['ChassisName'] = chassis['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Profile [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ChassisName',
            'Name',
            'ConfigState',
            'ModTime',
            'TargetPlatform',
            'Policies.Name',
            'Policies.ClassId',
            'Policies.ModTime',
            'Policies.Shared',
            'Policies.InSync'
        ]

        headers = [
            'Chassis',
            'Profile',
            'State',
            'Last Modified',
            'Target Platform',
            'Policy Name',
            'Class Id',
            'Modification Time',
            'Shared',
            'In Sync'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['Policies']
            ),
            order=order,
            headers=headers,
            underline=True,
            table=True,
            allow_order_subkeys=True,
            row_separator=True
        )

    def print_contract(self, chassiz, title=False):
        info = []
        for chassis in chassiz:
            if chassis['Contract'] is None:
                continue
            item = chassis['Contract']
            item['ChassisName'] = chassis['Name']
            info.append(
                item
            )

        if title:
            self.my_output.default(
                'Contract [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ChassisName',
            'ContractStatus',
            'ContractNumber',
            'ServiceStartDate',
            'ServiceEndDate',
            'ContractUpdatedTime',
            'ServiceDescription',
            'ServiceLevel',
            'ServiceSku',
            'PurchaseOrderNumber',
            'SalesOrderNumber'
        ]

        headers = [
            'Chassis',
            'Contract Status',
            'Contract Number',
            'Start Date',
            'End Date',
            'Last Updated',
            'Service Description',
            'Service Level',
            'Service Sku',
            'Purchase Order Number',
            'Sales Order Number'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_node(self, chassiz, title=False):
        items = []
        for chassis in chassiz:
            for alarm in chassis['NodeInfo']:
                item = alarm
                item['ChassisName'] = chassis['Name']
                items.append(
                    item
                )

        if title:
            self.my_output.default(
                'Node [#%s]' % (len(items)),
                underline=True,
                before_newline=True
            )

        if len(items) == 0:
            self.my_output.default('None')
            return

        order = [
            'ChassisName',
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
            'Chassis',
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
            items,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_io_module(self, chassiz, title=False):
        items = []
        for chassis in chassiz:
            for ifm in chassis['IfmInfo']:
                item = ifm
                item['ChassisName'] = chassis['Name']
                items.append(
                    item
                )

        if title:
            self.my_output.default(
                'I/O Module [#%s]' % (len(items)),
                underline=True,
                before_newline=True
            )

        if len(items) == 0:
            self.my_output.default('None')
            return

        order = [
            'ChassisName',
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
            'Chassis',
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

        self.my_output.my_table(
            items,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_network_port(self, chassiz, title=False):
        items = []
        for chassis in chassiz:
            for item in chassis['NetworkPortInfo']:
                item['ChassisName'] = chassis['Name']
                items.append(
                    item
                )

        if title:
            self.my_output.default(
                'Network Port [#%s]' % (len(items)),
                underline=True,
                before_newline=True
            )

        if len(items) == 0:
            self.my_output.default('None')
            return

        order = [
            'ChassisName',
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
            'Chassis',
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
            items,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_host_port(self, chassiz, title=False):
        items = []
        for chassis in chassiz:
            for item in chassis['HostPortInfo']:
                item['ChassisName'] = chassis['Name']
                items.append(
                    item
                )

        if title:
            self.my_output.default(
                'Host Port [#%s]' % (len(items)),
                underline=True,
                before_newline=True
            )

        if len(items) == 0:
            self.my_output.default('None')
            return

        order = [
            'ChassisName',
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
            'Chassis',
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
            items,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_fan_summary(self, chassiz, title=False):
        if title:
            self.my_output.default(
                'Fan Summary [#%s]' % (len(chassiz)),
                underline=True,
                before_newline=True
            )

        if len(chassiz) == 0:
            self.my_output.default('None')
            return

        order = [
            'Name',
            'FanModuleSummary',
            'FanSummary',
            'FanControlInfo.Mode',
            'FanModuleInfo.Name',
            'FanModuleInfo.Presence',
            'FanModuleInfo.OperState',
            'FanModuleInfo.FanCount'
        ]

        headers = [
            'Chassis',
            'Fan Module',
            'Fan',
            'Fan Control Mode',
            'Fan Module',
            'Presence',
            'Operational State',
            'Fans'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                chassiz,
                order,
                ['FanModuleInfo']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_fan(self, chassiz, title=False):
        items = []
        for chassis in chassiz:
            for item in chassis['FanInfo']:
                item['ChassisName'] = chassis['Name']
                items.append(
                    item
                )

        if title:
            self.my_output.default(
                'Fan [#%s]' % (len(items)),
                underline=True,
                before_newline=True
            )

        if len(items) == 0:
            self.my_output.default('None')
            return

        order = [
            'ChassisName',
            'Name',
            'Presence',
            'OperState',
            'Model',
            'Serial',
            'PartNumber'
        ]

        headers = [
            'Chassis',
            'Fan',
            'Presence',
            'Operational State',
            'Model',
            'Serial',
            'Part Number'
        ]

        self.my_output.my_table(
            items,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_fans(self, chassiz, title=False):
        self.print_fan_summary(chassiz, title=title)
        self.print_fan(chassiz, title=title)

    def print_power_control_state_info(self, chassiz, title=False):
        items = []
        for chassis in chassiz:
            item = chassis['PowerControlStateInfo']
            if item is None:
                item = {}
            item['ChassisName'] = chassis['Name']
            items.append(
                item
            )

        if title:
            self.my_output.default(
                'Power Control State [#%s]' % (len(items)),
                underline=True,
                before_newline=True
            )

        if len(items) == 0:
            self.my_output.default('None')
            return

        order = [
            'ChassisName',
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
            'Chassis',
            'Save Mode',
            'Extended Capacity',
            'Dynamic Rebalancing',
            'Allocated Budget',
            'Max Req',
            'Min Req',
            'Max Avail Non-Redundant (N)',
            'Max Avail Grid (N+N)',
            'Max Avail (N+1)',
            'Max Avail (N+2)'
        ]

        self.my_output.my_table(
            items,
            order=order,
            headers=headers,
            table=True
        )

    def print_psu_control_state_info(self, chassiz, title=False):
        items = []
        for chassis in chassiz:
            item = chassis['PsuControlStateInfo']
            if item is None:
                item = {}
            item['ChassisName'] = chassis['Name']
            items.append(
                item
            )

        if title:
            self.my_output.default(
                'PSU Control State [#%s]' % (len(items)),
                underline=True,
                before_newline=True
            )

        if len(items) == 0:
            self.my_output.default('None')
            return

        order = [
            'ChassisName',
            'InputPowerState',
            'OutputPowerState',
            'OperState',
            'Redundancy'
        ]

        headers = [
            'Chassis',
            'Input Power Health',
            'Output Power Health',
            'Redundancy Health',
            'Redundancy Mode'
        ]

        self.my_output.my_table(
            items,
            order=order,
            headers=headers,
            table=True
        )

    def print_psu(self, chassiz, title=False):
        if title:
            self.my_output.default(
                'PSU [#%s]' % (len(chassiz)),
                underline=True,
                before_newline=True
            )

        if len(chassiz) == 0:
            self.my_output.default('None')
            return

        order = [
            'Name',
            'PsuSummary',
            'PsuInfo.Dn',
            'PsuInfo.On',
            'PsuInfo.Voltage',
            'PsuInfo.Model',
            'PsuInfo.Serial'
        ]

        headers = [
            'Chassis',
            'State',
            'PSU',
            'On',
            'Voltage',
            'Model',
            'Serial'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                chassiz,
                order,
                ['PsuInfo']
            ),
            order=order,
            headers=headers,
            underline=True,
            row_separator=True,
            allow_order_subkeys=True,
            table=True
        )

    def print_psus(self, chassiz, title=False):
        self.print_psu(chassiz, title=title)
        self.print_psu_control_state_info(chassiz, title=title)
        self.print_power_control_state_info(chassiz, title=title)
