class MdAciPhyVlanOutput():
    def __init__(self):
        pass

    def print_aci_node_phy_vlan(self, controller, node_name, info, commands):
        self.print_page_header('Interface Phy - VLAN (%s:%s)' % (controller, node_name))
        self.print_aci_node_bar(controller, node_name, 'phy:vlan')
        self.print_aci_node_table_bar(controller, node_name, 'phy:vlan')

        order = [
            'Intf',
            'PI VLANs',
            'Encap VLANs'
        ]
        self.print_table_header(order)

        for item in info:
            if not item['up']:
                continue

            line = ''
            line = self.add_phy_interface(line, item, add_oper=True)
            if item['pi_vlans'] is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, ', '.join(item['pi_vlans']))
            if item['encap_vlan_ids'] is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, ', '.join(item['encap_vlan_ids']))

            self.my_output.print_stream(line, 'output')

            line = ''
            line = self.add_column(line, '&nbsp;')
            line = self.add_aci_connected_device_name(line, item)
            line = self.add_aci_connected_device_interface(line, item, last=True)
            self.my_output.print_stream(line, 'output')

        if 'vlan-extended' in commands:
            self.my_output.print_stream('## VLAN extended information', 'output')

            order = [
                'PI VLAN',
                'Name',
                'Encap',
                'Ports'
            ]
            self.print_table_header(order)

            for item in commands['vlan-extended']['parsed']:
                line = ''
                line = self.add_column(
                    line,
                    item['id']
                )
                line = self.add_column(
                    line,
                    item['name']
                )
                line = self.add_column(
                    line,
                    ', '.join(item['encap'])
                )
                line = self.add_column(
                    line,
                    ', '.join(item['ports'])
                )
                self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-phy-vlan' % (controller, node_name), subdir='apic')
