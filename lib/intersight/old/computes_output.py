from lib import output_helper
from lib.redfish import endpoint_settings as redfish_endpoint_settings


class ComputeOutput():
    def __init__(self, log_id=None):
        self.my_output = output_helper.OutputHelper(log_id=log_id)
        self.redfish_endpoint_settings_handler = redfish_endpoint_settings.RedfishEndpointSettings(
            log_id=log_id
        )

    def print(self, servers, state_enabled=True, legend_on=True, force_base_output=False):
        if self.settings['mac']:
            self.print_mac(
                servers,
                state_enabled=state_enabled,
                legend_on=legend_on
            )
            return

        servers = sorted(servers, key=lambda i: i['Name'])

        if force_base_output:
            order = [
                'Name',
                'Model',
                'Serial',
                'ManagementIp'
            ]

            headers = [
                'Name',
                'Model',
                'Serial',
                'IP'
            ]

        if not force_base_output:
            if state_enabled:
                order = [
                    'FlagState',
                    'FlagManagement',
                    'FlagWorkflow',
                    'Name',
                    'TypeModel',
                    'Serial',
                    'ManagementIp',
                    'Cpu',
                    'TotalMemoryUnit'
                ]

                try:
                    wf_header = 'WF (%sd)' % (servers[0]['Workflow']['Days'])
                except BaseException:
                    wf_header = 'WF (0d)'

                headers = [
                    'SF',
                    'MF',
                    wf_header,
                    'Name',
                    'Model',
                    'Serial',
                    'IP',
                    'CPU',
                    'Memory'
                ]
            else:
                order = [
                    'Name',
                    'TypeModel',
                    'Serial',
                    'ManagementIp',
                    'Cpu',
                    'TotalMemoryUnit'
                ]

                headers = [
                    'Name',
                    'Model',
                    'Serial',
                    'IP',
                    'CPU',
                    'Memory'
                ]

            # Extra columns based on settings

            if self.settings['id']:
                order.append('Moid')
                headers.append('Moid')

            if self.settings['fw']:
                order.append('FirmwareVersion')
                headers.append('Fw')

            if self.settings['pci']:
                order.append('PciModel')
                headers.append('PCI')

            if self.settings['fan']:
                order.append('FanSummary')
                headers.append('Fan')

            if self.settings['psu']:
                order.append('PsuSummary')
                headers.append('Psu')

            if self.settings['group']:
                order.append('Groups')
                headers.append('Groups')

            if self.settings['storage']:
                order.append('StorageDrives')
                headers.append('Storage Drives')
                order.append('StorageCapacity')
                headers.append('Storage Capacity')

            # PCI output requires special handling for multi-line support

            if self.settings['pci']:
                pci_servers = []
                for server in servers:
                    if self.settings['pci']:
                        if len(server['PciModels']) == 0:
                            server['PciModel'] = ''
                            pci_servers.append(server)
                            continue

                        if len(server['PciModels']) == 1:
                            server['PciModel'] = server['PciModels'][0]
                            pci_servers.append(server)
                            continue

                        if len(server['PciModels']) > 1:
                            pci_index = 1
                            for pci_model in server['PciModels']:
                                if pci_index == 1:
                                    new_server = copy.deepcopy(server)
                                    new_server['PciModel'] = pci_model
                                else:
                                    new_server = copy.deepcopy(server)
                                    for displayed_field in order:
                                        new_server[displayed_field] = ''
                                    new_server['PciModel'] = pci_model
                                pci_servers.append(new_server)
                                pci_index = pci_index + 1

                            continue

                    pci_servers.append(server)

                servers = copy.deepcopy(pci_servers)

            if self.settings['power']:
                if 'Cpu' in order:
                    order.remove('Cpu')
                if 'TotalMemoryUnit' in order:
                    order.remove('TotalMemoryUnit')
                if 'CPU' in headers:
                    headers.remove('CPU')
                if 'Memory' in headers:
                    headers.remove('Memory')

                order.append('Power.Summary.PowerNow')
                headers.append('Consumed [W]')
                order.append('Power.Summary.PowerMin')
                headers.append('Min [W]')
                order.append('Power.Summary.PowerAvg')
                headers.append('Avg [W]')
                order.append('Power.Summary.PowerMax')
                headers.append('Max [W]')

            if self.settings['thermal']:
                if 'Cpu' in order:
                    order.remove('Cpu')
                if 'TotalMemoryUnit' in order:
                    order.remove('TotalMemoryUnit')
                if 'CPU' in headers:
                    headers.remove('CPU')
                if 'Memory' in headers:
                    headers.remove('Memory')

                order.append('Thermal.Summary.FanHealth')
                headers.append('Fans')
                order.append('Thermal.Summary.SensorHealth')
                headers.append('Sensors')
                order.append('Thermal.Summary.HighestTemperature')
                headers.append('Highest (C)')
                order.append('Thermal.Summary.SmallestGap')
                headers.append('Min Gap (C)')
                order.append('Thermal.Summary.OverThreshold')
                headers.append('Over Threshold')

            if self.settings['contract']:
                order.append('ContractInfo.ContractStatus')
                headers.append('Contract Status')
                order.append('ContractInfo.ContractNumber')
                headers.append('Contract Number')
                for server in servers:
                    for key in server['ContractInfo']['__Output']:
                        server['__Output']['ContractInfo.%s' % (key)] = server['ContractInfo']['__Output'][key]

        # Print servers table

        self.my_output.my_table(
            servers,
            order=order,
            allow_order_subkeys=True,
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

    def print_mac(self, servers, state_enabled=True, legend_on=True):
        servers = sorted(servers, key=lambda i: i['Name'])

        order = [
            'FlagState',
            'Name',
            'ManagementIp',
            'MacAddressInfo.MacAddress',
            'MacAddressInfo.InterfaceName',
            'MacAddressInfo.AdapterModel',
            'MacAddressInfo.AdapterPciSlot'
        ]

        headers = [
            'SF',
            'Name',
            'IP',
            'MAC Address',
            'Interface',
            'Adapter',
            'Pci Slot'
        ]

        if not state_enabled:
            order.remove('FlagState')
            headers.remove('SF')

        self.my_output.my_table(
            self.my_output.expand_lists(
                servers,
                order,
                ['MacAddressInfo']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            table=True,
            row_separator=True
        )

    def print_power(self, servers):
        servers = sorted(servers, key=lambda i: i['Name'])

        order = [
            'PowerSource',
            'Name',
            'Model',
            'ManagementIp',
            'Serial',
            'OperPowerState',
            'PowerConsumedWatts',
            'PowerMinConsumedWatts',
            'PowerAvgConsumedWatts',
            'PowerMaxConsumedWatts'
        ]

        headers = [
            'Source',
            'Name',
            'Model',
            'IP',
            'Serial',
            'Power State',
            'Consumed [W]',
            'Min [W]',
            'Avg [W]',
            'Max [W]'
        ]

        self.my_output.my_table(
            servers,
            order=order,
            headers=headers,
            table=True
        )

    def print_thermal(self, servers):
        servers = sorted(servers, key=lambda i: i['Name'])

        order = [
            'ThermalSource',
            'Name',
            'Model',
            'ManagementIp',
            'Serial',
            'OperPowerState',
            'ThermalFanHealth',
            'ThermalSensorHealth',
            'ThermalHighestTemperature',
            'ThermalSmallestGap',
            'ThermalOverThreshold'
        ]

        headers = [
            'Source',
            'Name',
            'Model',
            'IP',
            'Serial',
            'Power State',
            'Fans Healthy',
            'Sensors Healthy',
            'Highest (C)',
            'Smallest Gap (C)',
            'Over Threshold'
        ]

        self.my_output.my_table(
            servers,
            order=order,
            headers=headers,
            table=True
        )

    def print_influx(self, servers):
        for server in servers:
            if server['Power'] is None:
                continue

            measurement = 'ipower'

            server_tags = [
                'Moid',
                'Model',
                'Serial',
                'Name'
            ]
            server_info = ''
            for server_tag in server_tags:
                server_info = '%s%s=%s,' % (
                    server_info,
                    server_tag.lower(),
                    server[server_tag]
                )
            server_info = server_info.rstrip(',')

            power_tags = [
                'PowerNow',
                'PowerMin',
                'PowerAvg',
                'PowerMax'
            ]
            power_fields = ''
            for power_tag in power_tags:
                power_fields = '%s%s=%s,' % (
                    power_fields,
                    power_tag.lower(),
                    server['Power']['Summary'][power_tag]
                )
            power_fields = power_fields.rstrip(',')

            timestamp = int(time.time() * 1000000000)

            influx_line = '%s,%s %s %s' % (
                measurement,
                server_info,
                power_fields,
                timestamp
            )

            self.my_output.default(
                influx_line
            )

    def get_storage_controller_summary(self, servers):
        summary = {}
        summary['servers'] = len(servers)
        summary['servers_with_sc'] = 0
        summary['servers_without_sc'] = 0
        summary['sc'] = 0
        summary['equipped'] = 0
        summary['vendor'] = {}

        for server in servers:
            if len(server['StorageControllersInfo']) == 0:
                summary['servers_without_sc'] = summary['servers_without_sc'] + 1
            else:
                summary['servers_with_sc'] = summary['servers_with_sc'] + 1

            summary['sc'] = summary['sc'] + len(server['StorageControllersInfo'])
            for controller in server['StorageControllersInfo']:
                if controller['Presence'] == 'equipped':
                    summary['equipped'] = summary['equipped'] + 1

                if controller['Vendor'] not in summary['vendor']:
                    summary['vendor'][controller['Vendor']] = 0

                summary['vendor'][controller['Vendor']] = summary['vendor'][controller['Vendor']] + 1

        return summary

    def print_storage_controller(self, servers, title=False):
        if title:
            self.my_output.default(
                'Storage Controller',
                underline=True,
                before_newline=True
            )

        servers = sorted(servers, key=lambda i: i['Name'])

        order = [
            'Name',
            'StorageControllersInfo.ControllerId',
            'StorageControllersInfo.Model',
            'StorageControllersInfo.Vendor',
            'StorageControllersInfo.Serial',
            'StorageControllersInfo.Presence',
            'StorageControllersInfo.PciSlot',
            'StorageControllersInfo.RaidSupport',
            'StorageControllersInfo.PhysicalDiskCount',
            'StorageControllersInfo.VirtualDriveCount'
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
            self.my_output.expand_lists(
                servers,
                order,
                ['StorageControllersInfo']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_storage_physical_disk(self, servers, title=False):
        if title:
            self.my_output.default(
                'Physical Disk',
                underline=True,
                before_newline=True
            )

        servers = sorted(servers, key=lambda i: i['Name'])

        order = [
            'Name',
            'PhysicalDisks.StateTick',
            'PhysicalDisks.StorageControllerId',
            'PhysicalDisks.DiskId',
            'PhysicalDisks.VirtualDriveId',
            'PhysicalDisks.SizeUnit',
            'PhysicalDisks.Type',
            'PhysicalDisks.Protocol',
            'PhysicalDisks.BootableTick',
            'PhysicalDisks.LinkSpeed',
            'PhysicalDisks.Pid',
            'PhysicalDisks.Model',
            'PhysicalDisks.Vendor',
            'PhysicalDisks.DriveFirmware',
            'PhysicalDisks.Serial',
            'PhysicalDisks.DiskState',
            'PhysicalDisks.Presence'
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
            self.my_output.expand_lists(
                servers,
                order,
                ['PhysicalDisks']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_storage_virtual_drive(self, servers, title=False):
        if title:
            self.my_output.default(
                'Virtual Drive',
                underline=True,
                before_newline=True
            )

        servers = sorted(servers, key=lambda i: i['Name'])

        order = [
            'Name',
            'VirtualDisks.StateTick',
            'VirtualDisks.StorageControllerId',
            'VirtualDisks.VirtualDriveId',
            'VirtualDisks.SizeUnit',
            'VirtualDisks.PhysicalDiskCount',
            'VirtualDisks.Type',
            'VirtualDisks.Name',
            'VirtualDisks.BootableTick',
            'VirtualDisks.ActualWriteCachePolicy',
            'VirtualDisks.DriveState'
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
            'State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                servers,
                order,
                ['VirtualDisks']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )
