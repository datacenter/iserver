from lib.vc import helper as vc_helper

class MdVcHostOutput():
    def __init__(self):
        pass

    def add_vc_host_power_state(self, line, item):
        if item['runtime']['powerState'] == 'poweredOn':
            return self.add_column(line, ':white_check_mark:')
        if item['runtime']['powerState'] == 'poweredOn':
            return self.add_column(line, ':x:')
        if item['runtime']['powerState'] == 'unknown':
            return self.add_column(line, ':x:')

        return self.add_column(line, item['runtime']['powerState'])

    def add_vc_host_connection_state(self, line, item):
        if item['runtime']['connectionState'] == 'connected':
            return self.add_column(line, ':white_check_mark:')
        if item['runtime']['connectionState'] == 'notResponding':
            return self.add_column(line, ':x:')

        return self.add_column(line, item['runtime']['connectionState'])

    def print_vc_host(self, info):
        self.print_page_header('vCenter Host')

        self.my_output.print_stream('## Overview', 'output')
        self.my_output.print_stream('\n- vCenter: [%s](../%s-host.md)' % (info['vcenter'], info['vcenter']), 'output')
        self.my_output.print_stream('- Host: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Hypervisor: %s' % (info['hypervisor']), 'output')
        self.my_output.print_stream('- Runtime', 'output')
        self.my_output.print_stream('\t- Power: %s' % (info['runtime']['powerState']), 'output')
        self.my_output.print_stream('\t- Connection: %s' % (info['runtime']['connectionState']), 'output')
        self.my_output.print_stream('\t- Standby Mode: %s' % (info['runtime']['standbyMode']), 'output')

        self.my_output.print_stream('## Details', 'output')
        self.my_output.print_stream(
            '- Physical adapter: [%s/%s](../nic/%s.md)' % (
                self.vc_nic_up_count[info['vcenter']][info['name']],
                self.vc_nic_count[info['vcenter']][info['name']],
                info['hash']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- VMkernel adapter: [%s/%s](../vnic/%s.md)' % (
                self.vc_vnic_up_count[info['vcenter']][info['name']],
                self.vc_vnic_count[info['vcenter']][info['name']],
                info['hash']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Network: [%s/%s](../net/%s.md)' % (
                self.vc_net_up_count[info['vcenter']][info['name']],
                self.vc_net_count[info['vcenter']][info['name']],
                info['hash']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Standard switch: [%s/%s](../switch/%s.md)' % (
                self.vc_switch_up_count[info['vcenter']][info['name']],
                self.vc_switch_count[info['vcenter']][info['name']],
                info['hash']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Distributed virtual switch: [%s/%s](../dvs/%s.md)' % (
                self.vc_dvs_up_count[info['vcenter']][info['name']],
                self.vc_dvs_count[info['vcenter']][info['name']],
                info['hash']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Virtual machine: [%s/%s](../dvs/%s.md)' % (
                self.vc_vm_up_count[info['vcenter']][info['name']],
                self.vc_vm_count[info['vcenter']][info['name']],
                info['hash']
            ),
            'output'
        )

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.my_output.print_stream('## Capacity and Usage', 'output')

        order = [
            'Type',
            'Capacity',
            'Usage',
            'Usage %'
        ]
        self.print_table_header(order)

        line = ''
        line = self.add_column(line, 'CPU')
        line = self.add_column(line, '%s [GHz]' % (info['cpuCapacity'] / 1000))
        if info['stats'] is None:
            line = self.add_column(line, '---')
            line = self.add_column(line, '---')
        else:
            if info['stats']['overallCpuUsage'] is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, '%s [GHz]' % (info['stats']['overallCpuUsage'] / 1000))
            line = self.add_column(line, '%s' % (info['stats']['overallCpuUsagePct']))
        self.my_output.print_stream(line, 'output')

        line = ''
        line = self.add_column(line, 'Memory')
        line = self.add_column(
            line,
            '%s' % (
                vc_helper.convert_memory(info['memorySize'])
            )
        )
        if info['stats'] is None:
            line = self.add_column(line, '---')
            line = self.add_column(line, '---')
        else:
            line = self.add_column(
                line,
                '%s' % (
                    vc_helper.convert_memory(info['stats']['overallMemoryUsage'])
                )
            )
            line = self.add_column(line, '%s' % (info['stats']['overallMemoryUsagePct']))
        self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('## Server', 'output')
        self.my_output.print_stream('- Vendor: %s' % (info['vendor']), 'output')
        self.my_output.print_stream('- Model: %s' % (info['model']), 'output')
        self.my_output.print_stream('- [Inventory](../../compute/%s-inv.md)' % (info['ServerMoid']), 'output')
        self.my_output.print_stream('- [Networking](../../compute/%s-net.md)' % (info['ServerMoid']), 'output')

        self.save_output('%s' % (info['hash']), subdir='vc/host')

    def print_vc_hosts(self, vcenter, info):
        self.print_vc_page_header(
            vcenter,
            'Host',
            'host'
        )

        self.my_output.print_stream('## vCenter', 'output')

        order = [
            'Host',
            'Power',
            'Connection',
            'Cluster',
            'CPU',
            'Memory',
            'Uptime',
            'VM'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_vc_host(line, item)
            line = self.add_vc_host_power_state(line, item)
            line = self.add_vc_host_connection_state(line, item)
            line = self.add_column(line, item['clusterName'])
            line = self.add_column(line, item['stats']['overallCpuUsagePct'])
            line = self.add_column(line, item['stats']['overallMemoryUsagePct'])
            line = self.add_column(line, item['_uptime'])
            line = self.add_column(
                line,
                '[%s](./vm/%s.md)' % (
                    item['vm_summary'],
                    item['hash']
                )
            )
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('## Compute', 'output')

        order = [
            'Host',
            'Ver',
            'Model',
            'Serial',
            'Compute',
            'VM'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_vc_host(line, item)
            line = self.add_column(line, item['_hypervisor'])
            line = self.add_column(line, item['model'])
            if item['ServerName'] is None:
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
            else:
                server_info = self.xd_handler.get_server_by_moid(
                    item['ServerMoid']
                )
                if server_info is None:
                    line = self.add_column(line, '---')
                else:
                    line = self.add_column(line, server_info['Serial'])

                line = self.add_column(
                    line,
                    '[%s](../compute/%s-inv.md)' % (
                        item['ServerName'],
                        item['ServerMoid']
                    )
                )

                line = self.add_column(
                    line,
                    '[%s](./vm/%s.md)' % (
                        item['vm_summary'],
                        item['hash']
                    )
                )

            self.my_output.print_stream(line, 'output')

        self.save_output('%s-hosts' % (vcenter), subdir='vc')

        for item in info:
            self.print_vc_host(item)
