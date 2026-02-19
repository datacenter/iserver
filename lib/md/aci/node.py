class MdAciNodeOutput():
    def __init__(self):
        pass

    def print_aci_node_interface_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## Interface', 'output')

        order = [
            'Interface',
            'Up',
            'Down',
            'Count'
        ]
        self.print_table_header(order)

        for key in ['100M', '1G', '10G', '25G', '100G', '400G', 'uplink', 'downlink', 'port']:
            line = ''
            line = self.add_column(line, key)
            line = self.add_column(line, info['%sUp' % (key)])
            line = self.add_column(line, info['%sDown' % (key)])
            line = self.add_column(line, info['%sCount' % (key)])
            self.my_output.print_stream(line, 'output')

    def print_aci_node_psu_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## PSU', 'output')

        order = [
            'Slot',
            'Oper',
            'Fan',
            'Model',
            'Serial',
            'Current',
            'Voltage'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(line, item['slotId'])
            line = self.add_column_tick_string(line, item['operSt'], 'ok')
            line = self.add_column_tick_string(line, item['fanOpSt'], 'ok')
            line = self.add_column(line, item['model'])
            line = self.add_column(line, item['ser'])
            line = self.add_column(line, item['drawnCurr'])
            line = self.add_column(line, item['volt'])
            self.my_output.print_stream(line, 'output')

    def print_aci_node(self, controller, info):
        self.print_page_header(
            'Node (%s:%s [%s])' % (
                controller,
                info['name'],
                info['id']
            )
        )
        self.print_aci_node_bar(controller, info['name'], 'node')
        self.my_output.print_stream('[Back](../README.md)', 'output')

        self.my_output.print_stream('- Dn: %s' % (info['dn']), 'output')
        self.my_output.print_stream('- Role: %s' % (info['role']), 'output')
        self.my_output.print_stream('- Fabric Address: %s' % (info['address']), 'output')
        if info['system'] is not None:
            self.my_output.print_stream('- Management Address: %s' % (info['system']['inbMgmtAddr']), 'output')
        self.my_output.print_stream('- Admin state: %s' % (info['adSt']), 'output')
        self.my_output.print_stream('- Fabric state: %s' % (info['fabricSt']), 'output')
        self.my_output.print_stream('- Model: %s' % (info['model']), 'output')
        self.my_output.print_stream('- Serial: %s' % (info['serial']), 'output')
        self.my_output.print_stream('- Version: %s' % (info['version']), 'output')

        self.print_aci_node_interface_addon(info['interfaces_summary'])
        self.print_aci_node_psu_addon(info['psu'])

        self.save_output('%s-%s-node' % (controller, info['name']), subdir='apic')
