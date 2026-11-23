class MdFiPcOutput():
    def __init__(self):
        pass

    def add_fi_pc_admin(self, line, info):
        return self.add_column_tick_string(
            line,
            info['AdminState'],
            'enabled'
        )

    def add_fi_pc_oper(self, line, info):
        return self.add_column_tick_string(
            line,
            info['OperState'],
            'up'
        )

    def print_fi_interface_pc_details(self, fi_name, fi_info, pc_info):
        self.print_page_header('Fabric Interconnect Port Channel')

        self.my_output.print_stream('- Fabric Interconnect: [%s](../%s-eth.md)' % (fi_name, fi_info['hash']), 'output')
        self.my_output.print_stream('- Switch ID: %s' % (pc_info['SwitchId']), 'output')
        self.my_output.print_stream('- Port Channel: %s' % (pc_info['PortChannelId']), 'output')
        self.my_output.print_stream('- Name: %s' % (pc_info['Name']), 'output')
        self.my_output.print_stream('- Description: %s' % (pc_info['Description']), 'output')
        self.my_output.print_stream('- Dn: %s' % (pc_info['Dn']), 'output')
        self.my_output.print_stream('- Role: %s' % (pc_info['Role']), 'output')

        self.my_output.print_stream('## State', 'output')
        if pc_info['AdminState'] == 'enabled':
            self.my_output.print_stream('- Admin state :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Admin state :x:', 'output')

        self.my_output.print_stream('- Oper state: %s' % (pc_info['OperState']), 'output')
        self.my_output.print_stream('- Oper speed: %s' % (pc_info['OperSpeed']), 'output')
        self.my_output.print_stream('- Bandwidth: %s' % (pc_info['BandWidth']), 'output')
        if len(pc_info['AccessVlan']) == 0:
            self.my_output.print_stream('- Access VLAN: ---', 'output')
        else:
            self.my_output.print_stream('- Access Vlan: %s' % (pc_info['AccessVlan']), 'output')
        if len(pc_info['AllowedVlans']) == 0:
            self.my_output.print_stream('- Allowed Vlans: ---', 'output')
        else:
            self.my_output.print_stream('- Allowed Vlans: %s' % (pc_info['AllowedVlans']), 'output')
        self.my_output.print_stream('- Members: %s' % (pc_info['MemberSummary']), 'output')

        self.my_output.print_stream('## Port Channel Members', 'output')

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

        for eth in pc_info['Ethernet']:
            line = ''
            line = self.add_column(line, '[%s](../eth/%s.md)' % (eth['Name'], eth['hash']))
            line = self.add_fi_eth_admin(line, eth)
            line = self.add_fi_eth_oper(line, eth)
            line = self.add_column(line, eth['OperSpeed'])
            line = self.add_column(line, eth['Mode'])
            line = self.add_column(line, eth['TransceiverType'])
            line = self.add_column(line, eth['Role'])
            line = self.add_fi_connected_device_name(line, eth)
            line = self.add_fi_connected_device_interface(line, eth, last=True)
            self.my_output.print_stream(line, 'output')

        self.save_output('%s' % (pc_info['hash']), subdir='fi/pc')

    def print_fi_interface_pc(self, fi_name, fi_info, info):
        if info is None:
            return

        self.print_page_header('Port Channel Interface (%s)' % (fi_name))
        self.print_fi_devices_bar(fi_name, 'pc')
        self.print_fi_table_bar(fi_name, 'pc')

        up = 0
        count = 0
        for item in info:
            if item['OperState'] == 'up':
                up = up + 1
            count = count + 1

        self.fi_pc_up_count[fi_name] = up
        self.fi_pc_count[fi_name] = count

        order = [
            'Port Channel ID',
            'Name',
            'Admin',
            'Oper',
            'Speed',
            'BW',
            'Role',
            'Switch ID',
            'Members'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(line, '[%s](./pc/%s.md)' % (item['PortChannelId'], item['hash']))
            line = self.add_column(line, item['Name'])
            line = self.add_fi_pc_admin(line, item)
            line = self.add_fi_pc_oper(line, item)
            line = self.add_column(line, item['OperSpeed'])
            line = self.add_column(line, item['BandWidth'])
            line = self.add_column(line, item['Role'])
            line = self.add_column(line, item['SwitchId'])
            line = self.add_column(line, item['MemberSummary'])
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('## Port Channel Members', 'output')

        order = [
            'PC',
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

        for item in info:
            for eth in item['Ethernet']:
                line = ''
                line = self.add_column(line, eth['PortChannelId'])
                line = self.add_column(line, '[%s](../eth/%s.md)' % (eth['Name'], eth['hash']))
                line = self.add_fi_eth_admin(line, eth)
                line = self.add_fi_eth_oper(line, eth)
                line = self.add_column(line, eth['OperSpeed'])
                line = self.add_column(line, eth['Mode'])
                line = self.add_column(line, eth['TransceiverType'])
                line = self.add_column(line, eth['Role'])
                line = self.add_fi_connected_device_name(line, eth)
                line = self.add_fi_connected_device_interface(line, eth, last=True)
                self.my_output.print_stream(line, 'output')

        self.my_output.print_stream(
            '\n\n',
            'output'
        )

        self.save_output('%s-pc' % (self.fi_names_hash[fi_name]), subdir='fi')

        for item in info:
            self.print_fi_interface_pc_details(
                fi_name,
                fi_info,
                item
            )
