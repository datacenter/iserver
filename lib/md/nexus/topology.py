from lib import ip_helper
from lib.nexus import helper as nexus_helper


class MdNexusTopologyOutput():
    def __init__(self):
        pass

    def get_nexus_topology(self, interfaces):
        links = []

        for device_name in self.nexus_device_names:
            for item in interfaces[device_name]:
                if item['type'] == 'eth':
                    if item['nei_device_name'] is None:
                        continue

                    if item['nei_device_name'] not in self.nexus_device_names:
                        continue

                    if item['nei_interface_name'] is not None and item['nei_interface_name'] == 'mgmt0':
                        continue

                    item['role'] = 'leaf'
                    if item['nexus_name'].startswith('spine-'):
                        item['role'] = 'spine'

                    links.append(
                        item
                    )

        paired = []
        b2b = []
        for link in links:
            if link['role'] == 'spine':
                link_pair = {}
                link_pair['order'] = 0
                link_pair['device_a'] = link['nexus_name']
                link_pair['interface_a'] = link['interface']
                link_pair['interface_a_hash'] = link['hash']
                link_pair['pc_a'] = link['portchan']
                link_pair['pc_a_hash'] = None
                if link['pc_state'] is not None:
                    link_pair['pc_a_hash'] = link['pc_state']['hash']
                link_pair['index_a'] = link['_index']
                link_pair['cdp_a'] = link['cdp_hash']
                link_pair['lldp_a'] = link['lldp_hash']
                link_pair['device_b'] = link['nei_device_name']
                link_pair['interface_b'] = link['nei_interface_name']
                link_pair['interface_b_hash'] = None
                link_pair['pc_b'] = None
                link_pair['pc_b_hash'] = None
                link_pair['cdp_b'] = None
                link_pair['lldp_b'] = None
                paired.append('%s-%s' % (link['nexus_name'], link['interface']))

                for other_end in links:
                    if other_end['nexus_name'] == link['nei_device_name']:
                        if other_end['interface'] == link['nei_interface_name']:
                            link_pair['interface_b_hash'] = other_end['hash']
                            link_pair['pc_b'] = other_end['portchan']
                            link_pair['pc_b_hash'] = None
                            if other_end['pc_state'] is not None:
                                link_pair['pc_b_hash'] = other_end['pc_state']['hash']
                            link_pair['cdp_b'] = other_end['cdp_hash']
                            link_pair['lldp_b'] = other_end['lldp_hash']
                            paired.append('%s-%s' % (other_end['nexus_name'], other_end['interface']))

                b2b.append(link_pair)

        for link in links:
            if link['role'] == 'leaf':
                if '%s-%s' % (link['nexus_name'], link['interface']) in paired:
                    continue

                link_pair = {}
                link_pair['order'] = 1
                link_pair['device_a'] = link['nexus_name']
                link_pair['interface_a'] = link['interface']
                link_pair['interface_a_hash'] = link['hash']
                link_pair['pc_a'] = link['portchan']
                link_pair['pc_a_hash'] = None
                if link['pc_state'] is not None:
                    link_pair['pc_a_hash'] = link['pc_state']['hash']
                link_pair['index_a'] = link['_index']
                link_pair['cdp_a'] = link['cdp_hash']
                link_pair['lldp_a'] = link['lldp_hash']
                link_pair['device_b'] = link['nei_device_name']
                link_pair['interface_b'] = link['nei_interface_name']
                link_pair['interface_b_hash'] = None
                link_pair['pc_b'] = None
                link_pair['pc_b_hash'] = None
                link_pair['cdp_b'] = None
                link_pair['lldp_b'] = None
                paired.append('%s-%s' % (link['nexus_name'], link['interface']))

                for other_end in links:
                    if other_end['nexus_name'] == link['nei_device_name']:
                        if other_end['interface'] == link['nei_interface_name']:
                            link_pair['interface_b_hash'] = other_end['hash']
                            link_pair['pc_b'] = other_end['portchan']
                            if other_end['pc_state'] is not None:
                                link_pair['pc_b_hash'] = other_end['pc_state']['hash']
                            link_pair['cdp_b'] = other_end['cdp_hash']
                            link_pair['lldp_b'] = other_end['lldp_hash']
                            paired.append('%s-%s' % (other_end['nexus_name'], other_end['interface']))

                b2b.append(link_pair)

        b2b = sorted(
            b2b,
            key = lambda i: (
                i['order'],
                i['device_a'],
                i['index_a']
            )
        )

        return b2b

    def print_nexus_topology(self, interfaces):
        self.print_page_header('Nexus Devices Topology')
        self.print_nexus_overview_bar('topology')

        order = [
            'Device A',
            'Eth A',
            'PC A',
            'CDP A',
            'LLDP A',
            'Device B',
            'Eth B',
            'PC B',
            'CDP B',
            'LLDP B'
        ]
        self.print_table_header(order)

        links = self.get_nexus_topology(interfaces)
        for item in links:
            line = ''
            line = self.add_column(line, item['device_a'])
            if item['interface_a_hash'] is None:
                line = self.add_column(
                    line,
                    nexus_helper.get_nexus_interface_id(item['interface_a'])
                )
            else:
                line = self.add_column(
                    line,
                    '[%s](./eth/%s.md)' % (
                        nexus_helper.get_nexus_interface_id(item['interface_a']),
                        item['interface_a_hash']
                    )
                )

            if item['pc_a_hash'] is None:
                line = self.add_column(line, item['pc_a'])
            else:
                line = self.add_column(line, '[%s](./pc/%s.md)' % (item['pc_a'], item['pc_a_hash']))

            if item['cdp_a'] is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, '[Link](./cdp/%s.md)' % (item['cdp_a']))

            if item['lldp_a'] is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, '[Link](./lldp/%s.md)' % (item['lldp_a']))

            line = self.add_column(line, item['device_b'])
            if item['interface_b_hash'] is None:
                line = self.add_column(
                    line,
                    nexus_helper.get_nexus_interface_id(item['interface_b'])
                )
            else:
                line = self.add_column(
                    line,
                    '[%s](./eth/%s.md)' % (
                        nexus_helper.get_nexus_interface_id(item['interface_b']),
                        item['interface_b_hash']
                    )
                )

            if item['pc_b_hash'] is None:
                line = self.add_column(line, item['pc_b'])
            else:
                line = self.add_column(line, '[%s](./pc/%s.md)' % (item['pc_b'], item['pc_b_hash']))

            if item['cdp_b'] is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, '[Link](./cdp/%s.md)' % (item['cdp_b']))

            if item['lldp_b'] is None:
                line = self.add_column(line, '---', last=True)
            else:
                line = self.add_column(line, '[Link](./lldp/%s.md)' % (item['lldp_b']), last=True)

            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '\n\n',
            'output'
        )

        self.save_output('topology', subdir='nexus')
