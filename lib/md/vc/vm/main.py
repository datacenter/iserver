from lib import ip_helper
from lib.md.vc.vm.nic.main import MdVcVmNicOutput


class MdVcVmOutput(MdVcVmNicOutput):
    def __init__(self):
        MdVcVmNicOutput.__init__(self)

    def print_vc_vm(self, vm):
        self.print_page_header('vCenter - Virtual Machine')

        self.my_output.print_stream('## Virtual Machine', 'output')
        self.my_output.print_stream('- Name: %s' % (vm['name']), 'output')
        self.my_output.print_stream('- VM UUID: %s' % (vm['uuid']), 'output')
        self.my_output.print_stream('- Connection state: %s' % (vm['connectionState']), 'output')
        self.my_output.print_stream('- Power state: %s' % (vm['powerState']), 'output')
        if vm['up']:
            self.my_output.print_stream('- Up :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Up :x:', 'output')

        self.my_output.print_stream('- Guest: %s' % (vm['guestFullName']), 'output')
        if vm['annotation'] is not None and len(vm['annotation']) > 0:
            self.my_output.print_stream('- Annotation: %s' % (vm['annotation']), 'output')
        self.my_output.print_stream('- VM Path: %s' % (vm['vmPathName']), 'output')

        self.my_output.print_stream('\nLocation', 'output')
        self.my_output.print_stream('- vCenter: [%s](../%s-vm.md)' % (vm['vcenter'], vm['vcenter']), 'output')
        self.my_output.print_stream('- Cluster: [%s](./%s.md)' % (vm['clusterName'], vm['cluster_hash']), 'output')
        self.my_output.print_stream('- Host: [%s](./%s.md)' % (vm['host'], vm['host_hash']), 'output')

        if vm['cpu'] is not None:
            self.my_output.print_stream('## CPU', 'output')
            self.my_output.print_stream('- Count: %s' % (vm['cpu']['count']), 'output')
            self.my_output.print_stream('- Reservation: %s' % (vm['cpu']['reservation']), 'output')
            self.my_output.print_stream('- Usage: %s' % (vm['cpuUsageUnit']), 'output')

        if vm['memory'] is not None:
            self.my_output.print_stream('## Memory', 'output')
            self.my_output.print_stream('- Size: %s' % (vm['memory']['memoryUnit']), 'output')
            self.my_output.print_stream('- Reservation: %s' % (vm['memory']['reservation']), 'output')
            self.my_output.print_stream('- Usage: %s' % (vm['guestMemoryUsagePct']), 'output')

        self.my_output.print_stream('## Network', 'output')
        order = [
            'NIC Label',
            'Type',
            'MAC',
            'Network',
            'VLAN',
            'vSwitch',
            'Uplink'
        ]
        self.print_table_header(order)

        for nic in vm['nic']:
            line = ''
            line = self.add_column(line, nic['label'])
            line = self.add_column(line, nic['type'])
            line = self.add_column(line, nic['macAddress'])
            line = self.add_column(line, nic['networkName'])
            if 'vmware' not in nic['fabric']:
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
            else:
                if 'vlans' not in nic['fabric']['vmware'] or len(nic['fabric']['vmware']['vlans']) == 0:
                    line = self.add_column(line, '---')
                else:
                    line = self.add_column(line, ','.join(nic['fabric']['vmware']['vlans']))

                devices = []
                if 'pnic' in nic['fabric']['vmware']:
                    for pnic in nic['fabric']['vmware']['pnic']:
                        devices.append(
                            pnic['device']
                        )

                if 'vswitchName' in nic['fabric']['vmware']:
                    line = self.add_column(
                        line,
                        nic['fabric']['vmware']['vswitchName']
                    )
                else:
                    line = self.add_column(line, '---')

                if len(devices) == 0:
                    line = self.add_column(line, '---')
                else:
                    line = self.add_column(line, ', '.join(devices))

            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

        order = [
            'NIC Label',
            'Uplink',
            'Discovered',
            'Fabric',
            'Switch',
            'Interface',
            'Connectivity Details'
        ]
        self.print_table_header(order)

        for nic in vm['nic']:
            if not nic['fabric']['collected'] or len(nic['fabric']['links']) == 0:
                line = ''
                line = self.add_column(line, nic['label'])
                line = self.add_column(line, '---')
                line = self.add_column(line, ':x:')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(
                    line,
                    '[Link](../nic/%s.md)' % (nic['hash'])
                )
                self.my_output.print_stream(line, 'output')
                continue

            for pnic in nic['fabric']['vmware']['pnic']:
                for adapter in nic['fabric']['server']['adapter']:
                    if ip_helper.is_mac_equal(pnic['mac'], adapter['MacAddress']):
                        for vlan_id in adapter['vlan']:
                            for ep in adapter['vlan'][vlan_id]['ep']:
                                line = ''
                                line = self.add_column(line, nic['label'])
                                line = self.add_column(line, pnic['device'])
                                line = self.add_column(line, ':white_check_mark:')
                                line = self.add_column(line, ep['fabric_type'])
                                line = self.add_column(line, ep['fabric_switch'])
                                line = self.add_column(line, ep['fabric_interface'])
                                line = self.add_column(
                                    line,
                                    '[Link](../nic/%s.md)' % (nic['hash'])
                                )
                                self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

        self.my_output.print_stream('## Storage', 'output')
        self.my_output.print_stream('- Provisioned: %s' % (vm['provisionedStorageUnit']), 'output')
        self.my_output.print_stream('- Used: %s [%s]' % (vm['usedStorageUnit'], vm['usedStoragePct']), 'output')
        if len(vm['disk']) > 0:
            self.my_output.print_stream('- Disk backing filename', 'output')
            for disk in vm['disk']:
                self.my_output.print_stream(
                    '\t- [%s] %s' % (
                        disk['label'],
                        disk['backingFilename']
                    ),
                    'output'
                )

        self.my_output.print_stream('', 'output')

        order = [
            'Disk Label',
            'Thin',
            'Disk Capacity',
            'Datastore',
            'DS Capacity',
            'DS Usage'
        ]
        self.print_table_header(order)

        for disk in vm['disk']:
            line = ''
            line = self.add_column(line, disk['label'])
            line = self.add_column_tick_bool(line, disk['thin'])
            line = self.add_column(line, disk['capacityUnit'])
            if disk['backingDatastore'] is None:
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, disk['backingDatastore']['name'])
                line = self.add_column(line, disk['backingDatastore']['capacity_unit'])
                line = self.add_column(line, disk['backingDatastore']['usage_unit'])
            self.my_output.print_stream(line, 'output')

        self.save_output(vm['hash'], subdir='vc/vm')

        for nic in vm['nic']:
            self.print_vc_vm_nic(
                vm,
                nic
            )

    def print_vc_host_vms(self, host, hosts):
        self.print_vc_host_page_header(
            'Virtual Machine',
            host,
            hosts
        )

        up = 0
        for vm in host['vm']:
            if vm['up']:
                up += 1

        self.my_output.print_stream(
            '## Up [%s/%s]\n' % (
                up,
                len(host['vm'])
            ),
            'output'
        )

        order = [
            'VM',
            'Up',
            'CPU',
            'Used',
            'Mem',
            'Used',
            'Disk',
            'Used',
            'NIC'
        ]
        self.print_table_header(order)

        for vm in host['vm']:
            if vm['up']:
                line = ''
                line = self.add_vc_host_link(line, 'vm', vm, up=True)
                if vm['up']:
                    line = self.add_column(line, ':white_check_mark:')
                else:
                    line = self.add_column(line, ':x:')
                line = self.add_column(line, vm['cpu']['count'])
                line = self.add_column(line, vm['cpuUsageUnit'])
                line = self.add_column(line, vm['memory']['memoryUnit'])
                line = self.add_column(line, vm['guestMemoryUsagePct'])
                line = self.add_column(line, vm['provisionedStorageUnit'])
                line = self.add_column(line, vm['usedStoragePct'])
                line = self.add_column(line, vm['numEthernetCards'])

                self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '## All [%s]\n' % (
                len(host['vm'])
            ),
            'output'
        )

        order = [
            'VM',
            'Up',
            'CPU',
            'Used',
            'Mem',
            'Used',
            'Disk',
            'Used',
            'NIC'
        ]
        self.print_table_header(order)

        for vm in host['vm']:
            line = ''
            line = self.add_vc_host_link(line, 'vm', vm, up=True)
            line = self.add_column_tick_bool(line, vm['up'])
            line = self.add_column(line, vm['cpu']['count'])
            line = self.add_column(line, vm['cpuUsageUnit'])
            line = self.add_column(line, vm['memory']['memoryUnit'])
            line = self.add_column(line, vm['guestMemoryUsagePct'])
            line = self.add_column(line, vm['provisionedStorageUnit'])
            line = self.add_column(line, vm['usedStoragePct'])
            line = self.add_column(line, vm['numEthernetCards'])

            self.vc_vm_count[host['vcenter']][host['name']] += 1
            if vm['up']:
                self.vc_vm_up_count[host['vcenter']][host['name']] += 1

            self.my_output.print_stream(line, 'output')

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(host['vm'], indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(host['hash'], subdir='vc/vm')

    def print_vc_cluster_vms(self, cluster, clusters, hosts):
        self.print_vc_cluster_page_header(
            'Virtual Machine',
            cluster,
            clusters
        )

        up = 0
        total = 0
        for host in hosts:
            if host['name'] in cluster['hosts']:
                for vm in host['vm']:
                    total += 1
                    if vm['up']:
                        up += 1

        self.my_output.print_stream(
            '## Up [%s/%s]\n' % (
                up,
                total
            ),
            'output'
        )

        order = [
            'Host',
            'VM',
            'Up',
            'CPU',
            'Used',
            'Mem',
            'Used',
            'Disk',
            'Used',
            'NIC'
        ]
        self.print_table_header(order)

        for host in hosts:
            if host['name'] not in cluster['hosts']:
                continue

            for vm in host['vm']:
                if not vm['up']:
                    continue

                line = ''
                line = self.add_column(
                    line,
                    '[%s](../vm/%s.md)' % (
                        vm['_host'],
                        vm['host_hash']
                    )
                )
                line = self.add_column(
                    line,
                    '[%s](../vm/%s.md)' % (
                        vm['name'],
                        vm['hash']
                    )
                )
                line = self.add_column_tick_bool(line, vm['up'])
                line = self.add_column(line, vm['cpu']['count'])
                line = self.add_column(line, vm['cpuUsageUnit'])
                line = self.add_column(line, vm['memory']['memoryUnit'])
                line = self.add_column(line, vm['guestMemoryUsagePct'])
                line = self.add_column(line, vm['provisionedStorageUnit'])
                line = self.add_column(line, vm['usedStoragePct'])
                line = self.add_column(line, vm['numEthernetCards'])

                self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '## All [%s]\n' % (
                total
            ),
            'output'
        )

        order = [
            'Host',
            'VM',
            'Up',
            'CPU',
            'Used',
            'Mem',
            'Used',
            'Disk',
            'Used',
            'NIC'
        ]
        self.print_table_header(order)

        for host in hosts:
            if host['name'] not in cluster['hosts']:
                continue

            for vm in host['vm']:
                line = ''
                line = self.add_column(
                    line,
                    '[%s](../vm/%s.md)' % (
                        vm['_host'],
                        vm['host_hash']
                    )
                )
                line = self.add_column(
                    line,
                    '[%s](../vm/%s.md)' % (
                        vm['name'],
                        vm['hash']
                    )
                )
                line = self.add_column_tick_bool(line, vm['up'])
                line = self.add_column(line, vm['cpu']['count'])
                line = self.add_column(line, vm['cpuUsageUnit'])
                line = self.add_column(line, vm['memory']['memoryUnit'])
                line = self.add_column(line, vm['guestMemoryUsagePct'])
                line = self.add_column(line, vm['provisionedStorageUnit'])
                line = self.add_column(line, vm['usedStoragePct'])
                line = self.add_column(line, vm['numEthernetCards'])

                self.vc_vm_count[cluster['vcenter']][cluster['name']] += 1
                if vm['up']:
                    self.vc_vm_up_count[cluster['vcenter']][cluster['name']] += 1

                self.my_output.print_stream(line, 'output')

        self.save_output(cluster['hash'], subdir='vc/vm')

    def print_vc_vms(self, vcenter, info):
        self.print_vc_page_header(
            vcenter,
            'Virtual Machine',
            'vm'
        )

        up = 0
        for vm in info:
            if vm['up']:
                up += 1

        self.my_output.print_stream(
            '## Up [%s/%s]\n' % (
                up,
                len(info)
            ),
            'output'
        )

        order = [
            'VM',
            'Up',
            'CPU',
            'Used',
            'Mem',
            'Used',
            'Disk',
            'Used',
            'NIC'
        ]
        self.print_table_header(order)

        for vm in info:
            if vm['up']:
                line = ''
                line = self.add_column(
                    line,
                    '[%s](./vm/%s.md)' % (
                        vm['name'],
                        vm['hash']
                    )
                )
                line = self.add_column_tick_bool(line, vm['up'])
                line = self.add_column(line, vm['cpu']['count'])
                line = self.add_column(line, vm['cpuUsageUnit'])
                line = self.add_column(line, vm['memory']['memoryUnit'])
                line = self.add_column(line, vm['guestMemoryUsagePct'])
                line = self.add_column(line, vm['provisionedStorageUnit'])
                line = self.add_column(line, vm['usedStoragePct'])
                line = self.add_column(line, vm['numEthernetCards'])

                self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '## All [%s]\n' % (
                len(info)
            ),
            'output'
        )

        order = [
            'VM',
            'Up',
            'CPU',
            'Used',
            'Mem',
            'Used',
            'Disk',
            'Used',
            'NIC'
        ]
        self.print_table_header(order)

        for vm in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./vm/%s.md)' % (
                    vm['name'],
                    vm['hash']
                )
            )
            line = self.add_column_tick_bool(line, vm['up'])
            if vm['cpu'] is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, vm['cpu']['count'])
            line = self.add_column(line, vm['cpuUsageUnit'])
            if vm['memory'] is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, vm['memory']['memoryUnit'])
            line = self.add_column(line, vm['guestMemoryUsagePct'])
            line = self.add_column(line, vm['provisionedStorageUnit'])
            line = self.add_column(line, vm['usedStoragePct'])
            line = self.add_column(line, vm['numEthernetCards'])

            self.my_output.print_stream(line, 'output')

            self.vc_vm_count[vcenter]['__ALL__'] += 1
            if vm['up']:
                self.vc_vm_up_count[vcenter]['__ALL__'] += 1

        self.save_output('%s-vm' % (vcenter), subdir='vc')

        for item in info:
            self.print_vc_vm(
                item
            )
