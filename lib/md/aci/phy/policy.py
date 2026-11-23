class MdAciPhyPolicyOutput():
    def __init__(self):
        pass

    def print_aci_node_phy_policy(self, controller, node_name, info):
        self.print_page_header('Interface Phy - Policy (%s:%s)' % (controller, node_name))
        self.print_aci_node_bar(controller, node_name, 'phy:policy')
        self.print_aci_node_table_bar(controller, node_name, 'phy:policy')

        order = [
            'Intf',
            'Leaf Prof',
            'Intf Prof',
            'Intf Sel',
            'PG Type',
            'PG Name',
            'AAE'
        ]
        self.print_table_header(order)

        for item in info:
            if item['policy_selector'] is None:
                continue

            line = ''
            line = self.add_phy_interface(line, item, add_oper=True)
            line = self.add_column(line, item['policy_selector']['leafPolicy'])
            line = self.add_column(line, item['policy_selector']['profile'])
            line = self.add_column(line, item['policy_selector']['name'])
            line = self.add_column(line, item['policy_selector']['policy_group_type_name'])
            line = self.add_column(line, item['policy_selector']['policy_group_name'])
            if item['policy_selector']['policy_group_info'] is None or item['policy_selector']['policy_group_info']['aaep'] is None:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, item['policy_selector']['policy_group_info']['aaep']['name'])

            self.my_output.print_stream(line, 'output')

            line = ''
            line = self.add_column(line, '&nbsp;')
            line = self.add_column(line, '&nbsp;')
            line = self.add_column(line, '&nbsp;')
            line = self.add_column(line, '&nbsp;')
            line = self.add_column(line, '&nbsp;')
            line = self.add_aci_connected_device_name(line, item)
            line = self.add_aci_connected_device_interface(line, item, last=True)
            self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-phy-policy' % (controller, node_name), subdir='apic')
