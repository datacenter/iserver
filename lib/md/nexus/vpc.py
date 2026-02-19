from lib import ip_helper
from lib.nexus import helper as nexus_helper


class MdNexusVpcOutput():
    def __init__(self):
        pass

    def get_vpc_domains(self, vpc_state):
        domain = {}
        for device_name in self.nexus_device_names:
            if 'vpc-domain-id' not in vpc_state[device_name]:
                continue

            domain_id = vpc_state[device_name]['vpc-domain-id']
            if domain_id not in domain:
                domain[domain_id] = []

            domain[domain_id].append(
                vpc_state[device_name]
            )

        for domain_id in domain:
            if 'vpc' in domain[domain_id]:
                domain[domain_id]['vpc'] = sorted(
                    domain[domain_id]['vpc'],
                    key=lambda i: i['id']
                )

            domain[domain_id] = sorted(
                domain[domain_id],
                key=lambda i: i['nexus_name']
            )

        return domain

    def print_nexus_vpc_domain(self, domain_id, vpc_domain):
        self.print_page_header('Nexus VPC Domain')

        order = [
            'Type',
            'Peer A',
            'Peer B'
        ]
        self.print_table_header(order)

        peer1 = None
        peer2 = None
        if len(vpc_domain) > 0:
            peer1 = vpc_domain[0]

        if len(vpc_domain) > 1:
            peer2 = vpc_domain[1]

        title = [
            'Device',
            'Domain ID',
            'Role',
            'VPC system mac',
            'VPC system prio',
            'VPC local system mac',
            'VPC local system prio',
            'VPC local role prio',
            'Peer status',
            'Keepalive status',
            'Keepalive destination',
            'Keepalive send interface',
            'Keepalive receive interface',
            'Keepalive VRF',
            'Keepalive UDP Port',
            'Keepalive ToS',
            'Keepalive interval',
            'Keepalive timeout',
            'Keepalive hold timeout',
            'Consistency',
            'VLAN consistency',
            'Num of VPCs',
            'Graceful consistency check status',
            'Auto recovery status',
            'Delay restore status',
            'Delay restore SVI status',
            'Delay restore orphan port status',
            'Operational L3 peer',
            'Virtual peer link'
        ]

        param = [
            'nexus_name',
            'vpc-domain-id',
            '_role',
            'vpc-system-mac',
            'vpc-system-prio',
            'vpc-local-system-mac',
            'vpc-local-system-prio',
            'vpc-local-role-prio',
            'vpc-peer-status',
            'vpc-peer-keepalive-status',
            'vpc-keepalive-dest',
            'vpc-keepalive-send-interface',
            'vpc-keepalive-receive-interface',
            'vpc-keepalive-vrf',
            'vpc-keepalive-udp-port',
            'vpc-keepalive-tos',
            'vpc-keepalive-interval',
            'vpc-keepalive-timeou',
            'vpc-keepalive-hold-timeout',
            'vpc-peer-consistency',
            'vpc-per-vlan-peer-consistency',
            'num-of-vpcs',
            'vpc-graceful-consistency-check-status',
            'vpc-auto-recovery-status',
            'vpc-delay-restore-status',
            'vpc-delay-restore-svi-status',
            'vpc-delay-restore-orphan-port-status',
            'operational-l3-peer',
            'virtual-peerlink'
        ]

        for index in range(0, len(title)):
            self.print_row_t2v(title[index], param[index], peer1, peer2)

        peerif1 = None
        peerif2 = None
        if peer1 is not None and len(peer1['peer']) > 0:
            peerif1 = peer1['peer'][0]
        if peer2 is not None and len(peer2['peer']) > 0:
            peerif2 = peer2['peer'][0]

        self.print_row_t2v('Peer interface', 'ifindex', peerif1, peerif2)

        self.print_row_t2v('Peer interface state', '_state', peerif1, peerif2)
        self.print_row_t2v('Peer eth interface', '_eth', peerif1, peerif2)

        self.my_output.print_stream('', 'output')
        if peer1 is not None:
            self.my_output.print_stream(peer1['nexus_name'], 'output')
            self.my_output.print_stream('```', 'output')
            self.my_output.print_stream(peer1['configuration'], 'output')
            self.my_output.print_stream('```', 'output')

        if peer2 is not None:
            self.my_output.print_stream(peer2['nexus_name'], 'output')
            self.my_output.print_stream('```', 'output')
            self.my_output.print_stream(peer2['configuration'], 'output')
            self.my_output.print_stream('```', 'output')

        peerif1 = None
        peerif2 = None
        if peer1 is not None and len(peer1['peer']) > 0:
            peerif1 = peer1['peer'][0]
        if peer2 is not None and len(peer2['peer']) > 0:
            peerif2 = peer2['peer'][0]

        # Get all vpc ids

        vpc_ids = []
        if peer1 is not None:
            for vpc in peer1['vpc']:
                if vpc['id'] not in vpc_ids:
                    vpc_ids.append(
                        vpc['id']
                    )

        if peer2 is not None:
            for vpc in peer2['vpc']:
                if vpc['id'] not in vpc_ids:
                    vpc_ids.append(
                        vpc['id']
                    )

        vpc_ids = sorted(vpc_ids)

        # Print each vpc

        for vpc_id in vpc_ids:
            self.my_output.print_stream('\n## VPC %s\n' % (vpc_id), 'output')

            peer1vpc = None
            if peer1 is not None:
                for vpc in peer1['vpc']:
                    if vpc['id'] == vpc_id:
                        peer1vpc = vpc
                        peer1vpc['_device'] = None
                        if len(peer1vpc['xd']) > 0:
                            peer1vpc['_device'] = peer1vpc['xd'][0]['DeviceSysName']

            peer2vpc = None
            if peer2 is not None:
                for vpc in peer2['vpc']:
                    if vpc['id'] == vpc_id:
                        peer2vpc = vpc
                        peer2vpc['_device'] = None
                        if len(peer2vpc['xd']) > 0:
                            peer2vpc['_device'] = peer2vpc['xd'][0]['DeviceSysName']


            order = [
                'Type',
                'Peer A',
                'Peer B'
            ]
            self.print_table_header(order)

            # Device
            line = ''
            line = self.add_column(line, 'Device')
            line = self.add_column(line, peer1['nexus_name'])
            if peer2 is None:
                line = self.add_column(line, '---', last=True)
            else:
                line = self.add_column(line, peer2['nexus_name'], last=True)
            self.my_output.print_stream(line, 'output')

            # VPC
            line = ''
            line = self.add_column(line, 'VPC')
            line = self.add_column(line, peer1vpc['id'])
            if peer2vpc is None:
                line = self.add_column(line, '---', last=True)
            else:
                line = self.add_column(line, peer2vpc['id'], last=True)
            self.my_output.print_stream(line, 'output')

            # Interface
            line = ''
            line = self.add_column(line, 'Interface')
            if peer1vpc['hash'] is None:
                line = self.add_column(line, peer1vpc['ifindex'])
            else:
                line = self.add_column(
                    line,
                    '[%s](../pc/%s.md)' % (
                        peer1vpc['ifindex'],
                        peer1vpc['hash']
                    )
                )

            if peer2vpc is None:
                line = self.add_column(line, '---', last=True)
            else:
                if peer2vpc['hash'] is None:
                    line = self.add_column(line, peer2vpc['ifindex'], last=True)
                else:
                    line = self.add_column(
                        line,
                        '[%s](../pc/%s.md)' % (
                            peer2vpc['ifindex'],
                            peer2vpc['hash']
                        ),
                        last=True
                    )

            self.my_output.print_stream(line, 'output')

            # Ethernet
            line = ''
            line = self.add_column(line, 'Ethernet')

            if peer1vpc is not None and len(peer1vpc['eth']) > 0:
                eth_ids = []
                for eth in peer1vpc['eth']:
                    eth_ids.append(
                        nexus_helper.get_nexus_interface_id(
                            eth
                        )
                    )

                eth_ids = sorted(eth_ids)
                eth_hash = []
                for eth_id in eth_ids:
                    ehash = ip_helper.get_string_md5(
                        '%s %s' % (
                            peer1['nexus_name'],
                            'Ethernet%s' % (eth_id)
                        )
                    )
                    eth_hash.append(
                        '[%s](../eth/%s.md)' % (
                            eth_id,
                            ehash
                        )
                    )
                line = self.add_column(line, ','.join(eth_hash))
            else:
                line = self.add_column(line, '---')

            if peer2vpc is not None and len(peer2vpc['eth']) > 0:
                eth_ids = []
                for eth in peer2vpc['eth']:
                    eth_ids.append(
                        nexus_helper.get_nexus_interface_id(
                            eth
                        )
                    )

                eth_ids = sorted(eth_ids)
                eth_hash = []
                for eth_id in eth_ids:
                    ehash = ip_helper.get_string_md5(
                        '%s %s' % (
                            peer2['nexus_name'],
                            'Ethernet%s' % (eth_id)
                        )
                    )
                    eth_hash.append(
                        '[%s](../eth/%s.md)' % (
                            eth_id,
                            ehash
                        )
                    )
                line = self.add_column(line, ','.join(eth_hash), last=True)
            else:
                line = self.add_column(line, '---', last=True)

            self.my_output.print_stream(line, 'output')

            # State
            line = ''
            line = self.add_column(line, 'State')
            if peer1vpc is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, peer1vpc['_state'])

            if peer2vpc is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, peer2vpc['_state'], last=True)

            self.my_output.print_stream(line, 'output')

            # Consistency
            line = ''
            line = self.add_column(line, 'Consistency')
            if peer1vpc is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, peer1vpc['consistency'])

            if peer2vpc is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, peer2vpc['consistency'], last=True)

            self.my_output.print_stream(line, 'output')

            # Device
            line = ''
            line = self.add_column(line, 'Device')
            if peer1vpc is None:
                line = self.add_column(line, '---')
            else:
                if peer1vpc['_device'] is None:
                    line = self.add_column(line, peer1vpc['_device'])
                else:
                    line = self.add_column(
                        line,
                        '[%s](../%s-eth.md)'% (
                            peer1vpc['_device'],
                            peer1vpc['_device']
                        )
                    )

            if peer2vpc is None:
                line = self.add_column(line, '---', last=True)
            else:
                if peer1vpc['_device'] is None:
                    line = self.add_column(line, peer2vpc['_device'], last=True)
                else:
                    line = self.add_column(
                        line,
                        '[%s](../%s-eth.md)'% (
                            peer2vpc['_device'],
                            peer2vpc['_device']
                        ),
                        last=True
                    )

            self.my_output.print_stream(line, 'output')

        self.save_output(domain_id, subdir='nexus/vpc-domain')

    def print_nexus_vpc(self, vpc_state):
        self.print_page_header('Nexus Devices Virtual Port Channel')
        self.print_nexus_overview_bar('vpc')

        order = [
            'ID',
            'Peer A',
            'PL',
            'Eth',
            'State',
            'Peer B',
            'PL',
            'Eth',
            'State',
            'Info'
        ]
        self.print_table_header(order)

        domains = self.get_vpc_domains(vpc_state)
        for domain_id in domains:
            line = ''
            if len(domains[domain_id]) != 2:
                line = self.add_column(line, '!%s' % (domain_id))
            else:
                line = self.add_column(line, domain_id)

            # 1st peer
            if len(domains[domain_id]) > 0:
                line = self.add_column(
                    line,
                    '%s (%s)' % (
                        domains[domain_id][0]['nexus_name'],
                        domains[domain_id][0]['_role_flag']
                    )
                )

                if len(domains[domain_id][0]['peer']) != 1:
                    line = self.add_column(line, '---')
                    line = self.add_column(line, '---')
                else:
                    peer_interface = domains[domain_id][0]['peer'][0]['ifindex']
                    peer_interface_type = nexus_helper.get_nexus_interface_type(
                        peer_interface
                    )
                    if peer_interface_type == 'pc':
                        if domains[domain_id][0]['peer'][0]['hash'] is None:
                            line = self.add_column(
                                line,
                                '%s (%s)' % (
                                    domains[domain_id][0]['peer'][0]['ifindex'],
                                    domains[domain_id][0]['peer'][0]['_state']
                                )
                            )
                        else:
                            line = self.add_column(
                                line,
                                '[%s](./pc/%s.md) (%s)' % (
                                    domains[domain_id][0]['peer'][0]['ifindex'],
                                    domains[domain_id][0]['peer'][0]['hash'],
                                    domains[domain_id][0]['peer'][0]['_state']
                                )
                            )
                    else:
                        line = self.add_column(line, '---')

                    if len(domains[domain_id][0]['peer'][0]['eth']) > 0:
                        eth_ids = []
                        for eth in domains[domain_id][0]['peer'][0]['eth']:
                            eth_ids.append(
                                nexus_helper.get_nexus_interface_id(
                                    eth
                                )
                            )

                        eth_ids = sorted(eth_ids)
                        eth_hash = []
                        for eth_id in eth_ids:
                            ehash = ip_helper.get_string_md5(
                                '%s %s' % (
                                    domains[domain_id][0]['nexus_name'],
                                    'Ethernet%s' % (eth_id)
                                )
                            )
                            eth_hash.append(
                                '[%s](./eth/%s.md)' % (
                                    eth_id,
                                    ehash
                                )
                            )
                        line = self.add_column(line, ','.join(eth_hash))
                    else:
                        line = self.add_column(line, '---')

                line = self.add_column(line, domains[domain_id][0]['vpc-peer-status'])

            else:
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')

            # 2nd peer
            if len(domains[domain_id]) == 2:
                line = self.add_column(
                    line,
                    '%s (%s)' % (
                        domains[domain_id][1]['nexus_name'],
                        domains[domain_id][1]['_role_flag']
                    )
                )

                if len(domains[domain_id][1]['peer']) != 1:
                    line = self.add_column(line, '---')
                    line = self.add_column(line, '---')
                else:
                    peer_interface = domains[domain_id][1]['peer'][0]['ifindex']
                    peer_interface_type = nexus_helper.get_nexus_interface_type(
                        peer_interface
                    )
                    if peer_interface_type == 'pc':
                        if domains[domain_id][1]['peer'][0]['hash'] is None:
                            line = self.add_column(
                                line,
                                '%s (%s)' % (
                                    domains[domain_id][1]['peer'][0]['ifindex'],
                                    domains[domain_id][1]['peer'][0]['_state']
                                )
                            )
                        else:
                            line = self.add_column(
                                line,
                                '[%s](./pc/%s.md) (%s)' % (
                                    domains[domain_id][1]['peer'][0]['ifindex'],
                                    domains[domain_id][1]['peer'][0]['hash'],
                                    domains[domain_id][1]['peer'][0]['_state']
                                )
                            )
                    else:
                        line = self.add_column(line, '---')

                    if len(domains[domain_id][1]['peer'][0]['eth']) > 0:
                        eth_ids = []
                        for eth in domains[domain_id][1]['peer'][0]['eth']:
                            eth_ids.append(
                                nexus_helper.get_nexus_interface_id(
                                    eth
                                )
                            )

                        eth_ids = sorted(eth_ids)
                        eth_hash = []
                        for eth_id in eth_ids:
                            ehash = ip_helper.get_string_md5(
                                '%s %s' % (
                                    domains[domain_id][1]['nexus_name'],
                                    'Ethernet%s' % (eth_id)
                                )
                            )
                            eth_hash.append(
                                '[%s](./eth/%s.md)' % (
                                    eth_id,
                                    ehash
                                )
                            )
                        line = self.add_column(line, ','.join(eth_hash))
                    else:
                        line = self.add_column(line, '---')

                line = self.add_column(line, domains[domain_id][1]['vpc-peer-status'])

            else:
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')

            line = self.add_column(line, '[Link](./vpc-domain/%s.md)' % (domain_id), last=True)
            self.my_output.print_stream(line, 'output')

        for domain_id in domains:
            self.my_output.print_stream(
                '## Domain #%s [Link](./vpc-domain/%s.md)' % (domain_id, domain_id),
                'output'
            )

            order = [
                'Peer',
                'ID',
                'PC',
                'Eth',
                'State',
                'Device'
            ]
            self.print_table_header(order)

            for peer_index in range(0,2):
                if len(domains[domain_id]) > peer_index:
                    for vpc in domains[domain_id][peer_index]['vpc']:
                        line = ''
                        line = self.add_column(
                            line,
                            '[%s](./%s-eth.md)' % (
                                domains[domain_id][peer_index]['nexus_name'],
                                domains[domain_id][peer_index]['nexus_name']
                            )
                        )
                        line = self.add_column(line, vpc['id'])

                        peer_interface_type = nexus_helper.get_nexus_interface_type(
                            vpc['ifindex']
                        )
                        if peer_interface_type == 'pc':
                            if vpc['hash'] is None:
                                line = self.add_column(
                                    line,
                                    '%s (%s)' % (
                                        vpc['ifindex'],
                                        vpc['_state']
                                    )
                                )
                            else:
                                line = self.add_column(
                                    line,
                                    '[%s](./pc/%s.md) (%s)' % (
                                        vpc['ifindex'],
                                        vpc['hash'],
                                        vpc['_state']
                                    )
                                )
                        else:
                            line = self.add_column(line, '---')

                        if len(vpc['eth']) > 0:
                            eth_ids = []
                            for eth in vpc['eth']:
                                eth_ids.append(
                                    nexus_helper.get_nexus_interface_id(
                                        eth
                                    )
                                )

                            eth_ids = sorted(eth_ids)
                            eth_hash = []
                            for eth_id in eth_ids:
                                ehash = ip_helper.get_string_md5(
                                    '%s %s' % (
                                        domains[domain_id][peer_index]['nexus_name'],
                                        'Ethernet%s' % (eth_id)
                                    )
                                )
                                eth_hash.append(
                                    '[%s](./eth/%s.md)' % (
                                        eth_id,
                                        ehash
                                    )
                                )
                            line = self.add_column(line, ','.join(eth_hash))
                        else:
                            line = self.add_column(line, '---')

                        line = self.add_column(
                            line,
                            vpc['_state']
                        )

                        devices = []
                        for peer_xd in vpc['xd']:
                            if peer_xd['DeviceSysName'] is not None:
                                devices.append(
                                    peer_xd['DeviceSysName']
                                )

                        line = self.add_column(
                            line,
                            ','.join(devices),
                            last=True
                        )

                        self.my_output.print_stream(line, 'output')

        self.save_output('vpc', subdir='nexus')

        for domain_id in domains:
            self.print_nexus_vpc_domain(
                domain_id,
                domains[domain_id]
            )
