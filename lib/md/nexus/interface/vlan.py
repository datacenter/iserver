from lib import ip_helper
from lib.nexus import helper as nexus_helper


class MdNexusInterfaceVlanOutput():
    def __init__(self):
        pass

    def print_nexus_interface_vlan_details(self, nexus_name, info, eth, pc, vlan):
        self.print_page_header('Nexus Interface VLAN')

        self.my_output.print_stream('- Device: [%s](../%s-vlan.md)' % (nexus_name, nexus_name), 'output')
        self.my_output.print_stream('- Interface: %s' % (info['interface']), 'output')
        self.my_output.print_stream('- Description: %s' % (info['svi_desc']), 'output')
        self.my_output.print_stream('- MAC: %s' % (info['svi_mac']), 'output')
        self.my_output.print_stream(
            '- State: admin (%s) oper (%s)' % (
                info['svi_admin_state'],
                info['svi_line_proto']
            ),
            'output'
        )

        if info['vlan_name'] is not None:
            self.my_output.print_stream('- VLAN name: %s' % (info['vlan_name']), 'output')

        if info['vn_segment'] is not None:
            self.my_output.print_stream('- VN Segment: %s' % (info['vn_segment']), 'output')

        if info['configuration'] is not None:
            self.my_output.print_stream('\n## Configuration\n', 'output')
            self.my_output.print_stream('```', 'output')
            self.my_output.print_stream(info['configuration'], 'output')
            self.my_output.print_stream('```', 'output')

        self.my_output.print_stream('## Member Ethernet Interfaces\n', 'output')

        order = [
            'Eth',
            'State',
            'Mode',
            'Speed',
            'PC',
            'CDP',
            'LLDP',
            'Device',
            'Interface'
        ]
        self.print_table_header(order)

        for item in eth:
            if item['interface'] not in vlan['interfaces']:
                continue

            line = ''
            line = self.add_column(line, '[%s](../eth/%s.md)' % (item['interface_id'], item['hash']))
            line = self.add_column(line, item['state'])
            line = self.add_nexus_port_mode(line, item)
            line = self.add_column(line, item['speed'])
            line = self.add_nexus_eth_pc(line, item)
            line = self.add_nexus_eth_cdp(line, item, up=True)
            line = self.add_nexus_eth_lldp(line, item, up=True)
            line = self.add_nexus_connected_device_name(line, item, up=True, last=False)
            line = self.add_nexus_connected_device_interface(line, item, up=True, last=True)
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

        self.my_output.print_stream('## Member Port Channel Interfaces\n', 'output')

        order = [
            'PC',
            'Description',
            'Mode',
            'State',
            'Reason',
            'Speed',
            'Rate',
            'Protocol',
            'Members'
        ]
        self.print_table_header(order)

        for item in pc:
            if item['interface'] not in vlan['interfaces']:
                continue

            line = ''
            line = self.add_column(line, '[%s](../pc/%s.md)' % (item['interface_id'], item['hash']))
            line = self.add_column(line, item['desc'])
            line = self.add_nexus_port_mode(line, item)
            line = self.add_column(line, item['state'])
            line = self.add_column(line, item['_reason'])
            line = self.add_column(line, item['speed'])
            line = self.add_column(line, item['ratemode'])
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
                        '[%s](../eth/%s.md)' % (
                            member_id,
                            member_hash
                        )
                    )

            line = self.add_column(line, ','.join(members), last=True)
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

        self.save_output('%s' % (info['hash']), subdir='nexus/vlan')

    def print_nexus_interface_vlan(self, nexus_name, info, eth, pc, vlan):
        self.print_page_header('VLAN Interface (%s)' % (nexus_name))
        self.print_nexus_devices_bar(nexus_name, 'vlan')
        self.print_nexus_table_bar(nexus_name, 'vlan')

        order = [
            'VLAN',
            'Description',
            'State',
            'Reason',
            'Interfaces',
            'VN Segment'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(line, '[%s](./vlan/%s.md)' % (item['interface_id'], item['hash']))
            line = self.add_column(line, item['svi_desc'])
            line = self.add_column(line, item['svi_line_proto'])
            line = self.add_column(line, item['_reason'])

            count = None
            for vitem in vlan:
                if item['interface_id'] == vitem['id']:
                    count = len(vitem['interfaces'])

            line = self.add_column(line, count)
            line = self.add_column(line, item['vn_segment'], last=True)

            self.nexus_vlan_count[nexus_name] = self.nexus_vlan_count[nexus_name] + 1
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '\n\n',
            'output'
        )

        self.save_output('%s-vlan' % (nexus_name), subdir='nexus')

        for item in info:
            for vitem in vlan:
                if item['interface_id'] == vitem['id']:
                    self.print_nexus_interface_vlan_details(
                        nexus_name,
                        item,
                        eth,
                        pc,
                        vitem
                    )
