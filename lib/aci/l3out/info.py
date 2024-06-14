from lib import filter_helper


class L3OutInfo():
    def __init__(self):
        self.l3out = None

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

    def get_l3out_name_from_dn(self, l3out_dn):
        # [0]: uni/tn-{name}/l3out-{name}
        tenant = l3out_dn.split('/')[1][3:]
        if '/l3out-' in l3out_dn:
            name = l3out_dn.split('/')[2][6:]
        if '/out-' in l3out_dn:
            name = l3out_dn.split('/')[2][4:]
        l3out_name = '%s/%s' % (
            tenant,
            name
        )
        return l3out_name

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

        profile_filter = []
        profile_filter.append('tenant:%s' % info['tenant'])
        profile_filter.append('l3out:%s' % info['name'])
        info['logicalNodeProfile'] = self.get_l3out_logical_node_profiles(
            profile_filter=profile_filter
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
        info['configured_node'] = []
        for logical_node_profile in info['logicalNodeProfile']:
            for node_info in logical_node_profile['configured_node']:
                if node_info['nodeDn'] not in node_dns:
                    node_dns.append(
                        node_info['nodeDn']
                    )
                    info['configured_node'].append(
                        node_info
                    )

        info['configured_node'] = sorted(
            info['configured_node'],
            key=lambda i: i['nodeT']
        )

        info['bgp_peer_connectivity_profile'] = []
        for logical_node_profile in info['logicalNodeProfile']:
            for bgp_info in logical_node_profile['bgp_peer_connectivity_profile']:
                info['bgp_peer_connectivity_profile'].append(
                    bgp_info
                )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_l3outs_info(self):
        if self.l3out is not None:
            return self.l3out

        managed_objects = self.get_l3out_mo()
        if managed_objects is None:
            return None

        self.l3out = []
        for managed_object in managed_objects:
            self.l3out.append(
                self.get_l3out_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'l3extOut.info',
            self.l3out
        )

        return self.l3out

    def match_l3out(self, l3out_info, l3out_filter):
        if l3out_filter is None or len(l3out_filter) == 0:
            return True

        for ap_rule in l3out_filter:
            (key, value) = ap_rule.split(':')
            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, l3out_info['name']):
                    return False

            if key == 'names':
                key_found = True
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
                key_found = True
                if not filter_helper.match_string(value, l3out_info['dn']):
                    return False

            if key == 'tenant':
                key_found = True
                if not filter_helper.match_string(value, l3out_info['tenant']):
                    return False

            if key == 'vrf':
                key_found = True
                if not filter_helper.match_string(value, l3out_info['l3extRsEctx']['nameTenant']):
                    return False

            if key == 'domain':
                key_found = True
                if l3out_info['l3extRsL3DomAtt'] is None:
                    return False

                if not filter_helper.match_string(value, l3out_info['l3extRsL3DomAtt']['name']):
                    return False

            if key == 'mpls':
                key_found = True
                if value == 'enabled':
                    if not l3out_info['mplsEnabled']:
                        return False

                if value == 'disabled':
                    if l3out_info['mplsEnabled']:
                        return False

            if key == 'bgp':
                key_found = True
                if value == 'enabled':
                    if not l3out_info['bgpExtP']['enabled']:
                        return False

                if value == 'disabled':
                    if l3out_info['bgpExtP']['enabled']:
                        return False

            if key == 'eigrp':
                key_found = True
                if value == 'enabled':
                    if not l3out_info['eigrpExtP']['enabled']:
                        return False

                if value == 'disabled':
                    if l3out_info['eigrpExtP']['enabled']:
                        return False

            if key == 'ospf':
                key_found = True
                if value == 'enabled':
                    if not l3out_info['ospfExtP']['enabled']:
                        return False

                if value == 'disabled':
                    if l3out_info['ospfExtP']['enabled']:
                        return False

            if key == 'pim':
                key_found = True
                if value == 'enabled':
                    if not l3out_info['pimExtP']['enabled']:
                        return False

                if value == 'disabled':
                    if l3out_info['pimExtP']['enabled']:
                        return False

            if key == 'node':
                key_found = True
                found = False
                for node in l3out_info['nodes']:
                    if filter_helper.match_string(value, node['nodeId']):
                        found = True

                if not found:
                    return False

            if key == 'fault':
                key_found = True
                if value == 'any':
                    if not l3out_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_l3out',
                        'Unsupported fault filtering value: %s' % (value)
                    )

            if not key_found:
                self.log.error(
                    'match_l3out',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_l3outs(
            self,
            l3out_filter=None,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_outs = self.get_l3outs_info()
        if all_outs is None:
            return None

        l3outs = []

        for l3out_info in all_outs:
            if not self.match_l3out(l3out_info, l3out_filter):
                continue

            if fault_info:
                l3out_info['faultInst'] = self.get_l3out_id_fault(
                    l3out_info['tenant'],
                    l3out_info['name'],
                    'faultInst'
                )

            if hfault_info:
                l3out_info['faultRecord'] = self.get_l3out_id_fault(
                    l3out_info['tenant'],
                    l3out_info['name'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                l3out_info['eventLog'] = self.get_l3out_id_event(
                    l3out_info['tenant'],
                    l3out_info['name'],
                    event_filter=event_filter
                )

            if audit_info:
                l3out_info['auditLog'] = self.get_l3out_id_audit(
                    l3out_info['tenant'],
                    l3out_info['name'],
                    audit_filter=audit_filter
                )

            l3outs.append(l3out_info)

        l3outs = sorted(
            l3outs,
            key=lambda i: i['nameTenant'].lower()
        )

        return l3outs
