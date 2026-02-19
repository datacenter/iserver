class MdAciPhyL2Output():
    def __init__(self):
        pass

    def map_aci_phy_l2_fec(self, fec):
        if fec == 'disable-fec':
            return None

        if fec == 'kp-fec':
            return 'kp'

        if fec == 'cl92-rs-fec':
            return 'cl92-rs'

        return fec

    def print_aci_node_phy_l2(self, controller, node_name, info):
        self.print_page_header('Interface Phy - L2 (%s:%s)' % (controller, node_name))
        self.print_aci_node_bar(controller, node_name, 'phy:l2')
        self.print_aci_node_table_bar(controller, node_name, 'phy:l2')

        order = [
            'Intf',
            'Type',
            'MTU',
            'Mode',
            'Speed',
            'FEC',
            'Device',
            'Interface'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_phy_interface(line, item, add_oper=True)
            if item['layerT'] == 'switched':
                line = self.add_column(line, 'L2 (%s)' % (item['portT']))
            else:
                line = self.add_column(line, 'L3 (%s)' % (item['portT']))
            line = self.add_column(line, item['mtu'])
            if item['stats'] is None:
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, item['stats']['operMode'])
                line = self.add_column(line, '%s (%s)' % (item['stats']['operSpeed'], item['stats']['operDuplex']))
                line = self.add_column(line, self.map_aci_phy_l2_fec(item['stats']['operFecMode']))
            line = self.add_aci_connected_device_name(line, item)
            line = self.add_aci_connected_device_interface(line, item, last=True)
            self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-phy-l2' % (controller, node_name), subdir='apic')
