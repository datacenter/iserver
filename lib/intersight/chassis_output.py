from lib import filter_helper
from lib import output_helper


class ChassisOutput():
    def __init__(self, log_id):
        self.my_output = output_helper.OutputHelper(log_id=log_id)

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
            'Health',
            'OperStateTick',
            'ProfileInfo.Name',
            'Model',
            'Serial',
            'ConnectionPath',
            'ConnectionStatus',
            'NodeCount',
            'IoCount',
            'ExpanderModuleCount',
            'FanModuleCount',
            'PsuCount'
        ]

        headers = [
            'Chassis',
            'Health',
            'State',
            'Profile',
            'Model',
            'Serial',
            'ConnPath',
            'ConnStatus',
            'Node',
            'I/O',
            'Expander',
            'FanModule',
            'PSU'
        ]

        self.my_output.my_table(
            chassiz,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_advisory(self, chassiz, title=False):
        info = []
        for chassis in chassiz:
            if 'AdvisorySummary' in chassis:
                item = chassis['AdvisorySummary']
                item['ChassisName'] = chassis['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Advisory Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ChassisName',
            'High',
            'Info'
        ]

        headers = [
            'Chassis',
            'High',
            'Info'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

        advisories = {}
        for chassis in chassiz:
            for chassis_advisory in chassis['AdvisoryInfo']:
                if chassis_advisory['Name'] not in advisories:
                    advisories[chassis_advisory['Name']] = chassis_advisory
                    advisories[chassis_advisory['Name']]['Chassis'] = []

                advisories[chassis_advisory['Name']]['Chassis'].append(
                    chassis['Name']
                )

        info = []
        for advisory_name in advisories:
            item = advisories[advisory_name]
            item['NameT'] = filter_helper.get_string_chunks(
                item['Name'],
                40,
                separator=' '
            )
            item['DescriptionT'] = filter_helper.get_string_chunks(
                item['Description'].replace('\n', ''),
                40,
                separator=' '
            )
            item['chassis'] = sorted(
                item['Chassis'],
                key=lambda i: i.lower()
            )
            info.append(
                item
            )

        if len(info) > 0:
            if title:
                self.my_output.default(
                    'Advisory [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )

            order = [
                'Chassis',
                'Severity',
                'BaseScore',
                'NameT',
                'DescriptionT',
                'CveIds',
                'DatePublished',
                'DateUpdated'
            ]

            headers = [
                'Chassis',
                'Severity',
                'Score',
                'Name',
                'Description',
                'CveIds',
                'DatePublished',
                'DateUpdated'
            ]

            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    ['Chassis', 'DescriptionT', 'NameT', 'CveIds']
                ),
                order=order,
                headers=headers,
                remove_empty_columns=True,
                allow_order_subkeys=True,
                row_separator=True,
                underline=True,
                table=True
            )

        if len(info) > 0:
            if title:
                self.my_output.default(
                    'Advisory Url [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )

            order = [
                'Chassis',
                'NameT',
                'Urls'
            ]

            headers = [
                'Chassis',
                'Name',
                'Urls'
            ]

            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    ['Chassis', 'NameT', 'Urls']
                ),
                order=order,
                headers=headers,
                remove_empty_columns=True,
                allow_order_subkeys=True,
                row_separator=True,
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

    def print_chassis_alarm(self, chassiz, title=False):
        items = []
        for chassis in chassiz:
            for alarm in chassis['AlarmInfo']:
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
                'Alarm [#%s]' % (len(items)),
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

    def print_contract(self, chassiz, title=False):
        info = []
        for chassis in chassiz:
            if chassis['ContractInfo'] is None:
                continue
            item = chassis['ContractInfo']
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

        for item in info:
            if item['ServiceStartDate'] == '0001-01-01T00:00:00Z':
                item['ServiceStartDate'] = '--'

            if item['ServiceEndDate'] == '0001-01-01T00:00:00Z':
                item['ServiceEndDate'] = '--'

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
            'Status',
            'Number',
            'Start Date',
            'End Date',
            'Last Updated',
            'Service Description',
            'Service Level',
            'Service Sku',
            'Purchase Order',
            'Sales Order'
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
            'Presence',
            'OperTick',
            'Model',
            'Serial',
            'PartNumber',
            'Version',
            'Vendor',
            'HostPortsCount',
            'NetworkPortsCount',
            'FansCount'
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
            'Vendor',
            'Host Ports',
            'Network Ports',
            'Fans'
        ]

        self.my_output.my_table(
            items,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_expander_module(self, chassiz, title=False):
        items = []
        for chassis in chassiz:
            for exp in chassis['ExpanderModuleInfo']:
                item = exp
                item['ChassisName'] = chassis['Name']
                items.append(
                    item
                )

        if title:
            self.my_output.default(
                'Expander Module [#%s]' % (len(items)),
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
            'OperTick',
            'Model',
            'Serial',
            'PartNumber',
            'Vendor',
            'FansCount'
        ]

        headers = [
            'Chassis',
            'I/O Module',
            'Presence',
            'OperState',
            'Model',
            'Serial',
            'P/N',
            'Vendor',
            'Fans'
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
            'PortChannelId'
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
            'Port Channel'
        ]

        self.my_output.my_table(
            items,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_fan_control(self, chassiz, title=False):
        if title:
            self.my_output.default(
                'Fan Control [#%s]' % (len(chassiz)),
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
            'FanControlInfo.Mode'
        ]

        headers = [
            'Chassis',
            'Fan Module',
            'Fan',
            'Fan Control Mode'
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
                item['Control'] = None
                if 'FanControlInfo' in chassis and chassis['FanControlInfo'] is not None:
                    item['Control'] = chassis['FanControlInfo']['Mode']
                if item['Control'] is None or len(item['Control']) == 0:
                    item['Control'] = '--'
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
            'Control',
            'Presence',
            'OperState',
            'Model',
            'Serial',
            'PartNumber'
        ]

        headers = [
            'Chassis',
            'Fan',
            'Control',
            'Presence',
            'State',
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
                'Power Control [#%s]' % (len(items)),
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

        for item in items:
            for key in order:
                if key not in item or item[key] is None or len(item[key]) == 0:
                    item[key] = '--'

        headers = [
            'Chassis',
            'Save Mode',
            'Ext Capacity',
            'Dyn Rebalancing',
            'Alloc Budget',
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
                'PSU Control [#%s]' % (len(items)),
                underline=True,
                before_newline=True
            )

        if len(items) == 0:
            self.my_output.default('None')
            return

        order = [
            'ChassisName',
            'InputPowerStateTick',
            'OutputPowerStateTick',
            'OperStateTick',
            'Redundancy'
        ]

        for item in items:
            for key in order:
                if key not in item or item[key] is None or len(item[key]) == 0:
                    item[key] = '--'

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
        items = []
        for chassis in chassiz:
            for item in chassis['PsuInfo']:
                item['ChassisName'] = chassis['Name']
                items.append(
                    item
                )

        if title:
            self.my_output.default(
                'PSU [#%s]' % (len(items)),
                underline=True,
                before_newline=True
            )

        if len(chassiz) == 0:
            self.my_output.default('None')
            return

        order = [
            'ChassisName',
            'Name',
            'StateTick',
            'Voltage',
            'Model',
            'Serial'
        ]

        headers = [
            'Chassis',
            'PSU',
            'State',
            'Voltage',
            'Model',
            'Serial'
        ]

        self.my_output.my_table(
            items,
            order=order,
            headers=headers,
            underline=True,
            row_separator=True,
            allow_order_subkeys=True,
            table=True
        )

    def print_inventory(self, chassiz_info, title=False):
        for chassis_info in chassiz_info:
            if title:
                self.my_output.default(
                    'Chassis Inventory: %s' % (chassis_info['Name']),
                    underline=True,
                    before_newline=True
                )

            order = [
                'Type',
                'Name',
                'Model',
                'Vendor',
                'Serial',
                'Pid'
            ]

            headers = [
                'Type',
                'Name',
                'Model',
                'Vendor',
                'Serial',
                'Pid'
            ]

            self.my_output.my_table(
                chassis_info['Inventory'],
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )
