class MdFiEthOutput():
    def __init__(self):
        pass

    def add_fi_eth_admin(self, line, info):
        return self.add_column_tick_string(
            line,
            info['AdminState'],
            'enabled'
        )

    def add_fi_eth_oper(self, line, info):
        return self.add_column_tick_string(
            line,
            info['OperState'],
            'up'
        )

    def print_fi_interface_eth_details(self, fi_name, fi_info, eth_info, servers):
        self.print_page_header('Fabric Interconnect Ethernet')

        self.my_output.print_stream('- Fabric Interconnect: [%s](../%s-eth.md)' % (fi_name, fi_info['hash']), 'output')
        self.my_output.print_stream('- Switch ID: %s' % (eth_info['SwitchId']), 'output')
        self.my_output.print_stream('- Interface: %s' % (eth_info['Name']), 'output')
        self.my_output.print_stream('- Dn: %s' % (eth_info['Dn']), 'output')
        self.my_output.print_stream('- MAC: %s' % (eth_info['MacAddress']), 'output')
        self.my_output.print_stream('- Role: %s' % (eth_info['Role']), 'output')

        self.my_output.print_stream('## State', 'output')
        if eth_info['AdminState'] == 'enabled':
            self.my_output.print_stream('- Admin state :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Admin state :x:', 'output')

        self.my_output.print_stream('- Oper state: %s' % (eth_info['OperState']), 'output')
        self.my_output.print_stream('- Oper speed: %s' % (eth_info['OperSpeed']), 'output')
        self.my_output.print_stream('- Transceiver: %s' % (eth_info['TransceiverType']), 'output')

        if eth_info['PortChannelId'] != 0:
            self.my_output.print_stream('## Port Channel', 'output')

            for pc_info in fi_info['EthernetPortChannel']:
                if pc_info['PortChannelId'] == eth_info['PortChannelId']:
                    self.my_output.print_stream(
                        '- Port Channel ID: [%s](../pc/%s.md)' % (
                            pc_info['PortChannelId'],
                            self.xd_handler.get_fi_pc_hash(fi_name, pc_info['PortChannelId'])
                        ),
                        'output'
                    )
                    self.my_output.print_stream('- Name: %s' % (pc_info['Name']), 'output')
                    self.my_output.print_stream('- Description: %s' % (pc_info['Description']), 'output')
                    self.my_output.print_stream('- BandWidth: %s' % (pc_info['BandWidth']), 'output')
                    self.my_output.print_stream('- Role: %s' % (pc_info['Role']), 'output')
                    if pc_info['AdminState'] == 'enabled':
                        self.my_output.print_stream('- Admin state :white_check_mark:', 'output')
                    else:
                        self.my_output.print_stream('- Admin state :x:', 'output')

                    self.my_output.print_stream('- Oper state: %s' % (pc_info['OperState']), 'output')
                    self.my_output.print_stream('- Oper speed: %s' % (pc_info['OperSpeed']), 'output')
                    self.my_output.print_stream('- Channel Members: %s' % (pc_info['MemberSummary']), 'output')
                    self.my_output.print_stream('', 'output')

                    order = [
                        'Eth',
                        'Admin',
                        'Oper',
                        'Speed',
                        'Mode',
                        'Trans',
                        'Role',
                        'Device',
                        'Interface'
                    ]
                    self.print_table_header(order)

                    for item in pc_info['Ethernet']:
                        line = ''
                        line = self.add_column(line, '[%s](./%s.md)' % (item['Name'], item['hash']))
                        line = self.add_fi_eth_admin(line, item)
                        line = self.add_fi_eth_oper(line, item)
                        line = self.add_column(line, item['OperSpeed'])
                        line = self.add_column(line, item['Mode'])
                        line = self.add_column(line, item['TransceiverType'])
                        line = self.add_column(line, item['Role'])
                        line = self.add_fi_connected_device_name(line, item)
                        line = self.add_fi_connected_device_interface(line, item, last=True)
                        self.my_output.print_stream(line, 'output')

        if eth_info['Peer'] is not None:
            for server in servers:
                if server['Moid'] == eth_info['Peer']['ServerMoid']:
                    self.print_server(server, 'AddOn')
                    self.my_output.print_stream('', 'output')
                    self.print_server_vc(server, 'AddOn')

        self.save_output('%s' % (eth_info['hash']), subdir='fi/eth')

    def print_fi_interface_eth(self, fi_name, fi_info, info, servers):
        if info is None:
            return

        self.print_page_header('Ethernet Interface (%s)' % (fi_name))
        self.print_fi_devices_bar(fi_name, 'eth')
        self.print_fi_table_bar(fi_name, 'eth')

        up = 0
        enabled = 0
        count = 0
        for item in info:
            if item['AdminState'] == 'enabled':
                enabled = enabled + 1
            if item['OperState'] == 'up':
                up = up + 1
            count = count + 1

        self.fi_eth_up_count[fi_name] = up
        self.fi_eth_config_count[fi_name] = enabled
        self.fi_eth_count[fi_name] = count

        self.my_output.print_stream(
            '## Up Interfaces %s/%s/%s' % (up, enabled, count),
            'output'
        )

        order = [
            'Eth',
            'Admin',
            'Oper',
            'Speed',
            'Mode',
            'Trans',
            'PC',
            'Role',
            'Device',
            'Interface'
        ]
        self.print_table_header(order)

        for item in info:
            if item['OperState'] != 'up':
                continue

            line = ''
            line = self.add_column(line, '[%s](./eth/%s.md)' % (item['Name'], item['hash']))
            line = self.add_fi_eth_admin(line, item)
            line = self.add_fi_eth_oper(line, item)
            line = self.add_column(line, item['OperSpeed'])
            line = self.add_column(line, item['Mode'])
            line = self.add_column(line, item['TransceiverType'])
            if item['PortChannelId'] == 0:
                line = self.add_column(line, '---')
            else:
                pc_hash = self.xd_handler.get_fi_pc_hash(fi_name, item['PortChannelId'])
                if pc_hash is None:
                    line = self.add_column(line, item['PortChannelId'])
                else:
                    line = self.add_column(
                        line,
                        '[%s](./pc/%s.md)' % (
                            item['PortChannelId'],
                            pc_hash
                        )
                    )
            line = self.add_column(line, item['Role'])
            line = self.add_fi_connected_device_name(line, item)
            line = self.add_fi_connected_device_interface(line, item, last=True)
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '\n\n',
            'output'
        )

        self.my_output.print_stream(
            '## All Interfaces',
            'output'
        )

        order = [
            'Eth',
            'Admin',
            'Oper',
            'Speed',
            'Mode',
            'Trans',
            'PC',
            'Role',
            'Device',
            'Interface'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(line, '[%s](./eth/%s.md)' % (item['Name'], item['hash']))
            line = self.add_fi_eth_admin(line, item)
            line = self.add_fi_eth_oper(line, item)
            line = self.add_column(line, item['OperSpeed'])
            line = self.add_column(line, item['Mode'])
            line = self.add_column(line, item['TransceiverType'])
            if item['PortChannelId'] == 0:
                line = self.add_column(line, '---')
            else:
                pc_hash = self.xd_handler.get_fi_pc_hash(fi_name, item['PortChannelId'])
                if pc_hash is None:
                    line = self.add_column(line, item['PortChannelId'])
                else:
                    line = self.add_column(
                        line,
                        '[%s](./pc/%s.md)' % (
                            item['PortChannelId'],
                            pc_hash
                        )
                    )
            line = self.add_column(line, item['Role'])
            line = self.add_fi_connected_device_name(line, item)
            line = self.add_fi_connected_device_interface(line, item, last=True)
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '\n\n',
            'output'
        )

        self.save_output('%s-eth' % (self.fi_names_hash[fi_name]), subdir='fi')

        for item in info:
            self.print_fi_interface_eth_details(
                fi_name,
                fi_info,
                item,
                servers
            )
