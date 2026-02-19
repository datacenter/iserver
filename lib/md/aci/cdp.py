from lib import ip_helper
from lib.aci import helper as aci_helper
from lib.nexus import helper as nexus_helper


class MdAciCdpOutput():
    def __init__(self):
        pass

    def print_aci_interface_cdp_addon(self, info, title=True):
        if title:
            self.my_output.print_stream('## CDP', 'output')

        if 'sysName' in info and info['sysName'] is not None and len(info['sysName']) > 0:
            self.my_output.print_stream('- Sys Name: %s' % (info['sysName']), 'output')
        if 'devId' in info and info['devId'] is not None and len(info['devId']) > 0:
            self.my_output.print_stream('- Device ID: %s' % (info['devId']), 'output')
        if 'platId' in info and info['platId'] is not None and len(info['platId']) > 0:
            self.my_output.print_stream('- Platform: %s' % (info['platId']), 'output')
        if 'ver' in info and info['ver'] is not None and len(info['ver']) > 0:
            self.my_output.print_stream('- Version: %s' % (info['ver']), 'output')
        if 'portId' in info and info['portId'] is not None and len(info['portId']) > 0:
            self.my_output.print_stream('- Interface: %s' % (info['portId']), 'output')
        if 'cap' in info and len(info['cap']) > 0:
            self.my_output.print_stream('- Capabilities', 'output')
            if isinstance(info['cap'], list):
                for cap in info['cap']:
                    self.my_output.print_stream('\t- %s' % (cap), 'output')
            else:
                for cap in info['cap'].split(','):
                    self.my_output.print_stream('\t- %s' % (cap), 'output')

    def add_aci_cdp_nei_interface(self, line, item):
        if item['xd']['DeviceType'] is not None and item['xd']['DeviceType'] == 'Nexus' and item['xd']['NexusDevice'] is not None:
            line = self.add_column(
                line,
                '[%s](../nexus/eth/%s.md)' % (
                    item['portId'],
                    nexus_helper.get_nexus_interface_hash(item['xd']['NexusDevice'], item['portId'])
                )
            )
            return line

        line = self.add_column(line, item['portId'])
        return line

    def get_aci_cdp_sys_description(self, content):
        content = content.replace('\n', ' ')
        if 'Cisco Nexus Operating System' in content:
            content = 'Cisco NX-OS'

        return content

    def print_aci_node_cdp_adjacency(self, info, controller, node_name, servers):
        self.print_page_header('ACI CDP')

        self.my_output.print_stream('## Local End', 'output')
        self.my_output.print_stream('\n- Controller: %s' % (controller), 'output')
        self.my_output.print_stream('- Node: %s' % (node_name), 'output')
        self.my_output.print_stream('- Interface: %s' % (info['interfaceId']), 'output')
        if 'index' in info:
            self.my_output.print_stream('- ifIndex: %s' % (info['index']), 'output')
        if 'duplex' in info:
            self.my_output.print_stream('- Duplex: %s' % (info['duplex']), 'output')
        if 'mtu' in info:
            self.my_output.print_stream('- MTU: %s' % (info['mtu']), 'output')
        if 'nativeVlan' in info:
            self.my_output.print_stream('- Native VLAN: %s' % (info['nativeVlan']), 'output')

        self.my_output.print_stream('\n## Remote End', 'output')
        if 'sysName' in info:
            self.my_output.print_stream('- Sys Name: %s' % (info['sysName']), 'output')
        if 'devId' in info:
            self.my_output.print_stream('- Device ID: %s' % (info['devId']), 'output')
        if 'platId' in info:
            self.my_output.print_stream('- Platform: %s' % (info['platId']), 'output')
        if 'ver' in info:
            self.my_output.print_stream('- Version: %s' % (info['ver']), 'output')
        if 'portId' in info:
            self.my_output.print_stream('- Interface: %s' % (info['portId']), 'output')
        if 'cap' in info and len(info['cap']) > 0:
            self.my_output.print_stream('- Capabilities', 'output')
            if isinstance(info['cap'], list):
                for cap in info['cap']:
                    self.my_output.print_stream('\t- %s' % (cap), 'output')
            else:
                for cap in info['cap'].split(','):
                    self.my_output.print_stream('\t- %s' % (cap), 'output')

        if info['xd']['ServerMoid'] is not None:
            for server in servers:
                if server['Moid'] == info['xd']['ServerMoid']:
                    self.print_server(server, 'AddOn')
                    self.my_output.print_stream('', 'output')
                    self.print_server_mac(server, info['mac'])
                    self.print_server_vc(server, 'AddOn')

        link_hash = ip_helper.get_string_md5(
            '%s %s' % (
                controller,
                info['dn']
            )
        )

        self.save_output('%s' % (link_hash), subdir='apic/cdp')

    def print_aci_node_cdp(self, info, controller, node_name, servers):
        self.print_page_header('CDP Adjacency (%s:%s)' % (controller, node_name))
        self.print_aci_node_bar(controller, node_name, 'cdp')
        self.print_aci_node_table_bar(controller, node_name, 'cdp')

        order = [
            'Interface',
            'CDP Platform',
            'CDP SysName',
            'Device',
            'Interface',
            'Info'
        ]
        self.print_table_header(order)

        items = []
        for item in info:
            if self.aci_node_mapping[controller][item['node_id']] == node_name:
                items.append(
                    item
                )

        items = sorted(
            items,
            key=lambda i: i['_index']
        )

        for item in items:
            line = ''
            line = self.add_column(line, item['interfaceId'])
            line = self.add_column(line, item['platId'])
            line = self.add_column(line, item['sysName'])
            line = self.add_column(line, self.get_xd_device_link(item['xd'], nei='cdp'))
            line = self.add_aci_cdp_nei_interface(line, item)
            line = '%s [Link](./cdp/%s.md)' % (
                line,
                item['hash']
            )

            self.my_output.print_stream(line, 'output')
            self.aci_node_cdp_count[controller][node_name] = self.aci_node_cdp_count[controller][node_name] + 1

        self.save_output('%s-%s-cdp' % (controller, node_name), subdir='apic')

        for item in items:
            self.print_aci_node_cdp_adjacency(
                item,
                controller,
                node_name,
                servers
            )

    def print_aci_cdp(self, info, controller):
        self.print_page_header('CDP Adjacency (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'cdp')
        self.print_aci_controller_table_bar(controller, 'cdp')

        order = [
            'Node',
            'Interface',
            'CDP Platform',
            'CDP SysName',
            'Device',
            'Interface',
            'Info'
        ]
        self.print_table_header(order)

        info = sorted(
            info,
            key=lambda i: (
                i['node_name'],
                i['_index']
            )
        )

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./%s-%s-cdp.md)' % (
                    item['node_name'],
                    controller,
                    item['node_name']
                )
            )
            line = self.add_column(line, item['interfaceId'])
            line = self.add_column(line, item['platId'])
            line = self.add_column(line, item['sysName'])
            line = self.add_column(line, self.get_xd_device_link(item['xd'], nei='cdp'))
            line = self.add_aci_cdp_nei_interface(line, item)
            line = '%s [Link](./cdp/%s.md)' % (
                line,
                item['hash']
            )

            self.my_output.print_stream(line, 'output')
            self.aci_cdp_count[controller] = self.aci_cdp_count[controller] + 1

        self.save_output('%s-cdp' % (controller), subdir='apic')
