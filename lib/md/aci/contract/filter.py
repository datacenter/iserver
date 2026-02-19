import json


class MdAciContractFilterOutput():
    def __init__(self):
        pass

    def print_aci_contract_filter_details(self, info):
        self.print_page_header('ACI Contract Filter')
        self.my_output.print_stream('- Controller: [%s](../%s-contract-filter.md)' % (info['apic'], info['apic']), 'output')
        self.my_output.print_stream('- Tenant: [%s](../%s-%s-contract-filter.md)' % (info['tenant'], info['apic'], info['tenant']), 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Dn: %s' % (info['dn']), 'output')
        self.my_output.print_stream('- Description: %s' % (info['descr']), 'output')

        self.my_output.print_stream('## Entry', 'output')
        order = [
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

        for item in info['vzEntry']:
            line = ''
            line = self.add_column(line, item['name'])
            line = self.add_column(line, item['etherT'])
            line = self.add_column(line, item['arpOpc'])
            line = self.add_column(line, item['prot'])
            line = self.add_column_tick_string(line, item['applyToFrag'], 'yes')
            line = self.add_column_tick_string(line, item['stateful'], 'yes')
            line = self.add_column(line, item['source'])
            line = self.add_column(line, item['destination'])
            line = self.add_column(line, item['tcpRules'])
            self.my_output.print_stream(line, 'output')

        if len(info['contract']) > 0:
            self.my_output.print_stream('## Standard Contracts using Filter', 'output')
            order = [
                'Tenant',
                'Name'
            ]
            self.print_table_header(order)

            for item in info['contract']:
                line = ''
                line = self.add_column(line, item.split('/')[0])
                line = self.add_column(line, item.split('/')[1])
                self.my_output.print_stream(line, 'output')

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(info['hash'], subdir='apic/contract')

    def print_aci_tenant_contract_filter(self, info, tenant, controller):
        self.print_page_header('Contract Filter (%s:%s)' % (controller, tenant))
        self.print_aci_tenant_bar(controller, tenant, 'contract-filter')
        self.print_aci_tenant_table_bar(controller, tenant, 'contract-filter')

        order = [
            'Name',
            'Entry',
            'Contract',
            'Taboo'
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
            line = self.add_column(line, item['entryCount'])
            line = self.add_column(line, item['standardCount'])
            line = self.add_column(line, item['tabooCount'])
            self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-contract-filter' % (controller, tenant), subdir='apic')

    def print_aci_contract_filter(self, info, controller):
        self.print_page_header('Contract Filter (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'contract-filter')
        self.print_aci_global_table_bar(controller, 'contract-filter')

        order = [
            'Tenant',
            'Name',
            'Entry',
            'Contract',
            'Taboo'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./%s-%s-contract-filter.md)' % (
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
            line = self.add_column(line, item['entryCount'])
            line = self.add_column(line, item['standardCount'])
            line = self.add_column(line, item['tabooCount'])
            self.my_output.print_stream(line, 'output')

            self.aci_contract_filter_count[controller] = self.aci_contract_filter_count[controller] + 1

        self.save_output('%s-contract-filter' % (controller), subdir='apic')

        for item in info:
            self.print_aci_contract_filter_details(item)
