class MdAciEpgOutput():
    def __init__(self):
        pass

    def print_aci_epg_addon(self, info, title=True, vlan=False):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## EPG', 'output')

        is_health = True
        is_ep = True
        is_domain = True
        is_contract = True
        is_port = True
        is_node = True
        is_member = True
        is_vlan = vlan
        for item in info:
            if 'health' not in item:
                is_health = False
            if 'endpointCount' not in item:
                is_ep = False
            if 'domainCount' not in item:
                is_domain = False
            if 'contractCount' not in item:
                is_contract = False
            if 'staticPortCount' not in item:
                is_port = False
            if 'node' not in item:
                is_node = False
            if 'member' not in item:
                is_member = False
            if 'vlan' not in item:
                is_vlan = False

        order = [
            'EPG'
        ]

        if is_health:
            order.append(
                'Health'
            )

        if is_ep:
            order.append(
                'EP'
            )

        if is_node:
            order.append(
                'Node'
            )

        if is_domain:
            order.append(
                'Domain'
            )

        if is_contract:
            order.append(
                'Contract'
            )

        if is_port:
            order.append(
                'StPort'
            )


        if is_member:
            order = order + [
                'StMem',
                'DynMem'
            ]

        if is_vlan:
            order = order + [
                'Encap',
                'Fabric'
            ]

        self.print_table_header(order)

        for item in info:
            line = ''
            if 'hash' in item:
                line = self.add_column(
                    line,
                    '[%s](../epg/%s.md)' % (
                        item['nameApTenant'],
                        item['hash']
                    )
                )
            else:
                line = self.add_column(line, item['nameApTenant'])

            if is_health:
                line = self.add_column(line, item['health'])
            if is_ep:
                line = self.add_column(line, item['endpointCount'])
            if is_node:
                line = self.add_column(line, len(item['node']))
            if is_domain:
                line = self.add_column(line, item['domainCount'])
            if is_contract:
                line = self.add_column(line, item['contractCount'])
            if is_port:
                line = self.add_column(line, item['staticPortCount'])
            if is_member:
                line = self.add_column(line, item['ifconnSummary']['fv']['stpathatt'])
                line = self.add_column(line, item['ifconnSummary']['fv']['dyatt'])
            if is_vlan:
                if item['vlan'] is None:
                    line = self.add_column(line, '---')
                    line = self.add_column(line, '---')
                else:
                    line = self.add_column(line, item['vlan']['encap'])
                    line = self.add_column(line, item['vlan']['fabEncap'])

            self.my_output.print_stream(line, 'output')

    def print_aci_epg_details(self, info):
        self.print_page_header('ACI Endpoint Group')
        self.my_output.print_stream('- Controller: %s' % (info['apic']), 'output')
        self.my_output.print_stream('- Tenant: %s' % (info['tenant']), 'output')
        self.my_output.print_stream('- Application Profile: %s' % (info['application_profile']), 'output')
        self.my_output.print_stream('- EPG: %s' % (info['name']), 'output')

        self.my_output.print_stream('## Properties', 'output')
        if info['adminUp']:
            self.my_output.print_stream('- Admin state :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Admin state :x:', 'output')

        self.my_output.print_stream(
            '- Bridge Domain: [%s](../bd/%s.md)' % (
                info['bdTenantName'],
                info['bd_hash']
            ),
            'output'
        )

        self.my_output.print_stream('- pcTag: %s' % (info['pcTag']), 'output')
        self.my_output.print_stream('- Intra EPG Isolation: %s' % (info['pcEnfPref']), 'output')
        self.my_output.print_stream('- Flood in Encapsulation: %s' % (info['floodOnEncap']), 'output')

        self.my_output.print_stream('## References', 'output')
        names = []
        for item in info['fabricNode']:
            names.append(
                item['name']
            )
        names = sorted(names)
        if len(names) == 0:
            self.my_output.print_stream('- Node (deployed leaves): ---', 'output')
        else:
            self.my_output.print_stream('- Node (deployed leaves)', 'output')
            for name in names:
                self.my_output.print_stream('\t- %s' % (name), 'output')

        self.my_output.print_stream('- Domain: %s' % (info['domainCount']), 'output')
        self.my_output.print_stream('- Endpoint Count: %s' % (info['endpointCount']), 'output')
        self.my_output.print_stream('- Contract Count: %s' % (info['contractCount']), 'output')
        self.my_output.print_stream('- Static Port: %s' % (info['staticPortCount']), 'output')
        self.my_output.print_stream('- Static Member: %s' % (info['ifconnSummary']['fv']['stpathatt']), 'output')
        self.my_output.print_stream('- Dynamic Member: %s' % (info['ifconnSummary']['fv']['dyatt']), 'output')

        if info['endpointCount'] > 0:
            self.print_aci_ep_addon(info['fvCEp'], vmm_enabled=True)

        if info['domainCount'] > 0:
            self.print_aci_domain_addon(info['domain'])

        if info['contractCount'] > 0:
            self.print_aci_contract_addon(
                consumed=info['contractConsumed'],
                provided=info['contractProvided'],
                taboo=info['contractTaboo']
            )

        if info['staticPortCount'] > 0:
            self.my_output.print_stream('## Static Port', 'output')

            order = [
                'Path Type',
                'Path',
                'Port Encap',
                'Deployment',
                'Mode'
            ]
            self.print_table_header(order)

            for port in info['staticPort']:
                line = ''
                line = self.add_column(line, port['pathType'])
                line = self.add_column(
                    line,
                    'Node-%s/%s' % (
                        port['pathNode'],
                        port['pathEp']
                    )
                )
                line = self.add_column(line, port['encap'])
                line = self.add_column(line, port['instrImedcy'])
                line = self.add_column(line, port['mode'])
                self.my_output.print_stream(line, 'output')

            self.my_output.print_stream('', 'output')

        if info['ifconnSummary']['fv']['stpathatt'] > 0:
            self.my_output.print_stream('## Static EPG Member', 'output')

            order = [
                'Node',
                'Path Type',
                'Path Name',
                'Encap'
            ]
            self.print_table_header(order)

            for member in info['member']:
                if member['memberType'] != 'static':
                    continue

                line = ''
                line = self.add_column(line, member['nodeName'])
                line = self.add_column(line, member['pathType'])
                line = self.add_column(line, member['pathName'])
                line = self.add_column(line, member['encap'])
                self.my_output.print_stream(line, 'output')

            self.my_output.print_stream('', 'output')

        if info['ifconnSummary']['fv']['dyatt'] > 0:
            self.my_output.print_stream('## Dynamic EPG Member', 'output')

            order = [
                'Node',
                'Path Type',
                'Path Name',
                'Encap'
            ]
            self.print_table_header(order)

            for member in info['member']:
                if member['memberType'] != 'dynamic':
                    continue

                line = ''
                line = self.add_column(line, member['nodeName'])
                line = self.add_column(line, member['pathType'])
                line = self.add_column(line, member['pathName'])
                line = self.add_column(line, member['encap'])
                self.my_output.print_stream(line, 'output')

            self.my_output.print_stream('', 'output')

        self.print_aci_phy_state_addon(info['interfacePhy'])

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(info, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(info['hash'], subdir='apic/epg')

    def print_aci_tenant_epg(self, info, tenant, controller):
        self.print_page_header('Endpoint Group (%s:%s)' % (controller, tenant))
        self.print_aci_tenant_bar(controller, tenant, 'epg')
        self.print_aci_tenant_table_bar(controller, tenant, 'epg')

        order = [
            'EPG',
            'BD',
            'EP',
            'Node',
            'Dom',
            'Con',
            'StPort',
            'StMem',
            'DynMem'
        ]
        self.print_table_header(order)

        for item in info:
            if item['tenant'] != tenant:
                continue

            line = ''
            line = self.add_column(
                line,
                '[%s](./epg/%s.md)' % (
                    item['nameApTenant'],
                    item['hash']
                )
            )
            line = self.add_column(
                line,
                '[%s](./epg/%s.md)' % (
                    item['bdTenantName'],
                    item['bd_hash']
                )
            )
            line = self.add_column(line, item['endpointCount'])
            line = self.add_column(line, item['nodeCount'])
            line = self.add_column(line, item['domainCount'])
            line = self.add_column(line, item['contractCount'])
            line = self.add_column(line, item['staticPortCount'])
            line = self.add_column(line, item['ifconnSummary']['fv']['stpathatt'])
            line = self.add_column(line, item['ifconnSummary']['fv']['dyatt'])
            self.my_output.print_stream(line, 'output')

            self.aci_epg_count[controller] = self.aci_epg_count[controller] + 1

        self.my_output.print_stream('## EPG to BD', 'output')
        order = [
            'EPG',
            'BD'
        ]
        self.print_table_header(order)

        for item in info:
            if item['tenant'] != tenant:
                continue

            line = ''
            line = self.add_column(
                line,
                '[%s](./epg/%s.md)' % (
                    item['nameApTenant'],
                    item['hash']
                )
            )
            line = self.add_column(
                line,
                '[%s](./epg/%s.md)' % (
                    item['bdTenantName'],
                    item['bd_hash']
                )
            )
            self.my_output.print_stream(line, 'output')

        self.save_output('%s-%s-epg' % (controller, tenant), subdir='apic')

    def print_aci_epg(self, info, controller):
        self.print_page_header('Endpoint Group (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'epg')
        self.print_aci_global_table_bar(controller, 'epg')

        order = [
            'EPG',
            'EP',
            'Node',
            'Dom',
            'Con',
            'StPort',
            'StMem',
            'DynMem'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./epg/%s.md)' % (
                    item['nameApTenant'],
                    item['hash']
                )
            )
            line = self.add_column(line, item['endpointCount'])
            line = self.add_column(line, item['nodeCount'])
            line = self.add_column(line, item['domainCount'])
            line = self.add_column(line, item['contractCount'])
            line = self.add_column(line, item['staticPortCount'])
            line = self.add_column(line, item['ifconnSummary']['fv']['stpathatt'])
            line = self.add_column(line, item['ifconnSummary']['fv']['dyatt'])
            self.my_output.print_stream(line, 'output')

            self.aci_epg_count[controller] = self.aci_epg_count[controller] + 1

        self.my_output.print_stream('## EPG to BD', 'output')
        order = [
            'EPG',
            'BD'
        ]
        self.print_table_header(order)

        for item in info:
            line = ''
            line = self.add_column(
                line,
                '[%s](./epg/%s.md)' % (
                    item['nameApTenant'],
                    item['hash']
                )
            )
            line = self.add_column(
                line,
                '[%s](./epg/%s.md)' % (
                    item['bdTenantName'],
                    item['bd_hash']
                )
            )
            self.my_output.print_stream(line, 'output')

        self.save_output('%s-epg' % (controller), subdir='apic')

        for item in info:
            self.print_aci_epg_details(item)
