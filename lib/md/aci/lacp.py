from lib import ip_helper


class MdAciLacpOutput():
    def __init__(self):
        pass

    def print_aci_lacp_adjacency(self, info, controller):
        self.print_page_header('ACI LACP')
        self.my_output.print_stream('- Dn: %s' % (info['dn']), 'output')
        self.my_output.print_stream('- Policy: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Admin state: %s' % (info['adminSt']), 'output')
        self.my_output.print_stream('- Operational state: %s' % (info['operChannelMode']), 'output')
        self.my_output.print_stream('- Switching state: %s' % (info['switchingSt']), 'output')

        order = [
            'Dn',
            'State',
            'Key',
            'Port',
            'PorPrio',
            'SysId',
            'SysPrio'
        ]

        line = ''
        line2 = ''
        for key in order:
            line = '%s %s |' % (line, key)
            line2 = '%s --- |' % (line2)
        line = line.rstrip('|')
        line2 = line2.rstrip('|')

        self.my_output.print_stream('', 'output')
        self.my_output.print_stream(line, 'output')
        self.my_output.print_stream(line2, 'output')

        for member in info['member']:
            line = '%s | %s |' % (member['tDn'], member['state'])

            found = False
            for lacp in info['lacp']:
                if lacp['id'] == member['tSKey']:
                    line = '%s %s |' % (line, lacp['adjacency']['key'])
                    line = '%s %s |' % (line, lacp['adjacency']['port'])
                    line = '%s %s |' % (line, lacp['adjacency']['portPrio'])
                    line = '%s %s |' % (line, lacp['adjacency']['sysId'])
                    line = '%s %s' % (line, lacp['adjacency']['sysPrio'])
                    found = True
                    break

            if not found:
                line = '%s --- | --- | --- | --- | ---' % (line)

            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

        for lacp in info['lacp']:
            if 'Server' in lacp and lacp['Server'] is not None:
                self.print_server(lacp['Server'], 'AddOn')
                self.my_output.print_stream('', 'output')
                self.print_server_mac(lacp['Server'], lacp['adjacency']['sysId'])
                self.print_server_vc(lacp['Server'], 'AddOn')

        link_hash = ip_helper.get_string_md5(
            '%s %s' % (
                controller,
                info['dn']
            )
        )

        self.save_output('%s' % (link_hash), subdir='apic/lacp')

    def print_aci_node_lacp(self, info, controller, node_name, mapping):
        self.print_page_header('LACP Adjacency (%s:%s)' % (controller, node_name))
        self.print_aci_node_bar(controller, node_name, 'lacp')
        self.print_aci_node_table_bar(controller, node_name, 'lacp')

        order = [
            'Port Channel',
            'Policy',
            'Phy Intf',
            'MAC',
            'Server',
            'LACP'
        ]

        line = ''
        line2 = ''
        for key in order:
            line = '%s %s |' % (line, key)
            line2 = '%s --- |' % (line2)
        line = line.rstrip('|')
        line2 = line2.rstrip('|')

        self.my_output.print_stream(line, 'output')
        self.my_output.print_stream(line2, 'output')

        for item in info:
            if mapping[controller][item['node_id']] != node_name:
                continue

            for x in range(4):
                try:
                    if item['lacp'][x]['id']:
                        pass
                except BaseException:
                    break

                if x == 0:
                    line = '%s |' % (item['id'])
                    line = '%s %s |' % (line, item['name'])
                    line = '%s %s |' % (line, item['lacp'][x]['id'])

                    try:
                        line = '%s %s |' % (line, item['lacp'][x]['adjacency']['sysId'])
                    except BaseException:
                        line = '%s --- |' % (line)

                    if item['lacp'][x]['ServerMoid'] is None:
                        line = '%s --- |' % (line)
                    else:
                        line = '%s [%s](../compute/%s-net.md) |' % (
                            line,
                            item['lacp'][x]['ServerName'],
                            item['lacp'][x]['ServerMoid']
                        )

                    link_hash = ip_helper.get_string_md5(
                        '%s %s' % (
                            controller,
                            item['dn']
                        )
                    )
                    line = '%s [Link](./lacp/%s.md)' % (line, link_hash)

                if x > 0:
                    line = ' | | |'
                    try:
                        line = '%s %s |' % (line, item['lacp'][x]['adjacency']['sysId'])
                    except BaseException:
                        line = '%s --- |' % (line)

                    if item['lacp'][x]['ServerMoid'] is None:
                        line = '%s --- | ---' % (line)
                    else:
                        line = '%s [%s](../compute/%s-net.md) | ---' % (
                            line,
                            item['lacp'][x]['ServerName'],
                            item['lacp'][x]['ServerMoid']
                        )

                self.my_output.print_stream(line, 'output')
                self.aci_node_lacp_count[controller][node_name] = self.aci_node_lacp_count[controller][node_name] + 1

        self.save_output('%s-%s-lacp' % (controller, node_name), subdir='apic')

        for item in info:
            self.print_aci_lacp_adjacency(item, controller)

    def print_aci_lacp(self, info, controller, mapping):
        self.print_page_header('Active LACP Adjacency')

        self.my_output.print_stream(
            '## %s\n' % (controller),
            'output'
        )

        self.my_output.print_stream(
            '\n[Back](../README.md) [Server](./%s-server.md) [EP](./%s-ep.md) [LLDP](./%s-lldp.md)\n' % (
                controller,
                controller,
                controller
            ),
            'output'
        )

        node_ids = []
        for item in info:
            if item['node_id'] not in node_ids:
                node_ids.append(
                    item['node_id']
                )

        node_ids = sorted(node_ids)

        for node_id in node_ids:
            self.my_output.print_stream('## Node: %s [%s]\n' % (mapping[controller][node_id], node_id), 'output')

            count = 0
            for item in info:
                if item['node_id'] != node_id:
                    continue

                try:
                    x = item['lacp'][0]['adjacency']['sysId']
                    count = count + 1
                except BaseException:
                    continue

            if count == 0:
                continue

            order = [
                'Port Channel',
                'Phy Intf',
                'MAC',
                'Server',
                'LACP'
            ]

            line = ''
            line2 = ''
            for key in order:
                line = '%s %s |' % (line, key)
                line2 = '%s --- |' % (line2)
            line = line.rstrip('|')
            line2 = line2.rstrip('|')

            self.my_output.print_stream(line, 'output')
            self.my_output.print_stream(line2, 'output')

            for item in info:
                if item['node_id'] != node_id:
                    continue

                for x in range(4):
                    if x == 0:
                        line = '%s |' % (item['id'])
                        try:
                            line = '%s %s |' % (line, item['lacp'][x]['id'])
                        except BaseException:
                            break

                        try:
                            line = '%s %s |' % (line, item['lacp'][x]['adjacency']['sysId'])
                        except BaseException:
                            line = '%s --- |' % (line)

                        if item['lacp'][x]['ServerMoid'] is None:
                            line = '%s --- |' % (line)
                        else:
                            line = '%s [%s](../compute/%s-net.md) |' % (
                                line,
                                item['lacp'][x]['ServerName'],
                                item['lacp'][x]['ServerMoid']
                            )

                        link_hash = ip_helper.get_string_md5(
                            '%s %s' % (
                                controller,
                                item['dn']
                            )
                        )
                        line = '%s [Link](./lacp/%s.md)' % (line, link_hash)

                    if x > 0:
                        line = ' | | |'
                        try:
                            test = '%s %s |' % (line, item['lacp'][x]['id'])
                        except BaseException:
                            break

                        try:
                            line = '%s %s |' % (line, item['lacp'][x]['adjacency']['sysId'])
                        except BaseException:
                            line = '%s --- |' % (line)

                        if item['lacp'][x]['ServerMoid'] is None:
                            line = '%s --- | ---' % (line)
                        else:
                            line = '%s [%s](../compute/%s-net.md) | ---' % (
                                line,
                                item['lacp'][x]['ServerName'],
                                item['lacp'][x]['ServerMoid']
                            )

                    self.my_output.print_stream(line, 'output')
                    self.aci_lacp_count[controller] = self.aci_lacp_count[controller] + 1

        self.save_output('%s-lacp' % (controller), subdir='apic')
