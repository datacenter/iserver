import json


class MdAciApOutput():
    def __init__(self):
        pass

    def print_aci_ap_details(self, info):
        self.print_page_header('ACI Application Profile')
        self.my_output.print_stream('- Controller: [%s](../%s-ap.md)' % (info['apic'], info['apic']), 'output')
        self.my_output.print_stream('- Tenant: [%s](../%s-%s-ap.md)' % (info['tenant'], info['apic'], info['tenant']), 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Health: %s' % (info['health']), 'output')
        self.my_output.print_stream('- Faults: %s' % (info['faults']), 'output')
        self.my_output.print_stream('- EPG: %s' % (len(info['epgs'])), 'output')
        self.my_output.print_stream('- Contract relations: %s' % (info['contractRelations']), 'output')
        self.my_output.print_stream('- Nodes using policy: %s' % (len(info['node'])), 'output')
        self.my_output.print_stream('- Domains', 'output')
        self.my_output.print_stream('- \tPhysical: %s' % (info['domainCount']['phy']), 'output')
        self.my_output.print_stream('- \tL2 External: %s' % (info['domainCount']['l2']), 'output')
        self.my_output.print_stream('- \tVMM: %s' % (info['domainCount']['vmm']), 'output')

        if len(info['epgs']) > 0:
            self.my_output.print_stream('## EPG', 'output')
            order = [
                'Name',
                'Class ID',
                'Preferred Group Member',
                'Flood',
                'BD',
                'Domain'
            ]
            self.print_table_header(order)
            for epg in info['epgs']:
                line = ''
                line = self.add_column(
                    line,
                    '[%s](../epg/%s.md)' % (
                        epg['nameTenant'],
                        epg['hash']
                    )
                )
                line = self.add_column(line, epg['pcTag'])
                line = self.add_column(line, epg['prefGrMemb'])
                line = self.add_column(line, epg['floodOnEncap'])
                line = self.add_column(
                    line,
                    '[%s/%s](../bd/%s.md)' % (
                        epg['bd_tenant_name'],
                        epg['bd_name'],
                        epg['bd_hash']
                    )
                )

                domains = []
                for domain in epg['domain']:
                    domains.append(
                        '[%s](../domain/%s.md)' % (
                            domain['name'],
                            domain['hash']
                        )
                    )
                if len(domains) == 0:
                    line = self.add_column(line, '---')
                else:
                    line = self.add_column(
                        line,
                        ', '.join(domains)
                    )

                self.my_output.print_stream(line, 'output')

        if len(info['contracts']) > 0:
            self.my_output.print_stream('## Contract', 'output')
            order = [
                'Contract',
                'Type',
                'EPG'
            ]
            self.print_table_header(order)
            for contract in info['contracts']:
                line = ''
                line = self.add_column(
                    line,
                    '[%s](../contract/%s.md)' % (
                        contract['contract'],
                        contract['contract_hash']
                    )
                )
                line = self.add_column(line, contract['type'])
                line = self.add_column(
                    line,
                    '[%s](../epg/%s.md)' % (
                        contract['epg'],
                        contract['epg_hash']
                    )
                )
                self.my_output.print_stream(line, 'output')

        self.print_aci_phy_state_addon(info['interfacePhy'])

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(info['hash'], subdir='apic/ap')

    def print_aci_tenant_ap(self, info, tenant, controller):
        self.print_page_header('Application Profile (%s:%s)' % (controller, tenant))
        self.print_aci_tenant_bar(controller, tenant, 'ap')
        self.print_aci_tenant_table_bar(controller, tenant, 'ap')

        order = [
            'Name',
            'EPG',
            'Contract',
            'Nodes'
        ]
        self.print_table_header(order)

        for item in info:
            if item['tenant'] != tenant:
                continue

            line = ''
            line = self.add_column(
                line,
                '[%s](./ap/%s.md)' % (
                    item['name'],
                    item['hash']
                )
            )
            line = self.add_column(line, len(item['epgs']))
            line = self.add_column(line, item['contractRelations'])
            line = self.add_column(line, len(item['node']))
            self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-ap' % (controller, tenant), subdir='apic')

    def print_aci_ap(self, info, controller):
        self.print_page_header('Application Profile (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'ap')
        self.print_aci_global_table_bar(controller, 'ap')

        order = [
            'Tenant',
            'Name',
            'EPG',
            'Contract',
            'Node'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./%s-%s-ap.md)' % (
                    item['tenant'],
                    item['apic'],
                    item['tenant']
                )
            )
            line = self.add_column(
                line,
                '[%s](./ap/%s.md)' % (
                    item['name'],
                    item['hash']
                )
            )
            line = self.add_column(line, len(item['epgs']))
            line = self.add_column(line, item['contractRelations'])
            line = self.add_column(line, len(item['node']))
            self.my_output.print_stream(line, 'output')

            self.aci_ap_count[controller] = self.aci_ap_count[controller] + 1

        self.save_output('%s-ap' % (controller), subdir='apic')

        for item in info:
            self.print_aci_ap_details(item)
