class MdAciPhyOpticsOutput():
    def __init__(self):
        pass

    def print_aci_node_phy_optics(self, controller, node_name, info, servers):
        self.print_page_header('Interface Phy - Optics (%s:%s)' % (controller, node_name))
        self.print_aci_node_bar(controller, node_name, 'phy:optics')
        self.print_aci_node_table_bar(controller, node_name, 'phy:optics')

        self.my_output.print_stream('## State', 'output')

        order = [
            'Intf',
            'Optics',
            'Type',
            'PN',
            'SN'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_phy_interface(line, item, add_oper=True)

            if item['fc_stats'] is None:
                continue

            if item['fc_stats']['actualType'] == 'unknown':
                continue

            line = self.add_column(line, item['fc_stats']['actualType'])
            line = self.add_column(
                line,
                '%s (Rev:%s)' % (
                    item['fc_stats']['typeName'],
                    item['fc_stats']['guiRev']
                )
            )
            line = self.add_column(line, item['fc_stats']['guiPN'])
            line = self.add_column(line, item['fc_stats']['guiSN'])
            self.my_output.print_stream(line, 'output')

            line = ''
            line = self.add_column(line, '&nbsp;')
            line = self.add_column(line, '&nbsp;')
            line = self.add_column(line, '&nbsp;')
            line = self.add_aci_connected_device_name(line, item)
            line = self.add_aci_connected_device_interface(line, item, last=True)
            self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-phy-optics' % (controller, node_name), subdir='apic')
