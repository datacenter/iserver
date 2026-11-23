import json
from lib import file_helper
from lib.nexus import helper as nexus_helper


class MdNexusInterfaceEthOutput():
    def __init__(self):
        pass

    def add_nexus_eth_pc(self, line, item, last=False):
        if item['pc_state'] is not None:
            line = self.add_column(line, '[%s](./pc/%s.md)' % (item['portchan'], item['pc_state']['hash']), last=last)
        else:
            line = self.add_column(line, item['portchan'], last=last)
        return line

    def add_nexus_eth_cdp(self, line, item, up=False, last=False):
        base = './'
        if up:
            base = '../'

        if 'cdp_hash' in item and item['cdp_hash'] is not None:
            line = self.add_column(line, '[Link](%scdp/%s.md)' % (base, item['cdp_hash']), last=False)
        else:
            line = self.add_column(line, '---', False)
        return line

    def add_nexus_eth_lldp(self, line, item, up=False, last=False):
        base = './'
        if up:
            base = '../'

        if 'lldp_hash' in item and item['lldp_hash'] is not None:
            line = self.add_column(line, '[Link](%slldp/%s.md)' % (base, item['lldp_hash']), last=False)
        else:
            line = self.add_column(line, '---', last=False)
        return line

    def print_nexus_interface_eth_details(self, nexus_name, info):
        self.print_page_header('Nexus Interface Ethernet')

        self.my_output.print_stream('- Device: [%s](../%s-eth.md)' % (nexus_name, nexus_name), 'output')
        self.my_output.print_stream('- Interface: %s' % (info['interface']), 'output')
        self.my_output.print_stream('- Description: %s' % (info['desc']), 'output')
        self.my_output.print_stream('- HW Description: %s' % (info['eth_hw_desc']), 'output')
        self.my_output.print_stream('- Mode: %s' % (info['portmode']), 'output')
        self.my_output.print_stream('- MAC: %s' % (info['eth_hw_addr']), 'output')
        if info['_reason'] is not None:
            self.my_output.print_stream(
                '- State: admin (%s) oper (%s) reason (%s)' % (
                    info['admin_state'],
                    info['state'],
                    info['_reason']
                ),
                'output'
            )
        else:
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
            if info['pc_state'] is not None:
                if info['pc_state']['configuration'] is not None:
                    self.my_output.print_stream('', 'output')
                    self.my_output.print_stream(info['pc_state']['configuration'], 'output')
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

        if info['portchan'] is not None:
            self.my_output.print_stream('\n## Port Channel\n', 'output')
            self.my_output.print_stream('- Bundle: %s' % (info['eth_bundle']), 'output')
            if info['pc_state'] is not None:
                self.my_output.print_stream(
                    '- Interface: [%s](../pc/%s.md) (%s)' % (
                        info['pc_state']['port-channel'],
                        info['pc_state']['hash'],
                        info['pc_state']['_state']
                    ),
                    'output'
                )

                self.my_output.print_stream('\n', 'output')
                order = [
                    'Member',
                    'Status'
                ]
                self.print_table_header(order)

                for member in info['pc_state']['member']:
                    line = ''
                    line = self.add_column(line, '[%s](../%s.md)' % (member['port'], member['hash']))
                    line = self.add_column(line, member['_state'], last=True)
                    self.my_output.print_stream(line, 'output')

                self.my_output.print_stream('\n', 'output')

            if info['vpc_state'] is not None:
                self.my_output.print_stream('\n## Virtual Port Channel\n', 'output')
                self.my_output.print_stream(
                    '- Domain ID: [%s](../vpc-domain/%s.md)' % (
                        info['vpc_state']['vpc-domain-id'],
                        info['vpc_state']['vpc-domain-id']
                    ),
                    'output'
                )
                self.my_output.print_stream('- Role: %s' % (info['vpc_state']['_role']), 'output')
                for peer in info['vpc_state']['peer']:
                    self.my_output.print_stream(
                        '- Peer interface: [%s](../pc/%s.md) (%s)' % (
                            peer['ifindex'],
                            peer['hash'],
                            peer['_state']
                        ),
                        'output'
                    )
                    peer_names = []
                    for peer_xd in peer['xd']:
                        if peer_xd['DeviceType'] is not None and peer_xd['DeviceType'] == 'Nexus':
                            nexus_name = self.get_short_name(
                                peer_xd['DeviceSysName']
                            )
                            if nexus_name not in peer_names:
                                peer_names.append(nexus_name)
                                self.my_output.print_stream(
                                    '- Peer device: %s' % (
                                        nexus_name
                                    ),
                                    'output'
                                )

                self.my_output.print_stream(
                    '- Peer state: %s, %s, %s (peer), %s (vlan)' % (
                        info['vpc_state']['vpc-peer-status'],
                        info['vpc_state']['vpc-peer-keepalive-status'],
                        info['vpc_state']['vpc-peer-consistency'],
                        info['vpc_state']['vpc-per-vlan-peer-consistency']
                    ),
                    'output'
                )

                self.my_output.print_stream('\n', 'output')
                order = [
                    'ID',
                    'ifIndex',
                    'State',
                    'Consistency'
                ]
                self.print_table_header(order)

                for vitem in info['vpc_state']['vpc']:
                    line = ''
                    line = self.add_column(line, vitem['id'])
                    line = self.add_column(line, '[%s](../pc/%s.md)' % (vitem['ifindex'], vitem['hash']))
                    line = self.add_column(line, vitem['_state'])
                    line = self.add_column(line, vitem['consistency'], last=True)
                    self.my_output.print_stream(line, 'output')

                self.my_output.print_stream('\n', 'output')

        if info['transceiver']['type'] is not None:
            self.my_output.print_stream('\n## Optics\n', 'output')
            self.my_output.print_stream('- Type: %s' % (info['transceiver']['type']), 'output')
            self.my_output.print_stream('- Name: %s' % (info['transceiver']['name']), 'output')
            self.my_output.print_stream('- P/N: %s' % (info['transceiver']['partnum']), 'output')
            self.my_output.print_stream('- Revision: %s' % (info['transceiver']['rev']), 'output')
            self.my_output.print_stream('- S/N: %s' % (info['transceiver']['serialnum']), 'output')
            self.my_output.print_stream('- Cisco PID: %s' % (info['transceiver']['cisco_product_id']), 'output')
            self.my_output.print_stream('- Cisco P/N: %s' % (info['transceiver']['cisco_part_number']), 'output')

        if info['portmode'] in ['access', 'trunk']:
            self.my_output.print_stream('\n## VLAN\n', 'output')

            order = [
                'VLAN',
                'Name',
                'State',
                'Type',
                'Mode'
            ]
            self.print_table_header(order)

            for vitem in info['vlans']:
                line = '%s |' % (vitem['id'])
                line = '%s %s |' % (line, vitem['name'])
                line = '%s %s |' % (line, vitem['state'])
                line = '%s %s |' % (line, vitem['type'])
                line = '%s %s |' % (line, vitem['mode'])

                self.my_output.print_stream(line, 'output')

            self.my_output.print_stream(
                '\n\n',
                'output'
            )

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output('%s' % (info['hash']), subdir='nexus/eth')

    def print_nexus_interface_eth(self, nexus_name, info):
        self.print_page_header('Ethernet Interface (%s)' % (nexus_name))
        self.print_nexus_devices_bar(nexus_name, 'eth')
        self.print_nexus_table_bar(nexus_name, 'eth')

        up = 0
        count = 0
        for item in info:
            if item['state'] == 'up':
                up = up + 1
            count = count + 1

        self.nexus_eth_up_count[nexus_name] = up
        self.nexus_eth_count[nexus_name] = count

        self.my_output.print_stream(
            '## Up Interfaces %s/%s' % (up, count),
            'output'
        )

        order = [
            'Eth',
            'Mode',
            'Speed',
            'PC',
            'CDP',
            'LLDP',
            'Device',
            'Interface'
        ]
        self.print_table_header(order)

        for item in info:
            if item['state'] != 'up':
                continue

            line = ''
            line = self.add_column(line, '[%s](./eth/%s.md)' % (item['interface_id'], item['hash']))
            line = self.add_nexus_port_mode(line, item)
            line = self.add_column(line, item['speed'])
            line = self.add_nexus_eth_pc(line, item)
            line = self.add_nexus_eth_cdp(line, item)
            line = self.add_nexus_eth_lldp(line, item)
            line = self.add_nexus_connected_device_name(line, item, last=False)
            line = self.add_nexus_connected_device_interface(line, item, last=True)
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '\n\n',
            'output'
        )

        self.my_output.print_stream(
            '## All Interfaces ',
            'output'
        )

        order = [
            'Eth',
            'Mode',
            'State',
            'Reason',
            'Speed',
            'PC',
            'CDP',
            'LLDP',
            'Device',
            'Interface'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(line, '[%s](./eth/%s.md)' % (item['interface_id'], item['hash']))
            line = self.add_nexus_port_mode(line, item)
            line = self.add_column(line, item['state'])
            line = self.add_column(line, item['_reason'])
            line = self.add_column(line, item['speed'])
            line = self.add_nexus_eth_pc(line, item)
            line = self.add_nexus_eth_cdp(line, item)
            line = self.add_nexus_eth_lldp(line, item)
            line = self.add_nexus_connected_device_name(line, item, last=False)
            line = self.add_nexus_connected_device_interface(line, item, last=True)
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '\n\n',
            'output'
        )

        self.save_output('%s-eth' % (nexus_name), subdir='nexus')

        for item in info:
            self.print_nexus_interface_eth_details(
                nexus_name,
                item
            )

    def print_nexus_interface_eth_up(self, info):
        self.print_page_header('Nexus Devices Ethernet Interfaces Up')
        self.print_nexus_overview_bar('up')

        order = [
            'Nexus',
            'Eth',
            'Mode',
            'Speed',
            'PC',
            'CDP',
            'LLDP',
            'Device',
            'Interface'
        ]
        self.print_table_header(order)

        for nexus_name in info:
            for item in info[nexus_name]:
                if item['type'] != 'eth':
                    continue

                if item['state'] != 'up':
                    continue

                line = ''
                line = self.add_column(line, '[%s](./%s-eth.md)' % (item['nexus_name'], item['nexus_name']))
                line = self.add_column(line, '[%s](./eth/%s.md)' % (item['interface_id'], item['hash']))
                line = self.add_nexus_port_mode(line, item)
                line = self.add_column(line, item['speed'])
                line = self.add_nexus_eth_pc(line, item)
                line = self.add_nexus_eth_cdp(line, item)
                line = self.add_nexus_eth_lldp(line, item)
                line = self.add_nexus_connected_device_name(line, item, last=False)
                line = self.add_nexus_connected_device_interface(line, item, last=True)
                self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '\n\n',
            'output'
        )

        self.save_output('eth-up', subdir='nexus')
