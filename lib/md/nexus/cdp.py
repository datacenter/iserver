from lib.aci import helper as aci_helper
from lib.nexus import helper as nexus_helper


class MdNexusCdpOutput():
    def __init__(self):
        pass

    def add_nexus_cdp_nei_interface(self, line, item):
        done = False

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
            line = self.add_column(line, item['port_id'])

        return line

    def print_nexus_cdp_adjacency(self, info, servers):
        self.print_page_header('Nexus CDP')

        self.my_output.print_stream('## Local End', 'output')
        self.my_output.print_stream('\n- Device: %s' % (info['device_name']), 'output')
        self.my_output.print_stream('- Interface: %s' % (info['intf_id']), 'output')
        if 'local_intf_mac' in info:
            self.my_output.print_stream('- MAC: %s' % (info['local_intf_mac']), 'output')
        if 'ifindex' in info:
            self.my_output.print_stream('- ifIndex: %s' % (info['ifindex']), 'output')
        if 'duplexmode' in info:
            self.my_output.print_stream('- Duplex: %s' % (info['duplexmode']), 'output')
        if 'mtu' in info:
            self.my_output.print_stream('- MTU: %s' % (info['mtu']), 'output')
        if 'nativevlan' in info:
            self.my_output.print_stream('- Native VLAN: %s' % (info['nativevlan']), 'output')
        if 'ttl' in info:
            self.my_output.print_stream('- TTL: %s' % (info['ttl']), 'output')

        self.my_output.print_stream('\n## Remote End', 'output')
        if 'sysname' in info:
            self.my_output.print_stream('- Sys Name: %s' % (info['sysname']), 'output')
        if 'device_id' in info:
            self.my_output.print_stream('- Device ID: %s' % (info['device_id']), 'output')
        if 'platform_id' in info:
            self.my_output.print_stream('- Platform: %s' % (info['platform_id']), 'output')
        if 'version' in info:
            self.my_output.print_stream('- Version: %s' % (info['version']), 'output')
        if 'v4addr' in info:
            self.my_output.print_stream('- IPv4: %s' % (info['v4addr']), 'output')
        if 'intf_id' in info:
            self.my_output.print_stream('- Interface: %s' % (info['port_id']), 'output')
        if 'remote_intf_mac' in info:
            self.my_output.print_stream('- MAC: %s' % (info['remote_intf_mac']), 'output')
        if 'capability' in info and len(info['capability']) > 0:
            self.my_output.print_stream('- Capabilities', 'output')
            if isinstance(info['capability'], list):
                for cap in info['capability']:
                    self.my_output.print_stream('\t- %s' % (cap), 'output')
            else:
                self.my_output.print_stream('\t- %s' % (info['capability']), 'output')

        if info['xd']['ServerMoid'] is not None:
            for server in servers:
                if server['Moid'] == info['xd']['ServerMoid']:
                    self.print_server(server, 'AddOn')
                    self.my_output.print_stream('', 'output')
                    self.print_server_mac(server, info['mac'])
                    self.print_server_vc(server, 'AddOn')

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output('%s' % (info['hash']), subdir='nexus/cdp')

    def print_nexus_cdp(self, info, name, servers):
        self.print_page_header('CDP Adjacency (%s)' % (name))
        self.print_nexus_devices_bar(name, 'cdp')
        self.print_nexus_table_bar(name, 'cdp')

        order = [
            'Interface',
            'CDP Platform',
            'CDP SysName',
            'Device',
            'Interface',
            'Info'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_nexus_interface(line, item['nexus_name'], item['intf_id'])
            line = self.add_column(line, item['platform_id'])
            line = self.add_column(line, item['sysname'])
            line = self.add_column(line, self.get_xd_device_link(item['xd'], nei='cdp'))
            line = self.add_nexus_cdp_nei_interface(line, item)
            line = '%s [Link](./cdp/%s.md)' % (
                line,
                item['hash']
            )

            self.my_output.print_stream(line, 'output')
            self.nexus_cdp_count[name] = self.nexus_cdp_count[name] + 1

        self.save_output('%s-cdp' % (name), subdir='nexus')

        for item in info:
            self.print_nexus_cdp_adjacency(item, servers)

    def print_nexus_cdp_all(self, info):
        self.print_page_header('CDP Adjacency')
        self.print_nexus_overview_bar('cdp')

        order = [
            'Nexus',
            'Interface',
            'CDP Platform',
            'CDP SysName',
            'Device',
            'Interface',
            'Info'
        ]
        self.print_table_header(order)

        for nexus_name in info:
            for item in info[nexus_name]:
                line = ''
                line = self.add_column(line, '[%s](./%s-cdp.md)' % (item['nexus_name'], item['nexus_name']))
                line = self.add_nexus_interface(line, item['nexus_name'], item['intf_id'])
                line = self.add_column(line, item['platform_id'])
                line = self.add_column(line, item['sysname'])
                line = self.add_column(line, self.get_xd_device_link(item['xd'], nei='cdp'))
                line = self.add_nexus_cdp_nei_interface(line, item)
                line = '%s [Link](./cdp/%s.md)' % (
                    line,
                    item['hash']
                )

                self.my_output.print_stream(line, 'output')

        self.save_output('cdp', subdir='nexus')
