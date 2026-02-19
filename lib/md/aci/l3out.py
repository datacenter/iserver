class MdAciL3OutOutput():
    def __init__(self):
        pass

    def print_aci_l3out_extepg_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## External EPG', 'output')

        order = [
            'Name',
            'pcTag',
            'Qos Class',
            'Target DSCP'
        ]
        self.print_table_header(order)

        for epg in info:
            line = ''
            line = self.add_column(line, epg['name'])
            line = self.add_column(line, epg['pcTag'])
            line = self.add_column(line, epg['prio'])
            line = self.add_column(line, epg['targetDscp'])
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def print_aci_l3out_lnp_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        for item in info:
            if title:
                self.my_output.print_stream('## Logical Nodel Profile', 'output')

            self.my_output.print_stream('- Tenant: %s' % (item['tenant']), 'output')
            self.my_output.print_stream('- Name: %s' % (item['name']), 'output')
            self.my_output.print_stream('- Dn: %s' % (item['dn']), 'output')
            self.my_output.print_stream('- Description: %s' % (item['descr']), 'output')
            self.my_output.print_stream('- L3Out: %s' % (item['l3out']), 'output')

            if len(item['configured_node']) > 0:
                self.my_output.print_stream('### Configured Node', 'output')
                order = [
                    'Node',
                    'Router ID',
                    'Loopback'
                ]
                self.print_table_header(order)

                for node in item['configured_node']:
                    line = ''
                    line = self.add_column(line, node['nodeDn'])
                    line = self.add_column(line, node['rtrId'])
                    line = self.add_column(line, node['rtrIdLoopBack'])
                    self.my_output.print_stream(line, 'output')

            if len(item['bgp_peer_connectivity_profile']) > 0:
                self.my_output.print_stream('### BGP Peer Connecvitity', 'output')
                order = [
                    'Peer',
                    'Enabled',
                    'BFD',
                    'Local ASN',
                    'Remote ASN',
                    'Path'
                ]
                self.print_table_header(order)

                for bgp in item['bgp_peer_connectivity_profile']:
                    line = ''
                    line = self.add_column(line, bgp['addr'])
                    line = self.add_column_tick_bool(line, bgp['enabled'])
                    line = self.add_column_tick_bool(line, bgp['isBfd'])
                    line = self.add_column_tick_bool(line, bgp['local_asn'])
                    line = self.add_column_tick_bool(line, bgp['asn'])
                    line = self.add_column_tick_bool(line, bgp['path'])
                    self.my_output.print_stream(line, 'output')

    def print_aci_l3out_details(self, info):
        self.print_page_header('ACI L3Out')
        self.my_output.print_stream('- Controller: [%s](../%s-l3out.md)' % (info['apic'], info['apic']), 'output')
        self.my_output.print_stream('- Tenant: %s' % (info['tenant']), 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Dn: %s' % (info['dn']), 'output')
        self.my_output.print_stream('- Description: %s' % (info['descr']), 'output')

        self.my_output.print_stream('## Properties', 'output')
        if info['l3extRsL3DomAtt'] is None:
            self.my_output.print_stream('- Domain L3: ---', 'output')
        else:
            self.my_output.print_stream('- Domain L3: %s' % (info['l3extRsL3DomAtt']['name']), 'output')

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

    def print_aci_tenant_l3out(self, info, tenant, controller):
        self.print_page_header('L3Out (%s:%s)' % (controller, tenant))
        self.print_aci_tenant_bar(controller, tenant, 'l3out')
        self.print_aci_tenant_table_bar(controller, tenant, 'l3out')

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
            if item['tenant'] != tenant or item['mplsEnabled']:
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

        self.save_output('%s-%s-l3out' % (controller, tenant), subdir='apic')

    def print_aci_l3out(self, info, controller):
        self.print_page_header('L3Out (%s)' % (controller))
        self.print_aci_controller_bar(controller, 'l3out')
        self.print_aci_global_table_bar(controller, 'l3out')

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
            if item['mplsEnabled']:
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

            self.aci_l3out_count[controller] = self.aci_l3out_count[controller] + 1

        self.save_output('%s-l3out' % (controller), subdir='apic')

        for item in info:
            if not item['mplsEnabled']:
                self.print_aci_l3out_details(item)
