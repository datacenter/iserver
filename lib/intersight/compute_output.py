import csv

from lib import filter_helper
from lib import output_helper

from lib.intersight.compute_aci_output import ComputeAciOutput
from lib.intersight.cond_alarm.output import ComputeCondAlarmOutput
from lib.intersight.compute_nx_output import ComputeNxOutput
from lib.intersight.equipment_psu.output import ComputePsuOutput
from lib.intersight.tam_advisory_instance.output import TamAdvisoryInstanceOutput


class ComputeOutput(
        ComputeAciOutput,
        ComputeCondAlarmOutput,
        ComputeNxOutput,
        ComputePsuOutput,
        TamAdvisoryInstanceOutput
        ):
    def __init__(self, log_id=None):
        self.my_output = output_helper.OutputHelper(log_id=log_id)
        ComputeAciOutput.__init__(self)
        ComputeCondAlarmOutput.__init__(self)
        ComputeNxOutput.__init__(self)
        ComputePsuOutput.__init__(self)
        TamAdvisoryInstanceOutput.__init__(self)

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
                'FlagManagement'
            ]

            headers = headers + [
                'SF',
                'MF'
            ]

            if 'Workflow' in servers[0]:
                order = order + [
                    'FlagWorkflow'
                ]

                headers = headers + [
                    'WF (%sd)' % (servers[0]['Workflow']['Days'])
                ]

            for server in servers:
                if 'Workflow' in server:
                    if len(server['FlagWorkflow']) == 0:
                        server['FlagWorkflow'] = '--'

        row_separator = False
        for server in servers:
            server['TagT'] = []
            for item in server['Tags']:
                server['TagT'].append(
                    '%s:%s' % (
                        item['Key'],
                        item['Value']
                    )
                )
            if len(server['TagT']) > 1:
                row_separator = True

        order = order + [
            'Name',
            'TagT',
            'TypeModel',
            'Serial',
            'ManagementIp',
            'Cpu',
            'TotalMemoryUnit'
        ]

        headers = headers + [
            'Name',
            'Tag',
            'Model',
            'Serial',
            'IP',
            'CPU',
            'Memory'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                servers,
                order,
                ['TagT']
            ),
            order=order,
            headers=headers,
            row_separator=row_separator,
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

    def print_board(self, servers, title=False):
        info = []
        for server in servers:
            if 'BoardInfo' in server:
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
            if 'BootInfo' in server:
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
            if 'ConnectorInfo' in server:
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
            if 'ContractInfo' in server:
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
            if 'CpuInfo' in server:
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

    def print_fan_module(self, servers, title=False):
        info = []
        for server in servers:
            if 'FanModuleInfo' in server:
                for item in server['FanModuleInfo']:
                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.default(
                'Fan Module [#%s]' % (len(info)),
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
            'Name',
            'OperState',
            'Presence'
        ]

        headers = [
            'Server',
            'State',
            'Fan Module',
            'OperState',
            'Presence'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_fan(self, servers, title=False):
        info = []
        for server in servers:
            if 'FanInfo' in server:
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
            'Name',
            'OperState',
            'Presence'
        ]

        headers = [
            'Server',
            'State',
            'Fan',
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
            if 'FirmwarewComponents' in server:
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
            if 'GpuInfo' in server:
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
            if 'HclInfo' in server:
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
            if 'HclInfo' in server:
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
            if 'HclInfo' in server:
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
            if 'HclInfo' in server:
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
            if 'MemoryInfo' in server:
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
            if 'AdapterInfo' in server:
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
            if 'ExtEthInfo' in server:
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
            if 'HostEthInfo' in server:
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
            if 'HostFcInfo' in server:
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
            if 'KvmInfo' in server:
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

    def print_pci(self, servers, title=False):
        info = []
        for server in servers:
            if 'PciDevicesInfo' in server:
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

        for item in info:
            item['ModelT'] = filter_helper.get_string_chunks(
                item['Model'],
                40
            )

        order = [
            'ServerName',
            'ModelT',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'FirmwareVersion'
        ]

        headers = [
            'Server',
            'PCI Device Model',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'Firmware'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['ModelT']
            ),
            order=order,
            headers=headers,
            remove_empty_columns=True,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_power_consumption(self, servers, title=False):
        info = []
        for server in servers:
            if 'Power' in server and server['Power'] is not None:
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
            if 'Power' in server and server['Power'] is not None:
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
            if 'Power' in server and server['Power'] is not None:
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
            if 'ProfileInfo' in server:
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

    def print_storage_controllers(self, servers, title=False):
        info = []
        for server in servers:
            if 'StorageControllersInfo' in server:
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

        for item in info:
            item['ModelT'] = filter_helper.get_string_chunks(
                item['Model'],
                30
            )

        order = []
        headers = []
        if len(servers) > 1:
            order = ['ServerName']
            headers = ['Server']

        order = order + [
            'ControllerId',
            'ModelT',
            'Vendor',
            'Serial',
            'Presence',
            'PciSlot',
            'RaidSupport',
            'PhysicalDiskCount',
            'VirtualDriveCount'
        ]

        headers = headers + [
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
            self.my_output.expand_lists(
                info,
                order,
                ['ModelT']
            ),
            order=order,
            headers=headers,
            remove_empty_columns=False,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_physical_disks_state(self, servers, title=False):
        info = []
        for server in servers:
            if 'PhysicalDisks' in server:
                for item in server['PhysicalDisks']:
                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.default(
                'Physical Disk - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = []
        headers = []
        if len(servers) > 1:
            order = ['ServerName']
            headers = ['Server']

        order = order + [
            'StateTick',
            'StorageControllerId',
            'DiskId',
            'VirtualDriveId',
            'SizeUnit',
            'Type',
            'Protocol',
            'BootableTick',
            'LinkSpeed',
            'DriveFirmware',
            'DiskState',
            'Presence'
        ]

        headers = headers + [
            'State',
            'Controller',
            'Disk Id',
            'VD',
            'Size',
            'Type',
            'Protocol',
            'Bootable',
            'Link Speed',
            'Fw',
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

    def print_physical_disks_inventory(self, servers, title=False):
        info = []
        for server in servers:
            if 'PhysicalDisks' in server:
                for item in server['PhysicalDisks']:
                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.default(
                'Physical Disk - Inventory [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = []
        headers = []
        if len(servers) > 1:
            order = ['ServerName']
            headers = ['Server']

        order = order + [
            'DiskId',
            'Pid',
            'Model',
            'Vendor',
            'Serial'
        ]

        headers = headers + [
            'Disk Id',
            'Pid',
            'Model',
            'Vendor',
            'Serial'
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
        self.print_physical_disks_state(servers, title=title)
        self.print_physical_disks_inventory(servers, title=title)

    def print_virtual_drives(self, servers, title=False):
        info = []
        for server in servers:
            if 'VirtualDisks' in server:
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

        order = []
        headers = []
        if len(servers) > 1:
            order = ['ServerName']
            headers = ['Server']

        order = order + [
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

        headers = headers + [
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
            if 'Thermal' in server:
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
            if 'Thermal' in server:
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
            if 'Thermal' in server:
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
            if 'TpmInfo' in server:
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
            if 'Workflow' in server:
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

    def print_inventory_rack(self, server_info, title=False):
        if title:
            self.my_output.default(
                'Server Inventory (R): %s' % (server_info['Name']),
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
            server_info['Inventory'],
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_inventory_chassis(self, chassis_info, title=False):
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

    def print_inventory_blade(self, server_info, title=False):
        if title:
            self.my_output.default(
                'Server Inventory (B): %s' % (server_info['Name']),
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
            server_info['Inventory'],
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_inventory(self, servers, chassiz_info, title=False):
        for server in servers:
            if server['Type'] == 'Rack':
                self.print_inventory_rack(
                    server,
                    title=title
                )

        chassis_moid = []
        for server in servers:
            if server['Type'] == 'Blade':
                if server['ChassisMoid'] not in chassis_moid:
                    chassis_moid.append(
                        server['ChassisMoid']
                    )

        for chassis_info in chassiz_info:
            if chassis_info['Moid'] in chassis_moid:
                self.print_inventory_chassis(
                    chassis_info,
                    title=title
                )

                for server in servers:
                    if server['Type'] == 'Blade':
                        if server['ChassisMoid'] == chassis_info['Moid']:
                            self.print_inventory_blade(
                                server,
                                title=title
                            )

    def print_inventory_csv(self, servers_info, chassiz_info, inventory_filename):
        fields = [
            'Inventory Type',
            'Inventory Name',
            'Inventory Model',
            'Inventory Vendor',
            'Inventory Serial',
            'Inventory PID',
            'Top Owner',
            'Chassis Serial',
            'Chassis PID',
            'Chassis Name',
            'Server Serial',
            'Server PID',
            'Server Name'
        ]
        rows = []

        for server_info in servers_info:
            if server_info['Type'] == 'Rack':
                for inventory_info in server_info['Inventory']:
                    row = []
                    row.append(inventory_info['Type'])
                    row.append(inventory_info['Name'])
                    row.append(inventory_info['Model'])
                    row.append(inventory_info['Vendor'])
                    row.append(inventory_info['Serial'])
                    row.append(inventory_info['Pid'])
                    row.append('Server')
                    row.append('N/A')
                    row.append('N/A')
                    row.append('N/A')
                    row.append(inventory_info['ServerSerial'])
                    row.append(inventory_info['ServerPid'])
                    row.append(server_info['Name'])
                    rows.append(
                        row
                    )

        chassis_moid = []
        for server_info in servers_info:
            if server_info['Type'] == 'Blade':
                if server_info['ChassisMoid'] not in chassis_moid:
                    chassis_moid.append(
                        server_info['ChassisMoid']
                    )

        for chassis_info in chassiz_info:
            if chassis_info['Moid'] in chassis_moid:
                for inventory_info in chassis_info['Inventory']:
                    row = []
                    row.append(inventory_info['Type'])
                    row.append(inventory_info['Name'])
                    row.append(inventory_info['Model'])
                    row.append(inventory_info['Vendor'])
                    row.append(inventory_info['Serial'])
                    row.append(inventory_info['Pid'])
                    row.append('Chassis')
                    row.append(chassis_info['ChassisSerial'])
                    row.append(chassis_info['ChassisPid'])
                    row.append(chassis_info['Name'])
                    row.append('N/A')
                    row.append('N/A')
                    row.append('N/A')
                    rows.append(
                        row
                    )

                for server_info in servers_info:
                    if server_info['Type'] == 'Blade':
                        if server_info['ChassisMoid'] == chassis_info['Moid']:
                            for inventory_info in server_info['Inventory']:
                                row = []
                                row.append(inventory_info['Type'])
                                row.append(inventory_info['Name'])
                                row.append(inventory_info['Model'])
                                row.append(inventory_info['Vendor'])
                                row.append(inventory_info['Serial'])
                                row.append(inventory_info['Pid'])
                                row.append('Chassis')
                                row.append(chassis_info['ChassisSerial'])
                                row.append(chassis_info['ChassisPid'])
                                row.append(chassis_info['Name'])
                                row.append(inventory_info['ServerSerial'])
                                row.append(inventory_info['ServerPid'])
                                row.append(server_info['Name'])
                                rows.append(
                                    row
                                )

        with open(inventory_filename, 'w', newline='') as file_handler:
            write = csv.writer(file_handler)
            write.writerow(fields)
            for row in rows:
                write.writerow(row)
