from lib.aci import helper as aci_helper


class MdAciAaeOutput():
    def __init__(self):
        pass

    def print_aci_aae_domain_addon(self, info, title=True):
        if title:
            self.my_output.print_stream('## Domain', 'output')

        order = [
            'Name',
            'Type'
        ]
        self.print_table_header(order)

        for domain in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](../domain/%s.md)' % (
                    domain['domainName'],
                    domain['hash']
                )
            )
            line = self.add_column(line, domain['domainType'])
            self.my_output.print_stream(line, 'output')

    def print_aci_aae_epg_addon(self, info, title=True):
        if title:
            self.my_output.print_stream('## Application EPG', 'output')

        order = [
            'Tenant',
            'Application Profile',
            'Name',
            'Encap',
            'Primary Encap'
        ]
        self.print_table_header(order)

        for epg in info:
            line = ''
            line = self.add_column(line, epg['tenant'])
            line = self.add_column(line, epg['application_profile'])
            line = self.add_column(line, '[%s](../epg/%s.md)' % (epg['name'], epg['hash']))
            line = self.add_column(line, epg['encap'])
            line = self.add_column(line, epg['primaryEncap'])
            self.my_output.print_stream(line, 'output')

    def print_aci_aae_policy_group_addon(self, info, title=True):
        if title:
            self.my_output.print_stream('## Policy Group', 'output')

        order = [
            'Name',
            'Type'
        ]
        self.print_table_header(order)

        for pg in info:
            line = ''
            line = self.add_column(line, pg['name'])
            line = self.add_column(
                line,
                aci_helper.get_policy_type_from_tcl(pg['type'])
            )
            self.my_output.print_stream(line, 'output')

    def print_aci_aae_vm_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## Virtual Machine', 'output')

        order = [
            'Dn',
            'Class'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(line, item['ctxDn'])
            line = self.add_column(line, item['ctxClass'])
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def print_aci_aae_port_group_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## Port Group', 'output')

        order = [
            'Dn',
            'Class'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(line, item['ctxDn'])
            line = self.add_column(line, item['ctxClass'])
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def print_aci_aae_details(self, info):
        self.print_page_header('ACI Attachable Access Entity')
        self.my_output.print_stream('- Controller: [%s](../%s-aae.md)' % (info['apic'], info['apic']), 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Dn: %s' % (info['dn']), 'output')
        self.my_output.print_stream('- Description: %s' % (info['descr']), 'output')
        self.my_output.print_stream('- Infrastructure VLAN Enabled: %s' % (info['infraVlanEnabled']), 'output')

        self.print_aci_aae_domain_addon(info['infraRsDomP'])
        self.print_aci_aae_epg_addon(info['infraRsFuncToEpg'])
        self.print_aci_aae_policy_group_addon(info['infraRtAttEntP'])
        self.print_aci_aae_vm_addon(info['vm'])
        self.print_aci_aae_port_group_addon(info['pg'])
        self.print_aci_phy_state_addon(info['interfacePhy'])

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(info['hash'], subdir='apic/aae')

    def print_aci_aae(self, info, controller):
        self.print_page_header('Attachable Access Entity (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'aae')
        self.print_aci_policy_table_bar(controller, 'aae')

        order = [
            'Name',
            'Infra',
            'Policy Group',
            'Domain',
            'EPG',
            'VM',
            'Port Group',
            'Node',
            'Intf'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./aae/%s.md)' % (
                    item['name'],
                    item['hash']
                )
            )
            line = self.add_column_tick_bool(line, item['infraVlanEnabled'])
            if len(item['policyGroups']) == 0:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, item['policyGroups'][0])

            line = self.add_column(line, item['domainCount'])
            line = self.add_column(line, item['epgCount'])
            line = self.add_column(line, item['vmCount'])
            line = self.add_column(line, item['portGroupCount'])
            line = self.add_column(line, item['nodeCount'])
            line = self.add_column(line, item['interfaceCount'])
            self.my_output.print_stream(line, 'output')

            if len(item['policyGroups']) > 1:
                for i in range(len(item['policyGroups'])):
                    if i == 0:
                        continue

                    line = ''
                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, item['policyGroups'][i])
                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, '&nbsp;')
                    self.my_output.print_stream(line, 'output')

            self.aci_aae_count[controller] = self.aci_aae_count[controller] + 1

        self.save_output('%s-aae' % (controller), subdir='apic')

        for item in info:
            self.print_aci_aae_details(item)
