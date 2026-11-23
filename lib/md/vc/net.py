class MdVcNetOutput():
    def __init__(self):
        pass

    def print_vc_net_standard(self, network, hosts, vms):
        self.print_page_header('vCenter - Standard Network')

        self.my_output.print_stream('- Name: %s' % (network['name']), 'output')
        self.my_output.print_stream(
            '- Host: %s/%s' % (
                network['numHostsUp'],
                network['numHosts']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Virtual machine: %s/%s' % (
                network['numVmsUp'],
                network['numVms']
            ),
            'output'
        )

        if network['numHosts'] > 0:
            self.my_output.print_stream('\n## Hosts\n', 'output')

            order = [
                'Host',
                'Cluster',
                'Power',
                'Connection',
                'CPU',
                'Memory',
                'Uptime'
            ]
            self.print_table_header(order)

            for item in hosts:
                if item['name'] not in network['host']:
                    continue

                line = ''
                line = self.add_vc_host(line, item, up=True, name='_name')
                line = self.add_column(line, item['clusterName'])
                line = self.add_vc_host_power_state(line, item)
                line = self.add_vc_host_connection_state(line, item)
                line = self.add_column(line, item['stats']['overallCpuUsagePct'])
                line = self.add_column(line, item['stats']['overallMemoryUsagePct'])
                line = self.add_column(line, item['_uptime'])
                self.my_output.print_stream(line, 'output')

        if network['numVms'] > 0:
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
                if vm['name'] in network['vm']:
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

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(network, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(network['hash'], subdir='vc/net')

    def print_vc_net_dpg(self, network, hosts, dvses, vms):
        self.print_page_header('vCenter - Distributed Port Group')

        self.my_output.print_stream('- Name: %s' % (network['name']), 'output')
        self.my_output.print_stream('- Distributed switch: %s' % (network['dvsName']), 'output')
        self.my_output.print_stream('- Trunk: %s' % (network['trunk']), 'output')
        self.my_output.print_stream('- VLANs: %s' % (','.join(network['vlans'])), 'output')
        self.my_output.print_stream(
            '- Host: %s/%s' % (
                network['numHostsUp'],
                network['numHosts']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Port: %s/%s' % (
                network['numPortsUp'],
                network['numPorts']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Virtual machine: %s/%s' % (
                network['numVmsUp'],
                network['numVms']
            ),
            'output'
        )

        if network['numHosts'] > 0:
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
                if item['name'] not in network['host']:
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
                        if hdvs['name'] == network['dvsName']:
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

        if network['numPorts'] > 0:
            self.my_output.print_stream('\n## Ports\n', 'output')

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

            for dvs in dvses:
                if dvs['name'] == network['dvsName']:
                    for port in dvs['port']:
                        if port['key'] not in network['ports']:
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
                        line = self.add_column(line, ','.join(port['vlans']))
                        self.my_output.print_stream(line, 'output')

        if network['numVms'] > 0:
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
                if vm['name'] in network['vm']:
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

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(network, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(network['hash'], subdir='vc/net')

    def print_vc_net_upg(self, network, hosts, dvses, vms):
        self.print_page_header('vCenter - Upstream Port Group')

        self.my_output.print_stream('- Name: %s' % (network['name']), 'output')
        self.my_output.print_stream('- Distributed switch: %s' % (network['dvsName']), 'output')
        self.my_output.print_stream('- Trunk: %s' % (network['trunk']), 'output')
        self.my_output.print_stream('- VLANs: %s' % (','.join(network['vlans'])), 'output')
        self.my_output.print_stream(
            '- Host: %s/%s' % (
                network['numHostsUp'],
                network['numHosts']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- Port: %s/%s' % (
                network['numPortsUp'],
                network['numPorts']
            ),
            'output'
        )

        if network['numHosts'] > 0:
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
                if item['name'] not in network['host']:
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
                        if hdvs['name'] == network['dvsName']:
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

        if network['numPorts'] > 0:
            self.my_output.print_stream('\n## Ports\n', 'output')

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

            for dvs in dvses:
                if dvs['name'] == network['dvsName']:
                    for port in dvs['port']:
                        if port['key'] not in network['ports']:
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
                        line = self.add_column(line, ','.join(port['vlans']))
                        self.my_output.print_stream(line, 'output')

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(network, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(network['hash'], subdir='vc/net')

    def print_vc_host_nets(self, host, hosts):
        self.print_vc_host_page_header(
            'Network',
            host,
            hosts
        )

        order = [
            'Name',
            'Type',
            'Hosts',
            'VMs'
        ]
        self.print_table_header(order)

        for net in host['network']:
            line = ''
            line = self.add_vc_host_link(line, 'net', net, up=True)
            line = self.add_column(line, net['_type'])
            line = self.add_column(line,
                '%s/%s' % (
                    net['numHostsUp'],
                    net['numHosts']
                )
            )
            line = self.add_column(
                line,
                '%s/%s' % (
                    net['numVmsUp'],
                    net['numVms']
                ),
                last=True
            )

            self.vc_net_count[host['vcenter']][host['name']] += 1
            if net['up']:
                self.vc_net_up_count[host['vcenter']][host['name']] += 1

            self.my_output.print_stream(line, 'output')

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(host['network'], indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(host['hash'], subdir='vc/net')

    def print_vc_cluster_nets(self, cluster, clusters, hosts):
        self.print_vc_cluster_page_header(
            'Network',
            cluster,
            clusters
        )

        order = [
            'Host',
            'Name'
        ]
        self.print_table_header(order)

        for host in hosts:
            if host['name'] not in cluster['hosts']:
                continue

            for net in host['network']:
                line = ''
                line = self.add_column(line, host['name'])
                line = self.add_column(line, net['name'])

                self.vc_net_count[host['vcenter']][cluster['name']] += 1
                if net['up']:
                    self.vc_net_up_count[host['vcenter']][cluster['name']] += 1

                self.my_output.print_stream(line, 'output')

        self.save_output(cluster['hash'], subdir='vc/net')

    def print_vc_nets(self, vcenter, nets, hosts, dvses, vms):
        self.print_vc_page_header(
            vcenter,
            'Network',
            'net'
        )

        order = [
            'Name',
            'Type',
            'Hosts',
            'VMs'
        ]
        self.print_table_header(order)

        for net in nets:
            line = ''
            line = self.add_vc_host_link(line, 'net', net)
            line = self.add_column(line, net['_type'])
            line = self.add_column(line,
                '%s/%s' % (
                    net['numHostsUp'],
                    net['numHosts']
                )
            )
            line = self.add_column(
                line,
                '%s/%s' % (
                    net['numVmsUp'],
                    net['numVms']
                ),
                last=True
            )

            self.vc_net_count[vcenter]['__ALL__'] += 1
            if net['up']:
                self.vc_net_up_count[vcenter]['__ALL__'] += 1

            self.my_output.print_stream(line, 'output')

        self.save_output('%s-net' % (vcenter), subdir='vc')

        for net in nets:
            if net['type'] == 'standard':
                self.print_vc_net_standard(
                    net,
                    hosts,
                    vms
                )

            if net['type'] == 'dvs' and not net['uplink']:
                self.print_vc_net_dpg(
                    net,
                    hosts,
                    dvses,
                    vms
                )

            if net['type'] == 'dvs' and net['uplink']:
                self.print_vc_net_upg(
                    net,
                    hosts,
                    dvses,
                    vms
                )
