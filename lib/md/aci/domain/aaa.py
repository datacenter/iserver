class MdAciDomainAaaOutput():
    def __init__(self):
        pass

    # def print_aci_domain_aaa_details(self, info):
    #     self.print_page_header('ACI Domain AAA')
    #     self.my_output.print_stream('- Controller: [%s](../%s-domain-aaa.md)' % (info['apic'], info['apic']), 'output')
    #     self.my_output.print_stream('- Name: %s' % (info['name']), 'output')

    #     self.my_output.print_stream('\n## Debug\n', 'output')
    #     self.my_output.print_stream('```', 'output')
    #     self.my_output.print_stream(json.dumps(info, indent=4), 'output')
    #     self.my_output.print_stream('```', 'output')

    #     self.save_output(info['hash'], subdir='apic/domain')

    def print_aci_domain_aaa(self, info, controller):
        self.print_page_header('Domain AAA (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'domain-aaa')
        self.print_aci_policy_table_bar(controller, 'domain-aaa')

        order = [
            'Name',
            'Dn'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(line, item['name'])
            line = self.add_column(line, item['dn'])
            self.my_output.print_stream(line, 'output')

            self.aci_domain_aaa_count[controller] = self.aci_domain_aaa_count[controller] + 1

        self.save_output('%s-domain-aaa' % (controller), subdir='apic')

        # for item in info:
        #     self.print_aci_domain_aaa_details(item)
