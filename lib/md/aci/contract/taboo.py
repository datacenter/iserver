import json


class MdAciContractTabooOutput():
    def __init__(self):
        pass

    def print_aci_contract_taboo_details(self, info):
        self.print_page_header('ACI Contract Taboo')
        self.my_output.print_stream('- Controller: [%s](../%s-contract-taboo.md)' % (info['apic'], info['apic']), 'output')
        self.my_output.print_stream('- Tenant: [%s](../%s-%s-contract-taboo.md)' % (info['tenant'], info['apic'], info['tenant']), 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Dn: %s' % (info['dn']), 'output')
        self.my_output.print_stream('- Description: %s' % (info['descr']), 'output')

        self.my_output.print_stream('## Subject', 'output')

        order = [
            'Name',
            'Descr',
            'Filter'
        ]
        self.print_table_header(order)

        for item in info['vzTSubj']:
            line = ''
            line = self.add_column(line, item['name'])
            line = self.add_column(line, item['descr'])
            line = self.add_column(line, ','.join(item['vzFilterName']))
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('## Filter', 'output')

        order = [
            'Name',
            'Entry',
            'Ether',
            'ARP',
            'Proto',
            'Fragments',
            'Stateful',
            'Src',
            'Dest',
            'Rules'
        ]
        self.print_table_header(order)

        for fitem in info['vzFilter']:
            for eitem in fitem['vzEntry']:
                line = ''
                line = self.add_column(line, fitem['nameTenant'])
                line = self.add_column(line, eitem['name'])
                line = self.add_column(line, eitem['etherT'])
                line = self.add_column(line, eitem['arpOpc'])
                line = self.add_column(line, eitem['prot'])
                line = self.add_column_tick_string(line, eitem['applyToFrag'], 'yes')
                line = self.add_column_tick_string(line, eitem['stateful'], 'yes')
                line = self.add_column(line, eitem['source'])
                line = self.add_column(line, eitem['destination'])
                line = self.add_column(line, eitem['tcpRules'])
                self.my_output.print_stream(line, 'output')

        if len(info['protectedEpg']) > 0:
            self.my_output.print_stream('## Protected EPG', 'output')

            order = [
                'Name',
                'Class'
            ]
            self.print_table_header(order)

            for item in info['protectedEpg']:
                line = ''
                line = self.add_column(line, item['nameLong'])
                line = self.add_column(line, item['class'])
                self.my_output.print_stream(line, 'output')

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(info['hash'], subdir='apic/contract')

    def print_aci_tenant_contract_taboo(self, info, tenant, controller):
        self.print_page_header('Contract Taboo (%s:%s)' % (controller, tenant))
        self.print_aci_tenant_bar(controller, tenant, 'contract-taboo')
        self.print_aci_tenant_table_bar(controller, tenant, 'contract-taboo')

        order = [
            'Name',
            'Subject',
            'Filter',
            'EPG'
        ]
        self.print_table_header(order)

        for item in info:
            if item['tenant'] != tenant:
                continue

            line = ''
            line = self.add_column(
                line,
                '[%s](./contract/%s.md)' % (
                    item['name'],
                    item['hash']
                )
            )
            line = self.add_column(line, item['subjectCount'])
            line = self.add_column(line, item['filterCount'])
            line = self.add_column(line, item['epgCount'])
            self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-contract-taboo' % (controller, tenant), subdir='apic')

    def print_aci_contract_taboo(self, info, controller):
        self.print_page_header('Contract Taboo (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'contract-taboo')
        self.print_aci_global_table_bar(controller, 'contract-taboo')

        order = [
            'Tenant',
            'Name',
            'Subject',
            'Filter',
            'EPG'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./%s-%s-contract-taboo.md)' % (
                    item['tenant'],
                    item['apic'],
                    item['tenant']
                )
            )
            line = self.add_column(
                line,
                '[%s](./contract/%s.md)' % (
                    item['name'],
                    item['hash']
                )
            )
            line = self.add_column(line, item['subjectCount'])
            line = self.add_column(line, item['filterCount'])
            line = self.add_column(line, item['epgCount'])
            self.my_output.print_stream(line, 'output')

            self.aci_contract_taboo_count[controller] = self.aci_contract_taboo_count[controller] + 1

        self.save_output('%s-contract-taboo' % (controller), subdir='apic')

        for item in info:
            self.print_aci_contract_taboo_details(item)
