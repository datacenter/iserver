from lib.aci import helper as aci_helper
from lib.nexus import helper as nexus_helper


class MdAciLldpOutput():
    def __init__(self):
        pass

    def print_aci_interface_lldp_addon(self, info, title=True):
        if title:
            self.my_output.print_stream('## LLDP', 'output')

        if info['sysName'] is not None and len(info['sysName']) > 0:
            self.my_output.print_stream('- Sys Name: %s' % (info['sysName']), 'output')

        if info['sysDesc'] is not None and len(info['sysDesc']) > 0:
            self.my_output.print_stream('- Sys Description: %s' % (info['sysDesc']), 'output')

        if info['chassisIdT'] is not None and len(info['chassisIdT']) > 0:
            self.my_output.print_stream('- Chassis Type: %s' % (info['chassisIdT']), 'output')

        if info['chassisIdV'] is not None and len(info['chassisIdV']) > 0:
            self.my_output.print_stream('- Chassis Id: %s' % (info['chassisIdV']), 'output')

        if info['portIdT'] is not None and len(info['portIdT']) > 0:
            self.my_output.print_stream('- Port Type: %s' % (info['portIdT']), 'output')

        if info['portIdV'] is not None and len(info['portIdV']) > 0:
            self.my_output.print_stream('- Port Id: %s' % (info['portIdV']), 'output')

        if info['portDesc'] is not None and len(info['portDesc']) > 0:
            self.my_output.print_stream('- Port Desription: %s' % (info['portDesc']), 'output')

        if info['portVlan'] is not None and len(info['portVlan']) > 0:
            self.my_output.print_stream('- VLAN: %s' % (info['portVlan']), 'output')

        if len(info['capability']) > 0:
            self.my_output.print_stream('- Capability', 'output')
            if isinstance(info['capability'], list):
                for cap in info['capability']:
                    self.my_output.print_stream('\t- %s' % (cap), 'output')
            else:
                for cap in info['capability'].split(','):
                    self.my_output.print_stream('\t- %s' % (cap), 'output')

    def add_aci_lldp_nei_device(self, line, item):
        device = self.get_xd_device_link(item['xd'], nei='lldp')
        if device is None:
            line = self.add_column(line, item['sysName'])
        else:
            line = self.add_column(line, device)

        return line

    def add_aci_lldp_nei_interface(self, line, item):
        done = False
        if item['portIdT'] == 'if-name' and item['portIdV'].startswith('Eth'):
            if item['xd']['DeviceType'] is not None and item['xd']['DeviceType'] == 'Nexus' and item['xd']['NexusDevice'] is not None:
                done = True
                line = self.add_column(
                    line,
                    '[%s](../nexus/eth/%s.md)' % (
                        item['portIdV'],
                        nexus_helper.get_nexus_interface_hash(item['xd']['NexusDevice'], item['portIdV'])
                    )
                )

            if not done:
                done = True
                line = self.add_column(line, item['portIdV'])

        if item['portIdT'] == 'local' and item['portIdV'].startswith('Eth'):
            if item['xd']['DeviceType'] is not None and item['xd']['DeviceType'] == 'ACI' and item['xd']['AciNodeId'] is not None:
                done = True
                line = self.add_column(
                    line,
                    '[%s](./phy/%s.md)' % (
                        item['portIdV'],
                        aci_helper.get_aci_interface_hash(item['xd']['AciApicName'], item['xd']['AciNodeId'], item['portIdV'])
                    )
                )

            if not done:
                done = True
                line = self.add_column(line, item['portIdV'])

        if not done:
            line = self.add_column(line, '---')

        return line

    def get_aci_lldp_sys_description(self, content):
        content = content.replace('\n', ' ')
        if 'Cisco Nexus Operating System' in content:
            content = 'Cisco NX-OS'

        return content

    def print_aci_node_lldp_adjacency(self, info, controller, node_name, servers):
        self.print_page_header('ACI LLDP')

        self.my_output.print_stream('## Local End', 'output')
        self.my_output.print_stream('\n- Controller: %s' % (controller), 'output')
        self.my_output.print_stream('- Node: %s' % (node_name), 'output')
        self.my_output.print_stream('- Interface: %s' % (info['interface_id']), 'output')

        self.my_output.print_stream('## Remote End', 'output')
        self.my_output.print_stream('- Sys Name: %s' % (info['sysName']), 'output')
        self.my_output.print_stream('- Sys Description: %s' % (info['sysDesc']), 'output')
        self.my_output.print_stream('- Chassis Type: %s' % (info['chassisIdT']), 'output')
        self.my_output.print_stream('- Chassis Id: %s' % (info['chassisIdV']), 'output')
        self.my_output.print_stream('- Port Type: %s' % (info['portIdT']), 'output')
        self.my_output.print_stream('- Port Id: %s' % (info['portIdV']), 'output')
        self.my_output.print_stream('- Port Desription: %s' % (info['portDesc']), 'output')
        self.my_output.print_stream('- VLAN: %s' % (info['portVlan']), 'output')
        if len(info['capability']) > 0:
            self.my_output.print_stream('- Capability', 'output')
            if isinstance(info['capability'], list):
                for cap in info['capability']:
                    self.my_output.print_stream('\t- %s' % (cap), 'output')
            else:
                for cap in info['capability'].split(','):
                    self.my_output.print_stream('\t- %s' % (cap), 'output')

        if info['xd']['ServerMoid'] is not None:
            for server in servers:
                if server['Moid'] == info['xd']['ServerMoid']:
                    self.print_server(server, 'AddOn')
                    self.my_output.print_stream('', 'output')
                    self.print_server_mac(server, info['mac'])
                    self.print_server_vc(server, 'AddOn')

        self.save_output(info['hash'], subdir='apic/lldp')

    def print_aci_node_lldp(self, info, controller, node_name, servers):
        self.print_page_header('LLDP Adjacency (%s:%s)' % (controller, node_name))
        self.print_aci_node_bar(controller, node_name, 'lldp')
        self.print_aci_node_table_bar(controller, node_name, 'lldp')

        order = [
            'Interface',
            'LLDP Port Desc',
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
            line = self.add_column(line, item['interface_id'])
            line = self.add_column(line, item['portDesc'])
            line = self.add_aci_lldp_nei_device(line, item)
            line = self.add_aci_lldp_nei_interface(line, item)
            line = '%s [Link](./lldp/%s.md)' % (
                line,
                item['hash']
            )

            self.my_output.print_stream(line, 'output')
            self.aci_node_lldp_count[controller][node_name] = self.aci_node_lldp_count[controller][node_name] + 1

        self.save_output('%s-%s-lldp' % (controller, node_name), subdir='apic')

        for item in items:
            self.print_aci_node_lldp_adjacency(
                item,
                controller,
                node_name,
                servers
            )

    def print_aci_lldp(self, info, controller):
        self.print_page_header('LLDP Adjacency (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'lldp')
        self.print_aci_controller_table_bar(controller, 'lldp')

        order = [
            'Node',
            'Interface',
            'LLDP Port Desc',
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
                '[%s](./%s-%s-lldp.md)' % (
                    item['node_name'],
                    controller,
                    item['node_name']
                )
            )
            line = self.add_column(line, item['interface_id'])
            line = self.add_column(line, item['portDesc'])
            line = self.add_aci_lldp_nei_device(line, item)
            line = self.add_aci_lldp_nei_interface(line, item)
            line = '%s [Link](./lldp/%s.md)' % (
                line,
                item['hash']
            )

            self.my_output.print_stream(line, 'output')
            self.aci_lldp_count[controller] = self.aci_lldp_count[controller] + 1

        self.save_output('%s-lldp' % (controller), subdir='apic')
