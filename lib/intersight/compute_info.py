from lib.intersight import cache as intersight_cache
from lib.intersight.compute_extra_attributes import ComputeExtraAttributes
from lib.intersight import compute_rack
from lib.intersight import compute_blade
from lib import output_helper


class ComputeInfo(ComputeExtraAttributes):
    """Class for intersight compute blade and rack objects
    """
    def __init__(self, iaccount, settings=None, log_id=None):
        self.settings = settings
        if settings is None:
            self.settings = self.get_default_settings()

        ComputeExtraAttributes.__init__(self, iaccount, self.settings, log_id=log_id)
        self.get_info_cache_mode = False

        self.rack_handler = compute_rack.ComputeRack(iaccount, log_id=log_id)
        self.blade_handler = compute_blade.ComputeBlade(iaccount, log_id=log_id)
        self.my_output = output_helper.OutputHelper(log_id=log_id)

        self.cache_handler = intersight_cache.IntersightCache(
            log_id=log_id
        )

    def get_default_settings(self):
        settings = {}
        settings['rack'] = True
        settings['blade'] = True
        settings['workflow'] = None

        keys = [
            'advisory',
            'alarm',
            'bios',
            'board',
            'boot',
            'chassis',
            'connector',
            'contract',
            'cpu',
            'env',
            'fabric',
            'fan',
            'fw',
            'gpu',
            'group',
            'hcl',
            'kvm',
            'license',
            'id',
            'locator',
            'mac',
            'memory',
            'net',
            'pci',
            'pn',
            'power',
            'profile',
            'psu',
            'registration',
            'server_setting_id',
            'storage',
            'thermal',
            'tpm'
        ]

        for key in keys:
            settings[key] = False

        return settings

    def get(self, server_id, include_object=False):
        server = self.rack_handler.get(server_id)
        if server is None:
            server = self.blade_handler.get(server_id)

        if server is None:
            return None

        server_info = self.get_server_info(
            server,
            include_object=include_object
        )

        return server_info

    def print_summary_table(self, server, legend_on=False):
        order = []
        headers = []

        if server['StateEnabled']:
            order = order + [
                'FlagState',
                'FlagManagement',
                'FlagWorkflow'
            ]

            headers = headers + [
                'SF',
                'MF',
                'WF (%sd)' % (server['Workflow']['Days'])
            ]

        order = order + [
            'Name',
            'TypeModel',
            'Serial',
            'ManagementIp',
            'Cpu',
            'TotalMemoryUnit'
        ]

        headers = headers + [
            'Name',
            'Model',
            'Serial',
            'IP',
            'CPU',
            'Memory'
        ]

        if self.settings['fw']:
            order.append('FirmwareVersion')
            headers.append('Fw')

        self.my_output.my_table(
            [server],
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
            'HddDiskCount',
            'HddDiskCapacityUnit',
            'SsdDiskCount',
            'SsdDiskCapacityUnit',
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
                    'HDD count',
                    'HDD capacity',
                    'SSD count',
                    'SSD capacity',
                    'Virtual Disks'
                ]
            )

    def print_advisory(self, server):
        if 'AdvisoryInfo' not in server:
            return

        keys = [
            'High',
            'Info'
        ]

        self.my_output.dictionary(
            server['AdvisorySummary'],
            title='Advisory Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=keys
        )

        for advisory in server['AdvisoryInfo']:
            keys = [
                'Severity',
                'BaseScore',
                'Name',
                'Description',
                'CveIds',
                'DatePublished',
                'DateUpdated',
                'Urls',
                'Recommendation',
                'Workaround'
            ]

            headers = [
                'Severity',
                'Base Score',
                'Name',
                'Description',
                'Cve Ids',
                'Date Published',
                'Date Updated',
                'Details',
                'Recommendation',
                'Workaround'
            ]

            if len(advisory['Workaround']) == 0:
                keys.remove('Workaround')
                headers.remove('Workaround')

            self.my_output.dictionary(
                advisory,
                title='Advisory %s' % (advisory['AdvisoryId']),
                underline=True,
                prefix="- ",
                justify=True,
                keys=keys,
                title_keys=headers
            )

    def print_alarm(self, server):
        if 'AlarmInfo' not in server:
            return

        keys = [
            'Critical',
            'Warning',
            'Info'
        ]

        self.my_output.dictionary(
            server['AlarmSummary'],
            title='Alarm Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=keys
        )

        for alarm in server['AlarmInfo']:
            keys = [
                'Severity',
                'Description',
                'CreateTime',
                'AffectedType',
                'AffectedName'
            ]

            headers = [
                'Severity',
                'Description',
                'Create Time',
                'Affected Type',
                'Affected Name'
            ]

            self.my_output.dictionary(
                alarm,
                title='Alarm %s' % (alarm['Name']),
                underline=True,
                prefix="- ",
                justify=True,
                keys=keys,
                title_keys=headers
            )

    def print_bios(self, server):
        if 'BiosInfo' not in server:
            return

        self.my_output.default('Bios info: tbd')

    def print_board(self, server):
        if 'BoardInfo' not in server:
            return

        keys = [
            'BoardId',
            'Model',
            'Serial',
            'Vendor',
            'ProcessorsCount',
            'MemoryArraysCount'
        ]

        headers = [
            'Board Id',
            'Model',
            'Serial',
            'Vendor',
            'Processors',
            'Memory Arrays'
        ]

        if server['BoardInfo']['PciSwitchCount'] > 0:
            keys.append('PciSwitchCount')
            headers.append('PCI Switch')

        if server['BoardInfo']['PciCoprocessorCardsCount'] > 0:
            keys.append('PciCoprocessorCardsCount')
            headers.append('PCI Coprocessor Card')

        if server['BoardInfo']['GraphicsCardsCount'] > 0:
            keys.append('GraphicsCardsCount')
            headers.append('Graphics Card')

        if server['BoardInfo']['StorageControllersCount'] > 0:
            keys.append('StorageControllersCount')
            headers.append('Storage Controller')

        if server['BoardInfo']['StorageFlexFlashControllersCount'] > 0:
            keys.append('StorageFlexFlashControllersCount')
            headers.append('Storage Flex Flash Controller')

        if server['BoardInfo']['StorageFlexUtilControllersCount'] > 0:
            keys.append('StorageFlexUtilControllersCount')
            headers.append('Storage Flex Util Controller')

        if server['BoardInfo']['SecurityUnitsCount'] > 0:
            keys.append('SecurityUnitsCount')
            headers.append('Security Units')

        if server['BoardInfo']['EquipmentTpmsCount'] > 0:
            keys.append('EquipmentTpmsCount')
            headers.append('TPM')

        self.my_output.dictionary(
            server['BoardInfo'],
            title='Motherboard Hardware Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_boot(self, server):
        if 'BootInfo' not in server:
            return

        keys = [
            'ConfiguredBootMode',
            'ActualBootMode',
            'SecureBoot'
        ]

        headers = [
            'Configured Boot Mode',
            'Actual Boot Mode',
            'Secure Boot'
        ]

        self.my_output.dictionary(
            server['BootInfo'],
            title='Boot Settings',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

        order = [
            'Order',
            'Name',
            'Type',
            'State'
        ]

        headers = [
            'Order',
            'Name',
            'Type',
            'State'
        ]

        self.my_output.my_table(
            server['BootInfo']['Order'],
            order=order,
            headers=headers,
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

    def print_connector(self, server):
        if 'ConnectorInfo' not in server:
            return

        keys = [
            'ConnectionStatus',
            'ConnectorVersion',
            'ClaimedByUserName',
            'ClaimedTime',
            'ConnectionStatusLastChangeTime',
            'PlatformType',
            'DeviceExternalIpAddress'
        ]

        headers = [
            'Connection Status',
            'Connector Version',
            'Claimed By',
            'Claimed Time',
            'Connection Status Last Update',
            'Platform Type',
            'Device External IP Address'
        ]

        self.my_output.dictionary(
            server['ConnectorInfo'],
            title='Device Connector',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_contract(self, server):
        if 'ContractInfo' not in server:
            return

        keys = [
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

        self.my_output.dictionary(
            server['ContractInfo'],
            title='Contract Coverage',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_cpu(self, server):
        if 'CpuInfo' not in server:
            return

        order = [
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
            server['CpuInfo'],
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_fan(self, server):
        if 'FanInfo' not in server:
            return

        order = [
            'StateTick',
            'ModuleId',
            'OperState',
            'Presence',
            'Dn'
        ]

        headers = [
            'State',
            'Fan Module Id',
            'OperState',
            'Presence',
            'Dn'
        ]

        self.my_output.my_table(
            server['FanInfo'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_firmware(self, server):
        if 'FirmwarewComponents' not in server:
            return

        order = [
            'Name',
            'Component',
            'Type',
            'PackageVersion',
            'Version',
            'Dn'
        ]

        headers = [
            'Name',
            'Component',
            'Type',
            'PackageVersion',
            'Version',
            'Dn'
        ]

        self.my_output.my_table(
            server['FirmwarewComponents'],
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_gpu(self, server):
        if 'GpuInfo' not in server:
            return

        order = [
            'Model',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'FirmwareVersion',
            'Dn'
        ]

        headers = [
            'GPU Device Model',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'Firmware',
            'Dn'
        ]

        self.my_output.my_table(
            server['GpuInfo'],
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_hcl_summary(self, server):
        keys = [
            'Status'
        ]

        headers = [
            'Overall'
        ]

        self.my_output.dictionary(
            server['HclInfo'],
            title='HCL Status',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_hcl_hardware(self, server):
        keys = [
            'HardwareStatus',
            'HclModel',
            'HclProcessor',
            'HclFirmwareVersion'
        ]

        headers = [
            'Status',
            'Model',
            'CPU',
            'Firmware'
        ]

        self.my_output.dictionary(
            server['HclInfo'],
            title='HCL - Server Hardware Compliance',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_hcl_software(self, server):
        keys = [
            'SoftwareStatus',
            'Reason',
            'HclOsVendor',
            'HclOsVersion'
        ]

        headers = [
            'Status',
            'Reason',
            'OS Vendor',
            'OS Version'
        ]

        self.my_output.dictionary(
            server['HclInfo'],
            title='HCL - Server Software Compliance',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_hcl_component(self, server):
        keys = [
            'ComponentStatus',
            'ServerReason'
        ]

        headers = [
            'Status',
            'Reason'
        ]

        self.my_output.dictionary(
            server['HclInfo'],
            title='HCL - Adapter Compliance',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

        order = [
            'Status',
            'HardwareStatus',
            'SoftwareStatus',
            'Reason',
            'HclModel',
            'HclCimcVersion',
            'HclDriverName',
            'HclDriverVersion',
            'HclFirmwareVersion'
        ]

        headers = [
            'Status',
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
            server['HclInfo']['Details'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_hcl(self, server):
        if 'HclInfo' not in server:
            return

        self.print_hcl_summary(server)
        self.print_hcl_hardware(server)
        self.print_hcl_software(server)
        self.print_hcl_component(server)

    def print_memory(self, server):
        if 'MemoryInfo' not in server:
            return

        order = [
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
            server['MemoryInfo'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_adapters(self, server):
        if 'AdaptersInfo' not in server:
            return

        self.my_output.default('Section: Network Adapters', before_newline=True, underline=True)

        order = [
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
            server['AdaptersInfo'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_ext_eth(self, server):
        if 'ExtEthInfo' not in server or len(server['ExtEthInfo']) == 0:
            return

        self.my_output.default('Section: External Ethernet (MLOM)', before_newline=True, underline=True)

        order = [
            'Dn',
            'InterfaceId',
            'MacAddress'
        ]

        headers = [
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

    def print_host_eth(self, server):
        if 'HostEthInfo' not in server or len(server['HostEthInfo']) == 0:
            return

        self.my_output.default('Section: Host Ethernet', before_newline=True, underline=True)

        order = [
            'AdapterName',
            'Name',
            'MacAddress'
        ]

        headers = [
            'Adapter Name',
            'Interface Name',
            'MAC Address'
        ]

        self.my_output.my_table(
            server['HostEthInfo'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_host_fc(self, server):
        if 'HostFcInfo' not in server or len(server['HostFcInfo']) == 0:
            return

        self.my_output.default('Section: Host FC', before_newline=True, underline=True)

        order = [
            'AdapterName',
            'Name',
            'Wwnn',
            'Wwpn'
        ]

        headers = [
            'Adapter Name',
            'Interface Name',
            'WWNN',
            'WWPN'
        ]

        self.my_output.my_table(
            server['HostFcInfo'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_kvm(self, server):
        if 'KvmInfo' not in server:
            return

        keys = [
            'KvmServerStateEnabled',
            'KvmVendor',
            'TunneledKvm'
        ]

        headers = [
            'Kvm Server State Enabled',
            'Kvm Vendor',
            'Tunneled Kvm'
        ]

        self.my_output.dictionary(
            server['KvmInfo'],
            title='Kvm Settings',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

        order = [
            'Name',
            'Address',
            'Subnet',
            'DefaultGateway',
            'HttpPort',
            'HttpsPort',
            'KvmPort',
            'KvmVlan'
        ]

        headers = [
            'Name',
            'Address',
            'Subnet',
            'Gateway',
            'Http Port',
            'Https Port',
            'Kvm Port',
            'Kvm Vlan'
        ]

        self.my_output.my_table(
            server['KvmInfo']['KvmIpAddresses'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_license(self, server):
        if 'LicenseInfo' not in server:
            return

        self.my_output.default('License Tier: %s' % (server['LicenseInfo']['Tier']))

    def print_net(self, server):
        if 'MacAddressInfo' not in server:
            self.print_adapters(server)
            self.print_ext_eth(server)
            self.print_host_eth(server)
            self.print_host_fc(server)

    def print_mac(self, server):
        if 'MacAddressInfo' not in server or len(server['MacAddressInfo']) == 0:
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

    def print_pci(self, server):
        if 'PciDevicesInfo' not in server:
            return

        order = [
            'Model',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'FirmwareVersion',
            'Dn'
        ]

        headers = [
            'PCI Device Model',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'Firmware',
            'Dn'
        ]

        self.my_output.my_table(
            server['PciDevicesInfo'],
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_pn(self, server):
        if 'PnInfo' not in server:
            return

        self.my_output.default('P/N info: tbd')

    def print_power(self, server):
        if 'Power' not in server:
            return

        if server['Power'] is None:
            self.my_output.default('No power consumption information found')

        if server['Power'] is not None and server['Redfish']['Enabled']:
            self.redfish_endpoint_settings_handler.print_redfish_endpoint_template(
                server['Serial'],
                'power',
                server['Power']
            )

        if server['Power'] is not None and server['UCSM']['Enabled']:
            self.ucsm_endpoint_settings_handler.print_ucsm_endpoint_template(
                server['Serial'],
                'power',
                server['Power']
            )

    def print_profile(self, server):
        if 'ProfileInfo' not in server:
            return

        keys = [
            'Name',
            'ConfigState',
            'ModTime',
            'TargetPlatform'
        ]

        headers = [
            'Name',
            'State',
            'Last Modified',
            'Target Platform'
        ]

        self.my_output.dictionary(
            server['ProfileInfo'],
            title='Server Profile',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

        order = [
            'Name',
            'ClassId',
            'ModTime',
            'Shared',
            'InSync'
        ]

        headers = [
            'Policy Name',
            'Class Id',
            'Modification Time',
            'Shared',
            'In Sync'
        ]

        self.my_output.my_table(
            server['ProfileInfo']['Policies'],
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_psu(self, server):
        if 'PsuInfo' not in server:
            return

        order = [
            'StateTick',
            'Dn',
            'Model',
            'Serial',
            'Vendor',
            'On',
            'Voltage'
        ]

        headers = [
            'State',
            'Dn',
            'PSU Model',
            'Serial',
            'Vendor',
            'On',
            'Voltage'
        ]

        self.my_output.my_table(
            server['PsuInfo'],
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_storage_summary(self, server):
        if 'StorageControllersInfo' not in server or 'PhysicalDisks' not in server and 'VirtualDisks' not in server:
            return

        order = [
            'StorageControllersCount',
            'PhysicalDiskCount',
            'PhysicalDiskCapacityUnit',
            'HddDiskCount',
            'HddDiskCapacityUnit',
            'SsdDiskCount',
            'SsdDiskCapacityUnit',
            'VirtualDiskCount',
            'VirtualDiskCapacityUnit'
        ]

        headers = [
            'Controllers',
            'Disks Count',
            'Capacity',
            'HDD Count',
            'HDD Capacity',
            'SSD Count',
            'SSD Capacity',
            'Virtual Drive Count',
            'Virtual Drive Capacity'
        ]

        if server['SsdDiskCount'] == 0:
            order.remove('SsdDiskCount')
            order.remove('SsdDiskCapacityUnit')
            headers.remove('SSD Count')
            headers.remove('SSD Capacity')

        if server['VirtualDiskCount'] == 0:
            order.remove('VirtualDiskCount')
            order.remove('VirtualDiskCapacityUnit')
            headers.remove('Virtual Drive Count')
            headers.remove('Virtual Drive Capacity')

        if server['HddDiskCount'] == 0:
            order.remove('HddDiskCount')
            order.remove('HddDiskCapacityUnit')
            headers.remove('HDD Count')
            headers.remove('HDD Capacity')

        self.my_output.dictionary(
            server,
            title='Storage Summary',
            underline=False,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_storage_controllers(self, server):
        if 'StorageControllersInfo' not in server:
            return

        for storage_controller in server['StorageControllersInfo']:
            self.my_output.dictionary(
                storage_controller,
                title='Storage Controller',
                underline=False,
                prefix="- ",
                justify=True,
                keys=[
                    'Model',
                    'Vendor',
                    'Serial',
                    'Presence',
                    'ControllerStatus',
                    'PciAddr',
                    'PciSlot',
                    'ControllerId',
                    'Name',
                    'Dn',
                    'RaidSupport',
                    'PhysicalDiskCount',
                    'VirtualDriveCount'
                ],
                title_keys=[
                    'Model',
                    'Vendor',
                    'Serial',
                    'Presence',
                    'Status',
                    'PCIe Address',
                    'PCI Slot',
                    'Controller Id',
                    'Name',
                    'Dn',
                    'Raid Support',
                    'Physical Disks Count',
                    'Virtual Drives Count'
                ]
            )

    def print_physical_disks(self, server):
        if 'PhysicalDisks' not in server:
            return

        order = [
            'StateTick',
            'DiskId',
            'SizeUnit',
            'Type',
            'BootableTick',
            'LinkSpeed',
            'StorageControllerName',
            'VirtualDriveId',
            'Model',
            'Vendor',
            'DriveFirmware',
            'Serial',
            'DiskState',
            'Presence',
            'Operability',
            'Dn'
        ]

        headers = [
            'State',
            'Disk Id',
            'Size',
            'Type',
            'Bootable',
            'Link Speed',
            'Controller',
            'Drive Id',
            'Model',
            'Vendor',
            'Fw',
            'Serial',
            'State',
            'Presence',
            'Operability',
            'Dn'
        ]

        self.my_output.my_table(
            server['PhysicalDisks'],
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_virtual_drives(self, server):
        if 'VirtualDisks' not in server:
            return

        order = [
            'StateTick',
            'VirtualDriveId',
            'SizeUnit',
            'PhysicalDiskCount',
            'Type',
            'Name',
            'BootableTick',
            'ActualWriteCachePolicy',
            'StorageControllerName',
            'DriveState',
            'Presence',
            'Operability',
            'Dn'
        ]

        headers = [
            'State',
            'Drive Id',
            'Size',
            'Disks',
            'Type',
            'Name',
            'Bootable',
            'Write Cache',
            'Controller',
            'State',
            'Presence',
            'Operability',
            'Dn'
        ]

        self.my_output.my_table(
            server['VirtualDisks'],
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_thermal(self, server):
        if 'Thermal' not in server:
            return

        if server['Thermal'] is None:
            self.my_output.default('No thermal information found')

        if server['Thermal'] is not None and server['Redfish']['Enabled']:
            self.redfish_endpoint_settings_handler.print_redfish_endpoint_template(
                server['Serial'],
                'thermal',
                server['Thermal']
            )

        if server['Thermal'] is not None and server['UCSM']['Enabled']:
            self.ucsm_endpoint_settings_handler.print_ucsm_endpoint_template(
                server['Serial'],
                'thermal',
                server['Thermal']
            )

    def print_tpm(self, server):
        if 'TpmInfo' not in server:
            return

        if server['TpmInfo'] is None:
            self.my_output.error('TPM information not collected')
            return

        order = [
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
            server['TpmInfo'],
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_workflows(self, server, workflow_count=10, show_empty_table=False):
        if 'Workflow' not in server:
            return

        if server['Workflow'] is None:
            return

        if workflow_count == 0:
            return

        workflows = server['Workflow']['Last'][:workflow_count]
        if len(workflows) == 0:
            if not show_empty_table:
                return

        order = [
            'Moid',
            'Name',
            'CreateTime',
            'Status',
            'Duration'
        ]

        headers = [
            'Workflow Moid',
            'Name',
            'Create Time',
            'Status',
            'Duration'
        ]

        self.my_output.my_table(
            workflows,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print(self, server, workflow_count=10, legend_on=False):
        self.print_summary_table(server, legend_on=legend_on)
        self.print_chassis(server)

        self.print_alarm(server)
        self.print_advisory(server)
        self.print_hcl(server)
        self.print_connector(server)
        self.print_contract(server)
        self.print_license(server)
        self.print_profile(server)
        self.print_bios(server)
        self.print_board(server)
        self.print_boot(server)
        self.print_cpu(server)
        self.print_gpu(server)
        self.print_kvm(server)
        self.print_memory(server)
        self.print_firmware(server)
        self.print_storage_summary(server)
        self.print_storage_controllers(server)
        self.print_physical_disks(server)
        self.print_virtual_drives(server)
        self.print_net(server)
        self.print_mac(server)
        self.print_pci(server)
        self.print_fan(server)
        self.print_psu(server)
        self.print_power(server)
        self.print_thermal(server)
        self.print_tpm(server)
        self.print_workflows(server, workflow_count=workflow_count)
        self.print_pn(server)
