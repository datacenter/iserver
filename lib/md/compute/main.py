import os
import json
from lib import file_helper
from lib import ip_helper
from lib.aci import helper as aci_helper
from lib.md.compute.inventory import MdComputeInventoryOutput
from lib.nexus import helper as nexus_helper


class MdComputeOutput(MdComputeInventoryOutput):
    def __init__(self):
        MdComputeInventoryOutput.__init__(self)

    def get_compute_template_dir(self):
        main_dir = file_helper.get_main_dir()
        if main_dir is None:
            return None

        directory = os.path.join(
            os.path.join(
                os.path.join(
                    main_dir,
                    'templates'
                ),
                'md'
            ),
            'compute'
        )

        return directory

    def add_server_power_tick(self, line, server_info):
        if server_info['OperPowerState'] == 'on':
            line = self.add_column(line, ':white_check_mark:')
        else:
            line = self.add_column(line, ':x:')
        return line

    def add_server_connected_tick(self, line, server_info):
        if server_info['Connected']:
            line = self.add_column(line, ':white_check_mark:')
        else:
            line = self.add_column(line, ':x:')
        return line

    def add_server_aci_interface(self, line, intf):
        line = self.add_column(
            line,
            '[%s](./apic/%s-server.md)' % (
                intf.split(':')[0],
                intf.split(':')[0]
            )
        )
        line = self.add_column(
            line,
            '[%s](./apic/%s-%s-server.md)' % (
                intf.split(':')[1],
                intf.split(':')[0],
                self.xd_handler.get_aci_node_name_by_id(
                    intf.split(':')[1]
                )
            )
        )
        line = self.add_column(
            line,
            '[%s](./apic/phy/%s.md)' % (
                intf.split(':')[2],
                aci_helper.get_aci_interface_hash(
                    intf.split(':')[0],
                    intf.split(':')[1],
                    intf.split(':')[2]
                )
            )
        )

        return line

    def add_server_nexus_interface(self, line, intf, add_empty=False):
        if add_empty:
            line = self.add_column(line, '---')

        line = self.add_column(
            line,
            '[%s](./nexus/%s-server.md)' % (
                intf.split(':')[0],
                intf.split(':')[0]
            )
        )

        line = self.add_column(
            line,
            '[%s](./nexus/eth/%s.md)' % (
                intf.split(':')[1],
                nexus_helper.get_nexus_interface_hash(
                    intf.split(':')[0],
                    intf.split(':')[1]
                )
            )
        )
        return line

    def print_servers_list(self, servers_info, moids, tag):
        self.print_page_header('Servers [%s]' % (tag))

        self.my_output.print_stream(
            '\n[Back](./README.md) Servers [MAC](./server-%s-mac.md) [Fabric](./server-%s-fabric.md) [Nexus](./server-%s-nexus.md) [ACI](./server-%s-aci.md)\n' % (
                tag,
                tag,
                tag,
                tag
            ),
            'output'
        )

        order = [
            'Intersight',
            'IMC',
            'P',
            'I',
            'Model',
            'CPU',
            'GPU',
            'Memory',
            'Link'
        ]
        self.print_table_header(order)

        self.server_tag_count['%s' % (tag)] = 0
        for server_info in servers_info:
            if server_info['Moid'] not in moids:
                continue

            link = 'https://us-east-1.intersight.com/an/infrastructure-service/an/compute/physical-summaries/%s/server' % (
                server_info['Moid']
            )
            line = '[%s](%s) |' % (server_info['Name'], link)

            link = 'https://%s' % (
                server_info['ManagementIp']
            )
            line = '%s [%s](%s) |' % (line, server_info['ManagementIp'], link)

            if server_info['OperPowerState'] == 'on':
                line = self.add_column(line, ':white_check_mark:')
            else:
                line = self.add_column(line, ':x:')

            if server_info['Connected']:
                line = self.add_column(line, ':white_check_mark:')
            else:
                line = self.add_column(line, ':x:')

            line = self.add_column(line, server_info['TypeModel'])
            line = self.add_column(line, server_info['Cpu'])
            if len(server_info['GpuInfo']) > 0:
                line = self.add_column(line, ':white_check_mark:')
            else:
                line = self.add_column(line, '', mapping=False)

            line = '%s %s |' % (line, server_info['TotalMemoryUnit'])
            line = '%s [Inv](./compute/%s-inv.md) [Net](./compute/%s-net.md)' % (line, server_info['Moid'], server_info['Moid'])

            self.my_output.print_stream(line, 'output')
            self.server_tag_count['%s' % (tag)] = self.server_tag_count['%s' % (tag)] + 1

        self.save_output('server-%s' % (tag))

    def print_servers_fabric(self, servers, moids, tag, perserver=False):
        self.print_page_header('Servers connectivity to fabric [%s]' % (tag))

        self.my_output.print_stream(
            '\n[Back](./README.md) [Servers](./server-%s.md) [MAC](./server-%s-mac.md) Fabric [Nexus](./server-%s-nexus.md) [ACI](./server-%s-aci.md)\n' % (
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
                    'Switch',
                    'Interface'
                ]
                self.print_table_header(order)

                self.server_tag_count['%s-fabric' % (tag)] = 0
                for server in servers:
                    if server['Moid'] != moid:
                        continue

                    for fabric in server['Fabric']:
                        for intf in fabric['aci']['intf']:
                            line = ''
                            line = self.add_column(line, self.get_adapter_model(fabric['AdapterModel']))
                            line = self.add_column(line, self.get_interface_dn(fabric['InterfaceDn']))
                            line = self.add_server_aci_interface(line, intf)
                            self.my_output.print_stream(line, 'output')
                            self.server_tag_count['%s-fabric' % (tag)] = self.server_tag_count['%s-fabric' % (tag)] + 1

                        for intf in fabric['nexus']['intf']:
                            line = ''
                            line = self.add_column(line, self.get_adapter_model(fabric['AdapterModel']))
                            line = self.add_column(line, self.get_interface_dn(fabric['InterfaceDn']))
                            line = self.add_server_nexus_interface(line, intf, add_empty=True)
                            self.my_output.print_stream(line, 'output')
                            self.server_tag_count['%s-fabric' % (tag)] = self.server_tag_count['%s-fabric' % (tag)] + 1

        if not perserver:
            order = [
                'Server',
                'Adapter',
                'Interface',
                'APIC',
                'Switch',
                'Interface'
            ]
            self.print_table_header(order)

            self.server_tag_count['%s-fabric' % (tag)] = 0
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
                        self.my_output.print_stream(line, 'output')
                        self.server_tag_count['%s-fabric' % (tag)] = self.server_tag_count['%s-fabric' % (tag)] + 1

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
                        line = self.add_server_nexus_interface(line, intf, add_empty=True)
                        self.my_output.print_stream(line, 'output')
                        self.server_tag_count['%s-fabric' % (tag)] = self.server_tag_count['%s-fabric' % (tag)] + 1

        self.save_output('server-%s-fabric' % (tag))

    def print_servers_mac(self, macs, moids, tag, perserver=False):
        self.print_page_header('Servers MAC Addresses [%s]' % (tag))

        self.my_output.print_stream(
            '\n[Back](./README.md) [Servers](./server-%s.md) MAC [Fabric](./server-%s-fabric.md) [Nexus](./server-%s-nexus.md) [ACI](./server-%s-aci.md)\n' % (
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
                    'MAC',
                    'APIC',
                    'Switch',
                    'Interface',
                    'Source'
                ]
                self.print_table_header(order)

                self.server_tag_count['%s-mac' % (tag)] = 0
                for mac in macs:
                    if mac['ServerMoid'] != moid:
                        continue

                    line = '%s |' % (self.get_adapter_model(mac['AdapterModel']))
                    line = '%s %s |' % (line, self.get_interface_dn(mac['InterfaceDn']))
                    line = '%s %s |' % (line, mac['MacAddress'])
                    if len(mac['intf']) == 0:
                        line = '%s --- | --- | --- | ---' % (line)
                    else:
                        if len(mac['intf'][0].split(':')) == 2:
                            if self.xd_handler.is_fi_name(mac['intf'][0].split(':')[0]):
                                line = '%s --- | [%s](./fi/%s-server.md) | %s |' % (
                                    line,
                                    mac['intf'][0].split(':')[0],
                                    self.xd_handler.get_fi_hash(mac['intf'][0].split(':')[0]),
                                    mac['intf'][0].split(':')[1]
                                )
                            else:
                                line = '%s --- | [%s](./nexus/%s-server.md) | %s |' % (
                                    line,
                                    mac['intf'][0].split(':')[0],
                                    mac['intf'][0].split(':')[0],
                                    mac['intf'][0].split(':')[1]
                                )
                        else:
                            line = '%s [%s](./apic/%s-server.md) | %s | %s |' % (
                                line,
                                mac['intf'][0].split(':')[0],
                                mac['intf'][0].split(':')[0],
                                mac['intf'][0].split(':')[1],
                                mac['intf'][0].split(':')[2]
                            )

                        new_sources = []
                        for source in mac['src']:
                            if source == 'mac-table':
                                if len(mac['intf'][0].split(':')) == 2:
                                    new_sources.append(
                                        '[mac](./nexus/%s-mac.md)' % (
                                            mac['intf'][0].split(':')[0]
                                        )
                                    )
                                    continue

                            if source == 'ep':
                                if len(mac['intf'][0].split(':')) == 3:
                                    new_sources.append(
                                        '[ep](./apic/%s-ep.md)' % (
                                            mac['intf'][0].split(':')[0]
                                        )
                                    )
                                    continue

                            if source == 'lacp':
                                if len(mac['intf'][0].split(':')) == 3:
                                    new_sources.append(
                                        '[lacp](./apic/%s-lacp.md)' % (
                                            mac['intf'][0].split(':')[0]
                                        )
                                    )
                                    continue

                            if source == 'lldp':
                                if len(mac['intf'][0].split(':')) == 2:
                                    new_sources.append(
                                        '[lldp](./nexus/%s-lldp.md)' % (
                                            mac['intf'][0].split(':')[0]
                                        )
                                    )
                                    continue

                                if len(mac['intf'][0].split(':')) == 3:
                                    new_sources.append(
                                        '[lldp](./apic/%s-lldp.md)' % (
                                            mac['intf'][0].split(':')[0]
                                        )
                                    )
                                    continue

                            new_sources.append(
                                source
                            )

                        line = '%s %s' % (line, ','.join(new_sources))

                    self.my_output.print_stream(line, 'output')
                    self.server_tag_count['%s-mac' % (tag)] = self.server_tag_count['%s-mac' % (tag)] + 1

                    if len(mac['intf']) > 1:
                        for i in range(len(mac['intf'])):
                            if i == 0:
                                continue

                            line = ' | | | | '

                            if len(mac['intf'][i].split(':')) == 2:
                                if self.xd_handler.is_fi_name(mac['intf'][i].split(':')[0]):
                                    line = '%s --- | [%s](./fi/%s-server.md) | %s |' % (
                                        line,
                                        mac['intf'][i].split(':')[0],
                                        self.xd_handler.get_fi_hash(mac['intf'][i].split(':')[0]),
                                        mac['intf'][i].split(':')[1]
                                    )
                                else:
                                    line = '%s --- | [%s](./nexus/%s-server.md) | %s |' % (
                                        line,
                                        mac['intf'][i].split(':')[0],
                                        mac['intf'][i].split(':')[0],
                                        mac['intf'][i].split(':')[1]
                                    )
                            else:
                                line = '%s [%s](./apic/%s-server.md) | %s | %s |' % (
                                    line,
                                    mac['intf'][i].split(':')[0],
                                    mac['intf'][i].split(':')[0],
                                    mac['intf'][i].split(':')[1],
                                    mac['intf'][i].split(':')[2]
                                )

                            if len(mac['src']) == 0:
                                line = '%s ---' % (line)
                            else:
                                new_sources = []
                                for source in mac['src']:
                                    if source == 'mac-table':
                                        if len(mac['intf'][i].split(':')) == 2:
                                            new_sources.append(
                                                '[mac](./nexus/%s-mac.md)' % (
                                                    mac['intf'][0].split(':')[0]
                                                )
                                            )
                                            continue

                                    if source == 'ep':
                                        if len(mac['intf'][i].split(':')) == 3:
                                            new_sources.append(
                                                '[ep](./apic/%s-ep.md)' % (
                                                    mac['intf'][0].split(':')[0]
                                                )
                                            )
                                            continue

                                    if source == 'lacp':
                                        if len(mac['intf'][i].split(':')) == 3:
                                            new_sources.append(
                                                '[lacp](./apic/%s-lacp.md)' % (
                                                    mac['intf'][0].split(':')[0]
                                                )
                                            )
                                            continue

                                    if source == 'lldp':
                                        if len(mac['intf'][i].split(':')) == 2:
                                            new_sources.append(
                                                '[lldp](./nexus/%s-lldp.md)' % (
                                                    mac['intf'][0].split(':')[0]
                                                )
                                            )
                                            continue

                                        if len(mac['intf'][i].split(':')) == 3:
                                            new_sources.append(
                                                '[lldp](./apic/%s-lldp.md)' % (
                                                    mac['intf'][0].split(':')[0]
                                                )
                                            )
                                            continue

                                    new_sources.append(
                                        source
                                    )

                                line = '%s %s' % (line, ','.join(new_sources))

                            self.my_output.print_stream(line, 'output')

        if not perserver:
            order = [
                'MAC',
                'Server',
                'P',
                'I',
                'APIC',
                'Switch',
                'Interface',
                'Source'
            ]
            self.print_table_header(order)

            self.server_tag_count['%s-mac' % (tag)] = 0
            for mac in macs:
                if mac['ServerMoid'] not in moids:
                    continue

                line = ''
                line = self.add_column(line, mac['MacAddress'])
                line = self.add_column(
                    line,
                    '[%s](./compute/%s-net.md)' % (
                        mac['ServerName'],
                        mac['ServerMoid']
                    )
                )

                server_info = self.xd_handler.get_server_by_moid(
                    mac['ServerMoid']
                )
                line = self.add_server_power_tick(line, server_info)
                line = self.add_server_connected_tick(line, server_info)

                if len(mac['intf']) == 0:
                    line = self.add_column(line, '---')
                    line = self.add_column(line, '---')
                    line = self.add_column(line, '---')
                    line = self.add_column(line, '---')
                else:
                    if len(mac['intf'][0].split(':')) == 2:
                        device_name = mac['intf'][0].split(':')[0]
                        interface_name = mac['intf'][0].split(':')[1]

                        if self.xd_handler.is_nexus_device_name(device_name):
                            line = self.add_column(line, '---')
                            line = self.add_column(
                                line,
                                '[%s](./nexus/%s-server.md)' % (
                                    device_name,
                                    device_name
                                )
                            )
                            line = self.add_column(
                                line,
                                '[%s](./nexus/eth/%s.md)' % (
                                    interface_name,
                                    nexus_helper.get_nexus_interface_hash(
                                        device_name,
                                        interface_name
                                    )
                                )
                            )

                        if self.xd_handler.is_fi_name(device_name):
                            line = self.add_column(line, '---')
                            line = self.add_column(
                                line,
                                '[%s](./fi/%s-eth.md)' % (
                                    device_name,
                                    self.xd_handler.get_fi_hash(device_name)
                                )
                            )
                            line = self.add_column(
                                line,
                                '[%s](./fi/eth/%s.md)' % (
                                    interface_name,
                                    self.xd_handler.get_fi_interface_hash(
                                        device_name,
                                        interface_name
                                    )
                                )
                            )

                        if not self.xd_handler.is_nexus_device_name(device_name) and not self.xd_handler.is_fi_name(device_name):
                            line = self.add_column(line, '---')
                            line = self.add_column(line, device_name)
                            line = self.add_column(line, interface_name)

                    else:
                        # ACI
                        line = self.add_column(
                            line,
                            '[%s](./apic/%s-server.md)' % (
                                mac['intf'][0].split(':')[0],
                                mac['intf'][0].split(':')[0]
                            )
                        )
                        node_name = self.xd_handler.get_aci_node_name_by_id(
                            mac['intf'][0].split(':')[1]
                        )
                        line = self.add_column(
                            line,
                            '[%s](./apic/%s-%s-server.md)' % (
                                node_name,
                                mac['intf'][0].split(':')[0],
                                node_name
                            )
                        )
                        interface_hash = aci_helper.get_aci_interface_hash(
                            mac['intf'][0].split(':')[0],
                            mac['intf'][0].split(':')[1],
                            mac['intf'][0].split(':')[2]
                        )
                        line = self.add_column(
                            line,
                            '[%s](./apic/phy/%s.md)' % (
                                mac['intf'][0].split(':')[2],
                                interface_hash
                            )
                        )

                    new_sources = []
                    for source in mac['src']:
                        if source == 'mac-table':
                            if len(mac['intf'][0].split(':')) == 2:
                                new_sources.append(
                                    '[mac](./nexus/%s-mac.md)' % (
                                        mac['intf'][0].split(':')[0]
                                    )
                                )
                                continue

                        if source == 'ep':
                            if len(mac['intf'][0].split(':')) == 3:
                                new_sources.append(
                                    '[ep](./apic/%s-ep.md)' % (
                                        mac['intf'][0].split(':')[0]
                                    )
                                )
                                continue

                        if source == 'lacp':
                            if len(mac['intf'][0].split(':')) == 3:
                                new_sources.append(
                                    '[lacp](./apic/%s-lacp.md)' % (
                                        mac['intf'][0].split(':')[0]
                                    )
                                )
                                continue

                        if source == 'lldp':
                            if len(mac['intf'][0].split(':')) == 2:
                                new_sources.append(
                                    '[lldp](./nexus/%s-lldp.md)' % (
                                        mac['intf'][0].split(':')[0]
                                    )
                                )
                                continue

                            if len(mac['intf'][0].split(':')) == 3:
                                new_sources.append(
                                    '[lldp](./apic/%s-lldp.md)' % (
                                        mac['intf'][0].split(':')[0]
                                    )
                                )
                                continue

                        new_sources.append(
                            source
                        )

                    line = self.add_column(line, ', '.join(new_sources))

                self.my_output.print_stream(line, 'output')
                self.server_tag_count['%s-mac' % (tag)] = self.server_tag_count['%s-mac' % (tag)] + 1

                if len(mac['intf']) > 1:
                    for i in range(len(mac['intf'])):
                        if i == 0:
                            continue

                        line = ''
                        line = self.add_column(line, mac['MacAddress'])
                        line = self.add_column(
                            line,
                            '[%s](./compute/%s-net.md)' % (
                                mac['ServerName'],
                                mac['ServerMoid']
                            )
                        )
                        line = self.add_server_power_tick(line, server_info)
                        line = self.add_server_connected_tick(line, server_info)

                        if len(mac['intf'][i].split(':')) == 2:
                            # Nexus
                            line = self.add_column(line, '---')
                            line = self.add_column(
                                line,
                                '[%s](./nexus/%s-server.md)' % (
                                    mac['intf'][i].split(':')[0],
                                    mac['intf'][i].split(':')[0]
                                )
                            )
                            interface_hash = nexus_helper.get_nexus_interface_hash(
                                mac['intf'][i].split(':')[0],
                                mac['intf'][i].split(':')[1]
                            )
                            line = self.add_column(
                                line,
                                '[%s](./nexus/eth/%s.md)' % (
                                    mac['intf'][i].split(':')[1],
                                    interface_hash
                                )
                            )
                        else:
                            # ACI
                            line = self.add_column(
                                line,
                                '[%s](./apic/%s-server.md)' % (
                                    mac['intf'][i].split(':')[0],
                                    mac['intf'][i].split(':')[0]
                                )
                            )
                            node_name = self.xd_handler.get_aci_node_name_by_id(
                                mac['intf'][i].split(':')[1]
                            )
                            line = self.add_column(
                                line,
                                '[%s](./apic/%s-%s-server.md)' % (
                                    node_name,
                                    mac['intf'][i].split(':')[0],
                                    node_name
                                )
                            )
                            interface_hash = aci_helper.get_aci_interface_hash(
                                mac['intf'][i].split(':')[0],
                                mac['intf'][i].split(':')[1],
                                mac['intf'][i].split(':')[2]
                            )
                            line = self.add_column(
                                line,
                                '[%s](./apic/phy/%s.md)' % (
                                    mac['intf'][i].split(':')[2],
                                    interface_hash
                                )
                            )

                        if len(mac['src']) == 0:
                            line = self.add_column(line, '---')
                        else:
                            new_sources = []
                            for source in mac['src']:
                                if source == 'mac-table':
                                    if len(mac['intf'][i].split(':')) == 2:
                                        new_sources.append(
                                            '[mac](./nexus/%s-mac.md)' % (
                                                mac['intf'][0].split(':')[0]
                                            )
                                        )
                                        continue

                                if source == 'ep':
                                    if len(mac['intf'][i].split(':')) == 3:
                                        new_sources.append(
                                            '[ep](./apic/%s-ep.md)' % (
                                                mac['intf'][0].split(':')[0]
                                            )
                                        )
                                        continue

                                if source == 'lacp':
                                    if len(mac['intf'][i].split(':')) == 3:
                                        new_sources.append(
                                            '[lacp](./apic/%s-lacp.md)' % (
                                                mac['intf'][0].split(':')[0]
                                            )
                                        )
                                        continue

                                if source == 'lldp':
                                    if len(mac['intf'][i].split(':')) == 2:
                                        new_sources.append(
                                            '[lldp](./nexus/%s-lldp.md)' % (
                                                mac['intf'][0].split(':')[0]
                                            )
                                        )
                                        continue

                                    if len(mac['intf'][i].split(':')) == 3:
                                        new_sources.append(
                                            '[lldp](./apic/%s-lldp.md)' % (
                                                mac['intf'][0].split(':')[0]
                                            )
                                        )
                                        continue

                                new_sources.append(
                                    source
                                )

                            line = '%s %s' % (line, ','.join(new_sources))

                        line = self.add_column(line, ', '.join(new_sources))

        self.save_output('server-%s-mac' % (tag))
        file_helper.set_file_json('/tmp/server-%s-mac' % (tag), macs)

    def print_server(self, server_info, info_type, add_all_servers_link=True):
        if info_type == 'AddOn':
            self.my_output.print_stream(
                '## Server',
                'output'
            )
        else:
            self.print_page_header('Server %s' % (info_type))

        link = 'https://us-east-1.intersight.com/an/infrastructure-service/an/compute/physical-summaries/%s/server' % (
            server_info['Moid']
        )

        self.my_output.print_stream(
            '- Intersight Name: [%s](%s)' % (server_info['Name'], link),
            'output'
        )

        self.my_output.print_stream(
            '- Intersight Moid: %s' % (server_info['Moid']),
            'output'
        )

        if server_info['Connected']:
            self.my_output.print_stream(
                '- Intersight Connected :white_check_mark:',
                'output'
            )
        else:
                self.my_output.print_stream(
                '- Intersight Connected :x:',
                'output'
            )

        if server_info['OperPowerState']:
            self.my_output.print_stream(
                '- Power :white_check_mark:',
                'output'
            )
        else:
            self.my_output.print_stream(
                '- Power :x:',
                'output'
            )

        link = 'https://%s' % (
            server_info['ManagementIp']
        )
        self.my_output.print_stream(
            '- IMC: [%s](%s)' % (server_info['ManagementIp'], link),
            'output'
        )

        self.my_output.print_stream(
            '- Model: %s' % (server_info['TypeModel']),
            'output'
        )

        self.my_output.print_stream(
            '- Serial: %s' % (server_info['Serial']),
            'output'
        )

        self.my_output.print_stream(
            '- CPU: %s' % (server_info['Cpu']),
            'output'
        )

        self.my_output.print_stream(
            '- Memory: %s' % (server_info['TotalMemoryUnit']),
            'output'
        )

        if 'Vc' in server_info and server_info['Vc'] is not None:
            if 'host' in server_info['Vc'] and server_info['Vc']['host'] is not None:
                if info_type == 'AddOn':
                    self.my_output.print_stream(
                        '- vCenter (%s): [%s](../../vc/host/%s.md)' % (
                            server_info['Vc']['host']['vc_instance'],
                            server_info['Vc']['host']['name'],
                            server_info['Vc']['host']['hash']
                        ),
                        'output'
                    )
                else:
                    self.my_output.print_stream(
                        '- vCenter (%s): [%s](../vc/host/%s.md)' % (
                            server_info['Vc']['host']['vc_instance'],
                            server_info['Vc']['host']['name'],
                            server_info['Vc']['host']['hash']
                        ),
                        'output'
                    )

        if 'Ocp' in server_info and server_info['Ocp'] is not None:
            if info_type == 'AddOn':
                self.my_output.print_stream(
                    '- OpenShift cluster [%s](../../ocp/cluster-%s.md) node [%s](../../ocp/node/%s-net.md)' % (
                        server_info['Ocp']['cluster'],
                        server_info['Ocp']['cluster'],
                        server_info['Ocp']['host'],
                        server_info['Ocp']['hash']
                    ),
                    'output'
                )

            if info_type == 'Networking':
                self.my_output.print_stream(
                    '- OpenShift cluster [%s](../ocp/cluster-%s.md) node [%s](../ocp/node/%s-net.md)' % (
                        server_info['Ocp']['cluster'],
                        server_info['Ocp']['cluster'],
                        server_info['Ocp']['host'],
                        server_info['Ocp']['hash']
                    ),
                    'output'
                )

            if info_type == 'Inventory':
                self.my_output.print_stream(
                    '- OpenShift cluster [%s](../ocp/cluster-%s.md) node [%s](../ocp/node/%s.md)' % (
                        server_info['Ocp']['cluster'],
                        server_info['Ocp']['cluster'],
                        server_info['Ocp']['host'],
                        server_info['Ocp']['hash']
                    ),
                    'output'
                )

        if info_type == 'Networking':
            self.my_output.print_stream(
                '- [Inventory information](./%s-inv.md)' % (server_info['Moid']),
                'output'
            )

        if info_type == 'Inventory':
            self.my_output.print_stream(
                '- [Network information](./%s-net.md)' % (server_info['Moid']),
                'output'
            )

        if info_type == 'AddOn':
            self.my_output.print_stream(
                '- [Inventory information](../../compute/%s-inv.md)' % (server_info['Moid']),
                'output'
            )
            self.my_output.print_stream(
                '- [Network information](../../compute/%s-net.md)' % (server_info['Moid']),
                'output'
            )

        if info_type in ['Inventory', 'Networking']:
            hw_info = self.get_server_hardware_info(
                server_info['Model']
            )
            if hw_info is not None:
                if 'links' in hw_info:
                    self.my_output.print_stream(
                        hw_info['links'],
                        'output'
                    )

            if add_all_servers_link:
                self.my_output.print_stream(
                    '\n[All servers](../server-all.md)\n',
                    'output'
                )

    def print_server_vc(self, server_info, info_type):
        if server_info['Vc']['host'] is None:
            return

        if info_type != 'AddOn':
            return

        if info_type == 'AddOn':
            self.my_output.print_stream(
                '## vCenter Host',
                'output'
            )

        self.my_output.print_stream(
            '- vCenter: %s' % (server_info['Vc']['host']['vCenter']['ip']),
            'output'
        )

        self.my_output.print_stream(
            '- Hostname: %s' % (server_info['Vc']['host']['name']),
            'output'
        )

        self.my_output.print_stream(
            '- Hypervisor: %s' % (server_info['Vc']['host']['hypervisor']),
            'output'
        )

    def get_server_hardware_template_dir(self):
        main_dir = file_helper.get_main_dir()
        if main_dir is None:
            return None

        directory = os.path.join(
            os.path.join(
                os.path.join(
                    main_dir,
                    'templates'
                ),
                'md'
            ),
            'compute'
        )

        return directory

    def get_server_hardware_info(self, model):
        base = self.get_server_hardware_template_dir()
        if base is None:
            return None

        directory = os.path.join(
            base,
            model
        )
        if not os.path.isdir(directory):
            return None

        info = {}
        info['picture'] = {}

        for filename in os.listdir(directory):
            if filename.split('.')[-1] == 'md':
                info[filename.split('.')[0]] = file_helper.get_file_text(
                    os.path.join(directory, filename)
                )

            if filename.split('.')[-1] == 'png':
                info['picture'][filename.split('.')[0]] = os.path.join(directory, filename)

        return info

    def add_server_hardware(self, model, name, title=None):
        info = self.get_server_hardware_info(model)
        if info is None:
            return

        if name in info['picture']:
            if title:
                self.my_output.print_stream('## %s' % (title), 'output')

            self.my_output.print_stream(
                '![%s](./hw/%s.png)' % (
                    name,
                    ip_helper.get_string_md5('%s %s' % (model, name))
                ),
                'output'
            )

        for key in info['picture']:
            self.copy_file(
                info['picture'][key],
                '%s.png' % (ip_helper.get_string_md5('%s %s' % (model, name))),
                subdir='compute/hw'
            )

    def print_net_macs(self, server):
        info = []

        for fabric_info in server['Fabric']:
            item = {}
            item['AdapterPciSlot'] = fabric_info['AdapterPciSlot']
            if item['AdapterPciSlot'] is None:
                item['AdapterPciSlot'] = '--'

            item['AdapterModel'] = self.get_adapter_model(fabric_info['AdapterModel'])
            item['InterfaceName'] = fabric_info['InterfaceName']
            item['MacAddress'] = fabric_info['MacAddress']
            item['FabricRef'] = fabric_info['intfRef']
            item['Fabric'] = fabric_info['intf']
            info.append(item)

        if len(info) == 0:
            return

        self.my_output.print_stream(
            '\n## Server Mac Address Fabric Visibility',
            'output'
        )

        order = [
            'PCI',
            'Model',
            'Interface',
            'MAC',
            'Fabric',
            'Device',
            'Interface',
            'LLDP'
        ]
        self.print_table_header(order)

        info = sorted(
            info,
            key=lambda i: (
                i['AdapterPciSlot'],
                i['InterfaceName']
            )
        )
        for item in info:
            line = ''
            line = self.add_column(line, item['AdapterPciSlot'])
            line = self.add_column(line, item['AdapterModel'])
            line = self.add_column(line, item['InterfaceName'])
            line = self.add_column(line, item['MacAddress'])
            if len(item['FabricRef']) == 0:
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---', last=True)
            else:
                line = self.add_column(line, item['FabricRef'][0]['fabric'])
                if item['FabricRef'][0]['type'] not in ['Nexus', 'ACI']:
                    line = self.add_column(line, item['FabricRef'][0]['device'])
                    line = self.add_column(line, item['FabricRef'][0]['intf'])
                    line = self.add_column(line, '---', last=True)

                if item['FabricRef'][0]['type'] == 'Nexus':
                    line = self.add_column(
                        line,
                        '[%s](../nexus/%s-eth.md)' % (
                            item['FabricRef'][0]['device'],
                            item['FabricRef'][0]['device']
                        )
                    )
                    line = self.add_column(
                        line,
                        '[%s](../nexus/eth/%s.md)' % (
                            item['FabricRef'][0]['intf'],
                            item['FabricRef'][0]['intf_hash']
                        )
                    )
                    if item['FabricRef'][0]['lldp_hash'] is None:
                        line = self.add_column(line, '---', last=True)
                    else:
                        line = self.add_column(
                            line,
                            '[Link](../nexus/lldp/%s.md)' % (
                                item['FabricRef'][0]['lldp_hash']
                            ),
                            last=True
                        )

                if item['FabricRef'][0]['type'] == 'ACI':
                    line = self.add_column(
                        line,
                        '[%s](../apic/%s-%s-phy.md)' % (
                            item['FabricRef'][0]['device'],
                            item['FabricRef'][0]['fabric'],
                            item['FabricRef'][0]['device_name']
                        )
                    )
                    line = self.add_column(
                        line,
                        '[%s](../apic/phy/%s.md)' % (
                            item['FabricRef'][0]['intf'],
                            item['FabricRef'][0]['intf_hash']
                        )
                    )
                    if item['FabricRef'][0]['lldp_hash'] is None:
                        line = self.add_column(line, '---', last=True)
                    else:
                        line = self.add_column(
                            line,
                            '[Link](../apic/lldp/%s.md)' % (
                                item['FabricRef'][0]['lldp_hash']
                            ),
                            last=True
                        )

            self.my_output.print_stream(line, 'output')

            if len(item['FabricRef']) > 1:
                for i in range(len(item['FabricRef'])):
                    if i == 0:
                        continue

                    line = ' | | | | | '
                    line = self.add_column(line, item['FabricRef'][i]['fabric'])
                    if item['FabricRef'][i]['type'] not in ['Nexus', 'ACI']:
                        line = self.add_column(line, item['FabricRef'][i]['device'])
                        line = self.add_column(line, item['FabricRef'][i]['intf'])
                        line = self.add_column(line, '---', last=True)

                    if item['FabricRef'][i]['type'] == 'Nexus':
                        line = self.add_column(
                            line,
                            '[%s](../nexus/%s-eth.md)' % (
                                item['FabricRef'][i]['device'],
                                item['FabricRef'][i]['device']
                            )
                        )
                        line = self.add_column(
                            line,
                            '[%s](../nexus/eth/%s.md)' % (
                                item['FabricRef'][i]['intf'],
                                item['FabricRef'][i]['intf_hash']
                            )
                        )
                        if item['FabricRef'][i]['lldp_hash'] is None:
                            line = self.add_column(line, '---', last=True)
                        else:
                            line = self.add_column(
                                line,
                                '[Link](../nexus/lldp/%s.md)' % (
                                    item['FabricRef'][i]['lldp_hash']
                                ),
                                last=True
                            )

                    if item['FabricRef'][i]['type'] == 'ACI':
                        line = self.add_column(
                            line,
                            '[%s](../apic/%s-%s-phy.md)' % (
                                item['FabricRef'][i]['device'],
                                item['FabricRef'][i]['fabric'],
                                item['FabricRef'][i]['device_name']
                            )
                        )
                        line = self.add_column(
                            line,
                            '[%s](../apic/phy/%s.md)' % (
                                item['FabricRef'][i]['intf'],
                                item['FabricRef'][i]['intf_hash']
                            )
                        )
                        if item['FabricRef'][i]['lldp_hash'] is None:
                            line = self.add_column(line, '---', last=True)
                        else:
                            line = self.add_column(
                                line,
                                '[Link](../apic/lldp/%s.md)' % (
                                    item['FabricRef'][i]['lldp_hash']
                                ),
                                last=True
                            )

                    self.my_output.print_stream(line, 'output')

    def print_server_mac(self, server, mac):
        info = []

        for fabric_info in server['Fabric']:
            item = {}
            item['AdapterPciSlot'] = fabric_info['AdapterPciSlot']
            if item['AdapterPciSlot'] is None:
                item['AdapterPciSlot'] = '--'

            item['AdapterModel'] = self.get_adapter_model(fabric_info['AdapterModel'])
            item['InterfaceName'] = fabric_info['InterfaceName']
            item['MacAddress'] = fabric_info['MacAddress']
            item['Fabric'] = fabric_info['intf']
            item['Source'] = ','.join(fabric_info['src'])
            if item['Source'] == '':
                item['Source'] = '---'
            info.append(item)

        if len(info) == 0:
            return

        order = [
            'PCI',
            'Model',
            'Interface',
            'MAC'
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
            if ip_helper.is_mac_equal(item['MacAddress'], mac):
                line = '%s |' % (item['AdapterPciSlot'])
                line = '%s %s |' % (line, item['AdapterModel'])
                line = '%s %s |' % (line, item['InterfaceName'])
                line = '%s %s' % (line, item['MacAddress'])
                self.my_output.print_stream(line, 'output')
