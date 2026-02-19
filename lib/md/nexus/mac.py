from lib.nexus import helper as nexus_helper


class MdNexusMacOutput():
    def __init__(self):
        pass

    def print_nexus_mac_table(self, info, name):
        self.print_page_header('Local MAC Address Table (%s)' % (name))
        self.print_nexus_devices_bar(name, 'mac')
        self.print_nexus_table_bar(name, 'mac')

        order = [
            'Interface',
            'VLAN',
            'MAC',
            'Type',
            'Age',
            'Server',
            'Interface'
        ]
        self.print_table_header(order)

        for item in info:
            item["_index"] = 0
            if item['port'].startswith('Eth'):
                item['_index'] = int(item['port'].split('Eth')[1].split('/')[1])

        info = sorted(
            info,
            key = lambda i: (
                i['_index'],
                i['vlan']
            )
        )

        for item in info:
            if item['port'].startswith('Eth'):
                line = ''
                line = self.add_nexus_interface(line, item['nexus_name'], item['port'])
                line = self.add_column(
                    line, '[%s](./vlan/%s.md)' % (
                        item['vlan'],
                        nexus_helper.get_nexus_interface_hash(item['nexus_name'], 'Vlan%s' % (item['vlan']))
                    )
                )

                line = self.add_column(line, item['mac_addr'])
                line = self.add_column(line, item['type'])
                line = self.add_column(line, item['age'])

                if item['ServerName'] is None:
                    line = '%s --- | ' % (line)
                else:
                    line = '%s [%s](../compute/%s-net.md) |' % (
                        line,
                        item['ServerName'],
                        item['ServerMoid']
                    )

                if item['ServerName'] is None:
                    line = '%s --- | ' % (line)
                else:
                    line = '%s %s' % (line, item['ServerInterface'])

                self.my_output.print_stream(line, 'output')
                self.nexus_mac_count[name] = self.nexus_mac_count[name] + 1

        self.save_output('%s-mac' % (name), subdir='nexus')
