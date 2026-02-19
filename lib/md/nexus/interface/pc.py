import json
from lib import ip_helper
from lib.nexus import helper as nexus_helper


class MdNexusInterfacePcOutput():
    def __init__(self):
        pass

    def print_nexus_interface_pc_details(self, nexus_name, info, vpc_state, all):
        self.print_page_header('Nexus Interface Port Channel')

        self.my_output.print_stream('- Device: [%s](../%s-pc.md)' % (nexus_name, nexus_name), 'output')
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

        vpc = False
        if 'vpc_status' in info:
            vpc = True
            self.my_output.print_stream('- VPC: %s' % (info['vpc_status']), 'output')

        if info['pc'] is not None:
            self.my_output.print_stream('## Members\n', 'output')

            self.my_output.print_stream('### Load Sharing [%]\n', 'output')

            order = [
                'Eth',
                'RX unicast',
                'TX unicast',
                'RX multicast',
                'TX multicast',
                'RX broadcast',
                'TX broadcast'
            ]
            self.print_table_header(order)

            for item in info['pc']['member']:
                line = ''
                line = self.add_column(line, '[%s](../eth/%s.md)' % (item['eth']['interface_id'], item['eth']['hash']))
                line = self.add_column(line, item['rx-ucst'])
                line = self.add_column(line, item['tx-ucst'])
                line = self.add_column(line, item['rx-mcst'])
                line = self.add_column(line, item['tx-mcst'])
                line = self.add_column(line, item['rx-bcst'])
                line = self.add_column(line, item['tx-bcst'], last=True)
                self.my_output.print_stream(line, 'output')

            self.my_output.print_stream('', 'output')

            self.my_output.print_stream('### Ethernet Interface Members\n', 'output')

            order = [
                'Eth',
                'State',
                'Mode',
                'Speed',
                'CDP',
                'LLDP',
                'Device',
                'Interface'
            ]
            self.print_table_header(order)

            for item in info['pc']['member']:
                line = ''
                line = self.add_column(line, '[%s](../eth/%s.md)' % (item['eth']['interface_id'], item['eth']['hash']))
                line = self.add_column(line, item['_state'])
                line = self.add_nexus_port_mode(line, item['eth'])
                line = self.add_column(line, item['eth']['speed'])
                line = self.add_nexus_eth_cdp(line, item['eth'], up=True)
                line = self.add_nexus_eth_lldp(line, item['eth'], up=True)
                line = self.add_nexus_connected_device_name(line, item['eth'], up=True, last=False)
                line = self.add_nexus_connected_device_interface(line, item['eth'], up=True, last=True)
                self.my_output.print_stream(line, 'output')
                if vpc_state is None:
                    vpc_state = item['eth']['vpc_state']

            self.my_output.print_stream('', 'output')

        if vpc and vpc_state is not None:
            self.my_output.print_stream('\n## Virtual Port Channel\n', 'output')
            self.my_output.print_stream('- Domain ID: [%s](../vpc-domain/%s.md)' % (vpc_state['vpc-domain-id'], vpc_state['vpc-domain-id']), 'output')
            self.my_output.print_stream('- Role: %s' % (vpc_state['_role']), 'output')
            for peer in vpc_state['peer']:
                self.my_output.print_stream(
                    '- Peer interface: [%s](./%s.md) (%s)' % (
                        peer['ifindex'],
                        peer['hash'],
                        peer['_state']
                    ),
                    'output'
                )
                peer_names = []
                for peer_xd in peer['xd']:
                    if peer_xd['DeviceType'] is not None and peer_xd['DeviceType'] == 'Nexus':
                        peer_nexus_name = self.get_short_name(
                            peer_xd['DeviceSysName']
                        )
                        if peer_nexus_name not in peer_names:
                            peer_names.append(peer_nexus_name)
                            self.my_output.print_stream(
                                '- Peer device: [%s](../%s-pc.md)' % (
                                    peer_nexus_name,
                                    peer_nexus_name
                                ),
                                'output'
                            )

            self.my_output.print_stream(
                '- Peer state: %s, %s, %s (peer), %s (vlan)' % (
                    vpc_state['vpc-peer-status'],
                    vpc_state['vpc-peer-keepalive-status'],
                    vpc_state['vpc-peer-consistency'],
                    vpc_state['vpc-per-vlan-peer-consistency']
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

            for vitem in vpc_state['vpc']:
                if nexus_helper.is_nexus_interface_equal(vitem['ifindex'], info['interface']):
                    line = ''
                    line = self.add_column(line, vitem['id'])
                    line = self.add_column(line, '[%s](../pc/%s.md)' % (vitem['ifindex'], vitem['hash']))
                    line = self.add_column(line, vitem['_state'])
                    line = self.add_column(line, vitem['consistency'], last=True)
                    self.my_output.print_stream(line, 'output')

            self.my_output.print_stream('\n', 'output')

        if info['configuration'] is not None:
            self.my_output.print_stream('\n## Configuration\n', 'output')

            self.my_output.print_stream('\n### %s\n' % (nexus_name), 'output')
            self.my_output.print_stream('```', 'output')
            self.my_output.print_stream(info['configuration'], 'output')
            if vpc and vpc_state is not None:
                self.my_output.print_stream('', 'output')
                self.my_output.print_stream(vpc_state['configuration'], 'output')

            if info['pc'] is not None:
                for member in info['pc']['member']:
                    if member['eth']['configuration'] is not None:
                        self.my_output.print_stream('', 'output')
                        self.my_output.print_stream(member['eth']['configuration'], 'output')
            self.my_output.print_stream('```', 'output')

        if vpc and vpc_state is not None:
            if vpc_state['peer_nexus'] is not None:
                self.my_output.print_stream('\n### %s\n' % (vpc_state['peer_nexus']), 'output')
                self.my_output.print_stream('```', 'output')

                if info['pc'] is not None:
                    for other_pc in all:
                        if other_pc['nexus_name'] == vpc_state['peer_nexus']:
                            if 'pc' in other_pc:
                                if other_pc['pc']['group'] == info['pc']['group']:
                                    self.my_output.print_stream(other_pc['configuration'], 'output')
                                    self.my_output.print_stream('', 'output')

                self.my_output.print_stream(vpc_state['peer_configuration'], 'output')

                if info['pc'] is not None:
                    for other_pc in all:
                        if other_pc['nexus_name'] == vpc_state['peer_nexus']:
                            if 'pc' in other_pc:
                                if other_pc['pc']['group'] == info['pc']['group']:
                                    for member in other_pc['pc']['member']:
                                        if member['eth']['configuration'] is not None:
                                            self.my_output.print_stream('', 'output')
                                            self.my_output.print_stream(member['eth']['configuration'], 'output')

                self.my_output.print_stream('```', 'output')

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output('%s' % (info['hash']), subdir='nexus/pc')

    def print_nexus_interface_pc(self, nexus_name, info, vpc_state, all):
        self.print_page_header('# Port Channel Interface (%s)' % (nexus_name))
        self.print_nexus_devices_bar(nexus_name, 'pc')
        self.print_nexus_table_bar(nexus_name, 'pc')

        self.my_output.print_stream(
            '## Port Channels',
            'output'
        )

        order = [
            'PC',
            'Description',
            'Mode',
            'State',
            'Reason',
            'Speed',
            'Protocol',
            'Members'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(line, '[%s](./pc/%s.md)' % (item['interface_id'], item['hash']))
            line = self.add_column(line, item['desc'])
            line = self.add_nexus_port_mode(line, item)
            line = self.add_column(line, item['state'])
            line = self.add_column(line, item['_reason'])
            line = self.add_column(line, item['speed'])
            line = self.add_column(line, item['proto'])

            members = []
            if item['eth_members'] is not None:
                for member in item['eth_members'].split(','):
                    member_id = nexus_helper.get_nexus_interface_id(member)
                    member_hash = ip_helper.get_string_md5(
                        '%s %s' % (
                            item['nexus_name'],
                            'Ethernet%s' % (member_id)
                        )
                    )
                    members.append(
                        '[%s](./eth/%s.md)' % (
                            member_id,
                            member_hash
                        )
                    )

            line = self.add_column(line, ','.join(members), last=True)

            self.nexus_pc_count[nexus_name] = self.nexus_pc_count[nexus_name] + 1
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

        self.my_output.print_stream(
            '## Port Channel Members',
            'output'
        )

        order = [
            'PC',
            'Eth',
            'State',
            'Mode',
            'Speed',
            'CDP',
            'LLDP',
            'Device',
            'Interface'
        ]
        self.print_table_header(order)

        for item in info:
            for member in item['pc']['member']:
                line = ''
                line = self.add_column(line, '[%s](./pc/%s.md)' % (item['interface_id'], item['hash']))
                line = self.add_column(line, '[%s](../eth/%s.md)' % (member['eth']['interface_id'], member['eth']['hash']))
                line = self.add_column(line, member['_state'])
                line = self.add_nexus_port_mode(line, member['eth'])
                line = self.add_column(line, member['eth']['speed'])
                line = self.add_nexus_eth_cdp(line, member['eth'])
                line = self.add_nexus_eth_lldp(line, member['eth'])
                line = self.add_nexus_connected_device_name(line, member['eth'], last=False)
                line = self.add_nexus_connected_device_interface(line, member['eth'], last=True)
                self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

        self.save_output('%s-pc' % (nexus_name), subdir='nexus')

        for item in info:
            self.print_nexus_interface_pc_details(
                nexus_name,
                item,
                vpc_state,
                all
            )
