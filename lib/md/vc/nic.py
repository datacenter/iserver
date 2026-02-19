import json


class MdVcNicOutput():
    def __init__(self):
        pass

    def print_vc_host_nic_cdp(self, host, nic):
        self.print_page_header('VMWare Host CDP')

        self.my_output.print_stream('## Local End', 'output')
        self.my_output.print_stream('\n- Host: %s' % (host['name']), 'output')
        self.my_output.print_stream('- Interface: %s' % (nic['_name']), 'output')
        self.my_output.print_stream('- MAC: %s' % (nic['mac']), 'output')
        if 'fullDuplex' in nic['cdp']:
            self.my_output.print_stream('- Full duplex: %s' % (nic['cdp']['fullDuplex']), 'output')
        if 'mtu' in nic['cdp']:
            self.my_output.print_stream('- MTU: %s' % (nic['cdp']['mtu']), 'output')
        if 'vlan' in nic['cdp']:
            self.my_output.print_stream('- VLAN: %s' % (nic['cdp']['vlan']), 'output')
        if 'ttl' in nic['cdp']:
            self.my_output.print_stream('- TTL: %s' % (nic['cdp']['ttl']), 'output')

        self.my_output.print_stream('\n## Remote End', 'output')
        if 'systemName' in nic['cdp']:
            self.my_output.print_stream('- Sys Name: %s' % (nic['cdp']['systemName']), 'output')
        if 'devId' in nic['cdp']:
            self.my_output.print_stream('- Device ID: %s' % (nic['cdp']['devId']), 'output')
        if 'portId' in nic['cdp']:
            self.my_output.print_stream('- Interface: %s' % (nic['cdp']['portId']), 'output')
        if 'hardwarePlatform' in nic['cdp']:
            self.my_output.print_stream('- Hardware: %s' % (nic['cdp']['hardwarePlatform']), 'output')
        if 'softwareVersion' in nic['cdp']:
            self.my_output.print_stream('- Software: %s' % (nic['cdp']['softwareVersion']), 'output')
        if 'address' in nic['cdp']:
            self.my_output.print_stream('- IPv4: %s' % (nic['cdp']['address']), 'output')
        if 'deviceCapability' in nic['cdp']:
            self.my_output.print_stream('- Capabilities', 'output')
            if isinstance(nic['cdp']['deviceCapability'], dict):
                for cap in nic['cdp']['deviceCapability']:
                    self.my_output.print_stream('\t- %s:%s' % (cap, nic['cdp']['deviceCapability'][cap]), 'output')

        self.save_output(nic['hash'], subdir='vc/cdp')

    def print_vc_host_nic_lldp(self, host, nic):
        self.print_page_header('VMWare Host LLDP')

        self.my_output.print_stream('## Local End', 'output')
        self.my_output.print_stream('\n- Host: %s' % (host['name']), 'output')
        self.my_output.print_stream('- Interface: %s' % (nic['_name']), 'output')
        self.my_output.print_stream('- MAC: %s' % (nic['mac']), 'output')

        self.my_output.print_stream('## Remote End', 'output')
        self.my_output.print_stream('- Sys Name: %s' % (nic['lldp']['systemName']), 'output')
        self.my_output.print_stream('- Sys Description: %s' % (nic['lldp']['systemDescription']), 'output')
        self.my_output.print_stream('- System Description: %s' % (nic['lldp']['systemDescription']), 'output')
        self.my_output.print_stream('- Port Description: %s' % (nic['lldp']['portDescription']), 'output')
        self.my_output.print_stream('- Chassis Id: %s' % (nic['lldp']['chassisId']), 'output')
        self.my_output.print_stream('- Port Id: %s' % (nic['lldp']['portId']), 'output')
        if 'deviceCapability' in nic['lldp']:
            self.my_output.print_stream('- Capabilities', 'output')
            if isinstance(nic['lldp']['deviceCapability'], dict):
                for cap in nic['lldp']['deviceCapability']:
                    self.my_output.print_stream('\t- %s:%s' % (cap, nic['lldp']['deviceCapability'][cap]), 'output')

        self.save_output(nic['hash'], subdir='vc/lldp')

    def print_vc_host_nic(self, host, nic):
        self.print_page_header('vCenter Host - Physical Adapter')

        self.my_output.print_stream('## Host', 'output')
        self.my_output.print_stream('- vCenter: %s' % (host['vcenter']), 'output')
        self.my_output.print_stream('- Cluster: %s' % (host['clusterName']), 'output')
        self.my_output.print_stream('- Host: %s' % (host['name']), 'output')

        self.my_output.print_stream('## Properties', 'output')
        self.my_output.print_stream('- Name: %s' % (nic['_name']), 'output')
        self.my_output.print_stream('- MAC: %s' % (nic['mac']), 'output')
        self.my_output.print_stream('- Location: PCI %s' % (nic['pci']), 'output')
        self.my_output.print_stream('- Driver: %s' % (nic['driver']), 'output')
        self.my_output.print_stream('- Driver version: %s' % (nic['driverVersion']), 'output')
        self.my_output.print_stream('- Firmware version: %s' % (nic['firmwareVersion']), 'output')
        self.my_output.print_stream('- Virtual Switch: %s' % (nic['vswitch']), 'output')

        self.my_output.print_stream('## State', 'output')
        self.my_output.print_stream('- Connected: %s' % (nic['up']), 'output')
        self.my_output.print_stream('- Auto negotiate: %s' % (nic['autoNegotiateSupported']), 'output')
        self.my_output.print_stream('- Wake on LAN support: %s' % (nic['wakeOnLanSupported']), 'output')
        if nic['up']:
            self.my_output.print_stream('- Speed: %s' % (nic['speedUnit']), 'output')
            self.my_output.print_stream('- Full duplex: %s' % (nic['duplex']), 'output')

        if len(nic['hintNetwork']) > 0:
            self.my_output.print_stream('- Network (hints)', 'output')
            for hint in nic['hintNetwork']:
                self.my_output.print_stream('\t- %s (vlan %s)' % (hint['subnet'], hint['vlan']), 'output')

        self.my_output.print_stream('## SR-IOV', 'output')
        self.my_output.print_stream('- Supported: %s' % (nic['sriov']['sriovCapable']), 'output')
        if nic['sriov']['sriovCapable']:
            self.my_output.print_stream('- Enabled: %s' % (nic['sriov']['sriovEnabled']), 'output')
            self.my_output.print_stream('- Active: %s' % (nic['sriov']['sriovActive']), 'output')
            self.my_output.print_stream('- Passthrough supported: %s' % (nic['sriov']['passthruCapable']), 'output')
            self.my_output.print_stream('- Passthrough enabled: %s' % (nic['sriov']['passthruEnabled']), 'output')
            self.my_output.print_stream('- Passthrough active: %s' % (nic['sriov']['passthruActive']), 'output')
            self.my_output.print_stream('- VF supported: %s' % (nic['sriov']['maxVirtualFunctionSupported']), 'output')
            self.my_output.print_stream('- VF requested: %s' % (nic['sriov']['numVirtualFunctionRequested']), 'output')
            self.my_output.print_stream('- VF active: %s' % (nic['sriov']['numVirtualFunction']), 'output')

        if nic['server'] is not None:
            self.my_output.print_stream('## Server', 'output')
            self.my_output.print_stream('- Server: [%s](../../compute/%s-net.md)' % (nic['server']['ServerName'], nic['server']['ServerMoid']), 'output')
            self.my_output.print_stream('- Adapter: %s' % (nic['server']['AdapterModel']), 'output')
            self.my_output.print_stream('- Interface: %s' % (nic['server']['InterfaceDn']), 'output')

        if nic['cdp'] is not None or nic['lldp'] is not None:
            self.my_output.print_stream('## Connected device', 'output')
            self.my_output.print_stream('- System name: %s' % (nic['switch_system_name']), 'output')
            if nic['switch_device_id'] is not None and len(nic['switch_device_id']) > 0:
                self.my_output.print_stream('- Device ID: %s' % (nic['switch_device_id']), 'output')
            if nic['switch_hw'] is not None and len(nic['switch_hw']) > 0:
                self.my_output.print_stream('- Hardware: %s' % (nic['switch_hw']), 'output')
            if nic['switch_sw'] is not None and len(nic['switch_sw']) > 0:
                self.my_output.print_stream('- Software: %s' % (nic['switch_sw']), 'output')
            self.my_output.print_stream('- Interface: %s' % (nic['switch_port']), 'output')
            if nic['cdp'] is not None:
                self.my_output.print_stream('- [CDP](../cdp/%s.md)' % (nic['hash']), 'output')
            if nic['lldp'] is not None:
                self.my_output.print_stream('- [LLDP](../lldp/%s.md)' % (nic['hash']), 'output')

        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(nic, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(host, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(nic['hash'], subdir='vc/nic')

        if nic['cdp'] is not None:
            self.print_vc_host_nic_cdp(host, nic)

        if nic['lldp'] is not None:
            self.print_vc_host_nic_lldp(host, nic)

    def add_vc_host_nic_nei_device(self, line, nic):
        if nic['switch_fabric_type'] is None or nic['switch_fabric_type'] not in ['Nexus', 'ACI']:
            line = self.add_column(line, nic['switch_system_name'])

        if nic['switch_fabric_type'] == 'ACI':
            if nic['cdp'] is not None:
                line = self.add_column(
                    line,
                    '[%s](../../apic/%s-%s-cdp.md)' % (nic['switch_system_name'], nic['switch_apic'], nic['switch_system_name'])
                )
            else:
                line = self.add_column(
                    line,
                    '[%s](../../apic/%s-%s-lldp.md)' % (nic['switch_system_name'], nic['switch_apic'], nic['switch_system_name'])
                )

        if nic['switch_fabric_type'] == 'Nexus':
            if nic['cdp'] is not None:
                line = self.add_column(
                    line,
                    '[%s](../../nexus/%s-cdp.md)' % (nic['switch_system_name'], nic['switch_system_name'])
                )
            else:
                line = self.add_column(
                    line,
                    '[%s](../../nexus/%s-lldp.md)' % (nic['switch_system_name'], nic['switch_system_name'])
                )

        return line

    def add_vc_host_nic_nei_interface(self, line, nic):
        if nic['switch_fabric_type'] is None or nic['switch_fabric_type'] not in ['Nexus', 'ACI']:
            line = self.add_column(line, nic['switch_port'])

        if nic['switch_fabric_type'] == 'ACI':
            line = self.add_column(line, nic['switch_port'])

        if nic['switch_fabric_type'] == 'Nexus':
            if nic['switch_port_hash'] is None:
                line = self.add_column(line, nic['switch_port'])
            else:
                line = self.add_column(
                    line,
                    '[%s](../../nexus/eth/%s.md)' % (
                        nic['switch_port'],
                        nic['switch_port_hash']
                    )
                )

        return line

    def add_vc_host_nic_nei_cdp(self, line, nic):
        if nic['cdp'] is None:
            line = self.add_column(line, '---')
        else:
            line = self.add_column(
                line,
                '[Link](../cdp/%s.md)' % (nic['hash'])
            )

        return line

    def add_vc_host_nic_nei_lldp(self, line, nic):
        if nic['lldp'] is None:
            line = self.add_column(line, '---')
        else:
            line = self.add_column(
                line,
                '[Link](../lldp/%s.md)' % (nic['hash'])
            )

        return line

    def print_vc_host_nics(self, host, hosts):
        self.print_vc_host_page_header(
            'Physical Adapter',
            host,
            hosts
        )

        order = [
            'Adapter',
            'Up',
            'MAC',
            'PCI',
            'Driver',
            'Speed',
            'SR-IOV',
            'Switch',
            'CDP',
            'LLDP'
        ]
        self.print_table_header(order)

        for nic in host['pnet']['pnic']:
            line = ''
            line = self.add_vc_host_link(line, 'nic', nic, up=True)
            line = self.add_column_tick_bool(line, nic['up'])
            line = self.add_column(line, nic['mac'])
            line = self.add_column(line, nic['pci'])
            line = self.add_column(line, nic['driver'])

            if 'speedUnit' in nic:
                line = self.add_column(line, nic['speedUnit'])
            else:
                line = self.add_column(line, '---')

            if 'sriov' in nic:
                if nic['sriov']['sriovCapable']:
                    line = self.add_column_tick_bool(line,  nic['sriov']['sriovEnabled'])
                else:
                    line = self.add_column(line, 'N/A')
            else:
                line = self.add_column(line, '---')

            if nic['vswitch_hash'] is not None:
                line = self.add_column(
                    line,
                    '[%s](../%s/%s.md)' % (
                        nic['vswitch'],
                        nic['vswitch_type'],
                        nic['vswitch_hash']
                    )
                )
            else:
                line = self.add_column(line, '---')

            line = self.add_column_tick_not_none(line, nic['cdp'])
            line = self.add_column_tick_not_none(line, nic['lldp'])

            self.vc_nic_count[host['vcenter']][host['name']] += 1
            if nic['up']:
                self.vc_nic_up_count[host['vcenter']][host['name']] += 1

            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '## CDP/LLDP\n',
            'output'
        )

        order = [
            'Adapter',
            'Device',
            'Interface',
            'CDP',
            'LLDP'
        ]
        self.print_table_header(order)

        for nic in host['pnet']['pnic']:
            line = ''
            line = self.add_vc_host_link(line, 'nic', nic, up=True)
            line = self.add_vc_host_nic_nei_device(line, nic)
            line = self.add_vc_host_nic_nei_interface(line, nic)
            line = self.add_vc_host_nic_nei_cdp(line, nic)
            line = self.add_vc_host_nic_nei_lldp(line, nic)
            self.my_output.print_stream(line, 'output')

        if host['ServerMoid'] is not None:
            self.my_output.print_stream(
                '## Server\n',
                'output'
            )

            self.my_output.print_stream('- Server: %s' % (host['ServerName']), 'output')
            self.my_output.print_stream('- [Inventory](../../compute/%s-inv.md)' % (host['ServerMoid']), 'output')
            self.my_output.print_stream('- [Networking](../../compute/%s-net.md)' % (host['ServerMoid']), 'output')
            self.my_output.print_stream('', 'output')

            order = [
                'Adapter',
                'MAC',
                'PCI',
                'Interface',
                'Model'
            ]
            self.print_table_header(order)

            for nic in host['ServerFabric']:
                line = ''
                if nic['vmnic'] is None:
                    line = self.add_column(line, nic['vmnic'])
                else:
                    line = self.add_vc_host_link(line, 'nic', nic, up=True)
                line = self.add_column(line, nic['MacAddress'])
                line = self.add_column(line, nic['AdapterPciSlot'])
                line = self.add_column(line, nic['InterfaceName'])
                line = self.add_column(line, nic['AdapterModel'])
                self.my_output.print_stream(line, 'output')

        #     self.my_output.print_stream('\n## Debug\n', 'output')
        #     self.my_output.print_stream('```', 'output')
        #     self.my_output.print_stream(json.dumps(host['ServerFabric'], indent=4), 'output')
        #     self.my_output.print_stream('```', 'output')

        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(host['pnet']['pnic'], indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.my_output.print_stream('', 'output')
        self.my_output.print_stream('[Back](../../README.md)', 'output')
        self.save_output(host['hash'], subdir='vc/nic')

        for nic in host['pnet']['pnic']:
            self.print_vc_host_nic(
                host,
                nic
            )

    def print_vc_cluster_nics(self, cluster, clusters, hosts):
        self.print_vc_cluster_page_header(
            'Physical Adapter',
            cluster,
            clusters
        )

        order = [
            'Host',
            'Name',
            'PCI',
            'Interface',
            'Driver',
            'Speed',
            'SR-IOV',
            'vSwitch',
            'Info'
        ]
        self.print_table_header(order)

        for host in hosts:
            if 'pnet' not in host or host['pnet'] is None:
                continue

            if host['name'] not in cluster['hosts']:
                continue

            for nic in host['pnet']['pnic']:
                line = ''
                line = self.add_column(line, host['name'])
                line = self.add_vc_host_link(line, 'nic', nic)
                line = self.add_column(line, nic['pci'])

                if nic['server'] is None:
                    line = self.add_column(line, '---')
                else:
                    line = self.add_column(
                        line,
                        '[%s](../compute/%s.md)' % (
                            self.get_interface_dn(nic['server']['InterfaceDn']),
                            nic['server']['ServerMoid']
                        )
                    )

                line = self.add_column(line, nic['driver'])

                if 'speedUnit' in nic:
                    line = self.add_column(line, nic['speedUnit'])
                else:
                    line = self.add_column(line, '---')

                if 'sriov' in nic:
                    if nic['sriov']['sriovCapable']:
                        line = self.add_column(line, ':white_check_mark:')
                    else:
                        line = self.add_column(line, '')
                else:
                    line = self.add_column(line, '---')

                if nic['vswitch_hash'] is not None:
                    line = self.add_column(
                        line,
                        '[%s](../%s/%s.md)' % (
                            nic['vswitch'],
                            nic['vswitch_type'],
                            nic['vswitch_hash']
                        )
                    )
                else:
                    line = self.add_column(line, '---')

                line = self.add_column(
                    line,
                    '[Link](./%s.md)' % (nic['hash'])
                )

                self.vc_nic_count[cluster['vcenter']][cluster['name']] += 1
                if nic['up']:
                    self.vc_nic_up_count[cluster['vcenter']][cluster['name']] += 1

                self.my_output.print_stream(line, 'output')

        self.save_output(cluster['hash'], subdir='vc/nic')
