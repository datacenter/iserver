from lib import ip_helper
from lib.aci import helper as aci_helper


class MdAciServerOutput():
    def __init__(self):
        pass

    def add_server_aci_sources(self, line, fabric):
        new_sources = []
        for source in fabric['aci']['src']:
            if source == 'ep':
                link_hash = ip_helper.get_string_md5(
                    '%s %s' % (
                        fabric['aci']['ep'][0]['apic'],
                        fabric['aci']['ep'][0]['dn']
                    )
                )
                new_sources.append(
                    '[ep](./apic/ep/%s.md)' % (link_hash)
                )
                continue

            if source == 'lacp':
                link_hash = ip_helper.get_string_md5(
                    '%s %s' % (
                        fabric['aci']['lacp'][0]['apic'],
                        fabric['aci']['lacp'][0]['dn']
                    )
                )
                new_sources.append(
                    '[lacp](./apic/lacp/%s.md)' % (link_hash)
                )
                continue

            if source == 'lldp':
                link_hash = ip_helper.get_string_md5(
                    '%s %s' % (
                        fabric['aci']['lldp'][0]['apic'],
                        fabric['aci']['lldp'][0]['dn']
                    )
                )
                new_sources.append(
                    '[lldp](./apic/lldp/%s.md)' % (link_hash)
                )
                continue

            new_sources.append(
                source
            )

        line = self.add_column(line, ','.join(new_sources))
        return line

    def print_aci_servers(self, servers, moids, tag, perserver=False):
        self.print_page_header('Servers connectivity to ACI [%s]' % (tag))

        self.my_output.print_stream(
            '\n[Back](./README.md) [Servers](./server-%s.md) [MAC](./server-%s-mac.md) [Fabric](./server-%s-fabric.md) [Nexus](./server-%s-nexus.md) ACI\n' % (
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

                self.my_output.print_stream(
                    '## %s [Inv](../compute/%s-inv.md) [Net](../compute/%s-net.md)\n' % (
                        server_info['Name'],
                        server_info['Moid'],
                        server_info['Moid']
                    ),
                    'output'
                )

                order = [
                    'Adapter',
                    'Interface',
                    'APIC',
                    'Node',
                    'Interface',
                    'Source'
                ]
                self.print_table_header(order)

                self.server_tag_count['%s-aci' % (tag)] = 0
                for server in servers:
                    if server['Moid'] != moid:
                        continue

                    for fabric in server['Fabric']:
                        for intf in fabric['aci']['intf']:
                            line = ''
                            line = self.add_column(line, self.get_adapter_model(fabric['AdapterModel']))
                            line = self.add_column(line, self.get_interface_dn(fabric['InterfaceDn']))
                            line = self.add_server_aci_interface(line, intf)
                            line = self.add_server_aci_sources(line, fabric)
                            self.my_output.print_stream(line, 'output')
                            self.server_tag_count['%s-aci' % (tag)] = self.server_tag_count['%s-aci' % (tag)] + 1

        if not perserver:
            order = [
                'Server',
                'Adapter',
                'Interface',
                'APIC',
                'Node',
                'Interface',
                'Source'
            ]
            self.print_table_header(order)

            self.server_tag_count['%s-aci' % (tag)] = 0
            for server in servers:
                if server['Moid'] not in moids:
                    continue

                for fabric in server['Fabric']:
                    for intf in fabric['aci']['intf']:
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
                        line = self.add_server_aci_interface(line, intf)
                        line = self.add_server_aci_sources(line, fabric)
                        self.my_output.print_stream(line, 'output')
                        self.server_tag_count['%s-aci' % (tag)] = self.server_tag_count['%s-aci' % (tag)] + 1

        self.save_output('server-%s-aci' % (tag))

    def print_aci_server(self, info, controller):
        self.print_page_header('Server (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'server')
        self.print_aci_controller_table_bar(controller, 'server')

        order = [
            'Node',
            'Intf',
            'Server',
            'MAC Address',
            'VMWare',
            'OpenShift',
            'EP',
            'LACP',
            'LLDP'
        ]
        self.print_table_header(order)

        for node_name in info:
            if len(info[node_name]) == 0:
                continue

            for item in sorted(info[node_name], key=lambda i: i['_index']):
                line = ''
                line = self.add_column(
                    line,
                    '[%s](./%s-%s-server.md)' % (
                        node_name,
                        controller,
                        node_name
                    )
                )

                item['interface_hash'] = aci_helper.get_aci_interface_hash(
                    controller,
                    self.xd_handler.get_aci_node_id_by_name(node_name),
                    item['InterfaceId']
                )

                line = self.add_phy_interface(
                    line,
                    item,
                    key_id='InterfaceId',
                    key_hash='interface_hash'
                )

                line = self.add_column(
                    line,
                    '[%s](../compute/%s-net.md)' % (
                        item['ServerName'],
                        item['ServerMoid']
                    )
                )

                line = self.add_column(line, item['Fabric']['MacAddress'])

                if self.xd_handler.get_server_vc_by_moid(item['ServerMoid']) is not None:
                    line = self.add_column(
                        line,
                        '[:white_check_mark:](./%s-vmware.md)' % (controller)
                    )
                else:
                    line = self.add_column(line, '---')

                if self.xd_handler.get_ocp_from_tags(item['ServerTags']) is not None:
                    line = self.add_column(
                        line,
                        '[:white_check_mark:](./%s-ocp.md)' % (controller)
                    )
                else:
                    line = self.add_column(line, '---')

                if len(item['Fabric']['aci']['ep']) > 0:
                    line = self.add_column(
                        line,
                        '[Link](./ep/%s.md)' % (
                            ip_helper.get_string_md5(
                                '%s %s' % (
                                    controller,
                                    item['Fabric']['aci']['ep'][0]['dn']
                                )
                            )
                        )
                    )
                else:
                    line = self.add_column(line, '---')

                if len(item['Fabric']['aci']['lacp']) > 0:
                    line = self.add_column(
                        line,
                        '[Link](./lacp/%s.md)' % (
                            ip_helper.get_string_md5(
                                '%s %s' % (
                                    controller,
                                    item['Fabric']['aci']['lacp'][0]['dn']
                                )
                            )
                        )
                    )
                else:
                    line = self.add_column(line, '---')

                if len(item['Fabric']['aci']['lldp']) > 0:
                    line = self.add_column(
                        line,
                        '[Link](./lldp/%s.md)' % (
                            ip_helper.get_string_md5(
                                '%s %s' % (
                                    controller,
                                    item['Fabric']['aci']['lldp'][0]['dn']
                                )
                            )
                        )
                    )
                else:
                    line = self.add_column(line, '---')

                self.my_output.print_stream(line, 'output')
                self.aci_server_count[controller] = self.aci_server_count[controller] + 1

        self.save_output('%s-server' % (controller), subdir='apic')

    def print_aci_vmware(self, info, controller):
        self.print_page_header('VMWare Server (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'vmware')
        self.print_aci_controller_table_bar(controller, 'vmware')

        self.my_output.print_stream('## Fabric view', 'output')

        order = [
            'Node',
            'Intf',
            'Server',
            'MAC Address',
            'EP',
            'LACP',
            'LLDP'
        ]
        self.print_table_header(order)

        for node_name in info:
            if len(info[node_name]) == 0:
                continue

            for item in sorted(info[node_name], key=lambda i: i['_index']):
                if self.xd_handler.get_server_vc_by_moid(item['ServerMoid']) is None:
                    continue

                line = ''
                line = self.add_column(
                    line,
                    '[%s](./%s-%s-server.md)' % (
                        node_name,
                        controller,
                        node_name
                    )
                )

                item['interface_hash'] = aci_helper.get_aci_interface_hash(
                    controller,
                    self.xd_handler.get_aci_node_id_by_name(node_name),
                    item['InterfaceId']
                )

                line = self.add_phy_interface(
                    line,
                    item,
                    key_id='InterfaceId',
                    key_hash='interface_hash'
                )

                line = self.add_column(
                    line,
                    '[%s](../compute/%s-net.md)' % (
                        item['ServerName'],
                        item['ServerMoid']
                    )
                )

                line = self.add_column(line, item['Fabric']['MacAddress'])

                if len(item['Fabric']['aci']['ep']) > 0:
                    line = self.add_column(
                        line,
                        '[Link](./ep/%s.md)' % (
                            ip_helper.get_string_md5(
                                '%s %s' % (
                                    controller,
                                    item['Fabric']['aci']['ep'][0]['dn']
                                )
                            )
                        )
                    )
                else:
                    line = self.add_column(line, '---')

                if len(item['Fabric']['aci']['lacp']) > 0:
                    line = self.add_column(
                        line,
                        '[Link](./lacp/%s.md)' % (
                            ip_helper.get_string_md5(
                                '%s %s' % (
                                    controller,
                                    item['Fabric']['aci']['lacp'][0]['dn']
                                )
                            )
                        )
                    )
                else:
                    line = self.add_column(line, '---')

                if len(item['Fabric']['aci']['lldp']) > 0:
                    line = self.add_column(
                        line,
                        '[Link](./lldp/%s.md)' % (
                            ip_helper.get_string_md5(
                                '%s %s' % (
                                    controller,
                                    item['Fabric']['aci']['lldp'][0]['dn']
                                )
                            )
                        )
                    )
                else:
                    line = self.add_column(line, '---')

                self.my_output.print_stream(line, 'output')
                self.aci_vmware_count[controller] = self.aci_vmware_count[controller] + 1

        self.my_output.print_stream('## VMWare view', 'output')

        order = [
            'Node',
            'Intf',
            'Server',
            'Cluster',
            'Host',
            'Device',
            'vSwitch'
        ]
        self.print_table_header(order)

        for node_name in info:
            if len(info[node_name]) == 0:
                continue

            for item in sorted(info[node_name], key=lambda i: i['_index']):
                if self.xd_handler.get_server_vc_by_moid(item['ServerMoid']) is None:
                    continue

                line = ''
                line = self.add_column(
                    line,
                    '[%s](./%s-%s-server.md)' % (
                        node_name,
                        controller,
                        node_name
                    )
                )

                item['interface_hash'] = aci_helper.get_aci_interface_hash(
                    controller,
                    self.xd_handler.get_aci_node_id_by_name(node_name),
                    item['InterfaceId']
                )

                line = self.add_phy_interface(
                    line,
                    item,
                    key_id='InterfaceId',
                    key_hash='interface_hash'
                )

                line = self.add_column(
                    line,
                    '[%s](../compute/%s-net.md)' % (
                        item['ServerName'],
                        item['ServerMoid']
                    )
                )

                vc_host = self.xd_handler.get_vc_host_by_serial(
                    item['ServerSerial']
                )

                vc_pnic = self.xd_handler.get_vc_pnic_by_mac(
                    item['Fabric']['MacAddress']
                )

                vc_cluster = None
                if vc_host is not None:
                    vc_cluster = self.xd_handler.get_vc_host_to_cluster(
                        vc_host['name']
                    )

                line = self.add_column(line, vc_cluster)

                if vc_host is not None:
                    line = self.add_column(line, vc_host['name'])
                else:
                    line = self.add_column(line, '---')

                if vc_pnic is not None:
                    line = self.add_column(line, vc_pnic['device'])
                    line = self.add_column(line, vc_pnic['uplink'], last=True)
                else:
                    line = self.add_column(line, '---')
                    line = self.add_column(line, '---', last=True)

                self.my_output.print_stream(line, 'output')

        self.save_output('%s-vmware' % (controller), subdir='apic')

    def print_aci_ocp(self, info, controller):
        self.print_page_header('OpenShift Server (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'ocp')
        self.print_aci_controller_table_bar(controller, 'ocp')

        order = [
            'Node',
            'Intf',
            'Server',
            'MAC Address',
            'EP',
            'LACP',
            'LLDP'
        ]
        self.print_table_header(order)

        for node_name in info:
            if len(info[node_name]) == 0:
                continue

            for item in sorted(info[node_name], key=lambda i: i['_index']):
                if self.xd_handler.get_ocp_from_tags(item['ServerTags']) is None:
                    continue

                line = ''
                line = self.add_column(
                    line,
                    '[%s](./%s-%s-server.md)' % (
                        node_name,
                        controller,
                        node_name
                    )
                )

                item['interface_hash'] = aci_helper.get_aci_interface_hash(
                    controller,
                    self.xd_handler.get_aci_node_id_by_name(node_name),
                    item['InterfaceId']
                )

                line = self.add_phy_interface(
                    line,
                    item,
                    key_id='InterfaceId',
                    key_hash='interface_hash'
                )

                line = self.add_column(
                    line,
                    '[%s](../compute/%s-net.md)' % (
                        item['ServerName'],
                        item['ServerMoid']
                    )
                )

                line = self.add_column(line, item['Fabric']['MacAddress'])

                if len(item['Fabric']['aci']['ep']) > 0:
                    line = self.add_column(
                        line,
                        '[Link](./ep/%s.md)' % (
                            ip_helper.get_string_md5(
                                '%s %s' % (
                                    controller,
                                    item['Fabric']['aci']['ep'][0]['dn']
                                )
                            )
                        )
                    )
                else:
                    line = self.add_column(line, '---')

                if len(item['Fabric']['aci']['lacp']) > 0:
                    line = self.add_column(
                        line,
                        '[Link](./lacp/%s.md)' % (
                            ip_helper.get_string_md5(
                                '%s %s' % (
                                    controller,
                                    item['Fabric']['aci']['lacp'][0]['dn']
                                )
                            )
                        )
                    )
                else:
                    line = self.add_column(line, '---')

                if len(item['Fabric']['aci']['lldp']) > 0:
                    line = self.add_column(
                        line,
                        '[Link](./lldp/%s.md)' % (
                            ip_helper.get_string_md5(
                                '%s %s' % (
                                    controller,
                                    item['Fabric']['aci']['lldp'][0]['dn']
                                )
                            )
                        )
                    )
                else:
                    line = self.add_column(line, '---')

                self.my_output.print_stream(line, 'output')
                self.aci_ocp_count[controller] = self.aci_ocp_count[controller] + 1

        self.save_output('%s-ocp' % (controller), subdir='apic')

    def print_aci_node_server(self, info, controller, node_name, node_id):
        self.print_page_header('Server (%s:%s)' % (controller, node_name))
        self.print_aci_node_bar(controller, node_name, 'server')
        self.print_aci_node_table_bar(controller, node_name, 'server')

        order = [
            'Intf',
            'Server',
            'MAC Address',
            'VMWare',
            'OpenShift',
            'EP',
            'LACP',
            'LLDP'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''

            item['interface_hash'] = aci_helper.get_aci_interface_hash(
                controller,
                node_id,
                item['InterfaceId']
            )

            line = self.add_phy_interface(
                line,
                item,
                key_id='InterfaceId',
                key_hash='interface_hash'
            )

            line = self.add_column(
                line,
                '[%s](../compute/%s-net.md)' % (
                    item['ServerName'],
                    item['ServerMoid']
                )
            )
            line = self.add_column(line, item['Fabric']['MacAddress'])

            if self.xd_handler.get_server_vc_by_moid(item['ServerMoid']) is not None:
                line = self.add_column(
                    line,
                    '[:white_check_mark:](./%s-%s-vmware.md)' % (controller, node_name)
                )
            else:
                line = self.add_column(line, '---')

            if self.xd_handler.get_ocp_from_tags(item['ServerTags']) is not None:
                line = self.add_column(
                    line,
                    '[:white_check_mark:](./%s-%s-ocp.md)' % (controller, node_name)
                )
            else:
                line = self.add_column(line, '---')

            if len(item['Fabric']['aci']['ep']) > 0:
                line = self.add_column(
                    line,
                    '[Link](./ep/%s.md)' % (
                        ip_helper.get_string_md5(
                            '%s %s' % (
                                controller,
                                item['Fabric']['aci']['ep'][0]['dn']
                            )
                        )
                    )
                )
            else:
                line = self.add_column(line, '---')

            if len(item['Fabric']['aci']['lacp']) > 0:
                line = self.add_column(
                    line,
                    '[Link](./lacp/%s.md)' % (
                        ip_helper.get_string_md5(
                            '%s %s' % (
                                controller,
                                item['Fabric']['aci']['lacp'][0]['dn']
                            )
                        )
                    )
                )
            else:
                line = self.add_column(line, '---')

            if len(item['Fabric']['aci']['lldp']) > 0:
                line = self.add_column(
                    line,
                    '[Link](./lldp/%s.md)' % (
                        ip_helper.get_string_md5(
                            '%s %s' % (
                                controller,
                                item['Fabric']['aci']['lldp'][0]['dn']
                            )
                        )
                    )
                )
            else:
                line = self.add_column(line, '---')

            self.my_output.print_stream(line, 'output')
            self.aci_node_server_count[controller][node_name] = self.aci_node_server_count[controller][node_name] + 1

        self.save_output('%s-%s-server' % (controller, node_name), subdir='apic')

    def print_aci_node_vmware(self, info, controller, node_name, node_id):
        self.print_page_header('VMWare Server (%s:%s)' % (controller, node_name))
        self.print_aci_node_bar(controller, node_name, 'vmware')
        self.print_aci_node_table_bar(controller, node_name, 'vmware')

        order = [
            'Intf',
            'Server',
            'Cluster',
            'Host',
            'Device',
            'vSwitch'
        ]
        self.print_table_header(order)

        for item in info:
            if self.xd_handler.get_server_vc_by_moid(item['ServerMoid']) is None:
                continue

            line = ''

            item['interface_hash'] = aci_helper.get_aci_interface_hash(
                controller,
                node_id,
                item['InterfaceId']
            )

            line = self.add_phy_interface(
                line,
                item,
                key_id='InterfaceId',
                key_hash='interface_hash'
            )

            line = self.add_column(
                line,
                '[%s](../compute/%s-net.md)' % (
                    item['ServerName'],
                    item['ServerMoid']
                )
            )

            vc_host = self.xd_handler.get_vc_host_by_serial(
                item['ServerSerial']
            )

            vc_pnic = self.xd_handler.get_vc_pnic_by_mac(
                item['Fabric']['MacAddress']
            )

            vc_cluster = None
            if vc_host is not None:
                vc_cluster = self.xd_handler.get_vc_host_to_cluster(
                    vc_host['name']
                )

            line = self.add_column(line, vc_cluster)

            if vc_host is not None:
                line = self.add_column(line, vc_host['name'])
            else:
                line = self.add_column(line, '---')

            if vc_pnic is not None:
                line = self.add_column(line, vc_pnic['device'])
                line = self.add_column(line, vc_pnic['uplink'], last=True)
            else:
                line = self.add_column(line, '---')
                line = self.add_column(line, '---', last=True)

            self.my_output.print_stream(line, 'output')
            self.aci_node_vmware_count[controller][node_name] = self.aci_node_vmware_count[controller][node_name] + 1

        self.save_output('%s-%s-vmware' % (controller, node_name), subdir='apic')

    def print_aci_node_ocp(self, info, controller, node_name, node_id):
        self.print_page_header('OpenShift Server (%s:%s)' % (controller, node_name))
        self.print_aci_node_bar(controller, node_name, 'ocp')
        self.print_aci_node_table_bar(controller, node_name, 'ocp')

        order = [
            'Intf',
            'Server',
            'MAC Address'
        ]
        self.print_table_header(order)

        for item in info:
            if self.xd_handler.get_ocp_from_tags(item['ServerTags']):
                continue

            line = ''

            item['interface_hash'] = aci_helper.get_aci_interface_hash(
                controller,
                node_id,
                item['InterfaceId']
            )

            line = self.add_phy_interface(
                line,
                item,
                key_id='InterfaceId',
                key_hash='interface_hash'
            )

            line = self.add_column(
                line,
                '[%s](../compute/%s-net.md)' % (
                    item['ServerName'],
                    item['ServerMoid']
                )
            )
            line = self.add_column(line, item['Fabric']['MacAddress'])

            self.my_output.print_stream(line, 'output')
            self.aci_node_ocp_count[controller][node_name] = self.aci_node_ocp_count[controller][node_name] + 1

        self.save_output('%s-%s-ocp' % (controller, node_name), subdir='apic')
