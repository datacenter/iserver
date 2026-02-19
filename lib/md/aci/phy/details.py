import json
from lib import filter_helper


class MdAciPhyDetailsOutput():
    def __init__(self):
        pass

    def print_aci_node_phy_details(self, info, servers, commands):
        self.print_page_header('Interface Phy')

        self.my_output.print_stream('- Controller: %s' % (info['apic']), 'output')
        self.my_output.print_stream('- Node: %s' % (info['pod_node_name']), 'output')
        self.my_output.print_stream('- Interface: %s' % (info['id']), 'output')
        self.my_output.print_stream('- Dn: %s' % (info['dn']), 'output')
        if info['descr'] is not None and len(info['descr']) > 0:
            self.my_output.print_stream('- Description: %s' % (info['descr']), 'output')

        self.my_output.print_stream('## State', 'output')

        if info['adminSt'] == 'up':
            self.my_output.print_stream('- Admin :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Admin :x:', 'output')

        if info['switchingSt'] == 'enabled':
            self.my_output.print_stream('- Switching :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Switching :x:', 'output')

        if info['stats'] is None:
            self.my_output.print_stream('- Operational :x:', 'output')
        else:
            if info['stats']['operSt'] == 'up':
                self.my_output.print_stream('- Operational :white_check_mark:', 'output')
            else:
                self.my_output.print_stream('- Operational :x:', 'output')
            self.my_output.print_stream(
                '- Speed: %s (%s)' % (
                    info['stats']['operSpeed'],
                    info['stats']['operDuplex']
                ),
                'output'
            )
            self.my_output.print_stream('- MAC: %s' % (info['stats']['backplaneMac']), 'output')
            self.my_output.print_stream('- Usage: %s' % (info['usage']), 'output')
            self.my_output.print_stream('- Mode: %s' % (info['stats']['operMode']), 'output')
            if len(info['stats']['operVlans']) > 0:
                self.my_output.print_stream('- Operational VLANs: %s' % (info['stats']['operVlans']), 'output')
            if len(info['stats']['allowedVlans']) > 0:
                self.my_output.print_stream('- Allowed VLANs: %s' % (info['stats']['allowedVlans']), 'output')
            if len(info['stats']['bundleIndex']) > 0:
                self.my_output.print_stream('- Port Channel Bundle: %s' % (info['stats']['bundleIndex']), 'output')

        if info['fc_stats'] is not None:
            self.my_output.print_stream('## Optics', 'output')
            self.my_output.print_stream('- State: %s' % (info['fc_stats']['state']), 'output')
            if info['fc_stats']['state'] == 'inserted':
                self.my_output.print_stream('- Name: %s' % (info['fc_stats']['guiName']), 'output')
                self.my_output.print_stream(
                    '- Type: %s (Rev %s) (%s)' % (
                        info['fc_stats']['typeName'],
                        info['fc_stats']['guiRev'],
                        info['fc_stats']['actualType']
                    ),
                    'output'
                )

        if info['cdp'] is not None:
            for cdp in info['cdp']:
                self.print_aci_interface_cdp_addon(cdp)

        if info['lldp'] is not None:
            for lldp in info['lldp']:
                self.print_aci_interface_lldp_addon(lldp)

        if info['xd'] is not None and info['xd']['ServerMoid'] is not None:
            for server in servers:
                if server['Moid'] == info['xd']['ServerMoid']:
                    self.print_server(server, 'AddOn')
                    self.my_output.print_stream('', 'output')
                    self.print_server_vc(server, 'AddOn')

        if info['policy_selector'] is not None:
            self.my_output.print_stream('', 'output')
            self.my_output.print_stream(
                '![AccessPolicy](./access_policy.png)',
                'output'
            )

            self.my_output.print_stream('## Access Policy', 'output')

            order = [
                'Policy Type',
                'Policy Name'
            ]
            self.print_table_header(order)

            line = ''
            line = self.add_column(line, 'Leaf Switch Profile')
            line = self.add_column(line, info['policy_selector']['leafPolicy'])
            self.my_output.print_stream(line, 'output')

            line = ''
            line = self.add_column(line, 'Interface Profile')
            line = self.add_column(line, info['policy_selector']['profile'])
            self.my_output.print_stream(line, 'output')

            line = ''
            line = self.add_column(line, 'Interface Selector')
            line = self.add_column(line, info['policy_selector']['name'])
            self.my_output.print_stream(line, 'output')

            line = ''
            line = self.add_column(line, 'Policy Group Type')
            line = self.add_column(line, info['policy_selector']['policy_group_type_name'])
            self.my_output.print_stream(line, 'output')

            line = ''
            line = self.add_column(line, 'Policy Group Name')
            line = self.add_column(line, info['policy_selector']['policy_group_name'])
            self.my_output.print_stream(line, 'output')

            if info['policy_selector']['policy_group_info'] is None or info['policy_selector']['policy_group_info']['aaep'] is None:
                line = ''
                line = self.add_column(line, 'Attachable Access Entity Profile')
                line = self.add_column(line, '---')
                self.my_output.print_stream(line, 'output')
            else:
                line = ''
                line = self.add_column(line, 'Attachable Access Entity Profile')
                line = self.add_column(line, info['policy_selector']['policy_group_info']['aaep']['name'])
                self.my_output.print_stream(line, 'output')

                self.my_output.print_stream('', 'output')
                self.my_output.print_stream('## Domains Associated with AAEP', 'output')

                self.print_aci_aaep_domain_addon(
                    info['policy_selector']['policy_group_info']['aaep']['infraRsDomP'],
                    title=False
                )

            if info['policy_selector']['policy_group_info'] is not None:
                self.my_output.print_stream('## Interface Policy', 'output')

                order = [
                    'Policy Type',
                    'Policy Name'
                ]
                self.print_table_header(order)

                if 'infraRsCdpIfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'CDP')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsCdpIfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsLldpIfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'LLDP')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsLldpIfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsCdpIfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'Link Level')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsCdpIfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsFcIfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'Link Level Flow Control')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsFcIfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsLacpPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'Port Channel')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsLacpPol']['name'])
                    self.my_output.print_stream(line, 'output')

                # line = ''
                # line = self.add_column(line, 'CoPP Level')
                # line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsCdpIfPol']['name'])
                # self.my_output.print_stream(line, 'output')

                if 'infraRsQosEgressDppIfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'Egress Data Plane')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsQosEgressDppIfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsQosIngressDppIfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'Ingress Data Plane')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsQosIngressDppIfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsL2IfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'L2')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsL2IfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsLinkFlapPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'Link Flap')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsLinkFlapPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsFcIfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'Fibre Channel')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsFcIfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsMacsecIfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'MACsec')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsMacsecIfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsMcpIfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'MCP')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsMcpIfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsMonIfInfraPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'Monitoring')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsMonIfInfraPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsL2PortSecurityPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'Port Security')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsL2PortSecurityPol']['name'])
                    self.my_output.print_stream(line, 'output')

                # line = ''
                # line = self.add_column(line, 'SyncE')
                # line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsCdpIfPol']['name'])
                # self.my_output.print_stream(line, 'output')

                if 'infraRsQosPfcIfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'Priority Flow Control')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsQosPfcIfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsQosSdIfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'Slow Drain')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsQosSdIfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsStormctrlIfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'Storm Control')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsStormctrlIfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                if 'infraRsStpIfPol' in info['policy_selector']['policy_group_info']:
                    line = ''
                    line = self.add_column(line, 'STP')
                    line = self.add_column(line, info['policy_selector']['policy_group_info']['infraRsStpIfPol']['name'])
                    self.my_output.print_stream(line, 'output')

                self.my_output.print_stream('', 'output')

        if info['epg_stats'] is not None and len(info['epg_stats']) > 0:
            self.my_output.print_stream('## Deployed Application EPG', 'output')
            self.print_aci_epg_addon(info['epg_stats'], title=False, vlan=True)

        if info['encap_vlans'] is not None:
            self.my_output.print_stream('## Encapsulation VLAN', 'output')

            order = [
                'Encap',
                'PI',
                'Name',
                'App EPG',
                'Ext EPG'
            ]
            self.print_table_header(order)

            for item in info['encap_vlans']:
                line = ''
                line = self.add_column(
                    line,
                    item['id']
                )
                line = self.add_column(
                    line,
                    item['pi']
                )

                if item['is_epg']:
                    line = self.add_column(
                        line,
                        '[%s](../epg/%s.md)' % (
                            item['name'],
                            item['epg_hash']
                        )
                    )

                if item['is_l3out']:
                    line = self.add_column(
                        line,
                        '[%s](../l3out/%s.md)' % (
                            item['name'],
                            item['l3out_hash']
                        )
                    )

                if not item['is_epg'] and not item['is_l3out']:
                    line = self.add_column(
                        line,
                        item['name']
                    )

                line = self.add_column_tick_bool(
                    line,
                    item['is_epg']
                )

                line = self.add_column_tick_bool(
                    line,
                    item['is_l3out'],
                    last=True
                )

                self.my_output.print_stream(line, 'output')

        if info['pi_vlans'] is not None:
            pi_vlans = filter_helper.get_values_from_range(
                ','.join(info['pi_vlans'])
            )

            if 'vlan-extended' in commands:
                self.my_output.print_stream('## Platform Independent (PI) VLAN', 'output')

                order = [
                    'VLAN',
                    'Name',
                    'Encap'
                ]
                self.print_table_header(order)

                for item in commands['vlan-extended']['parsed']:
                    if item['id'] in pi_vlans:
                        line = ''
                        line = self.add_column(
                            line,
                            item['id']
                        )
                        line = self.add_column(
                            line,
                            item['name']
                        )
                        line = self.add_column(
                            line,
                            ', '.join(item['encap'])
                        )
                        self.my_output.print_stream(line, 'output')

        self.save_output(info['hash'], subdir='apic/phy')
