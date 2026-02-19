import json


class MdAciDomainPhyOutput():
    def __init__(self):
        pass

    def print_aci_domain_phy_details(self, info):
        self.print_page_header('ACI Domain Phy')
        self.my_output.print_stream('- Controller: [%s](../%s-domain-phy.md)' % (info['apic'], info['apic']), 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')
        if len(info['aaep_names']) == 0:
            self.my_output.print_stream('- Associated AAE: ---', 'output')
        else:
            self.my_output.print_stream('- Associated AAE', 'output')
            for aae_name in info['aaep_names']:
                self.my_output.print_stream(
                    '\t- [%s](../aae/%s.md)' % (
                        aae_name,
                        info['aae_hash'][aae_name]
                    ),
                    'output'
                )

        if len(info['epg']) == 0:
            self.my_output.print_stream('- Associated EPG: ---', 'output')
        else:
            self.my_output.print_stream('- Associated EPG', 'output')
            for epg_info in info['epg']:
                self.my_output.print_stream(
                    '\t- [%s](../epg/%s.md)' % (
                        epg_info['name'],
                        epg_info['hash']
                    ),
                    'output'
                )

        self.print_aci_pool_vlan_addon(info['vlan_info'])
        self.print_aci_phy_state_addon(info['interfacePhy'])

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(info['hash'], subdir='apic/domain')

    def print_aci_domain_phy(self, info, controller):
        self.print_page_header('Domain Phy (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'domain-phy')
        self.print_aci_policy_table_bar(controller, 'domain-phy')

        order = [
            'Name',
            'AAE',
            'VLAN',
            'Node',
            'Interface'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./domain/%s.md)' % (
                    item['name'],
                    item['hash']
                )
            )
            if len(item['aaep_names']) == 0:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, item['aaep_names'][0])
            line = self.add_column(line, item['vlan'])
            line = self.add_column(line, item['nodeCount'])
            line = self.add_column(line, item['interfaceCount'])
            self.my_output.print_stream(line, 'output')

            if len(item['aaep_names']) > 1:
                for i in range(len(item['aaep_names'])):
                    if i == 0:
                        continue

                    line = ''
                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, item['aaep_names'][i])
                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, '&nbsp;')
                    self.my_output.print_stream(line, 'output')

            self.aci_domain_phy_count[controller] = self.aci_domain_phy_count[controller] + 1

        self.save_output('%s-domain-phy' % (controller), subdir='apic')

        for item in info:
            self.print_aci_domain_phy_details(item)
