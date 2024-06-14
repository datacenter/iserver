from lib import filter_helper
from lib import output_helper
from lib import log_helper


class ComputeBotOutput():
    def __init__(self, log_id=None):
        self.my_output = output_helper.OutputHelper(log_id=log_id)
        self.log_handler = log_helper.Log(log_id=log_id)

    def print_summary_table(self, servers, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'Server Summary [#%s]' % (len(servers)),
                underline=True,
                before_newline=True
            )

        if len(servers) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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

                if len(server['TagT']) == 0:
                    server['TagT'].append('--')

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            servers,
            order,
            headers,
            title='Server'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in servers:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('Server', order, rows)

        return output, html_output

    def print_board(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'BoardInfo' in server:
                item = server['BoardInfo']
                if '__show' in item and not item['__show']:
                        continue

                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.my_print(
                'Motherboard Hardware Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Board'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('Board', order, rows)

        return output, html_output

    def print_cpu(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'CpuInfo' in server:
                for item in server['CpuInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'CPU [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='CPU'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('CPU', order, rows)

        return output, html_output

    def print_gpu(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'GpuInfo' in server:
                for item in server['GpuInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'GPU [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'ServerName',
            'Model',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'FirmwareVersion'
        ]

        headers = [
            'Server',
            'GPU Device Model',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'Firmware'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='GPU'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('GPU', order, rows)

        return output, html_output

    def print_memory(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'MemoryInfo' in server:
                for item in server['MemoryInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Memory [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Memory'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('Memory', order, rows)

        return output, html_output

    def print_cimc(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'CimcInfo' in server:
                for item in server['CimcInfo']:
                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'IMC [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        for item in info:
            if len(item['FabricDomain']) == 0:
                item['Fabric'] = '--'
            else:
                item['Fabric'] = '%s:%s %s (%s)' % (
                    item['FabricDomain'],
                    item['FabricDevice'],
                    item['FabricInterface'],
                    item['FabricSource']
                )

        order = [
            'ServerName',
            'IpAddress',
            'Mask',
            'Gateway',
            'MacAddress',
            'Fabric'
        ]

        headers = [
            'Server',
            'IP',
            'Mask',
            'Gateway',
            'MAC',
            'Fabric'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='IMC'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('IMC', order, rows)

        return output, html_output

    def print_adapters(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'AdaptersInfo' in server:
                for item in server['AdaptersInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Network Adapters [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Network Adapters'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('NetworkAdapter', order, rows)

        return output, html_output

    def print_ext_eth(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'ExtEthInfo' in server:
                for item in server['ExtEthInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'External Ethernet (MLOM) [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        for item in info:
            if len(item['FabricDomain']) == 0:
                item['Fabric'] = '--'
            else:
                item['Fabric'] = '%s:%s %s (%s)' % (
                    item['FabricDomain'],
                    item['FabricDevice'],
                    item['FabricInterface'],
                    item['FabricSource']
                )

        order = [
            'ServerName',
            'InterfaceId',
            'MacAddress',
            'Fabric'
        ]

        headers = [
            'Server',
            'Interface ID',
            'MAC Address',
            'Fabric'
        ]

        self.my_output.my_table(
            server['ExtEthInfo'],
            order=order,
            headers=headers,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='External Ethernet (MLOM)'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('MLOM', order, rows)

        return output, html_output

    def print_host_eth(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'HostEthInfo' in server:
                for item in server['HostEthInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Host Ethernet [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        for item in info:
            if len(item['FabricDomain']) == 0:
                item['Fabric'] = '--'
            else:
                item['Fabric'] = '%s:%s %s (%s)' % (
                    item['FabricDomain'],
                    item['FabricDevice'],
                    item['FabricInterface'],
                    item['FabricSource']
                )

        order = [
            'ServerName',
            'AdapterName',
            'Name',
            'MacAddress',
            'Fabric'
        ]

        headers = [
            'Server',
            'Adapter Name',
            'Interface Name',
            'MAC Address',
            'Fabric'
        ]
        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Host Ethernet'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('HostEthernet', order, rows)

        return output, html_output

    def print_host_fc(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'HostFcInfo' in server:
                for item in server['HostFcInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Host FC [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Host FC'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('HostFC', order, rows)

        return output, html_output

    def print_storage_controllers(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'StorageControllerInfo' in server:
                for item in server['StorageControllerInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Storage Controller [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        for item in info:
            item['ModelT'] = filter_helper.get_string_chunks(
                item['Model'],
                30
            )

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
            row_separator=True,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Storage Controller'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('StorageController', order, rows)

        return output, html_output

    def print_physical_disks_state(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'PhysicalDiskInfo' in server:
                for item in server['PhysicalDiskInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Physical Disk - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'ServerName',
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

        headers = [
            'Server',
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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        order = [
            'ServerName',
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
            'Presence',
            'Pid',
            'Model',
            'Vendor',
            'Serial'
        ]

        headers = [
            'Server',
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
            'Presence',
            'Pid',
            'Model',
            'Vendor',
            'Serial'
        ]

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Physical Disk'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('PhysicalDisk', order, rows)

        return output, html_output

    def print_physical_disks_inventory(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'PhysicalDiskInfo' in server:
                for item in server['PhysicalDiskInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Physical Disk - Inventory [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'ServerName',
            'DiskId',
            'Pid',
            'Model',
            'Vendor',
            'Serial'
        ]

        headers = [
            'Server',
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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        return output, None

    def print_virtual_drives(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'VirtualDisks' in server:
                for item in server['VirtualDisks']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Virtual Drive [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Virtual Drive'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('VirtualDrive', order, rows)

        return output, html_output

    def print_tpm(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'TpmInfo' in server:
                for item in server['TpmInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Trusted Platform Module (TPM) [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Trusted Platform Module (TPM)'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('TPM', order, rows)

        return output, html_output

    def print_pci(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'PciDevicesInfo' in server:
                for item in server['PciDevicesInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'PCI [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='PCI'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('PCI', order, rows)

        return output, html_output

    def print_fan_module(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'FanModuleInfo' in server:
                for item in server['FanModuleInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Fan Module [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Fan Module'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('FanModule', order, rows)

        return output, html_output

    def print_fan(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'FanInfo' in server:
                for item in server['FanInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Fan [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            'Presence'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Fan'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('Fan', order, rows)

        return output, html_output

    def print_psu(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'PsuInfo' in server:
                for item in server['PsuInfo']:
                    if '__show' in item and not item['__show']:
                        continue

                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'PSU [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'ServerName',
            'Name',
            'StateTick',
            'PresenceTick',
            'Voltage',
            'Model',
            'Serial',
            'Vendor'
        ]

        headers = [
            'Server',
            'Name',
            'State',
            'Present',
            'Voltage',
            'Model',
            'Serial',
            'Vendor'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='PSU'
        )

        html_output = self.my_output.get_output()

        rows = []
        for server in info:
            row = []
            for key in order:
                row.append(server[key])
            rows.append(row)

        self.log_handler.bot_csv('PSU', order, rows)

        return output, html_output

    def print_boot(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'BootInfo' in server:
                item = server['BootInfo']
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.my_print(
                'Boot [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Boot'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_connector(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'ConnectorInfo' in server:
                item = server['ConnectorInfo']
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.my_print(
                'Connector [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Connector'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_contract(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'ContractInfo' in server:
                item = server['ContractInfo']
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.my_print(
                'Contract [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Contract'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_firmware(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'FirmwarewComponents' in server:
                for item in server['FirmwarewComponents']:
                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Firmware [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'ServerName',
            'Name',
            'Component',
            'Type',
            'PackageVersion',
            'Version'
        ]

        headers = [
            'Server',
            'Name',
            'Component',
            'Type',
            'PackageVersion',
            'Version'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Firmware'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_hcl_summary(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'HclInfo' in server:
                item = server['HclInfo']
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.my_print(
                'HCL Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='HCL Summary'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_hcl_hardware(self, servers, title=False):
        self.my_output.clear_output()
        info = []
        for server in servers:
            if 'HclInfo' in server:
                item = server['HclInfo']
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.my_print(
                'HCL Server Hardware Compliance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='HCL Server Hardware Compliance'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_hcl_software(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'HclInfo' in server:
                item = server['HclInfo']
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.my_print(
                'HCL Server Software Compliance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='HCL Server Software Compliance'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_hcl_component(self, servers, title=False):
        self.my_output.clear_output()
        info = []
        for server in servers:
            if 'HclInfo' in server:
                item = server['HclInfo']
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.my_print(
                'HCL Server Adapter Compliance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            row_separator=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='HCL Server Adapter Compliance'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_kvm(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'KvmInfo' in server:
                item = server['KvmInfo']
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.my_print(
                'KVM [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='KVM'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_license(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'LicenseInfo' in server:
                item = server['LicenseInfo']
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.my_print(
                'License [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'Name',
            'Tier'
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
            allow_order_subkeys=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='License'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_power_consumption(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'Power' in server and server['Power'] is not None:
                item = server['Power']['Data']['PowerControl']
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.my_print(
                'Power Consumption [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Power Consumption'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_power_voltage(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'Power' in server and server['Power'] is not None:
                for item in server['Power']['Data']['Voltage']:
                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Power Sensor [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Power Sensor'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_power_supply(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'Power' in server and server['Power'] is not None:
                for item in server['Power']['Data']['PowerSupply']:
                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Power Supply [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Power Supply'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_profile(self, servers, title=False):
        self.my_output.clear_output()

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
            self.my_output.my_print(
                'Profile [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            row_separator=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Profile'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_thermal_summary(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'Thermal' in server:
                item = server['Thermal']['Summary']
                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if title:
            self.my_output.my_print(
                'Thermal Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Thermal Summary'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_thermal_sensor(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'Thermal' in server:
                for item in server['Thermal']['Data']['Temperature']:
                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Thermal Sensor [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Thermal Sensor'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_thermal_fan(self, servers, title=False):
        self.my_output.clear_output()

        info = []
        for server in servers:
            if 'Thermal' in server:
                for item in server['Thermal']['Data']['Fan']:
                    item['ServerName'] = server['Name']
                    info.append(
                        item
                    )

        if title:
            self.my_output.my_print(
                'Thermal Fan [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

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
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Thermal Fan'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_inventory_rack(self, server_info, title=False):
        self.my_output.clear_output()

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
        self.my_output.clear_output()

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
        self.my_output.clear_output()

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
        self.my_output.clear_output()

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

    def print_advisory(self, servers, title=False):
        self.my_output.clear_output()

        advisories = {}
        for server in servers:
            for server_advisory in server['AdvisoryInfo']:
                if server_advisory['Name'] not in advisories:
                    advisories[server_advisory['Name']] = server_advisory
                    advisories[server_advisory['Name']]['Server'] = []

                advisories[server_advisory['Name']]['Server'].append(
                    server['Name']
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
            item['Server'] = sorted(
                item['Server'],
                key=lambda i: i.lower()
            )
            info.append(
                item
            )

        if title:
            self.my_output.my_print(
                'Advisory [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'Server',
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
                ['Server', 'DescriptionT', 'NameT', 'CveIds']
            ),
            order=order,
            headers=headers,
            remove_empty_columns=True,
            allow_order_subkeys=True,
            row_separator=True,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Thermal Fan'
        )

        html_output = self.my_output.get_output()

        return output, html_output

        # if len(info) > 0:
        #     if title:
        #         self.my_output.default(
        #             'Advisory Url [#%s]' % (len(info)),
        #             underline=True,
        #             before_newline=True
        #         )

        #     order = [
        #         'Server',
        #         'NameT',
        #         'Urls'
        #     ]

        #     headers = [
        #         'Server',
        #         'Name',
        #         'Urls'
        #     ]

        #     self.my_output.my_table(
        #         self.my_output.expand_lists(
        #             info,
        #             order,
        #             ['Server', 'NameT', 'Urls']
        #         ),
        #         order=order,
        #         headers=headers,
        #         remove_empty_columns=True,
        #         allow_order_subkeys=True,
        #         row_separator=True,
        #         underline=True,
        #         table=True
        #     )

    def print_tag(self, servers, title=False):
        self.my_output.clear_output()

        if title:
            self.my_output.my_print(
                'Server Tags',
                underline=True,
                before_newline=True
            )

        if len(servers) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        tags = {}
        for server in servers:
            for tag in server['Tags']:
                if tag['Key'] == 'Intersight.LicenseTier':
                    continue

                tag_kv = '%s:%s' % (
                    tag['Key'],
                    tag['Value']
                )

                if tag_kv not in tags:
                    tags[tag_kv] = {}
                    tags[tag_kv]['count'] = 0
                    tags[tag_kv]['server'] = []

                tags[tag_kv]['count'] = tags[tag_kv]['count'] + 1
                tags[tag_kv]['server'].append(server['Name'])

        info = []
        for tag in tags:
            item = {}
            item['tag'] = tag
            item['count'] = tags[tag]['count']
            info.append(item)

        info = sorted(
            info,
            key=lambda i: i['tag']
        )

        order = [
            'tag',
            'count'
        ]

        headers = [
            'Tag',
            'Count'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=False,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Server Tags'
        )

        html_output = self.my_output.get_output()

        return output, html_output

    def print_alarm(self, alarms, title=False):
        self.my_output.clear_output()

        info = []
        for alarm in alarms:
            alarm['DescriptionT'] = filter_helper.get_string_chunks(
                alarm['Description'],
                40,
                separator=' '
            )
            alarm['AffectedTypeT'] = alarm['AffectedType'].split('.')
            alarm['AffectedNameT'] = alarm['AffectedName'].split('/')
            alarm['NameCodeT'] = []
            alarm['NameCodeT'].append(alarm['Name'])
            if alarm['Name'] != alarm['Code']:
                alarm['NameCodeT'].append('Code: %s' % (alarm['Code']))

            alarm['TimeT'] = []
            alarm['TimeT'].append('(C) %s' % (alarm['CreateTime']))
            alarm['TimeT'].append('(U) %s' % (alarm['LastTransitionTime']))

            info.append(
                alarm
            )

        if title:
            self.my_output.my_print(
                'Alarm [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.my_print('None')
            return self.my_output.get_output(), None

        order = [
            'Severity',
            'AffectedTypeT',
            'AffectedNameT',
            'TimeT',
            'NameCodeT',
            'DescriptionT'
        ]

        headers = [
            'Severity',
            'Affected Type',
            'Affected Name',
            'When',
            'Alarm',
            'Description'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['AffectedTypeT', 'DescriptionT', 'AffectedNameT', 'NameCodeT', 'TimeT']
            ),
            order=order,
            headers=headers,
            remove_empty_columns=False,
            allow_order_subkeys=True,
            row_separator=True,
            underline=True,
            table=True,
            stream='output'
        )

        output = self.my_output.get_output()

        self.my_output.clear_output()

        self.my_output.my_table_html(
            info,
            order,
            headers,
            title='Alarm'
        )

        html_output = self.my_output.get_output()

        return output, html_output
