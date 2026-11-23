class MdAciPhyStateOutput():
    def __init__(self):
        pass

    def print_aci_phy_state_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## Policy usage - Interface Phy', 'output')

        order = [
            'Node',
            'Intf',
            'State (ASO)',
            'PC',
            'Device',
            'Interface'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](../%s-%s-phy.md)' % (
                    item['nodeName'],
                    item['apic'],
                    item['nodeName']
                )
            )
            line = self.add_phy_interface(line, item, up=True)
            line = self.add_phy_interface_state(line, item)
            line = self.add_phy_interface_pc(line, item)
            line = self.add_aci_connected_device_name(line, item)
            line = self.add_aci_connected_device_interface(line, item, last=True)
            self.my_output.print_stream(line, 'output')

    def print_aci_node_phy_state(self, controller, node_name, info, servers, commands):
        self.print_page_header('Interface Phy - State (%s:%s)' % (controller, node_name))
        self.print_aci_node_bar(controller, node_name, 'phy')
        self.print_aci_node_table_bar(controller, node_name, 'phy')

        up = 0
        for item in info:
            if item['up']:
                up += 1

        self.aci_node_phy_up_count[controller][node_name] = up
        self.aci_node_phy_count[controller][node_name] = len(info)

        self.my_output.print_stream('# Up Interfaces %s/%s' % (up, len(info)), 'output')
        order = [
            'Intf',
            'State (ASO)',
            'PC',
            'CDP',
            'LLDP',
            'Device',
            'Interface'
        ]
        self.print_table_header(order)

        for item in info:
            if not item['up']:
                continue

            line = ''
            line = self.add_phy_interface(line, item)
            line = self.add_phy_interface_state(line, item)
            line = self.add_phy_interface_pc(line, item)
            line = self.add_phy_interface_cdp(line, item)
            line = self.add_phy_interface_lldp(line, item)
            line = self.add_aci_connected_device_name(line, item)
            line = self.add_aci_connected_device_interface(line, item, last=True)
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('# All Interfaces', 'output')
        order = [
            'Intf',
            'State (ASO)',
            'PC',
            'CDP',
            'LLDP',
            'Device',
            'Interface'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_phy_interface(line, item)
            line = self.add_phy_interface_state(line, item)
            line = self.add_phy_interface_pc(line, item)
            line = self.add_phy_interface_cdp(line, item)
            line = self.add_phy_interface_lldp(line, item)
            line = self.add_aci_connected_device_name(line, item)
            line = self.add_aci_connected_device_interface(line, item, last=True)
            self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-phy' % (controller, node_name), subdir='apic')

        for item in info:
            self.print_aci_node_phy_details(
                item,
                servers,
                commands
            )
