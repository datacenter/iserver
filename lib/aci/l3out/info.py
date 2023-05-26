from lib import filter_helper


class L3OutInfo():
    def __init__(self):
        pass

    def get_l3out_count(self, tenant_name=None, mpls=None):
        l3out_filter = []

        if tenant_name is not None:
            l3out_filter.append(
                'tenant:%s' % (tenant_name)
            )

        if mpls is not None:
            if mpls:
                l3out_filter.append(
                    'mpls:enabled'
                )
            else:
                l3out_filter.append(
                    'mpls:disabled'
                )

        l3outs = self.get_l3outs(
            l3out_filter=l3out_filter
        )

        return len(l3outs)

    def get_l3out_info(self, managed_object):
        keys = [
            'descr',
            'dn',
            'enforceRtctrl',
            'mplsEnabled',
            'name',
            'targetDscp',
            'userdom'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['mplsEnabled'] == 'yes':
            info['mplsEnabled'] = True
            info['mplsEnabledTick'] = '\u2713'
            info['__Output']['mplsEnabledTick'] = 'Green'
        else:
            info['mplsEnabled'] = False
            info['mplsEnabledTick'] = '\u2717'
            info['__Output']['mplsEnabledTick'] = 'Red'

        # Dn format
        # [0]: uni/tn-{name}/l3out-{name}
        info['tenant'] = info['dn'].split('/')[1][3:]

        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        info['l3extRsL3DomAtt'] = None
        if managed_object['l3extRsL3DomAtt'] is not None:
            info['l3extRsL3DomAtt'] = self.get_l3out_domain_info(
                managed_object['l3extRsL3DomAtt']
            )

        info['bgpExtP'] = self.get_l3out_bgp_info(
            managed_object['bgpExtP']
        )

        info['ospfExtP'] = self.get_l3out_ospf_info(
            managed_object['ospfExtP']
        )

        info['eigrpExtP'] = self.get_l3out_eigrp_info(
            managed_object['eigrpExtP']
        )

        info['pimExtP'] = self.get_l3out_pim_info(
            managed_object['pimExtP']
        )

        info['l3extRsEctx'] = self.get_l3out_vrf_info(
            managed_object['l3extRsEctx']
        )

        info['nodeProfiles'] = self.get_l3out_node_profiles_info(
            info['tenant'],
            info['name']
        )

        info['l3extInstP'] = []
        for epg_mo in managed_object['l3extInstP']:
            epg_info = self.get_l3out_epg_info(
                epg_mo
            )
            if epg_mo is not None:
                info['l3extInstP'].append(
                    epg_info
                )

        node_dns = []
        info['nodes'] = []
        for node_profile in info['nodeProfiles']:
            for node_info in node_profile['nodes']:
                if node_info['nodeDn'] not in node_dns:
                    node_dns.append(
                        node_info['nodeDn']
                    )
                    info['nodes'].append(
                        node_info
                    )

        return info

    def match_l3out(self, l3out_info, l3out_filter):
        if l3out_filter is None or len(l3out_filter) == 0:
            return True

        for ap_rule in l3out_filter:
            (key, value) = ap_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, l3out_info['name']):
                    return False

            if key == 'names':
                found = False
                for name in value.split(','):
                    if '/' in name:
                        if filter_helper.match_string(name, l3out_info['nameTenant']):
                            found = True
                            break
                    else:
                        if not filter_helper.match_string(name, l3out_info['name']):
                            return False

                if not found:
                    return False

            if key == 'dn':
                if not filter_helper.match_string(value, l3out_info['dn']):
                    return False

            if key == 'tenant':
                if not filter_helper.match_string(value, l3out_info['tenant']):
                    return False

            if key == 'vrf':
                if not filter_helper.match_string(value, l3out_info['l3extRsEctx']['nameTenant']):
                    return False

            if key == 'domain':
                if l3out_info['l3extRsL3DomAtt'] is None:
                    return False

                if not filter_helper.match_string(value, l3out_info['l3extRsL3DomAtt']['name']):
                    return False

            if key == 'mpls':
                if value == 'enabled':
                    if not l3out_info['mplsEnabled']:
                        return False

                if value == 'disabled':
                    if l3out_info['mplsEnabled']:
                        return False

            if key == 'bgp':
                if value == 'enabled':
                    if not l3out_info['bgpExtP']['enabled']:
                        return False

                if value == 'disabled':
                    if l3out_info['bgpExtP']['enabled']:
                        return False

            if key == 'eigrp':
                if value == 'enabled':
                    if not l3out_info['eigrpExtP']['enabled']:
                        return False

                if value == 'disabled':
                    if l3out_info['eigrpExtP']['enabled']:
                        return False

            if key == 'ospf':
                if value == 'enabled':
                    if not l3out_info['ospfExtP']['enabled']:
                        return False

                if value == 'disabled':
                    if l3out_info['ospfExtP']['enabled']:
                        return False

            if key == 'pim':
                if value == 'enabled':
                    if not l3out_info['pimExtP']['enabled']:
                        return False

                if value == 'disabled':
                    if l3out_info['pimExtP']['enabled']:
                        return False

            if key == 'node':
                found = False
                for node in l3out_info['nodes']:
                    if filter_helper.match_string(value, node['nodeId']):
                        found = True

                if not found:
                    return False

        return True

    def get_l3outs(self, l3out_filter=None):
        l3outs = []

        if not self.initialize_l3out():
            self.log.error(
                'get_l3outs',
                'Initialization failed'
            )
            return l3outs

        for managed_object in self.mo_l3out:
            l3out_info = self.get_l3out_info(
                managed_object
            )

            if not self.match_l3out(l3out_info, l3out_filter):
                continue

            l3outs.append(l3out_info)

        l3outs = sorted(
            l3outs,
            key=lambda i: i['nameTenant'].lower()
        )

        self.log.apic_mo(
            'l3extOut.info',
            l3outs
        )

        return l3outs
