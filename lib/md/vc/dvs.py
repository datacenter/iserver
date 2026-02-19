class MdVcDvsOutput():
    def __init__(self):
        pass

    def print_vc_host_dvs(self, host, switch, networks, vms):
        self.print_page_header('vCenter Host - Distributed Virtual Switch')

        self.my_output.print_stream('## Host', 'output')
        self.my_output.print_stream('- vCenter: %s' % (host['vcenter']), 'output')
        self.my_output.print_stream('- Cluster: %s' % (host['clusterName']), 'output')
        self.my_output.print_stream('- Host: %s' % (host['name']), 'output')

        self.my_output.print_stream('## Properties', 'output')
        self.my_output.print_stream('- Name: %s' % (switch['name']), 'output')
        self.my_output.print_stream('- MTU: %s' % (switch['mtu']), 'output')
        self.my_output.print_stream('- Configured ports: %s' % (switch['configNumPorts']), 'output')
        self.my_output.print_stream('- Ports: %s' % (switch['numPorts']), 'output')
        self.my_output.print_stream('- Ports available: %s' % (switch['numPortsAvailable']), 'output')

        self.my_output.print_stream('## State', 'output')
        if len(switch['pnic']) > 0:
            self.my_output.print_stream(
                '- Uplink: %s/%s' % (
                    switch['numUplinksUp'],
                    len(switch['pnic'])
                ),
                'output'
            )
        else:
            self.my_output.print_stream(
                '- Uplink: ---',
                'output'
            )

        if len(switch['networkNonEmptyName']) > 0:
            self.my_output.print_stream(
                '- Network: %s/%s' % (
                    len(switch['networkNoneEmptyUpName']),
                    len(switch['networkNonEmptyName'])
                ),
                'output'
            )
        else:
            self.my_output.print_stream(
                '- Network: ---',
                'output'
            )

        if len(switch['vmName']) > 0:
            self.my_output.print_stream(
                '- Virtual Machine: %s/%s' % (
                    len(switch['vmUpName']),
                    len(switch['vmName'])
                ),
                'output'
            )
        else:
            self.my_output.print_stream(
                '- Virtual Machine: ---',
                'output'
            )

        if len(switch['pnic']) > 0:
            self.my_output.print_stream('## Uplink', 'output')

            order = [
                'Uplink',
                'Adapter',
                'Up',
                'Nei Device',
                'Interface',
                'CDP',
                'LLDP'
            ]
            self.print_table_header(order)

            for nic in switch['pnic']:
                line = ''
                line = self.add_column(line, nic['uplink'])
                line = self.add_vc_host_link(line, 'nic', nic['_info'], up=True)
                line = self.add_column_tick_bool(line, nic['_info']['up'])
                line = self.add_vc_host_nic_nei_device(line, nic['_info'])
                line = self.add_vc_host_nic_nei_interface(line, nic['_info'])
                line = self.add_vc_host_nic_nei_cdp(line, nic['_info'])
                line = self.add_vc_host_nic_nei_lldp(line, nic['_info'])
                self.my_output.print_stream(line, 'output')

        if len(switch['networkNonEmptyName']) > 0:
            self.my_output.print_stream('## Network', 'output')

            order = [
                'Network',
                'Up',
                'Status',
                'Accessible',
                'VM',
                'VLAN'
            ]
            self.print_table_header(order)

            for network_name in switch['networkName']:
                if len(switch['networkVm'][network_name]) > 0:
                    for network in networks:
                        if network['name'] == network_name:
                            line = ''
                            line = self.add_vc_host_link(line, 'net', network, up=True)
                            if network['overallStatus'] == 'green' and network['accessible']:
                                line = self.add_column(line, ':white_check_mark:')
                            else:
                                line = self.add_column(line, ':x:')
                            line = self.add_column(line, network['overallStatus'])
                            line = self.add_column(line, network['accessible'])
                            line = self.add_column(
                                line,
                                '%s/%s' % (
                                    len(switch['networkVmUp'][network_name]),
                                    len(switch['networkVm'][network_name])
                                )
                            )
                            if len(network['vlans']) == 0 or 0 in network['vlans']:
                                line = self.add_column(line, '---')
                            else:
                                line = self.add_column(line, ','.join(network['vlans']))
                            self.my_output.print_stream(line, 'output')

            self.my_output.print_stream('## Virtual Machine', 'output')

        if len(switch['vmName']) > 0:
            order = [
                'Network',
                'VM',
                'Up',
                'NIC',
                'MAC'
            ]
            self.print_table_header(order)

            for network_name in switch['networkName']:
                for network in networks:
                    if network['name'] == network_name:
                        if len(switch['networkVm'][network_name]) > 0:
                            for vm_name in switch['vmName']:
                                for vm in vms:
                                    if vm['name'] == vm_name:
                                        for nic in vm['nic']:
                                            if nic['networkName'] == network_name:
                                                line = ''
                                                line = self.add_vc_host_link(line, 'net', network, up=True)
                                                line = self.add_vc_host_link(line, 'vm', vm, up=True)
                                                line = self.add_column_tick_bool(line, vm['up'])
                                                line = self.add_column(line, nic['label'])
                                                line = self.add_column(line, nic['macAddress'])
                                                self.my_output.print_stream(line, 'output')

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(switch, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(switch['hash'], subdir='vc/dvs')

    def print_vc_host_dvses(self, host, hosts, networks, vms):
        self.print_vc_host_page_header(
            'Distributed Virtual Switch',
            host,
            hosts
        )

        self.my_output.print_stream('## DVS', 'output')

        order = [
            'DVS',
            'Up',
            'MTU',
            'Uplink',
            'Network',
            'VM'
        ]
        self.print_table_header(order)

        for vswitch in host['pnet']['dvswitch']:
            line = ''
            line = self.add_vc_host_link(line, 'dvs', vswitch, up=True)
            line = self.add_column_tick_bool(line, vswitch['up'])
            line = self.add_column(line, vswitch['mtu'])
            line = self.add_column(
                line,
                '%s/%s' % (
                    vswitch['numUplinksUp'],
                    len(vswitch['pnic'])
                )
            )
            line = self.add_column(
                line,
                '%s/%s' % (
                    len(vswitch['networkUpName']),
                    len(vswitch['networkName'])
                )
            )
            line = self.add_column(
                line,
                '%s/%s' % (
                    len(vswitch['vmUpName']),
                    len(vswitch['vmName'])
                )
            )

            self.vc_dvs_count[host['vcenter']][host['name']] += 1
            if vswitch['up']:
                self.vc_dvs_up_count[host['vcenter']][host['name']] += 1

            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('## Uplink', 'output')

        order = [
            'DVS',
            'Uplink',
            'Adapter',
            'Up',
            'Nei Device',
            'Interface',
            'CDP',
            'LLDP'
        ]
        self.print_table_header(order)

        for vswitch in host['pnet']['dvswitch']:
            for nic in vswitch['pnic']:
                line = ''
                line = self.add_vc_host_link(line, 'dvs', vswitch, up=True)
                line = self.add_column(line, nic['uplink'])
                line = self.add_vc_host_link(line, 'nic', nic['_info'], up=True)
                line = self.add_column_tick_bool(line, nic['_info']['up'])
                line = self.add_vc_host_nic_nei_device(line, nic['_info'])
                line = self.add_vc_host_nic_nei_interface(line, nic['_info'])
                line = self.add_vc_host_nic_nei_cdp(line, nic['_info'])
                line = self.add_vc_host_nic_nei_lldp(line, nic['_info'])
                self.my_output.print_stream(line, 'output')

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(host, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(host['hash'], subdir='vc/dvs')

        for vswitch in host['pnet']['dvswitch']:
            self.print_vc_host_dvs(
                host,
                vswitch,
                networks,
                vms
            )

    def print_vc_dvs(self, dvs, vms, hosts):
        self.print_page_header('vCenter - Distributed Virtual Switch')

        self.my_output.print_stream('## DVS', 'output')
        self.my_output.print_stream('- vCenter: %s' % (dvs['vcenter']), 'output')
        self.my_output.print_stream('- DVS: %s' % (dvs['name']), 'output')
        self.my_output.print_stream('- Manufacturer: %s' % (dvs['vendor']), 'output')
        self.my_output.print_stream('- Version: %s' % (dvs['version']), 'output')
        self.my_output.print_stream(
            '- Host: %s/%s' % (
                dvs['numHostsUp'],
                dvs['numHosts']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Upstream port group: %s/%s' % (
                dvs['numUpgUp'],
                dvs['numUpg']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Upstream port: %s/%s' % (
                dvs['numUplinkUp'],
                dvs['numUplink']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Upstream host adapter: %s/%s' % (
                dvs['numAdapterUp'],
                dvs['numAdapter']
            ),
            'output'
        )

        self.my_output.print_stream(
            '- Distributed port group: %s/%s' % (
                dvs['numDpgUp'],
                dvs['numDpg']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Downstream Port: %s/%s' % (
                dvs['numDownlinkUp'],
                dvs['numDownlink']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Virtual machine: %s/%s' % (
                dvs['numVmsUp'],
                dvs['numVms']
            ),
            'output'
        )

        if dvs['numHosts'] > 0:
            self.my_output.print_stream('\n## Hosts\n', 'output')

            order = [
                'Host',
                'Cluster',
                'Power',
                'Connection',
                'CPU',
                'Memory',
                'Uptime',
                'Uplink'
            ]
            self.print_table_header(order)

            for item in hosts:
                if item['name'] not in dvs['host']:
                    continue

                line = ''
                line = self.add_vc_host(line, item, up=True, name='_name')
                line = self.add_column(line, item['clusterName'])
                line = self.add_vc_host_power_state(line, item)
                line = self.add_vc_host_connection_state(line, item)
                line = self.add_column(line, item['stats']['overallCpuUsagePct'])
                line = self.add_column(line, item['stats']['overallMemoryUsagePct'])
                line = self.add_column(line, item['_uptime'])

                num_uplinks = None
                num_uplinks_up = None
                if item['pnet'] is not None:
                    for hdvs in item['pnet']['dvswitch']:
                        if hdvs['name'] == dvs['name']:
                            num_uplinks = hdvs['numUplinks']
                            num_uplinks_up = hdvs['numUplinksUp']

                if num_uplinks is None:
                    line = self.add_column(line, '---', last=True)
                else:
                    line = self.add_column(
                        line,
                        '%s/%s' % (
                            num_uplinks_up,
                            num_uplinks
                        ),
                        last=True
                    )

                self.my_output.print_stream(line, 'output')

        if dvs['numUpg'] > 0:
            self.my_output.print_stream('\n## Uplink Port Groups\n', 'output')

            order = [
                'Name',
                'Up',
                'Trunk',
                'VLAN',
                'Ports'
            ]
            self.print_table_header(order)
            for pg in dvs['portgroup']:
                if pg['uplink']:
                    line = ''
                    line = self.add_column(line, pg['name'])
                    line = self.add_column_tick_bool(line, pg['up'])
                    line = self.add_column_tick_bool(line, pg['trunk'])
                    line = self.add_column(line, ','.join(pg['vlans']))
                    line = self.add_column(
                        line,
                        '%s/%s' % (
                            pg['numPortsUp'],
                            pg['numPorts']
                        )
                    )
                    self.my_output.print_stream(line, 'output')

        if dvs['numPorts'] > 0:
            self.my_output.print_stream('\n## Uplink Ports\n', 'output')

            order = [
                'Port ID',
                'Name',
                'Peer Name',
                'Peer Port',
                'Port Group',
                'State',
                'VLAN ID'
            ]
            self.print_table_header(order)
            for port in dvs['port']:
                if not port['uplink']:
                    continue

                line = ''
                line = self.add_column(line, port['key'])
                line = self.add_column(line, port['name'])
                if port['peerType'] is None:
                    line = self.add_column(line, port['peerName'])
                    line = self.add_column(line, port['peerNic'])
                else:
                    if port['peerType'] not in ['pnic', 'vmVnic']:
                        line = self.add_column(line, port['peerName'])
                        line = self.add_column(line, port['peerNic'])
                    if port['peerType'] == 'pnic':
                        line = self.add_vc_host_link(line, 'dvs', port, up=True, name='_host', hname='host_hash')
                        line = self.add_vc_host_link(line, 'nic', port, up=True, name='peerNic', hname='host_nic_hash')
                    if port['peerType'] == 'vmVnic':
                        line = self.add_vc_host_link(line, 'vm', port, up=True, name='peerName', hname='vm_hash')
                        line = self.add_column(line, port['peerNic'])

                line = self.add_column(line, port['portgroupName'])
                line = self.add_column_tick_bool(line, port['linkUp'])
                line = self.add_column_tick_bool(line, port['trunk'])
                line = self.add_column(line, ','.join(port['vlans']))
                self.my_output.print_stream(line, 'output')

            self.my_output.print_stream('## Uplink Adapters', 'output')

            order = [
                'Host',
                'Uplink',
                'Adapter',
                'Up',
                'Nei Device',
                'Interface',
                'CDP',
                'LLDP'
            ]
            self.print_table_header(order)

            for item in hosts:
                if item['name'] not in dvs['host']:
                    continue

                if item['pnet'] is None:
                    continue

                for switch in item['pnet']['dvswitch']:
                    if switch['name'] != dvs['name']:
                        continue

                    for nic in switch['pnic']:
                        line = ''
                        line = self.add_vc_host(line, item, up=True, name='_name')
                        line = self.add_column(line, nic['uplink'])
                        line = self.add_vc_host_link(line, 'nic', nic['_info'], up=True)
                        line = self.add_column_tick_bool(line, nic['_info']['up'])
                        line = self.add_vc_host_nic_nei_device(line, nic['_info'])
                        line = self.add_vc_host_nic_nei_interface(line, nic['_info'])
                        line = self.add_vc_host_nic_nei_cdp(line, nic['_info'])
                        line = self.add_vc_host_nic_nei_lldp(line, nic['_info'])
                        self.my_output.print_stream(line, 'output')

        if dvs['numDpg'] > 0:
            self.my_output.print_stream('\n## Distributed Port Groups\n', 'output')

            order = [
                'Name',
                'Up',
                'Trunk',
                'VLAN',
                'Ports',
                'VM'
            ]
            self.print_table_header(order)
            for pg in dvs['portgroup']:
                if not pg['uplink']:
                    line = ''
                    line = self.add_column(line, pg['name'])
                    line = self.add_column_tick_bool(line, pg['up'])
                    line = self.add_column_tick_bool(line, pg['trunk'])
                    line = self.add_column(line, ','.join(pg['vlans']))
                    line = self.add_column(
                        line,
                        '%s/%s' % (
                            pg['numPortsUp'],
                            pg['numPorts']
                        )
                    )
                    line = self.add_column(
                        line,
                        '%s/%s' % (
                            pg['numVmsUp'],
                            pg['numVms']
                        )
                    )
                    self.my_output.print_stream(line, 'output')

        if dvs['numPorts'] > 0:
            self.my_output.print_stream('\n## Downstream Ports\n', 'output')

            order = [
                'Port ID',
                'Name',
                'Peer Name',
                'Peer Port',
                'Port Group',
                'State',
                'VLAN ID'
            ]
            self.print_table_header(order)
            for port in dvs['port']:
                if port['uplink']:
                    continue

                line = ''
                line = self.add_column(line, port['key'])
                line = self.add_column(line, port['name'])
                if port['peerType'] is None:
                    line = self.add_column(line, port['peerName'])
                    line = self.add_column(line, port['peerNic'])
                else:
                    if port['peerType'] not in ['pnic', 'vmVnic']:
                        line = self.add_column(line, port['peerName'])
                        line = self.add_column(line, port['peerNic'])
                    if port['peerType'] == 'pnic':
                        line = self.add_vc_host_link(line, 'dvs', port, up=True, name='_host', hname='host_hash')
                        line = self.add_vc_host_link(line, 'nic', port, up=True, name='peerNic', hname='host_nic_hash')
                    if port['peerType'] == 'vmVnic':
                        line = self.add_vc_host_link(line, 'vm', port, up=True, name='peerName', hname='vm_hash')
                        line = self.add_column(line, port['peerNic'])

                line = self.add_column(line, port['portgroupName'])
                line = self.add_column_tick_bool(line, port['linkUp'])
                line = self.add_column_tick_bool(line, port['trunk'])
                line = self.add_column(line, ','.join(port['vlans']))
                self.my_output.print_stream(line, 'output')

        if dvs['numVms'] > 0:
            self.my_output.print_stream('\n## VMs\n', 'output')

            order = [
                'Host',
                'VM',
                'Up',
                'CPU',
                'Used',
                'Mem',
                'Used',
                'Disk',
                'Used',
                'NIC'
            ]
            self.print_table_header(order)
            for vm in vms:
                if vm['name'] in dvs['vm']:
                    line = ''
                    line = self.add_vc_host_link(line, 'vm', vm, up=True, name='_host', hname='host_hash')
                    line = self.add_vc_host_link(line, 'vm', vm, up=True)
                    line = self.add_column_tick_bool(line, vm['up'])
                    line = self.add_column(line, vm['cpu']['count'])
                    line = self.add_column(line, vm['cpuUsageUnit'])
                    line = self.add_column(line, vm['memory']['memoryUnit'])
                    line = self.add_column(line, vm['guestMemoryUsagePct'])
                    line = self.add_column(line, vm['provisionedStorageUnit'])
                    line = self.add_column(line, vm['usedStoragePct'])
                    line = self.add_column(line, vm['numEthernetCards'])
                    self.my_output.print_stream(line, 'output')

        # file_helper.set_file_json('/tmp/%s.json' % (dvs['hash']), dvs)
        self.save_output(dvs['hash'], subdir='vc/dvs')

    def print_vc_dvses(self, vcenter, dvs, vms, hosts):
        self.print_vc_page_header(
            vcenter,
            'Distributed Virtual Switch',
            'dvs'
        )

        order = [
            'DVS',
            'Version',
            'Host',
            'Uplink PG',
            'Uplink Port',
            'Uplink Adapter',
            'Distributed PG',
            'Downlink Port',
            'VM'
        ]
        self.print_table_header(order)

        for switch in dvs:
            line = ''
            line = self.add_vc_host_link(line, 'dvs', switch)
            line = self.add_column(line, switch['version'])
            line = self.add_column(
                line,
                '%s/%s' % (
                    switch['numHostsUp'],
                    switch['numHosts']
                )
            )
            line = self.add_column(
                line,
                '%s/%s' % (
                    switch['numUpgUp'],
                    switch['numUpg']
                )
            )
            line = self.add_column(
                line,
                '%s/%s' % (
                    switch['numUplinkUp'],
                    switch['numUplink']
                )
            )

            # num_adapter = 0
            # num_adapter_up = 0
            # for item in hosts:
            #     if item['name'] not in switch['host']:
            #         continue

            #     if item['pnet'] is not None:
            #         for hdvs in item['pnet']['dvswitch']:
            #             if hdvs['name'] == switch['name']:
            #                 num_adapter += hdvs['numUplinks']
            #                 num_adapter_up += hdvs['numUplinksUp']

            line = self.add_column(
                line,
                '%s/%s' % (
                    switch['numAdapterUp'],
                    switch['numAdapter']
                )
            )

            line = self.add_column(
                line,
                '%s/%s' % (
                    switch['numDpgUp'],
                    switch['numDpg']
                )
            )
            line = self.add_column(
                line,
                '%s/%s' % (
                    switch['numDownlinkUp'],
                    switch['numDownlink']
                )
            )
            line = self.add_column(
                line,
                '%s/%s' % (
                    switch['numVmsUp'],
                    switch['numVms']
                )
            )

            self.vc_dvs_count[vcenter]['__ALL__'] += 1
            if switch['up']:
                self.vc_dvs_up_count[vcenter]['__ALL__'] += 1

            self.my_output.print_stream(line, 'output')

        self.save_output('%s-dvs' % (vcenter), subdir='vc')

        for switch in dvs:
            self.print_vc_dvs(
                switch,
                vms,
                hosts
            )
