from lib.nexus import helper as nexus_helper


class MdNexusServerOutput():
    def __init__(self):
        pass

    def print_servers_nexus(self, servers, moids, tag, perserver=False, skip_empty=True):
        self.print_page_header('Servers connectivity to Nexus [%s]' % (tag))

        self.my_output.print_stream(
            '\n[Back](./README.md) [Servers](./server-%s.md) [MAC](./server-%s-mac.md) [Fabric](./server-%s-fabric.md) Nexus [ACI](./server-%s-aci.md)\n' % (
                tag,
                tag,
                tag,
                tag
            ),
            'output'
        )

        if perserver:
            for moid in moids:
                server_info = self.xd_handler.get_server_by_moid(moid)

                self.server_tag_count['%s-nexus' % (tag)] = 0
                for server in servers:
                    if server['Moid'] != moid:
                        continue

                    for fabric in server['Fabric']:
                        for intf in fabric['nexus']['intf']:
                            self.server_tag_count['%s-nexus' % (tag)] = self.server_tag_count['%s-nexus' % (tag)] + 1

                if self.server_tag_count['%s-nexus' % (tag)] == 0 and skip_empty:
                    continue

                self.my_output.print_stream(
                    '## %s [Inv](./compute/%s-inv.md) [Net](./compute/%s-net.md)\n' % (
                        server_info['Name'],
                        server_info['Moid'],
                        server_info['Moid']
                    ),
                    'output'
                )

                order = [
                    'Adapter',
                    'Interface',
                    'Nexus',
                    'Interface',
                    'Source'
                ]
                self.print_table_header(order)

                for server in servers:
                    if server['Moid'] != moid:
                        continue

                    for fabric in server['Fabric']:
                        for intf in fabric['nexus']['intf']:
                            line = ''
                            line = self.add_column(line, self.get_adapter_model(fabric['AdapterModel']))
                            line = self.add_column(line, self.get_interface_dn(fabric['InterfaceDn']))
                            line = self.add_server_nexus_interface(line, intf, add_empty=False)
                            line = self.add_column(line, ','.join(fabric['nexus']['src']))
                            self.my_output.print_stream(line, 'output')

        if not perserver:
            order = [
                'Server',
                'Adapter',
                'Interface',
                'Nexus',
                'Interface',
                'Source'
            ]
            self.print_table_header(order)

            self.server_tag_count['%s-nexus' % (tag)] = 0
            for server in servers:
                if server['Moid'] not in moids:
                    continue

                for fabric in server['Fabric']:
                    for intf in fabric['nexus']['intf']:
                        line = ''
                        line = self.add_column(
                            line,
                            '[%s](./compute/%s-net.md)' % (
                                server['Name'],
                                server['Moid']
                            )
                        )
                        line = self.add_column(line, self.get_adapter_model(fabric['AdapterModel']))
                        line = self.add_column(line, self.get_interface_dn(fabric['InterfaceDn']))
                        line = self.add_server_nexus_interface(line, intf, add_empty=False)
                        line = self.add_column(line, ','.join(fabric['nexus']['src']))
                        self.my_output.print_stream(line, 'output')
                        self.server_tag_count['%s-nexus' % (tag)] = self.server_tag_count['%s-nexus' % (tag)] + 1

        self.save_output('server-%s-nexus' % (tag))

    def print_nexus_fabric_servers(self, info):
        self.print_page_header('Servers (Nexus Fabric)')

        line = 'All '
        for nexus_device_name in self.nexus_device_names:
            line = '%s[%s](./%s-server.md) ' % (line, nexus_device_name, nexus_device_name)

        self.my_output.print_stream(
            '\n%s\n' % (line.strip()),
            'output'
        )

        self.my_output.print_stream(
            '\n[Back](../README.md)\n',
            'output'
        )

        order = [
            'Nexus',
            'Interface',
            'Server',
            'VMWare',
            'OpenShift',
            'MAC',
            'LLDP',
            'MAC Table'
        ]
        self.print_table_header(order)

        moids = []

        for item in sorted(info, key=lambda i: (i['Nexus'], i['_index'])):
            if item['ServerMoid'] not in moids:
                self.nexus_fabric_server_count = self.nexus_fabric_server_count + 1
                moids.append(
                    item['ServerMoid']
                )

            if len(item['Lldp']) > 0:
                for litem in item['Lldp']:
                    line = ''
                    line = self.add_column(
                        line,
                        '[%s](./nexus/%s-server.md)' % (
                            item['Nexus'],
                            item['Nexus']
                        )
                    )
                    line = self.add_nexus_interface(line, item['Nexus'], item['InterfaceId'])
                    line = self.add_column(
                        line,
                        '[%s](../compute/%s-net.md) ' % (
                            item['ServerName'],
                            item['ServerMoid']
                        )
                    )
                    if self.xd_handler.get_server_vc_by_moid(item['ServerMoid']) is not None:
                        line = self.add_column(
                            line,
                            '[:white_check_mark:](./%s-vmware.md)' % (item['Nexus'])
                        )
                    else:
                        line = self.add_column(line, '---')

                    if self.xd_handler.get_ocp_from_tags(item['ServerTags']) is not None:
                        line = self.add_column(
                            line,
                            '[:white_check_mark:](./%s-ocp.md)' % (item['Nexus'])
                        )
                    else:
                        line = self.add_column(line, '---')

                    line = self.add_column(line, item['MacAddress'])
                    line = self.add_column(
                        line,
                        '[Link](./lldp/%s.md)' % (
                            litem['hash']
                        )
                    )

                    if len(item['Mac']) > 0:
                        line = '%s Yes' % (
                            line
                        )
                    else:
                        line = '%s No' % (
                            line
                        )

                    self.my_output.print_stream(line, 'output')
                    self.nexus_fabric_server_intf_count = self.nexus_fabric_server_intf_count + 1

            else:
                line = ''
                line = self.add_column(
                    line,
                    '[%s](./nexus/%s-server.md)' % (
                        item['Nexus'],
                        item['Nexus']
                    )
                )
                line = self.add_nexus_interface(line, item['Nexus'], item['InterfaceId'])
                line = self.add_column(
                    line,
                    '[%s](../compute/%s-net.md) ' % (
                        item['ServerName'],
                        item['ServerMoid']
                    )
                )
                if self.xd_handler.get_server_vc_by_moid(item['ServerMoid']) is not None:
                    line = self.add_column(
                        line,
                        '[:white_check_mark:](./%s-vmware.md)' % (item['Nexus'])
                    )
                else:
                    line = self.add_column(line, '---')

                if self.xd_handler.get_ocp_from_tags(item['ServerTags']) is not None:
                    line = self.add_column(
                        line,
                        '[:white_check_mark:](./%s-ocp.md)' % (item['Nexus'])
                    )
                else:
                    line = self.add_column(line, '---')

                line = self.add_column(line, item['MacAddress'])
                line = self.add_column(line, '---')

                if len(item['Mac']) > 0:
                    line = '%s Yes' % (
                        line
                    )
                else:
                    line = '%s No' % (
                        line
                    )

                self.my_output.print_stream(line, 'output')
                self.nexus_fabric_server_intf_count = self.nexus_fabric_server_intf_count + 1

        self.save_output('server', subdir='nexus')

    def print_nexus_servers(self, info, name):
        self.print_page_header('Servers (%s)' % (name))
        self.print_nexus_devices_bar(name, 'server')
        self.print_nexus_table_bar(name, 'server')

        order = [
            'Interface',
            'Server',
            'Interface',
            'MAC',
            'VMWare',
            'OpenShift',
            'LLDP',
            'MAC Table'
        ]
        self.print_table_header(order)

        for item in sorted(info, key=lambda i: i['_index']):
            if len(item['Lldp']) > 0:
                if len(item['Lldp']) > 1:
                    print('[ERROR] %s - %s - %s' % (name, item['InterfaceId'], len(item['Lldp'])))

                for litem in item['Lldp']:
                    if litem['device_name'] == name:
                        line = ''
                        line = self.add_nexus_interface(line, name, item['InterfaceId'])
                        line = self.add_column(
                            line,
                            '[%s](../compute/%s-net.md) ' % (
                                item['ServerName'],
                                item['ServerMoid']
                            )
                        )
                        line = self.add_column(line, item['ServerInterface'])
                        line = self.add_column(line, item['MacAddress'])
                        if self.xd_handler.get_server_vc_by_moid(item['ServerMoid']) is not None:
                            line = self.add_column(
                                line,
                                '[:white_check_mark:](./%s-vmware.md)' % (name)
                            )
                        else:
                            line = self.add_column(line, '---')

                        if self.xd_handler.get_ocp_from_tags(item['ServerTags']) is not None:
                            line = self.add_column(
                                line,
                                '[:white_check_mark:](./%s-ocp.md)' % (name)
                            )
                        else:
                            line = self.add_column(line, '---')

                        line = self.add_column(
                            line,
                            '[Link](./lldp/%s.md)' % (
                                litem['hash']
                            )
                        )

                        if len(item['Mac']) > 0:
                            line = '%s Yes' % (
                                line
                            )
                        else:
                            line = '%s No' % (
                                line
                            )

                        self.my_output.print_stream(line, 'output')
                        self.nexus_server_count[name] = self.nexus_server_count[name] + 1

            else:
                line = ''
                line = self.add_nexus_interface(line, name, item['InterfaceId'])
                line = self.add_column(
                    line,
                    '[%s](../compute/%s-net.md) ' % (
                        item['ServerName'],
                        item['ServerMoid']
                    )
                )

                line = self.add_column(line, item['ServerInterface'])
                line = self.add_column(line, item['MacAddress'])
                if self.xd_handler.get_server_vc_by_moid(item['ServerMoid']) is not None:
                    line = self.add_column(
                        line,
                        '[:white_check_mark:](./%s-vmware.md)' % (item['Nexus'])
                    )
                else:
                    line = self.add_column(line, '---')

                if self.xd_handler.get_ocp_from_tags(item['ServerTags']) is not None:
                    line = self.add_column(
                        line,
                        '[:white_check_mark:](./%s-ocp.md)' % (item['Nexus'])
                    )
                else:
                    line = self.add_column(line, '---')

                line = self.add_column(line, '---')

                if len(item['Mac']) > 0:
                    line = '%s Yes' % (
                        line
                    )
                else:
                    line = '%s No' % (
                        line
                    )

                self.my_output.print_stream(line, 'output')
                self.nexus_server_count[name] = self.nexus_server_count[name] + 1

        self.save_output('%s-server' % (name), subdir='nexus')
