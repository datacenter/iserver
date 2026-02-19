from lib import ip_helper


class MdComputeInventoryOutput():
    def __init__(self):
        pass

    def print_cpu(self, server):
        info = []

        if 'CpuInfo' in server:
            for item in server['CpuInfo']:
                if '__show' in item and not item['__show']:
                    continue

                if item['Presence'] == 'equipped':
                    info.append(
                        item
                    )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## CPU',
            'output'
        )

        order = [
            'SocketDesignation',
            'Vendor',
            'Architecture',
            'Model',
            'NumCores',
            'NumCoresEnabled',
            'NumThreads',
            'Speed',
            'Stepping',
            'OperState'
        ]

        headers = [
            'Socket',
            'Vendor',
            'Arch',
            'Model',
            'Cores',
            'Enabled',
            'Threads',
            'Speed [GHz]',
            'Stepping',
            'OperState'
        ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_memory(self, server):
        info = []

        if 'MemoryInfo' in server:
            for item in server['MemoryInfo']:
                if '__show' in item and not item['__show']:
                    continue

                if item['Presence'] == 'equipped':
                    info.append(
                        item
                    )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## Memory',
            'output'
        )

        order = [
            'MemoryId',
            'ArrayId',
            'Bank',
            'OperState',
            'Location',
            'CapacityUnit',
            'Clock',
            'FormFactor',
            'Type',
            'Model',
            'Serial'
        ]

        headers = [
            'Id',
            'Array',
            'Bank',
            'Oper',
            'Location',
            'Capacity',
            'Clock',
            'Form Factor',
            'Type',
            'Model',
            'Serial'
        ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_storage_controller(self, server):
        info = []
        if 'StorageControllerInfo' in server:
            for item in server['StorageControllerInfo']:
                if '__show' in item and not item['__show']:
                    continue

                if item['Presence'] == 'equipped':
                    info.append(
                        item
                    )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## Storage Controller',
            'output'
        )

        order = [
            'ControllerId',
            'Model',
            'Vendor',
            'Serial',
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
            'PCI Slot',
            'Raid Support',
            'PD',
            'VD'
        ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_physical_disk(self, server):
        info = []
        if 'PhysicalDiskInfo' in server:
            for item in server['PhysicalDiskInfo']:
                if '__show' in item and not item['__show']:
                    continue

                if item['Presence'] == 'equipped':
                    info.append(
                        item
                    )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## Physical Disk',
            'output'
        )

        for item in info:
            for key in ['DiskState', 'VirtualDriveId', 'DriveFirmware']:
                if item[key] is None or len(item[key]) == 0:
                    item[key] = '--'

        order = [
            'StorageControllerId',
            'DiskId',
            'VirtualDriveId',
            'SizeUnit',
            'Type',
            'Protocol',
            'BootableTick',
            'LinkSpeed',
            'DriveFirmware',
            'DiskState'
        ]

        headers = [
            'Controller',
            'Disk Id',
            'VD',
            'Size',
            'Type',
            'Protocol',
            'Bootable',
            'Link Speed',
            'Fw',
            'State'
        ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

        self.my_output.print_stream(
            '\n',
            'output'
        )

        for item in info:
            for key in ['Pid', 'Model', 'PartNumber', 'Vendor', 'Serial']:
                if key not in item:
                    item[key] = None

                if item[key] is None or len(item[key]) == 0:
                    item[key] = '--'


        order = [
            'StorageControllerId',
            'DiskId',
            'Pid',
            'Model',
            'PartNumber',
            'Vendor',
            'Serial'
        ]

        headers = [
            'Controller',
            'Disk Id',
            'Pid',
            'Model',
            'PN',
            'Vendor',
            'Serial'
        ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_virtual_drive(self, server):
        info = []
        if 'VirtualDisks' in server:
            for item in server['VirtualDisks']:
                if '__show' in item and not item['__show']:
                    continue

                info.append(
                    item
                )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## Virtual Drive',
            'output'
        )

        order = [
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

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_cimc(self, server):
        if 'CimcInfo' in server and len(server['CimcInfo']) > 0:
            self.my_output.print_stream(
                '# IMC',
                'output'
            )

            self.my_output.print_stream(
                '- Address: %s' % (server['CimcInfo'][0]['IpAddress']),
                'output'
            )

            self.my_output.print_stream(
                '- Mask: %s' % (server['CimcInfo'][0]['Mask']),
                'output'
            )

            self.my_output.print_stream(
                '- Gateway: %s' % (server['CimcInfo'][0]['Gateway']),
                'output'
            )

            self.my_output.print_stream(
                '- MacAddress: %s' % (server['CimcInfo'][0]['MacAddress']),
                'output'
            )

    def print_adapter(self, server):
        info = []
        if 'AdaptersInfo' in server:
            for item in server['AdaptersInfo']:
                if '__show' in item and not item['__show']:
                    continue

                item['ServerName'] = server['Name']
                info.append(
                    item
                )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## Network Adapter',
            'output'
        )

        for item in info:
            for key in ['Pid']:
                if key not in item:
                    item[key] = None
                if item[key] is None or len(item[key]) == 0:
                    item[key] = '--'

        if server['Type'] == 'Rack':
            order = [
                'PciSlot',
                'Model',
                'Pid',
                'Serial',
                'Vendor',
                'ExtEthIfsCount',
                'HostEthIfsCount',
                'HostFcIfsCount'
            ]

            headers = [
                'PciSlot',
                'Model',
                'PID',
                'Serial',
                'Vendor',
                'DCE',
                'Eth',
                'HBA'
            ]

        if server['Type'] == 'Blade':
            order = [
                'Name',
                'Model',
                'Pid',
                'Serial',
                'Vendor',
                'ExtEthIfsCount',
                'HostEthIfsCount',
                'HostFcIfsCount'
            ]

            headers = [
                'Name',
                'Model',
                'PID',
                'Serial',
                'Vendor',
                'DCE',
                'Eth',
                'HBA'
            ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_ext_eth(self, server):
        info = []
        if 'ExtEthInfo' in server:
            for item in server['ExtEthInfo']:
                if '__show' in item and not item['__show']:
                    continue

                info.append(
                    item
                )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## External Ethernet (MLOM)',
            'output'
        )

        order = [
            'AdapterModel',
            'InterfaceId',
            'MacAddress'
        ]

        headers = [
            'Adapter Model',
            'Interface ID',
            'MAC Address'
        ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_host_eth(self, server):
        info = []
        if 'HostEthInfo' in server:
            for item in server['HostEthInfo']:
                if '__show' in item and not item['__show']:
                    continue

                info.append(
                    item
                )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## Host Ethernet',
            'output'
        )

        order = [
            'AdapterName',
            'AdapterModel',
            'Name',
            'MacAddress'
        ]

        headers = [
            'Adapter Name',
            'Adapter Model',
            'Interface Name',
            'MAC Address'
        ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_host_fc(self, server):
        info = []
        if 'HostFcInfo' in server:
            for item in server['HostFcInfo']:
                if '__show' in item and not item['__show']:
                    continue

                info.append(
                    item
                )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## Host FC',
            'output'
        )

        order = [
            'AdapterName',
            'AdapterModel',
            'Name',
            'Wwnn',
            'Wwpn'
        ]

        headers = [
            'Adapter Name',
            'Adapter Model',
            'Interface Name',
            'WWNN',
            'WWPN'
        ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_pci(self, server):
        info = []
        if 'PciDevicesInfo' in server:
            for item in server['PciDevicesInfo']:
                if '__show' in item and not item['__show']:
                    continue

                info.append(
                    item
                )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## PCI',
            'output'
        )

        order = [
            'Model',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'FirmwareVersion'
        ]

        headers = [
            'PCI Device Model',
            'Pid',
            'Serial',
            'SlotId',
            'Vendor',
            'Firmware'
        ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_pci_node(self, server):
        info = []
        if 'PciNodesInfo' in server:
            for item in server['PciNodesInfo']:
                if '__show' in item and not item['__show']:
                    continue

                for key in ['ControllerId', 'Model', 'Serial', 'Vendor']:
                    try:
                        item[key] = item['GpuInfo'][key]
                    except BaseException:
                        item[key] = '--'

                info.append(
                    item
                )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## PCI Node',
            'output'
        )

        order = [
            'SlotId',
            'Model',
            'Serial',
            'ControllerId',
            'Model',
            'Serial',
            'Vendor'
        ]

        headers = [
            'Slot',
            'Model',
            'Serial',
            'GPU - Id',
            'GPU - Model',
            'GPU - Serial',
            'GPU - Vendor'
        ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_fan_module(self, server):
        info = []
        if 'FanModuleInfo' in server:
            for item in server['FanModuleInfo']:
                info.append(
                    item
                )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## Fan Module',
            'output'
        )

        order = [
            'Name',
            'OperState',
            'Presence'
        ]

        headers = [
            'Fan Module',
            'OperState',
            'Presence'
        ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_fan(self, server):
        info = []
        if 'FanInfo' in server:
            for item in server['FanInfo']:
                if '__show' in item and not item['__show']:
                    continue

                info.append(
                    item
                )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## Fan',
            'output'
        )

        order = [
            'Name',
            'OperState',
            'Presence'
        ]

        headers = [
            'Fan',
            'OperState',
            'Presence'
        ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_psu(self, server):
        info = []
        if 'PsuInfo' in server:
            for item in server['PsuInfo']:
                if '__show' in item and not item['__show']:
                    continue

                info.append(
                    item
                )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## PSU',
            'output'
        )

        order = [
            'Name',
            'StateTick',
            'PresenceTick',
            'Voltage',
            'Model',
            'Serial',
            'Vendor'
        ]

        headers = [
            'Name',
            'State',
            'Present',
            'Voltage',
            'Model',
            'Serial',
            'Vendor'
        ]

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_tpm(self, server):
        info = []
        if 'TpmInfo' in server:
            for item in server['TpmInfo']:
                info.append(
                    item
                )

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## Trusted Platform Module',
            'output'
        )

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

        self.my_output.my_table_md(
            info,
            order,
            headers,
            stream='output'
        )

    def print_servers_details(self, servers_info):
        for server_info in servers_info:
            self.print_server(server_info, 'Inventory')
            self.print_cpu(server_info)
            self.print_memory(server_info)
            self.print_storage_controller(server_info)
            self.print_physical_disk(server_info)
            self.print_virtual_drive(server_info)
            self.print_cimc(server_info)
            self.print_adapter(server_info)
            self.print_ext_eth(server_info)
            self.print_host_eth(server_info)
            self.print_host_fc(server_info)
            self.print_pci(server_info)
            self.print_pci_node(server_info)
            self.print_fan_module(server_info)
            self.print_fan(server_info)
            self.print_psu(server_info)
            self.print_tpm(server_info)

            self.save_output(
                '%s-inv' % (server_info['Moid']),
                subdir='compute'
            )

            self.print_server(server_info, 'Networking')
            self.add_server_hardware(server_info['Model'], 'rear_view_net', title='Server Rear View')
            self.print_adapter(server_info)
            self.print_net_macs(server_info)

            self.save_output(
                '%s-net' % (server_info['Moid']),
                subdir='compute'
            )
