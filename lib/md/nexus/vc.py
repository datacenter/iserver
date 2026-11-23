class MdNexusVcOutput():
    def __init__(self):
        pass

    def print_nexus_fabric_servers_vcenter_fabric_view(self, info, moids, vcenter):
        self.nexus_fabric_vcenter_count[vcenter] = len(moids)
        self.nexus_fabric_vcenter_intf_count[vcenter] = 0

        self.print_page_header('vCenter [%s] (Nexus Fabric) \n' % (vcenter))
        self.my_output.print_stream(
            '\n[Back](../README.md) Fabric [VMWare](./vcenter-%s-server-vmware.md)\n' % (vcenter),
            'output'
        )

        order = [
            'Nexus',
            'Interface',
            'Server',
            'Port',
            'MAC',
            'LLDP',
            'MAC Table'
        ]
        self.print_table_header(order)

        for item in sorted(info, key=lambda i: (i['Nexus'], i['_index'])):
            if item['ServerMoid'] not in moids:
                continue

            if len(item['Lldp']) > 0:
                for litem in item['Lldp']:
                    line = ''
                    line = self.add_column(line, '[%s](./%s-vmware.md)' % (item['Nexus'], item['Nexus']))
                    line = self.add_nexus_interface(line, item['Nexus'], item['InterfaceId'])
                    line = self.add_column(
                        line,
                        '[%s](../compute/%s-net.md) ' % (
                            item['ServerName'],
                            item['ServerMoid']
                        )
                    )
                    line = self.add_column(line, item['ServerInterface'])
                    line = self.add_column(line, item['MacAddress'])

                    line = '%s [Link](./lldp/%s.md) |' % (
                        line,
                        litem['hash']
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
                    self.nexus_fabric_vcenter_intf_count[vcenter] = self.nexus_fabric_vcenter_intf_count[vcenter] + 1

            else:
                line = ''
                line = self.add_column(line, '[%s](./%s-vmware.md)' % (item['Nexus'], item['Nexus']))
                line = self.add_nexus_interface(line, item['Nexus'], item['InterfaceId'])
                line = self.add_column(
                    line,
                    '[%s](../compute/%s-net.md) ' % (
                        item['ServerName'],
                        item['ServerMoid']
                    )
                )
                line = self.add_column(line, item['ServerInterface'])
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
                self.nexus_fabric_vcenter_intf_count[vcenter] = self.nexus_fabric_vcenter_intf_count[vcenter] + 1

        self.save_output('vcenter-%s-server-fabric' % (vcenter), subdir='nexus')

    def print_nexus_fabric_servers_vcenter_vmware_view(self, info, moids, vcenter):
        self.print_page_header('vCenter [%s] (Nexus Fabric)' % (vcenter))

        self.my_output.print_stream(
            '\n[Back](../README.md) [Fabric](./vcenter-%s-server-fabric.md) VMWare\n' % (vcenter),
            'output'
        )

        order = [
            'Nexus',
            'Interface',
            'Cluster',
            'Host',
            'Device',
            'vSwitch'
        ]
        self.print_table_header(order)

        for item in sorted(info, key=lambda i: (i['Nexus'], i['_index'])):
            if item['ServerMoid'] not in moids:
                continue

            if item['ServerInterface'] == 'imc':
                continue

            line = ''
            line = self.add_column(line, '[%s](./%s-vmware.md)' % (item['Nexus'], item['Nexus']))
            line = self.add_nexus_interface(line, item['Nexus'], item['InterfaceId'])

            vc_host = self.xd_handler.get_vc_host_by_serial(
                item['ServerSerial']
            )

            vc_pnic = self.xd_handler.get_vc_pnic_by_mac(
                item['MacAddress']
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
            self.nexus_fabric_vcenter_intf_count[vcenter] = self.nexus_fabric_vcenter_intf_count[vcenter] + 1

        self.save_output('vcenter-%s-server-vmware' % (vcenter), subdir='nexus')

    def print_nexus_fabric_servers_vcenter(self, info, moids, vcenter):
        self.print_nexus_fabric_servers_vcenter_fabric_view(info, moids, vcenter)
        self.print_nexus_fabric_servers_vcenter_vmware_view(info, moids, vcenter)

    def print_nexus_servers_vcenter(self, info, name):
        self.print_page_header('VMWare Servers (%s)\n' % (name))
        self.print_nexus_devices_bar(name, 'vmware')
        self.print_nexus_table_bar(name, 'vmware')

        order = [
            'Interface',
            'Server',
            'Inteface',
            'Cluster',
            'Host',
            'Device',
            'vSwitch'
        ]
        self.print_table_header(order)

        for item in sorted(info, key=lambda i: i['_index']):
            vc_host = self.xd_handler.get_vc_host_by_serial(
                item['ServerSerial']
            )
            if vc_host is None:
                continue

            line = ''
            line = self.add_nexus_interface(line, name, item['InterfaceId'])
            line = '%s [%s](../compute/%s-net.md) |' % (
                line,
                item['ServerName'],
                item['ServerMoid']
            )

            line = self.add_column(line, item['ServerInterface'])

            vc_pnic = self.xd_handler.get_vc_pnic_by_mac(
                item['MacAddress']
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
            self.nexus_vmware_count[name] = self.nexus_vmware_count[name] + 1

        self.save_output('%s-vmware' % (name), subdir='nexus')
