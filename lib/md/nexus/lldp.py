from lib.aci import helper as aci_helper
from lib.nexus import helper as nexus_helper


class MdNexusLldpOutput():
    def __init__(self):
        pass

    def add_nexus_lldp_nei_interface(self, line, item):
        done = False
        if item['chassis_id'].startswith('vmnic'):
            line = self.add_column(line, item['chassis_id'])
            done = True

        if item['port_id'].startswith('Eth'):
            if item['xd']['DeviceType'] is not None and item['xd']['DeviceType'] == 'Nexus' and item['xd']['NexusDevice'] is not None:
                done = True
                line = self.add_column(
                    line,
                    '[%s](./eth/%s.md)' % (
                        item['port_id'],
                        nexus_helper.get_nexus_interface_hash(item['xd']['NexusDevice'], item['port_id'])
                    )
                )

            if item['xd']['DeviceType'] is not None and item['xd']['DeviceType'] == 'FI' and item['xd']['FI'] is not None:
                done = True
                if self.xd_handler.is_fi_name(item['xd']['FI']):
                    line = self.add_column(
                        line,
                        '[%s](../fi/eth/%s.md)' % (
                            item['port_id'],
                            self.xd_handler.get_fi_interface_hash(
                                item['xd']['FI'],
                                item['port_id']
                            )
                        )
                    )
                else:
                    line = self.add_column(line, item['port_id'])

            if item['xd']['DeviceType'] is not None and item['xd']['DeviceType'] == 'ACI' and item['xd']['AciNodeId'] is not None:
                done = True
                line = self.add_column(
                    line,
                    '[%s](../apic/phy/%s.md)' % (
                        item['port_id'],
                        aci_helper.get_aci_interface_hash(item['xd']['AciApicName'], item['xd']['AciNodeId'], item['port_id'])
                    )
                )

            if not done:
                done = True
                line = self.add_column(line, item['port_id'])

        if not done:
            line = self.add_column(line, '---')

        return line

    def print_nexus_lldp_adjacency(self, info, servers):
        self.print_page_header('Nexus LLDP')

        self.my_output.print_stream('## Local End', 'output')
        self.my_output.print_stream('\n- Device: [%s](../%s-lldp.md)' % (info['nexus_name'], info['nexus_name']), 'output')
        self.my_output.print_stream('- Interface: [%s](../eth/%s.md)' % (info['l_port_id'], info['l_port_hash']), 'output')

        self.my_output.print_stream('## Remote End', 'output')
        self.my_output.print_stream('- Sys Name: %s' % (info['sys_name']), 'output')
        self.my_output.print_stream('- Sys Description: %s' % (info['sys_desc']), 'output')
        self.my_output.print_stream('- Chassis Type: %s' % (info['chassis_type']), 'output')
        self.my_output.print_stream('- Chassis Id: %s' % (info['chassis_id']), 'output')
        self.my_output.print_stream('- Port Type: %s' % (info['port_type']), 'output')
        self.my_output.print_stream('- Port Id: %s' % (info['port_id']), 'output')
        self.my_output.print_stream('- Port Desription: %s' % (info['port_desc']), 'output')
        self.my_output.print_stream('- VLAN: %s' % (info['vlan_id']), 'output')

        if info['xd']['ServerMoid'] is not None:
            for server in servers:
                if server['Moid'] == info['xd']['ServerMoid']:
                    self.print_server(server, 'AddOn')
                    self.my_output.print_stream('', 'output')
                    self.print_server_mac(server, info['mac'])

        self.save_output('%s' % (info['hash']), subdir='nexus/lldp')

    def print_nexus_lldp(self, info, name, servers):
        self.print_page_header('LLDP Adjacency (%s)' % (name))
        self.print_nexus_devices_bar(name, 'lldp')
        self.print_nexus_table_bar(name, 'lldp')

        order = [
            'Interface',
            'LLDP Port Desc',
            'Device',
            'Interface',
            'Info'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_nexus_interface(line, item['nexus_name'], item['l_port_id'])
            line = self.add_column(line, item['port_desc'])
            line = self.add_column(line, self.get_xd_device_link(item['xd'], nei='lldp'))
            line = self.add_nexus_lldp_nei_interface(line, item)
            line = '%s [Link](./lldp/%s.md)' % (
                line,
                item['hash']
            )

            self.my_output.print_stream(line, 'output')
            self.nexus_lldp_count[name] = self.nexus_lldp_count[name] + 1

        self.save_output('%s-lldp' % (name), subdir='nexus')

        for item in info:
            self.print_nexus_lldp_adjacency(item, servers)

    def print_nexus_lldp_all(self, info):
        self.print_page_header('LLDP Adjacency')
        self.print_nexus_overview_bar('lldp')

        order = [
            'Nexus',
            'Interface',
            'LLDP Port Desc',
            'Device',
            'Interface',
            'Info'
        ]
        self.print_table_header(order)

        for nexus_name in info:
            for item in info[nexus_name]:
                line = ''
                line = self.add_column(line, '[%s](./%s-lldp.md)' % (item['nexus_name'], item['nexus_name']))
                line = self.add_nexus_interface(line, item['nexus_name'], item['l_port_id'])
                line = self.add_column(line, item['port_desc'])
                line = self.add_column(line, self.get_xd_device_link(item['xd'], nei='lldp'))
                line = self.add_nexus_lldp_nei_interface(line, item)
                line = '%s [Link](./lldp/%s.md)' % (
                    line,
                    item['hash']
                )

                self.my_output.print_stream(line, 'output')

        self.save_output('lldp', subdir='nexus')
