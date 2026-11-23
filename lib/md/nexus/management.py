from lib.nexus import helper as nexus_helper


class MdNexusManagementOutput():
    def __init__(self):
        pass

    def print_nexus_interface_mgmt_details(self, nexus_name, info):
        self.print_page_header('Nexus Interface Management')

        self.my_output.print_stream('- Device: %s' % (nexus_name), 'output')
        self.my_output.print_stream('- Interface: %s' % (info['interface']), 'output')
        self.my_output.print_stream('- HW Description: %s' % (info['eth_hw_desc']), 'output')
        self.my_output.print_stream('- IP: %s/%s' % (info['eth_ip_addr'], info['eth_ip_mask']), 'output')
        self.my_output.print_stream('- MAC: %s' % (info['eth_hw_addr']), 'output')
        self.my_output.print_stream(
            '- State: admin (%s) oper (%s)' % (
                info['admin_state'],
                info['state']
            ),
            'output'
        )

        if info['state'] == 'up':
            if info['xd']['DeviceType'] is None:
                self.my_output.print_stream(
                    '- Connected device: --- Unknown ---',
                    'output'
                )

            if info['xd']['DeviceType'] is not None and info['xd']['DeviceType'] == 'Server':
                self.my_output.print_stream(
                    '- Connected device: [C] [%s](../../compute/%s-net.md)' % (
                        self.get_short_name(info['xd']['ServerName']),
                        info['xd']['ServerMoid']
                    ),
                    'output'
                )

            if info['xd']['DeviceType'] is not None and info['xd']['DeviceType'] == 'Nexus':
                nexus_name = self.get_short_name(
                    info['xd']['DeviceSysName']
                )

                self.my_output.print_stream(
                    '- Connected device: [N] %s' % (
                        nexus_name
                    ),
                    'output'
                )

            if info['xd']['DeviceType'] is not None and info['xd']['DeviceType'] == 'ACI':
                node_name = self.get_short_name(
                    info['xd']['DeviceSysName']
                )
                self.my_output.print_stream(
                    '- Connected device: [A] %s' % (
                        node_name
                    ),
                    'output'
                )

            if info['xd']['CdpHash'] is not None:
                self.my_output.print_stream(
                    '- [CDP](../cdp/%s.md)' % (
                        info['xd']['CdpHash']
                    ),
                    'output'
                )

            if info['xd']['LldpHash'] is not None:
                self.my_output.print_stream(
                    '- [LLDP](../lldp/%s.md)' % (
                        info['xd']['LldpHash']
                    ),
                    'output'
                )

        if info['configuration'] is not None:
            self.my_output.print_stream('\n## Configuration\n', 'output')
            self.my_output.print_stream('```', 'output')
            self.my_output.print_stream(info['configuration'], 'output')
            self.my_output.print_stream('```', 'output')

        self.my_output.print_stream('\n## Settings\n', 'output')
        self.my_output.print_stream('- MTU: %s' % (info['eth_mtu']), 'output')
        self.my_output.print_stream('- BW: %s' % (info['eth_mtu']), 'output')
        if 'eth_mode' in info:
            self.my_output.print_stream('- Mode: %s' % (info['eth_mode']), 'output')
        if 'eth_duplex' in info:
            self.my_output.print_stream('- Duplex: %s' % (info['eth_duplex']), 'output')
        if 'eth_speed' in info:
            self.my_output.print_stream('- Speed: %s' % (info['eth_speed']), 'output')
        if 'eth_autoneg' in info:
            self.my_output.print_stream('- Auto negotiation: %s' % (info['eth_autoneg']), 'output')

        self.save_output('%s' % (info['hash']), subdir='nexus/mgmt')

    def print_nexus_management(self, info):
        self.print_page_header('Nexus Devices Management Connectivity')
        self.print_nexus_overview_bar('mgmt')

        self.my_output.print_stream(
            '## Device mgmt0 view\n',
            'output'
        )

        order = [
            'Device',
            'State',
            'MAC',
            'IP',
            'Speed',
            'MTU',
            'Device',
            'Interface',
            'CDP',
            'LLDP',
            'Info'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(line, item['nexus_name'])
            line = self.add_column(line, item['state'])
            line = self.add_column(line, item['eth_hw_addr'])
            line = self.add_column(line, '%s/%s' % (item['ip_addr'], item['eth_ip_mask']))
            line = self.add_column(line, item['speed'])
            line = self.add_column(line, item['mtu'])
            line = self.add_column(line, '[%s](./%s-eth.md)' % (item['nei_device_name'], item['nei_device_name']))

            display_name = item['nei_interface_name']
            if nexus_helper.get_nexus_interface_type(item['nei_interface_name']) == 'eth':
                display_name = nexus_helper.get_nexus_interface_id(item['nei_interface_name'])

            if item['nei_interface_hash'] is not None:
                line = self.add_column(line, '[%s](./eth/%s.md)' % (display_name, item['nei_interface_hash']))
            else:
                line = self.add_column(line, display_name)

            if item['cdp_hash'] is not None:
                line = self.add_column(
                    line,
                    '[Link](./cdp/%s.md)' % (
                        item['cdp_hash']
                    )
                )
            else:
                line = self.add_column(line, '---')

            if item['lldp_hash'] is not None:
                line = self.add_column(
                    line,
                    '[Link](./lldp/%s.md)' % (
                        item['lldp_hash']
                    )
                )
            else:
                line = self.add_column(line, '---')

            line = self.add_column(
                line,
                '[Link](./mgmt/%s.md)' % (
                    item['hash']
                ),
                last=True
            )

            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '\n\n',
            'output'
        )

        self.my_output.print_stream(
            '## Management switch view\n',
            'output'
        )

        info = sorted(
            info,
            key = lambda i: (
                i['nei_device_name'],
                i['nei_index']
            )
        )

        order = [
            'Management Switch',
            'Interface',
            'Device',
            'State',
            'MAC',
            'IP',
            'Speed',
            'MTU',
            'CDP',
            'LLDP'
        ]
        self.print_table_header(order)

        for item in info:
            if item['nei_device_name'] is None:
                continue

            line = ''
            line = self.add_column(line, '[%s](./%s-eth.md)' % (item['nei_device_name'], item['nei_device_name']))

            display_name = item['nei_interface_name']
            if nexus_helper.get_nexus_interface_type(item['nei_interface_name']) == 'eth':
                display_name = nexus_helper.get_nexus_interface_id(item['nei_interface_name'])

            if item['nei_interface_hash'] is not None:
                line = self.add_column(line, '[%s](./eth/%s.md)' % (display_name, item['nei_interface_hash']))
            else:
                line = self.add_column(line, display_name)

            line = self.add_column(line, item['nexus_name'])
            line = self.add_column(line, item['state'])
            line = self.add_column(line, item['eth_hw_addr'])
            line = self.add_column(line, '%s/%s' % (item['ip_addr'], item['eth_ip_mask']))
            line = self.add_column(line, item['speed'])
            line = self.add_column(line, item['mtu'])

            if item['cdp_hash'] is not None:
                line = '%s [Link](./cdp/%s.md) |' % (
                    line,
                    item['cdp_hash']
                )
            else:
                line = '%s --- |' % (line)

            if item['lldp_hash'] is not None:
                line = '%s [Link](./lldp/%s.md)' % (
                    line,
                    item['lldp_hash']
                )
            else:
                line = '%s ---' % (line)

            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '\n\n',
            'output'
        )

        self.save_output('management', subdir='nexus')

        for item in info:
            self.print_nexus_interface_mgmt_details(
                item['nexus_name'],
                item
            )
