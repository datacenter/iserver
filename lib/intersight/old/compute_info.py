import time

from lib.intersight import cache as intersight_cache
from lib.intersight.compute_extra_attributes import ComputeExtraAttributes
from lib.intersight import compute_rack
from lib.intersight import compute_blade
from lib import output_helper


class ComputeInfo(ComputeExtraAttributes):
    """Class for intersight compute blade and rack objects
    """
    def __init__(self, iaccount, log_id=None):
        ComputeExtraAttributes.__init__(self, iaccount, log_id=log_id)
        self.get_info_cache_mode = False

        self.rack_handler = compute_rack.ComputeRack(iaccount, log_id=log_id)
        self.blade_handler = compute_blade.ComputeBlade(iaccount, log_id=log_id)
        self.my_output = output_helper.OutputHelper(log_id=log_id)

        self.cache_handler = intersight_cache.IntersightCache(
            iaccount,
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
            'state',
            'storage',
            'thermal',
            'tpm'
        ]

        for key in keys:
            settings[key] = False

        return settings

    def set_cache(self, server_mo, cache_settings, cache_disabled=False):
        start_time = int(time.time() * 1000)
        self.log.debug(
            'compute_info.set_intersight_cache',
            'Start managed objects preparation'
        )

        moids = []
        serial = {}
        device_moids = {}
        registration_moids = {}
        board_moids = {}
        adapter_moids = {}
        boot_moids = {}

        moids.append(server_mo['Moid'])
        serial[server_mo['Moid']] = server_mo['Serial']
        device_moids[server_mo['Moid']] = server_mo['DeviceMoId']
        registration_moids[server_mo['Moid']] = server_mo['RegisteredDevice']['Moid']
        board_moids[server_mo['Moid']] = server_mo['Board']['Moid']

        adapter_moids[server_mo['Moid']] = []
        for adapter_mo in server_mo['Adapters']:
            adapter_moids[server_mo['Moid']].append(
                adapter_mo['Moid']
            )

        boot_moids[server_mo['Moid']] = {}

        boot_moids[server_mo['Moid']]['cdd'] = []
        for item in server_mo['BootCddDevices']:
            boot_moids[server_mo['Moid']]['cdd'].append(
                item['Moid']
            )

        boot_moids[server_mo['Moid']]['cdd'] = []
        for item in server_mo['BootCddDevices']:
            boot_moids[server_mo['Moid']]['cdd'].append(
                item['Moid']
            )

        boot_moids[server_mo['Moid']]['cdd'] = []
        for item in server_mo['BootCddDevices']:
            boot_moids[server_mo['Moid']]['cdd'].append(
                item['Moid']
            )

        boot_moids[server_mo['Moid']]['hdd'] = []
        for item in server_mo['BootHddDevices']:
            boot_moids[server_mo['Moid']]['hdd'].append(
                item['Moid']
            )

        boot_moids[server_mo['Moid']]['iscsi'] = []
        for item in server_mo['BootIscsiDevices']:
            boot_moids[server_mo['Moid']]['iscsi'].append(
                item['Moid']
            )

        boot_moids[server_mo['Moid']]['nvme'] = []
        for item in server_mo['BootNvmeDevices']:
            boot_moids[server_mo['Moid']]['nvme'].append(
                item['Moid']
            )

        boot_moids[server_mo['Moid']]['pxe'] = []
        for item in server_mo['BootPxeDevices']:
            boot_moids[server_mo['Moid']]['pxe'].append(
                item['Moid']
            )

        boot_moids[server_mo['Moid']]['san'] = []
        for item in server_mo['BootSanDevices']:
            boot_moids[server_mo['Moid']]['san'].append(
                item['Moid']
            )

        boot_moids[server_mo['Moid']]['sd'] = []
        for item in server_mo['BootSdDevices']:
            boot_moids[server_mo['Moid']]['sd'].append(
                item['Moid']
            )

        boot_moids[server_mo['Moid']]['uefi'] = []
        for item in server_mo['BootUefiShellDevices']:
            boot_moids[server_mo['Moid']]['uefi'].append(
                item['Moid']
            )

        boot_moids[server_mo['Moid']]['usb'] = []
        for item in server_mo['BootUsbDevices']:
            boot_moids[server_mo['Moid']]['usb'].append(
                item['Moid']
            )

        boot_moids[server_mo['Moid']]['vmedia'] = []
        for item in server_mo['BootVmediaDevices']:
            boot_moids[server_mo['Moid']]['vmedia'].append(
                item['Moid']
            )

        keys = []

        if cache_settings['board']:
            keys.append('board')

        if cache_settings['cpu']:
            keys.append('cpu')

        if cache_settings['gpu']:
            keys.append('gpu')

        if cache_settings['fan']:
            keys.append('fanmodule')

        if cache_settings['memory']:
            keys.append('memory')

        if cache_settings['pci']:
            keys.append('pci')

        if cache_settings['net']:
            keys.append('adapter')
            keys.append('adapter_ext_eth_interface')
            keys.append('adapter_host_eth_interface')
            keys.append('adapter_host_fc_interface')

        if cache_settings['psu']:
            keys.append('psu')

        if cache_settings['storage']:
            keys.append('storage_controller')
            keys.append('virtual_drive')
            keys.append('physical_disk')

        if cache_settings['fw']:
            keys.append('firmware')

        if cache_settings['boot']:
            keys.append('boot_bios')
            keys.append('boot_mode')
            keys.append('boot_security')
            keys.append('boot_hdd')
            keys.append('boot_cdd')
            keys.append('boot_iscsi')
            keys.append('boot_nvme')
            keys.append('boot_pxe')
            keys.append('boot_san')
            keys.append('boot_sd')
            keys.append('boot_uefi')
            keys.append('boot_usb')
            keys.append('boot_vmedia')

        if cache_settings['advisory']:
            keys.append('advisory')
            self.set_intersight_cache(
                'advisories',
                moids,
                device_moids,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_disabled=cache_disabled
            )

        if cache_settings['alarm']:
            keys.append('alarm')

        if cache_settings['connector'] or cache_settings['registration']:
            keys.append('connector')

        if cache_settings['contract']:
            keys.append('contract')

        if cache_settings['hcl']:
            keys.append('hcl')

        if cache_settings['profile']:
            keys.append('profile')

        # if cache_settings['locator']:
        #     keys.append('locator_led')

        if cache_settings['workflow'] is not None:
            keys.append('workflow')
            self.set_intersight_cache(
                'workflows',
                moids,
                device_moids,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_disabled=cache_disabled
            )

        if len(keys) > 0:
            for key in keys:
                self.set_intersight_cache(
                    key,
                    moids,
                    device_moids,
                    registration_moids,
                    board_moids,
                    adapter_moids,
                    boot_moids,
                    serial,
                    cache_settings['workflow'],
                    cache_disabled=cache_disabled
                )

        if cache_settings['hcl']:
            self.set_intersight_cache(
                'hcl_detail',
                moids,
                device_moids,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_disabled=cache_disabled
            )

        if cache_settings['storage']:
            self.set_intersight_cache(
                'physical_disk_usage',
                moids,
                device_moids,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_disabled=cache_disabled
            )

        if cache_settings['tpm']:
            self.set_intersight_cache(
                'tpm',
                moids,
                device_moids,
                registration_moids,
                board_moids,
                adapter_moids,
                boot_moids,
                serial,
                cache_settings['workflow'],
                cache_disabled=cache_disabled
            )

        if cache_settings['power']:
            if server_mo['ManagementMode'] == 'UCSM':
                if self.ucsm_endpoint_settings_handler.is_ucsm_endpoint(server_mo['Serial']):
                    server_serial = {}
                    server_serial[server_mo['Moid']] = server_mo['Serial']
                    self.set_redfish_cache(
                        'power-ucsm',
                        moids,
                        server_serial,
                        cache_disabled=cache_disabled
                    )

            if server_mo['ManagementMode'] != 'UCSM':
                if self.redfish_endpoint_settings_handler.is_redfish_endpoint(server_mo['Serial']):
                    server_serial = {}
                    server_serial[server_mo['Moid']] = server_mo['Serial']
                    self.set_redfish_cache(
                        'power',
                        moids,
                        server_serial,
                        cache_disabled=cache_disabled
                    )

        if cache_settings['thermal']:
            if server_mo['OperPowerState'] == 'on':
                if server_mo['ManagementMode'] == 'UCSM':
                    if self.ucsm_endpoint_settings_handler.is_ucsm_endpoint(server_mo['Serial']):
                        server_serial = {}
                        server_serial[server_mo['Moid']] = server_mo['Serial']
                        self.set_redfish_cache(
                            'thernal-ucsm',
                            moids,
                            server_serial,
                            cache_disabled=cache_disabled
                        )

                if server_mo['ManagementMode'] != 'UCSM':
                    if self.redfish_endpoint_settings_handler.is_redfish_endpoint(server_mo['Serial']):
                        server_serial = {}
                        server_serial[server_mo['Moid']] = server_mo['Serial']
                        self.set_redfish_cache(
                            'thermal',
                            moids,
                            server_serial,
                            cache_disabled=cache_disabled
                        )

        duration = int(time.time() * 1000) - start_time
        self.log.debug(
            'compute_info.get_managed_objects',
            'Finished managed objects preparation: %s ms' % (duration)
        )

    def get(self, server_id):
        server = self.rack_handler.get(server_id)
        if server is None:
            server = self.blade_handler.get(server_id)

        if server is None:
            return None

        server_info = self.get_server_info(
            server,
            self.settings
        )

        return server_info

    def print_summary_table(self, server, legend_on=False, title=False):
        if title:
            self.my_output.default(
                'Server Summary',
                underline=True,
                before_newline=True
            )

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

    def print_advisory(self, server):
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

    def print_board(self, server):
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

    def print_boot(self, server, title=False):
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

        if title:
            self.my_output.default(
                'Boot Order',
                underline=True,
                before_newline=True
            )

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

    def print_cpu(self, server, title=False):
        if 'CpuInfo' not in server:
            return

        if title:
            self.my_output.default(
                'CPU [#%s]' % (len(server['CpuInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['CpuInfo']) == 0:
            self.my_output.default('None')
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

    def print_fan(self, server, title=False):
        if 'FanInfo' not in server:
            return

        if title:
            self.my_output.default(
                'Fan [#%s]' % (len(server['FanInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['FanInfo']) == 0:
            self.my_output.default('None')
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

    def print_firmware(self, server, title=False):
        if 'FirmwarewComponents' not in server:
            return

        if title:
            self.my_output.default(
                'Firmware [#%s]' % (len(server['FirmwarewComponents'])),
                underline=True,
                before_newline=True
            )

        if len(server['FirmwarewComponents']) == 0:
            self.my_output.default('None')
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

    def print_gpu(self, server, title=False):
        if title:
            self.my_output.default(
                'GPU [#%s]' % (len(server['GpuInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['GpuInfo']) == 0:
            self.my_output.default('None')
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

    def print_memory(self, server, title=False):
        if 'MemoryInfo' not in server:
            return

        if title:
            self.my_output.default(
                'Memory [#%s]' % (len(server['MemoryInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['MemoryInfo']) == 0:
            self.my_output.default('None')
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

    def print_adapters(self, server, title=False):
        if 'AdaptersInfo' not in server:
            return

        if title:
            self.my_output.default(
                'Network Adapters [#%s]' % (len(server['AdaptersInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['AdaptersInfo']) == 0:
            self.my_output.default('None')
            return

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

    def print_ext_eth(self, server, title=False):
        if 'ExtEthInfo' not in server:
            return

        if title:
            self.my_output.default(
                'External Ethernet (MLOM) [#%s]' % (len(server['ExtEthInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['ExtEthInfo']) == 0:
            self.my_output.default('None')
            return

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

    def print_host_eth(self, server, title=False):
        if 'HostEthInfo' not in server:
            return

        if title:
            self.my_output.default(
                'Host Ethernet [#%s]' % (len(server['HostEthInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['HostEthInfo']) == 0:
            self.my_output.default('None')
            return

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

    def print_host_fc(self, server, title=False):
        if 'HostFcInfo' not in server:
            return

        if title:
            self.my_output.default(
                'Host FC [#%s]' % (len(server['HostFcInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['HostFcInfo']) == 0:
            self.my_output.default('None')
            return

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

    def print_net(self, server, title=False):
        self.print_adapters(server, title=title)
        self.print_ext_eth(server, title=title)
        self.print_host_eth(server, title=title)
        self.print_host_fc(server, title=title)

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

    def print_pci(self, server, title=False):
        if 'PciDevicesInfo' not in server:
            return

        if title:
            self.my_output.default(
                'PCI [#%s]' % (len(server['PciDevicesInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['PciDevicesInfo']) == 0:
            self.my_output.default('None')
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

    def print_psu(self, server, title=False):
        if 'PsuInfo' not in server:
            return

        if title:
            self.my_output.default(
                'PSU [#%s]' % (len(server['PsuInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['PsuInfo']) == 0:
            self.my_output.default('None')
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

    def print_storage_controllers(self, server, title=False):
        if 'StorageControllersInfo' not in server:
            return

        if title:
            self.my_output.default(
                'Storage Controller [#%s]' % (len(server['StorageControllersInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['StorageControllersInfo']) == 0:
            self.my_output.default('None')
            return

        order = [
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
            server['StorageControllersInfo'],
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            table=True
        )

    def print_physical_disks(self, server, title=False):
        if 'PhysicalDisks' not in server:
            return

        if title:
            self.my_output.default(
                'Physical Disk [#%s]' % (len(server['PhysicalDisks'])),
                underline=True,
                before_newline=True
            )

        if len(server['PhysicalDisks']) == 0:
            self.my_output.default('None')
            return

        order = [
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
            server['PhysicalDisks'],
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            table=True
        )

    def print_virtual_drives(self, server, title=False):
        if 'VirtualDisks' not in server:
            return

        if title:
            self.my_output.default(
                'Virtual Drive [#%s]' % (len(server['VirtualDisks'])),
                underline=True,
                before_newline=True
            )

        if len(server['VirtualDisks']) == 0:
            self.my_output.default('None')
            return

        order = [
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
            server['VirtualDisks'],
            order=order,
            headers=headers,
            remove_empty_columns=False,
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

    def print_tpm(self, server, title=False):
        if 'TpmInfo' not in server:
            return

        if title:
            self.my_output.default(
                'Trusted Platform Module [#%s]' % (len(server['TpmInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['TpmInfo']) == 0:
            self.my_output.default('None')
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

    def print_workflows(self, server, workflow_count=10, show_empty_table=False, title=False):
        workflows = server['Workflow']['Last'][:workflow_count]
        if len(workflows) == 0:
            if not show_empty_table:
                return

        if title:
            self.my_output.default(
                'Workflow [#%s]' % (len(workflows)),
                underline=True,
                before_newline=True
            )

        if len(workflows) == 0:
            self.my_output.default('None')
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

    def print(self, server, workflow_count=10, legend_on=False, title=False):
        self.print_summary_table(server, legend_on=legend_on, title=title)
        if server['Type'] == 'Blade':
            self.print_chassis(server)

        self.print_board(server)
        self.print_cpu(server, title=title)
        self.print_gpu(server, title=title)
        self.print_memory(server, title=title)
        self.print_storage_controllers(server, title=title)
        self.print_physical_disks(server, title=title)
        self.print_virtual_drives(server, title=title)
        self.print_pci(server, title=title)
        self.print_net(server, title=title)
        self.print_mac(server, title=title)
        self.print_fan(server, title=title)
        self.print_psu(server, title=title)
        self.print_tpm(server, title=title)

        self.print_firmware(server, title=title)
        self.print_boot(server, title=title)
        self.print_kvm(server)

        self.print_power(server)
        self.print_thermal(server)

        self.print_alarm(server)
        self.print_advisory(server)
        self.print_hcl(server)
        self.print_connector(server)
        self.print_contract(server)
        self.print_license(server)
        self.print_profile(server)
        self.print_workflows(server, workflow_count=workflow_count, title=title)
