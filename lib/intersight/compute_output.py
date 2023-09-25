from lib import filter_helper
from lib import output_helper


class ComputeOutput():
    def __init__(self, log_id=None):
        self.my_output = output_helper.OutputHelper(log_id=log_id)

    def print_summary_table(self, servers, legend_on=False, title=False):
        if title:
            self.my_output.default(
                'Server Summary [#%s]' % (len(servers)),
                underline=True,
                before_newline=True
            )

        if len(servers) == 0:
            self.my_output.default('None')
            return

        order = []
        headers = []

        if servers[0]['StateEnabled']:
            order = order + [
                'FlagState',
                'FlagManagement',
                'FlagWorkflow'
            ]

            headers = headers + [
                'SF',
                'MF',
                'WF (%sd)' % (servers[0]['Workflow']['Days'])
            ]

            for server in servers:
                if len(server['FlagWorkflow']) == 0:
                    server['FlagWorkflow'] = '--'

        order = order + [
            'Name',
            'Moid',
            'TypeModel',
            'Serial',
            'ManagementIp',
            'Cpu',
            'TotalMemoryUnit'
        ]

        headers = headers + [
            'Name',
            'Moid',
            'Model',
            'Serial',
            'IP',
            'CPU',
            'Memory'
        ]

        self.my_output.my_table(
            servers,
            order=order,
            headers=headers,
            table=True
        )

        if legend_on:
            self.print_flags_legend()

    def print_flags_legend(self):
        legend = {}
        legend['power'] = '(P+) on (P-) off'
        legend['health'] = '(H)ealthy (W)arning (C)ritical'
        legend['locator'] = '(L)ocator on'

        self.my_output.dictionary(
            legend,
            title='State Flags (SF)',
            underline=False,
            prefix="- ",
            justify=True,
            keys=[
                'power',
                'health',
                'locator'
            ],
            title_keys=[
                'Power',
                'Health',
                'Locator'
            ]
        )

        legend = {}
        legend['connected'] = '(C) connected (c) disconnected'
        legend['ucsm'] = '(U)csm ready (u)csm capable'
        legend['redfish'] = '(R)edfish ready (r)edfish capable'
        legend['imc'] = '(I)mc ready (i)imc capable'

        self.my_output.dictionary(
            legend,
            title='Management Flags (MF)',
            underline=False,
            prefix="- ",
            justify=True,
            keys=[
                'connected',
                'ucsm',
                'redfish',
                'imc'
            ],
            title_keys=[
                'Intersight API',
                'UCSM API',
                'Redfish API',
                'IMC API'
            ]
        )

        legend = {}
        legend['running'] = '(R)'
        legend['last'] = '(F)'
        legend['some'] = '(f)'

        self.my_output.dictionary(
            legend,
            title='Workflow Flags (SF)',
            underline=False,
            prefix="- ",
            justify=True,
            keys=[
                'running',
                'last',
                'some'
            ],
            title_keys=[
                'Running',
                'Last Failed',
                'Failed'
            ]
        )

    def print_summary_dictionary(self, server):
        self.my_output.dictionary(
            server,
            title='Identity',
            underline=False,
            prefix="- ",
            justify=True,
            keys=[
                'Moid',
                'Name',
                'Type',
                'Model',
                'Serial',
                'ManagementIp'
            ],
            title_keys=[
                'Server ID',
                'Name',
                'Type',
                'Model',
                'Serial',
                'IP'
            ]
        )

        if server['Redfish']['Capable']:
            self.my_output.dictionary(
                server['Redfish'],
                title='Redfish',
                underline=False,
                prefix="- ",
                justify=True,
                keys=[
                    'Capable',
                    'Enabled'
                ],
                title_keys=[
                    'Capable',
                    'Enabled'
                ]
            )

        self.my_output.dictionary(
            server,
            title='State',
            underline=False,
            prefix="- ",
            justify=True,
            keys=[
                'OperPowerState',
                'LocatorLedOn',
                'Health',
                'ManagementMode',
                'Connected',
                'FirmwareVersion',
                'PsuSummary',
                'FanSummary'
            ],
            title_keys=[
                'Power',
                'Locator',
                'Health',
                'Mode',
                'Connected',
                'Firmware',
                'PSU',
                'Fan'
            ]
        )

        self.my_output.dictionary(
            server,
            title='CPU and Memory',
            underline=False,
            prefix="- ",
            justify=True,
            keys=[
                'NumCpus',
                'NumThreads',
                'NumCpuCores',
                'NumCpuCoresEnabled',
                'TotalMemoryUnit'
            ],
            title_keys=[
                'CPU Sockets',
                'Threads',
                'Cores',
                'Enabled Cores',
                'Memory'
            ]
        )

        keys = [
            'StorageControllersCount',
            'PhysicalDiskCount',
            'PhysicalDiskCapacityUnit',
            'VirtualDiskCount'
        ]

        match = False
        for key in keys:
            if key in server:
                match = True
                break

        if match:
            self.my_output.dictionary(
                server,
                title='Storage',
                underline=False,
                prefix="- ",
                justify=True,
                keys=keys,
                title_keys=[
                    'Controllers',
                    'Disks count',
                    'Disks capacity',
                    'Virtual Disks'
                ]
            )

    def print_advisory(self, servers, title=False):
        info = []
        for server in servers:
            item = server['AdvisorySummary']
            item['ServerName'] = server['Name']
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
            'ServerName',
            'High',
            'Info'
        ]

        headers = [
            'Server',
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

        info = []
        for server in servers:
            for item in server['AdvisoryInfo']:
                item['ServerName'] = server['Name']
                item['NameT'] = filter_helper.get_string_chunks(
                    item['Name'],
                    40,
                    separator=' '
                )
                item['DescriptionT'] = filter_helper.get_string_chunks(
                    item['Description'],
                    40,
                    separator=' '
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
                'ServerName',
                'Severity',
                'BaseScore',
                'NameT',
                'DescriptionT',
                'CveIds',
                'DatePublished',
                'DateUpdated'
            ]

            headers = [
                'Server',
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
                    ['DescriptionT', 'NameT', 'CveIds']
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
                'ServerName',
                'NameT',
                'Urls'
            ]

            headers = [
                'Server',
                'Name',
                'Urls'
            ]

            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    ['NameT', 'Urls']
                ),
                order=order,
                headers=headers,
                remove_empty_columns=True,
                allow_order_subkeys=True,
                row_separator=True,
                underline=True,
                table=True
            )

        # for advisory in server['AdvisoryInfo']:
        #     keys = [
        #         'Severity',
        #         'BaseScore',
        #         'Name',
        #         'Description',
        #         'CveIds',
        #         'DatePublished',
        #         'DateUpdated',
        #         'Urls',
        #         'Recommendation',
        #         'Workaround'
        #     ]

        #     headers = [
        #         'Severity',
        #         'Base Score',
        #         'Name',
        #         'Description',
        #         'Cve Ids',
        #         'Date Published',
        #         'Date Updated',
        #         'Details',
        #         'Recommendation',
        #         'Workaround'
        #     ]

        #     if len(advisory['Workaround']) == 0:
        #         keys.remove('Workaround')
        #         headers.remove('Workaround')

        #     self.my_output.dictionary(
        #         advisory,
        #         title='Advisory %s' % (advisory['AdvisoryId']),
        #         underline=True,
        #         prefix="- ",
        #         justify=True,
        #         keys=keys,
        #         title_keys=headers
        #     )

    def print_alarm(self, servers, title=False):
        info = []
        for server in servers:
            item = server['AlarmSummary']
            item['ServerName'] = server['Name']
            info.append(
                item
            )

        if title:
            self.my_output.default(
                'Alarm Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Critical',
            'Warning',
            'Info'
        ]

        headers = [
            'Server',
            'Critical',
            'Warning',
            'Info'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

        info = []
        for server in servers:
            for item in server['AlarmInfo']:
                item['ServerName'] = server['Name']
                item['DescriptionT'] = filter_helper.get_string_chunks(
                    item['Description'],
                    40,
                    separator=' '
                )
                info.append(
                    item
                )

        if len(info) > 0:
            if title:
                self.my_output.default(
                    'Alarm [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )

            order = [
                'ServerName',
                'Severity',
                'DescriptionT',
                'CreateTime',
                'AffectedType',
                'AffectedName'
            ]

            headers = [
                'Server',
                'Severity',
                'Description',
                'Create Time',
                'Affected Type',
                'Affected Name'
            ]

            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    ['DescriptionT']
                ),
                order=order,
                headers=headers,
                remove_empty_columns=True,
                allow_order_subkeys=True,
                row_separator=True,
                underline=True,
                table=True
            )

    def print_board(self, servers, title=False):
        info = []
        for server in servers:
            item = server['BoardInfo']
            item['ServerName'] = server['Name']
            info.append(
                item
            )

        if title:
            self.my_output.default(
                'Motherboard Hardware Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'BoardId',
            'Vendor',
            'ProcessorsCount',
            'MemoryArraysCount',
            'PciSwitchCount',
            'PciCoprocessorCardsCount',
            'GraphicsCardsCount',
            'StorageControllersCount',
            'StorageFlexFlashControllersCount',
            'StorageFlexUtilControllersCount',
            'SecurityUnitsCount',
            'EquipmentTpmsCount'
        ]

        headers = [
            'Server',
            'Board Id',
            'Vendor',
            'CPU',
            'MemArr',
            'PCI Switch',
            'PCI Cooprocessor',
            'Graphics',
            'Storage Ctrl',
            'FlexFlash Ctrl',
            'FlexUtil Ctrl',
            'Sec',
            'TPM'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_boot(self, servers, title=False):
        info = []
        for server in servers:
            item = server['BootInfo']
            item['ServerName'] = server['Name']
            info.append(
                item
            )

        if title:
            self.my_output.default(
                'Boot [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'ConfiguredBootMode',
            'ActualBootMode',
            'SecureBoot',
            'Order.Order',
            'Order.Name',
            'Order.Type',
            'Order.State'
        ]

        headers = [
            'Server',
            'Configured Boot Mode',
            'Actual Boot Mode',
            'Secure Boot',
            'Order',
            'Name',
            'Type',
            'State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['Order']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_chassis(self, server):
        if 'ChassisInfo' not in server:
            return

        keys = [
            'Name',
            'Model',
            'Serial',
            'Blades',
            'Health'
        ]

        headers = [
            'Name',
            'Model',
            'Serial',
            'Blades',
            'Health'
        ]

        self.my_output.dictionary(
            server['ChassisInfo'],
            title='Chassis',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_connector(self, servers, title=False):
        info = []
        for server in servers:
            item = server['ConnectorInfo']
            item['ServerName'] = server['Name']
            info.append(
                item
            )

        if title:
            self.my_output.default(
                'Connector [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'ConnectionStatus',
            'ConnectorVersion',
            'ClaimedByUserName',
            'ClaimedTime',
            'ConnectionStatusLastChangeTime',
            'PlatformType',
            'DeviceExternalIpAddress'
        ]

        headers = [
            'Server',
            'Connection Status',
            'Connector Version',
            'Claimed By',
            'Claimed Time',
            'Connection Status Last Update',
            'Platform Type',
            'Device External IP Address'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_contract(self, servers, title=False):
        info = []
        for server in servers:
            item = server['ContractInfo']
            item['ServerName'] = server['Name']
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
            'ServerName',
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
            'Server',
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

    def print_cpu(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['CpuInfo']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'CPU [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'StateTick',
            'ProcessorId',
            'SocketDesignation',
            'Vendor',
            'Architecture',
            'Model',
            'NumCores',
            'NumCoresEnabled',
            'NumThreads',
            'Speed',
            'Stepping',
            'Presence',
            'OperState',
            'Thermal'
        ]

        headers = [
            'Server',
            'State',
            'CPU Id',
            'Socket',
            'Vendor',
            'Arch',
            'Model',
            'Cores',
            'Enabled',
            'Threads',
            'Speed [GHz]',
            'Stepping',
            'Presence',
            'OperState',
            'Thermal'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_fan(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['FanInfo']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Fan [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'StateTick',
            'ModuleId',
            'OperState',
            'Presence',
            'Dn'
        ]

        headers = [
            'Server',
            'State',
            'Fan Module Id',
            'OperState',
            'Presence',
            'Dn'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_firmware(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['FirmwarewComponents']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Firmware [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Name',
            'Component',
            'Type',
            'PackageVersion',
            'Version',
            'Dn'
        ]

        headers = [
            'Server',
            'Name',
            'Component',
            'Type',
            'PackageVersion',
            'Version',
            'Dn'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_gpu(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['GpuInfo']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'GPU [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Model',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'FirmwareVersion',
            'Dn'
        ]

        headers = [
            'Server',
            'GPU Device Model',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'Firmware',
            'Dn'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_hcl_summary(self, servers, title=False):
        info = []
        for server in servers:
            item = server['HclInfo']
            item['ServerName'] = server['Name']
            info.append(
                item
            )

        if title:
            self.my_output.default(
                'HCL Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Status'
        ]

        headers = [
            'Server',
            'Overall'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_hcl_hardware(self, servers, title=False):
        info = []
        for server in servers:
            item = server['HclInfo']
            item['ServerName'] = server['Name']
            info.append(
                item
            )

        if title:
            self.my_output.default(
                'HCL Server Hardware Compliance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'HardwareStatus',
            'HclModel',
            'HclProcessor',
            'HclFirmwareVersion'
        ]

        headers = [
            'Server',
            'Status',
            'Model',
            'CPU',
            'Firmware'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_hcl_software(self, servers, title=False):
        info = []
        for server in servers:
            item = server['HclInfo']
            item['ServerName'] = server['Name']
            info.append(
                item
            )

        if title:
            self.my_output.default(
                'HCL Server Software Compliance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'SoftwareStatus',
            'Reason',
            'HclOsVendor',
            'HclOsVersion'
        ]

        headers = [
            'Server',
            'Status',
            'Reason',
            'OS Vendor',
            'OS Version'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_hcl_component(self, servers, title=False):
        info = []
        for server in servers:
            item = server['HclInfo']
            item['ServerName'] = server['Name']
            info.append(
                item
            )

        if title:
            self.my_output.default(
                'HCL Server Adapter Compliance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'ComponentStatus',
            'Details.Status',
            'Details.HardwareStatus',
            'Details.SoftwareStatus',
            'Details.Reason',
            'Details.HclModel',
            'Details.HclCimcVersion',
            'Details.HclDriverName',
            'Details.HclDriverVersion',
            'Details.HclFirmwareVersion'
        ]

        headers = [
            'Server',
            'Status',
            'Component',
            'Hardware',
            'Software',
            'Reason',
            'Model',
            'Cimc Version',
            'Driver Name',
            'Driver Version',
            'Firmware Version'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['Details']
            ),
            order=order,
            headers=headers,
            underline=True,
            table=True,
            allow_order_subkeys=True,
            row_separator=True
        )

        # order = [
        #     'Status',
        #     'HardwareStatus',
        #     'SoftwareStatus',
        #     'Reason',
        #     'HclModel',
        #     'HclCimcVersion',
        #     'HclDriverName',
        #     'HclDriverVersion',
        #     'HclFirmwareVersion'
        # ]

        # headers = [
        #     'Status',
        #     'Hardware',
        #     'Software',
        #     'Reason',
        #     'Model',
        #     'Cimc Version',
        #     'Driver Name',
        #     'Driver Version',
        #     'Firmware Version'
        # ]

        # self.my_output.my_table(
        #     server['HclInfo']['Details'],
        #     order=order,
        #     headers=headers,
        #     underline=True,
        #     table=True
        # )

    def print_hcl(self, servers, title=True):
        self.print_hcl_summary(servers, title=title)
        self.print_hcl_hardware(servers, title=title)
        self.print_hcl_software(servers, title=title)
        self.print_hcl_component(servers, title=title)

    def print_memory(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['MemoryInfo']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Memory [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'StateTick',
            'MemoryId',
            'ArrayId',
            'Bank',
            'Location',
            'CapacityUnit',
            'Clock',
            'LatencyUnit',
            'FormFactor',
            'Type',
            'Model',
            'Serial',
            'OperState',
            'Presence',
            'Thermal'
        ]

        headers = [
            'Server',
            'State',
            'Memory Id',
            'Array',
            'Bank',
            'Location',
            'Capacity',
            'Clock',
            'Latency',
            'Form Factor',
            'Type',
            'Model',
            'Serial',
            'Oper State',
            'Presence',
            'Thermal'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_adapters(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['AdaptersInfo']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Network Adapters [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Name',
            'PciSlot',
            'Model',
            'Serial',
            'Vendor',
            'HostEthIfsCount',
            'HostFcIfsCount',
            'ExtEthIfsCount'
        ]

        headers = [
            'Server',
            'Name',
            'PciSlot',
            'Model',
            'Serial',
            'Vendor',
            'Eth',
            'HBA',
            'DCE'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_ext_eth(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['ExtEthInfo']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'External Ethernet (MLOM) [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Dn',
            'InterfaceId',
            'MacAddress'
        ]

        headers = [
            'Server',
            'Adapter Dn',
            'Interface ID',
            'MAC Address'
        ]

        self.my_output.my_table(
            server['ExtEthInfo'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_host_eth(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['HostEthInfo']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Host Ethernet [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'AdapterName',
            'Name',
            'MacAddress'
        ]

        headers = [
            'Server',
            'Adapter Name',
            'Interface Name',
            'MAC Address'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_host_fc(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['HostFcInfo']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Host FC [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'AdapterName',
            'Name',
            'Wwnn',
            'Wwpn'
        ]

        headers = [
            'Server',
            'Adapter Name',
            'Interface Name',
            'WWNN',
            'WWPN'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_kvm(self, servers, title=False):
        info = []
        for server in servers:
            item = server['KvmInfo']
            item['ServerName'] = server['Name']
            info.append(
                item
            )

        if title:
            self.my_output.default(
                'KVM [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'KvmServerStateEnabled',
            'KvmVendor',
            'TunneledKvm',
            'KvmIpAddresses.Name',
            'KvmIpAddresses.Address',
            'KvmIpAddresses.Subnet',
            'KvmIpAddresses.DefaultGateway',
            'KvmIpAddresses.HttpPort',
            'KvmIpAddresses.HttpsPort',
            'KvmIpAddresses.KvmPort',
            'KvmIpAddresses.KvmVlan'
        ]

        headers = [
            'Server',
            'Kvm Server Enabled',
            'Kvm Vendor',
            'Tunneled Kvm',
            'Address Name',
            'Address',
            'Subnet',
            'Gateway',
            'Http Port',
            'Https Port',
            'Kvm Port',
            'Kvm Vlan'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['KvmIpAddresses']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_license(self, servers, title=False):
        if title:
            self.my_output.default(
                'License [#%s]' % (len(servers)),
                underline=True,
                before_newline=True
            )

        if len(servers) == 0:
            self.my_output.default('None')
            return

        order = [
            'Name',
            'LicenseInfo.Tier'
        ]

        headers = [
            'Server',
            'License'
        ]

        self.my_output.my_table(
            servers,
            order=order,
            headers=headers,
            table=True,
            allow_order_subkeys=True
        )

    def print_net(self, servers, title=False):
        self.print_adapters(servers, title=title)
        self.print_ext_eth(servers, title=title)
        self.print_host_eth(servers, title=title)
        self.print_host_fc(servers, title=title)

    def print_mac(self, server, title=False):
        if 'MacAddressInfo' not in server:
            return

        if title:
            self.my_output.default(
                'MAC Address [#%s]' % (len(server['MacAddressInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['MacAddressInfo']) == 0:
            self.my_output.default('None')
            return

        macs = sorted(
            server['MacAddressInfo'],
            key=lambda i: i['MacAddress']
        )

        order = [
            'MacAddress',
            'InterfaceName',
            'AdapterModel',
            'AdapterPciSlot'
        ]

        headers = [
            'MAC Address',
            'Interface',
            'Adapter',
            'Pci Slot'
        ]

        if len(macs) > 0 and 'Fabric' in macs[0]:
            order = order + [
                'Fabric.Type',
                'Fabric.Controller',
                'Fabric.Node',
                'Fabric.Port',
                'Fabric.Source'
            ]

            headers = headers + [
                'Fabric Type',
                'Controller',
                'Node',
                'Port',
                'Source'
            ]

            self.my_output.my_table(
                macs,
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )
        else:
            self.my_output.my_table(
                macs,
                order=order,
                headers=headers,
                underline=True,
                table=True
            )

    def print_mac_lldp_adjacency(self, server, title=False):
        if title:
            self.my_output.default(
                'Interface LLDP adjacency [#%s]' % (len(server['MacAddressInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['MacAddressInfo']) == 0:
            self.my_output.default('None')
            return

        for item in server['MacAddressInfo']:
            if item['adjacency'] is None:
                item['adjacency'] = {}
                item['adjacency']['pod_node_name'] = '--'
                item['adjacency']['interface_id'] = '--'
                item['adjacency']['health'] = '--'
                item['adjacency']['faults'] = '--'

        server['MacAddressInfo'] = sorted(
            server['MacAddressInfo'],
            key=lambda i: (
                i['AdapterModel'],
                i['InterfaceName'],
            )
        )

        order = [
            'MacAddress',
            'InterfaceName',
            'AdapterModel',
            'AdapterPciSlot',
            'adjacency.pod_node_name',
            'adjacency.interface_id',
            'adjacency.health',
            'adjacency.faults',
        ]

        headers = [
            'MAC Address',
            'Interface',
            'Adapter',
            'Pci Slot',
            'ACI Node',
            'Interface',
            'Nei Health',
            'Nei Faults'
        ]

        self.my_output.my_table(
            server['MacAddressInfo'],
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            merge=True
        )

    def print_pci(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['PciDevicesInfo']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'PCI [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Model',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'FirmwareVersion',
            'Dn'
        ]

        headers = [
            'Server',
            'PCI Device Model',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'Firmware',
            'Dn'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_power_consumption(self, servers, title=False):
        info = []
        for server in servers:
            item = server['Power']['Data']['PowerControl']
            item['ServerName'] = server['Name']
            info.append(
                item
            )

        if title:
            self.my_output.default(
                'Power Consumption [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'PowerConsumedWatts',
            'MinConsumedWatts',
            'AverageConsumedWatts',
            'MaxConsumedWatts',
            'LimitException'
        ]

        headers = [
            'Server',
            'Current',
            'Min',
            'Average',
            'Max',
            'Limit action'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=False,
            table=True
        )

    def print_power_voltage(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['Power']['Data']['Voltage']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Power Sensor [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Name',
            'State',
            'Health',
            'ReadingVolts',
            'UpperThresholdCritical'
        ]

        headers = [
            'Server',
            'Sensor Name',
            'State',
            'Health',
            'Volts',
            'Upper Threshold'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=False,
            table=True
        )

    def print_power_supply(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['Power']['Data']['PowerSupply']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Power Supply [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Name',
            'State',
            'Health',
            'SerialNumber',
            'FirmwareVersion',
            'PowerOutputWatts',
            'PowerInputWatts',
            'MaximumVoltage',
            'MinimumVoltage',
            'MaximumFrequencyHz',
            'MinimumFrequencyHz'
        ]

        headers = [
            'Server',
            'PSU Name',
            'State',
            'Health',
            'Serial',
            'Firmware',
            'Output (Watt)',
            'Input (Watt)',
            'Max (V)',
            'Min (V)',
            'Max (Hz)',
            'Min (Hz)'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=False,
            table=True
        )

    def print_power(self, servers, title=False):
        self.print_power_consumption(servers, title=title)
        self.print_power_voltage(servers, title=title)
        self.print_power_supply(servers, title=title)

    def print_profile(self, servers, title=False):
        info = []
        for server in servers:
            if server['ProfileInfo'] is not None:
                item = server['ProfileInfo']
                item['ServerName'] = server['Name']
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
            'ServerName',
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
            'Server',
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

    def print_psu(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['PsuInfo']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'PSU [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'StateTick',
            'Dn',
            'Model',
            'Serial',
            'Vendor',
            'On',
            'Voltage'
        ]

        headers = [
            'Server',
            'State',
            'Dn',
            'PSU Model',
            'Serial',
            'Vendor',
            'On',
            'Voltage'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_storage_controllers(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['StorageControllersInfo']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Storage Controller [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'ControllerId',
            'Model',
            'Vendor',
            'Serial',
            'Presence',
            'PciSlot',
            'RaidSupport',
            'PhysicalDiskCount',
            'VirtualDriveCount'
        ]

        headers = [
            'Server',
            'Controller',
            'Model',
            'Vendor',
            'Serial',
            'Presence',
            'PCI Slot',
            'Raid Support',
            'PD',
            'VD'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            table=True
        )

    def print_physical_disks(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['PhysicalDisks']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Physical Disk [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'StateTick',
            'StorageControllerId',
            'DiskId',
            'VirtualDriveId',
            'SizeUnit',
            'Type',
            'Protocol',
            'BootableTick',
            'LinkSpeed',
            'Pid',
            'Model',
            'Vendor',
            'DriveFirmware',
            'Serial',
            'DiskState',
            'Presence'
        ]

        headers = [
            'Server',
            'State',
            'Controller',
            'Disk Id',
            'VD',
            'Size',
            'Type',
            'Protocol',
            'Bootable',
            'Link Speed',
            'Pid',
            'Model',
            'Vendor',
            'Fw',
            'Serial',
            'State',
            'Presence'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            table=True
        )

    def print_virtual_drives(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['VirtualDisks']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Virtual Drive [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'StateTick',
            'StorageControllerId',
            'VirtualDriveId',
            'SizeUnit',
            'PhysicalDiskCount',
            'Type',
            'Name',
            'BootableTick',
            'ActualWriteCachePolicy',
            'DriveState'
        ]

        headers = [
            'Server',
            'State',
            'Controller',
            'Drive Id',
            'Size',
            'Disks',
            'Type',
            'Name',
            'Bootable',
            'Write Cache',
            'Drive State'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            table=True
        )

    def print_thermal_summary(self, servers, title=False):
        info = []
        for server in servers:
            item = server['Thermal']['Summary']
            item['ServerName'] = server['Name']
            info.append(
                item
            )

        if title:
            self.my_output.default(
                'Thermal Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'SensorHealth',
            'HighestTemperature',
            'SmallestGap',
            'OverThreshold',
            'FanHealth'
        ]

        headers = [
            'Server',
            'Sensors Health',
            'Highest (C)',
            'Smallest Gap (C)',
            'Over Threshold',
            'Fans Health'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=False,
            table=True
        )

    def print_thermal_sensor(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['Thermal']['Data']['Temperature']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Thermal Sensor [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Name',
            'State',
            'Health',
            'PhysicalContext',
            'ReadingCelsius',
            'UpperThresholdCritical'
        ]

        headers = [
            'Server',
            'Sensor Name',
            'State',
            'Health',
            'Location',
            'Value (Celcius)',
            'Upper Threshold (Celcius)'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=False,
            table=True
        )

    def print_thermal_fan(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['Thermal']['Data']['Fan']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Thermal Fan [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Name',
            'State',
            'Health',
            'Value'
        ]

        headers = [
            'Server',
            'Fan Name',
            'State',
            'Health',
            'Value'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=False,
            table=True
        )

    def print_thermal(self, servers, title=False):
        self.print_thermal_summary(servers, title=title)
        self.print_thermal_sensor(servers, title=title)
        self.print_thermal_fan(servers, title=title)

    def print_tpm(self, servers, title=False):
        info = []
        for server in servers:
            for item in server['TpmInfo']:
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.default(
                'Trusted Platform Module [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'ServerName',
            'Presence',
            'ActivationStatus',
            'AdminState',
            'Version',
            'Model',
            'Vendor',
            'Serial',
            'FirmwareVersion'
        ]

        headers = [
            'Server',
            'TPM',
            'Activation Status',
            'Admin State',
            'Version',
            'Model',
            'Vendor',
            'Serial',
            'Firmware Version'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_workflows(self, servers, workflow_count=10, title=False):
        info = []
        for server in servers:
            workflows = server['Workflow']['Last'][:workflow_count]
            for workflow in workflows:
                item = workflow
                item['ServerName'] = server['Name']
                info.append(item)

        if title:
            self.my_output.default(
                'Workflow [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'ServerName',
            'Moid',
            'Name',
            'CreateTime',
            'Status',
            'Duration'
        ]

        headers = [
            'Server',
            'Workflow Moid',
            'Name',
            'Create Time',
            'Status',
            'Duration'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
