import copy

from lib import filter_helper
from lib import ip_helper


class BridgeDomainInfo():
    def __init__(self):
        self.bridge_domains = None

    def get_bridge_domain_count(self, tenant_name=None):
        bridge_domain_filter = None
        if tenant_name is not None:
            bridge_domain_filter = ['tenant:%s' % (tenant_name)]

        bridge_domains = self.get_bridge_domains(
            bridge_domain_filter=bridge_domain_filter
        )
        return len(bridge_domains)

    def get_bridge_domain_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'arpFlood',
            'bcastP',
            'descr',
            'dn',
            'epClear',
            'epMoveDetectMode',
            'hostBasedRouting',
            'intersiteBumTrafficAllow',
            'intersiteL2Stretch',
            'ipLearning',
            'ipv6McastAllow',
            'limitIpLearnToSubnets',
            'llAddr',
            'mac',
            'mcastARPDrop',
            'mcastAllow',
            'mtu',
            'multiDstPktAct',
            'name',
            'pcTag',
            'seg',
            'type',
            'unicastRoute',
            'unkMacUcastAct',
            'unkMcastAct',
            'v6unkMcastAct',
            'vmac',
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['vmac'] == 'not-applicable':
            info['vmac'] = ''

        info['unkMacUcastActT'] = info['unkMacUcastAct']
        if info['unkMacUcastAct'] == 'flood':
            info['unkMacUcastActT'] = 'Flood'
        if info['unkMacUcastAct'] == 'proxy':
            info['unkMacUcastActT'] = 'Hardware Proxy'

        info['multiDstPktActT'] = info['multiDstPktAct']
        if info['multiDstPktAct'] == 'bd-flood':
            info['multiDstPktActT'] = 'Flood in BD'
        if info['multiDstPktAct'] == 'drop':
            info['multiDstPktActT'] = 'Drop'
        if info['multiDstPktAct'] == 'encap-flood':
            info['multiDstPktActT'] = 'Flood in Encap'

        if info['arpFlood'] == 'yes':
            info['arpFloodTick'] = '\u2713'
        else:
            info['arpFloodTick'] = '\u2717'

        if info['epClear'] == 'yes':
            info['epClearTick'] = '\u2713'
        else:
            info['epClearTick'] = '\u2717'

        if info['intersiteL2Stretch'] == 'yes':
            info['intersiteL2StretchTick'] = '\u2713'
        else:
            info['intersiteL2StretchTick'] = '\u2717'

        if info['unicastRoute'] == 'yes':
            info['unicastRouteTick'] = '\u2713'
        else:
            info['unicastRouteTick'] = '\u2717'

        if info['ipLearning'] == 'yes':
            info['ipLearningTick'] = '\u2713'
        else:
            info['ipLearningTick'] = '\u2717'

        if info['limitIpLearnToSubnets'] == 'yes':
            info['limitIpLearnToSubnetsTick'] = '\u2713'
        else:
            info['limitIpLearnToSubnetsTick'] = '\u2717'

        if info['hostBasedRouting'] == 'yes':
            info['hostBasedRoutingTick'] = '\u2713'
        else:
            info['hostBasedRoutingTick'] = '\u2717'

        info['vmacT'] = info['vmac']
        if info['vmac'] is None or len(info['vmac']) == 0:
            info['vmacT'] = '--'

        info['epMoveDetectModeT'] = info['epMoveDetectMode']
        if info['epMoveDetectMode'] is None or len(info['epMoveDetectMode']) == 0:
            info['epMoveDetectModeT'] = '--'

        if info['mcastAllow'] == 'yes':
            info['mcastAllowTick'] = '\u2713'
            info['__Output']['mcastAllowTick'] = 'Green'
        else:
            info['mcastAllowTick'] = '\u2717'
            info['__Output']['mcastAllowTick'] = 'Red'

        info['unkMcastActT'] = info['unkMcastAct']
        if info['unkMcastAct'] == 'flood':
            info['unkMcastActT'] = 'Flood'
        if info['unkMcastAct'] == 'opt-flood':
            info['unkMcastActT'] = 'Optimized Flood'

        if info['ipv6McastAllow'] == 'yes':
            info['ipv6McastAllowTick'] = '\u2713'
            info['__Output']['ipv6McastAllowTick'] = 'Green'
        else:
            info['ipv6McastAllowTick'] = '\u2717'
            info['__Output']['ipv6McastAllowTick'] = 'Red'

        info['v6unkMcastActT'] = info['v6unkMcastAct']
        if info['v6unkMcastAct'] == 'flood':
            info['v6unkMcastActT'] = 'Flood'
        if info['v6unkMcastAct'] == 'opt-flood':
            info['v6unkMcastActT'] = 'Optimized Flood'

        info['tenant'] = info['dn'].split('/')[1][3:]
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        subnets = []
        info['fvSubnet'] = []
        for subnet_managed_object in managed_object['fvSubnet']:
            subnet_info = self.get_bridge_domain_subnet_info(
                subnet_managed_object
            )
            info['fvSubnet'].append(
                subnet_info
            )
            subnets.append(
                subnet_info['ip']
            )
        info['fvSubnetCount'] = len(
            info['fvSubnet']
        )
        info['fvSubnets'] = ','.join(subnets)

        info['fvRsCtx'] = self.get_bridge_domain_vrf_info(
            managed_object['fvRsCtx']
        )

        info['fvRsBDToOut'] = []
        for l3out_managed_object in managed_object['fvRsBDToOut']:
            info['fvRsBDToOut'].append(
                self.get_bridge_domain_l3out_info(
                    l3out_managed_object
                )
            )
        info['l3OutCount'] = len(
            info['fvRsBDToOut']
        )

        info['fvRsIgmpsn'] = self.get_bridge_domain_igmp_info(
            managed_object['fvRsIgmpsn']
        )

        info['fvRsMldsn'] = self.get_bridge_domain_mld_info(
            managed_object['fvRsMldsn']
        )

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_bridge_domains_info(self):
        if self.bridge_domains is not None:
            return self.bridge_domains

        bridge_domains_mo = self.get_bridge_domains_mo()
        if bridge_domains_mo is None:
            return None

        self.bridge_domains = []
        for managed_object in bridge_domains_mo:
            self.bridge_domains.append(
                self.get_bridge_domain_info(
                    managed_object
                )
            )

        return self.bridge_domains

    def match_bridge_domain(self, bridge_domain_info, bridge_domain_filter):
        if bridge_domain_filter is None or len(bridge_domain_filter) == 0:
            return True

        for aepg_rule in bridge_domain_filter:
            (key, value) = aepg_rule.split(':')
            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, bridge_domain_info['name']):
                    return False

            if key == 'dn':
                key_found = True
                if not filter_helper.match_string(value, bridge_domain_info['dn']):
                    return False

            if key == 'tenant':
                key_found = True
                if not filter_helper.match_string(value, bridge_domain_info['tenant']):
                    return False

            if key == 'vrf':
                key_found = True
                if bridge_domain_info['fvRsCtx'] is None or 'name' not in bridge_domain_info['fvRsCtx']:
                    return False

                if not filter_helper.match_tenant_name(value, bridge_domain_info['fvRsCtx']['nameTenant']):
                    return False

            if key == 'epg':
                key_found = True
                if 'fvAEPg' not in bridge_domain_info or bridge_domain_info['fvAEPg'] is None:
                    return False

                found = False
                for epg_info in bridge_domain_info['fvAEPg']:
                    if filter_helper.match_tenant_name(value, epg_info['nameTenant']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'l3out':
                key_found = True
                if bridge_domain_info['fvRsBDToOut'] is None:
                    return False

                found = False
                for l3out_info in bridge_domain_info['fvRsBDToOut']:
                    if filter_helper.match_tenant_name(value, l3out_info['nameTenant']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'subnet':
                key_found = True
                if bridge_domain_info['fvSubnet'] is None:
                    return False

                found = False
                for bd_subnet in bridge_domain_info['fvSubnet']:
                    if ip_helper.is_subnet_in_subnet(bd_subnet['network'], value):
                        found = True
                        break

                if not found:
                    return False

            if key == 'ip':
                key_found = True
                if bridge_domain_info['fvSubnet'] is None:
                    return False

                found = False
                for bd_subnet in bridge_domain_info['fvSubnet']:
                    if ip_helper.is_ipv4_in_cidr(value, bd_subnet['network']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'fault':
                key_found = True
                if value == 'any':
                    if not bridge_domain_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_bd',
                        'Unsupported fault filtering value: %s' % (value)
                    )

            if not key_found:
                self.log.error(
                    'match_bd',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_bridge_domain(
            self,
            tenant_name,
            bridge_domain_name,
            endpoint_info=False,
            endpoint_vm_info=False,
            snoop_info=False,
            vrf_info=False,
            epg_info=False
            ):
        bridge_domain_filter = []
        bridge_domain_filter.append(
            'tenant:%s' % (tenant_name)
        )
        bridge_domain_filter.append(
            'name:%s' % (bridge_domain_name)
        )

        bridge_domains = self.get_bridge_domains(
            bridge_domain_filter=bridge_domain_filter,
            endpoint_info=endpoint_info,
            endpoint_vm_info=endpoint_vm_info,
            snoop_info=snoop_info,
            vrf_info=vrf_info,
            epg_info=epg_info
        )
        if len(bridge_domains) == 1:
            return bridge_domains[0]

        self.log.error(
            'get_bridge_domain',
            'Not found: %s/%s (%s)' % (
                tenant_name,
                bridge_domain_name,
                len(bridge_domains)
            )
        )

        return None

    def get_bridge_domains(
            self,
            bridge_domain_filter=None,
            endpoint_info=False,
            endpoint_vm_info=False,
            endpoint_fabric_info=False,
            snoop_info=False,
            vrf_info=False,
            epg_info=False,
            node_info=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_bridge_domains = self.get_bridge_domains_info()
        if all_bridge_domains is None:
            return None

        bridge_domains = []
        for bridge_domain_info in all_bridge_domains:
            if vrf_info:
                bridge_domain_info['fvCtx'] = copy.deepcopy(
                    self.get_vrf(
                        bridge_domain_info['fvRsCtx']['dn']
                    )
                )

            if epg_info:
                epg_filter = ['bd:%s/%s' % (bridge_domain_info['tenant'], bridge_domain_info['name'])]
                bridge_domain_info['fvAEPg'] = copy.deepcopy(
                    self.get_epgs(
                        epg_filter=epg_filter,
                        bd_info=True,
                        endpoint_info=True
                    )
                )
                bridge_domain_info['epgCount'] = len(
                    bridge_domain_info['fvAEPg']
                )

            if not self.match_bridge_domain(bridge_domain_info, bridge_domain_filter):
                continue

            if endpoint_info:
                endpoint_filter = ['bd:%s/%s' % (bridge_domain_info['tenant'], bridge_domain_info['name'])]
                bridge_domain_info['fvCEp'] = copy.deepcopy(
                    self.get_endpoints(
                        endpoint_filter=endpoint_filter,
                        vm_info=endpoint_vm_info,
                        fabric_info=endpoint_fabric_info
                    )
                )

                bridge_domain_info['endpointCount'] = 0
                if bridge_domain_info['fvCEp'] is not None:
                    bridge_domain_info['endpointCount'] = len(
                        bridge_domain_info['fvCEp']
                    )

                bridge_domain_info['fvSubnet'] = copy.deepcopy(
                    self.get_subnet_usage(
                        bridge_domain_info['fvSubnet'],
                        bridge_domain_info['fvCEp']
                    )
                )

            if snoop_info:
                bridge_domain_info['fvRsIgmpsn']['policy'] = copy.deepcopy(
                    self.get_policy_snoop_igmp(
                        bridge_domain_info['fvRsIgmpsn']['tenant'],
                        bridge_domain_info['fvRsIgmpsn']['actualPolicyName']
                    )
                )

                bridge_domain_info['fvRsMldsn']['policy'] = copy.deepcopy(
                    self.get_policy_snoop_mld(
                        bridge_domain_info['fvRsMldsn']['tenant'],
                        bridge_domain_info['fvRsMldsn']['actualPolicyName']
                    )
                )

            if node_info:
                ap_node_info = self.get_bridge_domain_node(
                    bridge_domain_info['tenant'],
                    bridge_domain_info['name']
                )
                bridge_domain_info['node'] = None
                bridge_domain_info['interface'] = None
                if ap_node_info is not None:
                    bridge_domain_info['node'] = ap_node_info['node']
                    bridge_domain_info['interface'] = ap_node_info['interface']

            if fault_info:
                bridge_domain_info['faultInst'] = self.get_bridge_domain_id_fault(
                    bridge_domain_info['tenant'],
                    bridge_domain_info['name'],
                    'faultInst'
                )

            if hfault_info:
                bridge_domain_info['faultRecord'] = self.get_bridge_domain_id_fault(
                    bridge_domain_info['tenant'],
                    bridge_domain_info['name'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                bridge_domain_info['eventLog'] = self.get_bridge_domain_id_event(
                    bridge_domain_info['tenant'],
                    bridge_domain_info['name'],
                    event_filter=event_filter
                )

            if audit_info:
                bridge_domain_info['auditLog'] = self.get_bridge_domain_id_audit(
                    bridge_domain_info['tenant'],
                    bridge_domain_info['name'],
                    audit_filter=audit_filter
                )

            bridge_domains.append(bridge_domain_info)

        bridge_domains = sorted(
            bridge_domains,
            key=lambda i: i['nameTenant'].lower()
        )

        self.log.apic_mo(
            'fvBD.info',
            bridge_domains
        )

        return bridge_domains
