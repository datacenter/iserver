class MdAciBdOutput():
    def __init__(self):
        pass

    def print_aci_bd_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## Bridge Domain', 'output')

        is_vrf = True
        is_l3out = True
        is_epg = True
        is_ep = True
        for item in info:
            if 'fvCtx' not in item:
                is_vrf = False
            if 'l3OutCount' not in item:
                is_l3out = False
            if 'epgCount' not in item:
                is_epg = False
            if 'endpointCount' not in item:
                is_ep = False

        order = [
            'Name',
            'Subnet'
        ]

        if is_vrf:
            order.append(
            'VRF'
            )

        if is_l3out:
            order.append(
            'L3Out'
            )

        if is_epg:
            order.append(
            'EPG'
            )

        if is_ep:
            order.append(
            'EP'
            )
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(line, item['nameTenant'])
            line = self.add_column(line, item['fvSubnets'])
            if is_vrf:
                line = self.add_column(line, item['fvCtx']['name'])
            if is_l3out:
                line = self.add_column(line, item['l3OutCount'])
            if is_epg:
                line = self.add_column(line, item['epgCount'])
            if is_ep:
                line = self.add_column(line, item['endpointCount'])

            self.my_output.print_stream(line, 'output')

    def print_aci_bd_subnet_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## Subnet', 'output')

        order = [
            'Network',
            'Gateway',
            'Scope',
            'Learning',
            'Virtual',
            'Preferred',
            'Usage'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(line, item['network'])
            line = self.add_column(line, item['gateway'])
            line = self.add_column(line, item['scope'])
            line = self.add_column_tick_string(line, item['ipDPLearning'], 'enabled')
            line = self.add_column_tick_string(line, item['ipDPLearning'], 'yes')
            line = self.add_column_tick_string(line, item['preferred'], 'yes')
            line = self.add_column(line, item['usage'])
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def print_aci_bd_details(self, info):
        self.print_page_header('ACI Bridge Domain')
        self.my_output.print_stream('- Controller: %s' % (info['apic']), 'output')
        self.my_output.print_stream('- Tenant: %s' % (info['tenant']), 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Dn: %s' % (info['dn']), 'output')
        self.my_output.print_stream('- Description: %s' % (info['descr']), 'output')

        self.my_output.print_stream('## Properties', 'output')
        self.my_output.print_stream('- Type: %s' % (info['type']), 'output')
        self.my_output.print_stream('- MAC: %s' % (info['mac']), 'output')
        self.my_output.print_stream('- pcTag: %s' % (info['pcTag']), 'output')
        self.my_output.print_stream('- VXLAN Segment: %s' % (info['seg']), 'output')
        self.my_output.print_stream('- Unicast Routing: %s' % (info['unicastRoute']), 'output')
        self.my_output.print_stream('- IP Learning: %s' % (info['ipLearning']), 'output')
        self.my_output.print_stream('- Advertise Host Routes: %s' % (info['hostBasedRouting']), 'output')
        self.my_output.print_stream('- Limit Local IP Learning to BD/EPG Subnets: %s' % (info['limitIpLearnToSubnets']), 'output')
        self.my_output.print_stream('- ARP Flooding: %s' % (info['arpFlood']), 'output')
        self.my_output.print_stream(
            '- VRF: [%s](../vrf/%s.md)' % (
                info['fvCtx']['nameTenant'],
                info['fvCtx']['hash']
            ),
            'output'
        )
        names = []
        for item in info['fvRsBDToOut']:
            names.append(
                '[%s](../l3out/%s.md)' % (
                    item['nameTenant'],
                    item['hash']
                )
            )
        if len(names) == 0:
            self.my_output.print_stream('- L3Out: ---', 'output')
        else:
            self.my_output.print_stream('- L3Out: %s' % (','.join(names)), 'output')

        self.my_output.print_stream('## References\n', 'output')
        self.my_output.print_stream('- Subnet: %s' % (info['fvSubnetCount']), 'output')
        self.my_output.print_stream('- L3Out: %s' % (info['l3OutCount']), 'output')
        self.my_output.print_stream('- Endpoint: %s' % (info['endpointCount']), 'output')
        self.my_output.print_stream('- EPG: %s' % (info['epgCount']), 'output')
        self.my_output.print_stream('- Node: %s' % (len(info['node'])), 'output')
        self.my_output.print_stream('- Interface: %s' % (len(info['interface'])), 'output')

        self.print_aci_bd_subnet_addon(info['fvSubnet'])
        self.print_aci_epg_addon(info['fvAEPg'])
        self.print_aci_ep_addon(info['fvCEp'], vmm_enabled=True)
        self.print_aci_phy_state_addon(info['interfacePhy'])

        self.save_output(info['hash'], subdir='apic/bd')

    def print_aci_tenant_bd(self, info, tenant, controller):
        self.print_page_header('Bridge Domain (%s:%s)' % (controller, tenant))
        self.print_aci_tenant_bar(controller, tenant, 'bd')
        self.print_aci_tenant_table_bar(controller, tenant, 'bd')

        order = [
            'Name',
            'Subnet',
            'VRF',
            'L3Out',
            'EPG',
            'EP'
        ]
        self.print_table_header(order)

        for item in info:
            if item['tenant'] != tenant:
                continue

            line = ''
            line = self.add_column(
                line,
                '[%s](./bd/%s.md)' % (
                    item['name'],
                    item['hash']
                )
            )
            line = self.add_column(line, item['fvSubnets'])
            line = self.add_column(
                line,
                '[%s](./bd/%s.md)' % (
                    item['fvCtx']['name'],
                    item['fvCtx']['hash']
                )
            )
            line = self.add_column(line, item['l3OutCount'])
            line = self.add_column(line, item['epgCount'])
            line = self.add_column(line, item['endpointCount'])

            self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-bd' % (controller, tenant), subdir='apic')

    def print_aci_bd(self, info, controller):
        self.print_page_header('Bridge Domain (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'bd')
        self.print_aci_global_table_bar(controller, 'bd')

        order = [
            'Name',
            'Subnet',
            'VRF',
            'L3Out',
            'EPG',
            'EP'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./bd/%s.md)' % (
                    item['nameTenant'],
                    item['hash']
                )
            )
            line = self.add_column(line, item['fvSubnets'])
            line = self.add_column(
                line,
                '[%s](./bd/%s.md)' % (
                    item['fvCtx']['name'],
                    item['fvCtx']['hash']
                )
            )
            line = self.add_column(line, item['l3OutCount'])
            line = self.add_column(line, item['epgCount'])
            line = self.add_column(line, item['endpointCount'])

            self.my_output.print_stream(line, 'output')

            self.aci_bd_count[controller] = self.aci_bd_count[controller] + 1

        self.save_output('%s-bd' % (controller), subdir='apic')

        for item in info:
            self.print_aci_bd_details(item)
