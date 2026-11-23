class MdAciPoolVlanOutput():
    def __init__(self):
        pass

    def print_aci_pool_vlan_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## Pool VLAN', 'output')

        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Allocation mode: %s' % (info['allocMode']), 'output')
        self.my_output.print_stream('- VLAN count: %s' % (info['vlanCount']), 'output')
        self.my_output.print_stream('- EPG count: %s' % (info['epgCount']), 'output')
        self.my_output.print_stream('', 'output')

        order = [
            'Name',
            'Role',
            'Mode',
            'From',
            'To'
        ]
        self.print_table_header(order)

        for vlan in info['fvnsEncapBlk']:
            line = ''
            line = self.add_column(line, vlan['name'])
            line = self.add_column(line, vlan['role'])
            line = self.add_column(line, vlan['allocMode'])
            line = self.add_column(line, vlan['fromVlan'])
            line = self.add_column(line, vlan['toVlan'])
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def print_aci_pool_vlan_domain_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## Domain', 'output')

        order = [
            'Name',
            'Type'
        ]
        self.print_table_header(order)

        for domain in info:
            line = ''
            line = self.add_column(line, domain['domainName'])
            line = self.add_column(line, domain['tCl'])
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def print_aci_pool_vlan_vm_addon(self, info, title=True):
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

    def print_aci_pool_vlan_pg_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## VMM Port Group', 'output')

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

    def print_aci_pool_vlan_details(self, info):
        self.print_page_header('ACI Pool VLAN')
        self.my_output.print_stream('- Controller: [%s](../%s-vlan-pool.md)' % (info['apic'], info['apic']), 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')

        self.print_aci_pool_vlan_addon(info, title=False)
        self.print_aci_pool_vlan_domain_addon(info['fvnsRtVlanNs'])
        self.print_aci_pool_vlan_vm_addon(info['VlanNsToVirtualMachines'])
        self.print_aci_pool_vlan_pg_addon(info['VlanNsToVmmPortGroups'])
        self.print_aci_phy_state_addon(info['interfacePhy'])

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(info['hash'], subdir='apic/pool')

    def print_aci_pool_vlan(self, info, controller):
        self.print_page_header('Pool VLAN (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'pool-vlan')
        self.print_aci_policy_table_bar(controller, 'pool-vlan')

        order = [
            'Name',
            'Mode',
            'Block',
            'Domain',
            'Node',
            'Intf',
            'VM',
            'VMM PG'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./pool/%s.md)' % (
                    item['name'],
                    item['hash']
                )
            )
            line = self.add_column(line, item['allocMode'])
            if len(item['fvnsEncapBlk']) == 0:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, item['fvnsEncapBlk'][0]['blockInfo'])

            if len(item['fvnsRtVlanNs']) == 0:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, item['fvnsRtVlanNs'][0]['domainName'])

            line = self.add_column(line, item['nodeCount'])
            line = self.add_column(line, item['interfaceCount'])
            line = self.add_column(line, item['vmCount'])
            line = self.add_column(line, item['pgCount'])
            self.my_output.print_stream(line, 'output')

            if len(item['fvnsEncapBlk']) > 1 or len(item['fvnsRtVlanNs']) > 1:
                for i in range(max(len(item['fvnsEncapBlk']), len(item['fvnsRtVlanNs']))):
                    if i == 0:
                        continue

                    line = ''
                    line = self.add_column(line, '&nbsp;')
                    line = self.add_column(line, '&nbsp;')
                    try:
                        line = self.add_column(line, item['fvnsEncapBlk'][i]['blockInfo'])
                    except BaseException:
                        line = self.add_column(line, '&nbsp;')
                    try:
                        line = self.add_column(line, item['fvnsRtVlanNs'][i]['domainName'])
                    except BaseException:
                        line = self.add_column(line, '&nbsp;')

                    line = self.add_column(line, '&nbsp;')
                    self.my_output.print_stream(line, 'output')

            self.aci_pool_vlan_count[controller] = self.aci_pool_vlan_count[controller] + 1

        self.save_output('%s-pool-vlan' % (controller), subdir='apic')

        for item in info:
            self.print_aci_pool_vlan_details(item)
