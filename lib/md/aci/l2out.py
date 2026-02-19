import json


class MdAciL2OutOutput():
    def __init__(self):
        pass

    def print_aci_l2out_details(self, info):
        self.print_page_header('ACI L2Out')
        self.my_output.print_stream('- Controller: [%s](../%s-l2out.md)' % (info['apic'], info['apic']), 'output')
        self.my_output.print_stream('- Tenant: %s' % (info['tenant']), 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Dn: %s' % (info['dn']), 'output')
        self.my_output.print_stream('- Description: %s' % (info['descr']), 'output')

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(info['hash'], subdir='apic/l2out')

    def print_aci_tenant_l2out(self, info, tenant, controller):
        self.print_page_header('L2Out (%s:%s)' % (controller, tenant))
        self.print_aci_tenant_bar(controller, tenant, 'l2out')
        self.print_aci_tenant_table_bar(controller, tenant, 'l2out')

        order = [
            'Tenant',
            'Name',
            'Path',
            'Node'
        ]
        self.print_table_header(order)

        for item in info:
            if item['tenant'] != tenant:
                continue

            line = ''
            line = self.add_column(line, item['tenant'])
            line = self.add_column(
                line,
                '[%s](./l2out/%s.md)' % (
                    item['name'],
                    item['hash']
                )
            )
            line = self.add_column(line, item['pathCount'])
            line = self.add_column(line, item['nodeCount'])
            self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-l2out' % (controller, tenant), subdir='apic')

    def print_aci_l2out(self, info, controller):
        self.print_page_header('L2Out (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'l2out')
        self.print_aci_global_table_bar(controller, 'l2out')

        order = [
            'Tenant',
            'Name',
            'Path',
            'Node'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(line, item['tenant'])
            line = self.add_column(
                line,
                '[%s](./l2out/%s.md)' % (
                    item['name'],
                    item['hash']
                )
            )
            line = self.add_column(line, item['pathCount'])
            line = self.add_column(line, item['nodeCount'])
            self.my_output.print_stream(line, 'output')

            self.aci_l2out_count[controller] = self.aci_l2out_count[controller] + 1

        self.save_output('%s-l2out' % (controller), subdir='apic')

        for item in info:
            self.print_aci_l2out_details(item)
