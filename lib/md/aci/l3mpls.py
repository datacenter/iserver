class MdAciL3MplsOutput():
    def __init__(self):
        pass

    def print_aci_l3mpls_details(self, info):
        self.print_page_header('ACI SR-MPLS L3Out')
        self.my_output.print_stream('- Controller: [%s](../%s-l3out.md)' % (info['apic'], info['apic']), 'output')
        self.my_output.print_stream('- Tenant: %s' % (info['tenant']), 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Dn: %s' % (info['dn']), 'output')
        self.my_output.print_stream('- Description: %s' % (info['descr']), 'output')

        self.my_output.print_stream('## Properties', 'output')
        self.my_output.print_stream('- External L3Out: %s' % (info['l3extRsEctx']['nameTenant']), 'output')

        if info['bgpExtP']['enabled']:
            self.my_output.print_stream('- BGP :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- BGP :x:', 'output')

        if info['ospfExtP']['enabled']:
            self.my_output.print_stream('- OSPF :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- OSPF :x:', 'output')

        if info['eigrpExtP']['enabled']:
            self.my_output.print_stream('- EIGRP :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- EIGRP :x:', 'output')

        if info['pimExtP']['enabled']:
            self.my_output.print_stream('- PIM :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- PIM :x:', 'output')

        self.print_aci_l3out_extepg_addon(info['l3extInstP'])
        self.print_aci_l3out_lnp_addon(info['logicalNodeProfile'])

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(info['hash'], subdir='apic/l3out')

    def print_aci_tenant_l3mpls(self, info, tenant, controller):
        self.print_page_header('SR-MPLS L3Out (%s:%s)' % (controller, tenant))
        self.print_aci_tenant_bar(controller, tenant, 'l3mpls')
        self.print_aci_tenant_table_bar(controller, tenant, 'l3mpls')

        order = [
            'Name',
            'BGP',
            'OSPF',
            'EIGRP',
            'PIM',
            'Node',
            'LNP',
            'extEPG'

        ]
        self.print_table_header(order)

        for item in info:
            if item['tenant'] != tenant or not item['mplsEnabled']:
                continue

            line = ''
            line = self.add_column(
                line,
                '[%s](./l3out/%s.md)' % (
                    item['name'],
                    item['hash']
                )
            )
            line = self.add_column_tick_bool(line, item['bgpExtP']['enabled'])
            line = self.add_column_tick_bool(line, item['ospfExtP']['enabled'])
            line = self.add_column_tick_bool(line, item['eigrpExtP']['enabled'])
            line = self.add_column_tick_bool(line, item['pimExtP']['enabled'])
            line = self.add_column(line, item['nodeCount'])
            line = self.add_column(line, item['lnpCount'])
            line = self.add_column(line, item['extEpgCount'])
            self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-l3mpls' % (controller, tenant), subdir='apic')

    def print_aci_l3mpls(self, info, controller):
        self.print_page_header('SR-MPLS L3Out (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'l3mpls')
        self.print_aci_global_table_bar(controller, 'l3mpls')

        order = [
            'Name',
            'BGP',
            'OSPF',
            'EIGRP',
            'PIM',
            'Node',
            'LNP',
            'extEPG'

        ]
        self.print_table_header(order)

        for item in info:
            if not item['mplsEnabled']:
                continue

            line = ''
            line = self.add_column(
                line,
                '[%s](./l3out/%s.md)' % (
                    item['nameTenant'],
                    item['hash']
                )
            )
            line = self.add_column_tick_bool(line, item['bgpExtP']['enabled'])
            line = self.add_column_tick_bool(line, item['ospfExtP']['enabled'])
            line = self.add_column_tick_bool(line, item['eigrpExtP']['enabled'])
            line = self.add_column_tick_bool(line, item['pimExtP']['enabled'])
            line = self.add_column(line, item['nodeCount'])
            line = self.add_column(line, item['lnpCount'])
            line = self.add_column(line, item['extEpgCount'])
            self.my_output.print_stream(line, 'output')

            self.aci_l3mpls_count[controller] = self.aci_l3mpls_count[controller] + 1

        self.save_output('%s-l3mpls' % (controller), subdir='apic')

        for item in info:
            if item['mplsEnabled']:
                self.print_aci_l3mpls_details(item)
