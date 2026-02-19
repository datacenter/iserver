import json


class MdAciDomainVmmOutput():
    def __init__(self):
        pass

    def print_aci_domain_vmm_details(self, info):
        self.print_page_header('ACI Domain VMM')
        self.my_output.print_stream('- Controller: [%s](../%s-domain-vmm.md)' % (info['apic'], info['apic']), 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')

        self.my_output.print_stream('## Properties', 'output')
        self.my_output.print_stream('- Encapsulation: %s' % (info['encapMode']), 'output')
        self.my_output.print_stream('- Access mode: %s' % (info['accessMode']), 'output')
        self.my_output.print_stream('- Endpoint Retention Time: %s' % (info['epRetTime']), 'output')
        self.my_output.print_stream('- Enabled Tag Collection: %s' % (info['enableTag']), 'output')
        self.my_output.print_stream('- Enabled VM Folder Data Retrieval: %s' % (info['enableVmFolder']), 'output')

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

        self.my_output.print_stream('## vCenter', 'output')

        order = [
            'Name',
            'Address',
            'User'
        ]
        self.print_table_header(order)

        for item in info['vmmCtrlrP']:
            line = ''
            line = self.add_column(line, item['name'])
            line = self.add_column(line, item['hostOrIp'])
            line = self.add_column(line, item['usr'])
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('## Associated EPG', 'output')

        order = [
            'Name',
            'Deployment',
            'Resolution',
            'VLAN',
            'Switching'
        ]
        self.print_table_header(order)

        for item in info['vmmEpPD']:
            line = ''
            line = self.add_column(line, item['tenantAppEpg'])
            line = self.add_column(line, item['instrImedcy'])
            line = self.add_column(line, item['resImedcy'])
            line = self.add_column(line, '%s (%s) [%s]' % (item['vlanId'], item['allocMode'], item['encapCtx']))
            line = self.add_column(line, item['switchingMode'])
            self.my_output.print_stream(line, 'output')

        self.print_aci_pool_vlan_addon(info['vlan_info'])
        self.print_aci_phy_state_addon(info['interfacePhy'])

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(info['hash'], subdir='apic/domain')

    def print_aci_domain_vmm(self, info, controller):
        self.print_page_header('Domain VMM (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'domain-vmm')
        self.print_aci_policy_table_bar(controller, 'domain-vmm')

        order = [
            'Name',
            'AAE',
            'VLAN',
            'Controller',
            'EPG',
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
            line = self.add_column(line, item['controllerCount'])
            line = self.add_column(line, item['epgCount'])
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
                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, '&nbsp;')
                    self.my_output.print_stream(line, 'output')

            self.aci_domain_vmm_count[controller] = self.aci_domain_vmm_count[controller] + 1

        self.save_output('%s-domain-vmm' % (controller), subdir='apic')

        for item in info:
            self.print_aci_domain_vmm_details(item)
