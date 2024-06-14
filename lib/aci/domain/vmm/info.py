from lib import filter_helper


class DomainVmmInfo():
    def __init__(self):
        self.domain_vmm = None

    def get_domain_vmm_info(self, managed_object):
        keys = [
            'accessMode',
            'aveTimeOut',
            'configInfraPg',
            'ctrlKnob',
            'dn',
            'enableAVE',
            'enableTag',
            'enableVmFolder',
            'encapMode',
            'epInventoryType',
            'epRetTime',
            'hvAvailMonitor',
            'name'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # No clue why I get unknown value while APIC UI gets vlan value...
        if info['encapMode'] == 'unknown':
            info['encapMode'] = 'vlan'

        info['accessModeT'] = '--'
        if info['accessMode'] == 'read-write':
            info['accessModeT'] = 'RW'
        if info['accessMode'] == 'read-only':
            info['accessModeT'] = 'RO'

        info['vmmVSwitchPolicyContRn'] = None
        if 'vmmVSwitchPolicyCont' in managed_object:
            if managed_object['vmmVSwitchPolicyCont'] is not None:
                info['vmmVSwitchPolicyCont'] = managed_object['vmmVSwitchPolicyCont']['rn']

        info['vmmCtrlrP'] = []
        if 'vmmCtrlrP' in managed_object:
            if managed_object['vmmCtrlrP'] is not None:
                for item in managed_object['vmmCtrlrP']:
                    vc_info = {}
                    vc_info['name'] = item['name']
                    vc_info['rootContName'] = item['rootContName']
                    vc_info['hostOrIp'] = item['hostOrIp']
                    vc_info['usr'] = ''
                    if 'vmmUsrAccP' in managed_object:
                        if managed_object['vmmUsrAccP'] is not None:
                            for user_item in managed_object['vmmUsrAccP']:
                                cred_name = '%s_cred' % (item['name'])
                                if user_item['name'].lower() == cred_name.lower():
                                    vc_info['usr'] = user_item['usr']

                    info['vmmCtrlrP'].append(
                        vc_info
                    )

        info['numOfUplinks'] = None
        if 'vmmUplinkPCont' in managed_object:
            if managed_object['vmmUplinkPCont'] is not None:
                info['numOfUplinks'] = managed_object['vmmUplinkPCont']['numOfUplinks']

        info['aaep_names'] = []
        if 'infraRtDomP' in managed_object:
            if managed_object['infraRtDomP'] is not None:
                for item in managed_object['infraRtDomP']:
                    # "tCl": "infraAttEntityP",
                    # "tDn": "uni/infra/attentp-UCSB1-R3DC_AAEP"
                    if item['tCl'] == 'infraAttEntityP':
                        info['aaep_names'].append(
                            item['tDn'].split('/')[2][8:]
                        )

        info['vlan'] = None
        if 'infraRsVlanNs' in managed_object:
            if managed_object['infraRsVlanNs'] is not None:
                if managed_object['infraRsVlanNs']['tCl'] == 'fvnsVlanInstP':
                    info['vlan'] = managed_object['infraRsVlanNs']['tDn'].split('vlanns-[')[1].split(']')[0]

        info['aaaDomain'] = []
        for item in managed_object['aaaDomainRef']:
            info['aaaDomain'].append(
                item['name']
            )

        info['vmmEpPD'] = []
        for epg_mo in managed_object['vmmEpPD']:
            info['vmmEpPD'].append(
                self.get_domain_vmm_epg_info(
                    epg_mo
                )
            )

        info['epgCount'] = len(
            info['vmmEpPD']
        )

        info['reln'] = []
        if 'infraRtDomP' in managed_object:
            if managed_object['infraRtDomP'] is not None:
                for item in managed_object['infraRtDomP']:
                    # "tCl": "infraAttEntityP",
                    # "tDn": "uni/infra/attentp-UCSB1-R3DC_AAEP"
                    if item['tCl'] == 'infraAttEntityP':
                        reln_info = {}
                        reln_info['tCl'] = item['tCl']
                        reln_info['tDn'] = item['tDn']
                        reln_info['type'] = 'AAEP'
                        reln_info['name'] = item['tDn'].split('/')[2][8:]
                        info['reln'].append(
                            reln_info
                        )
                        continue

                    self.log.error(
                        'get_domain_phy_info',
                        'Unsupported infraRtDomP tCl: %s' % (item['tCl'])
                    )

        if 'vmmEpPD' in managed_object:
            if managed_object['vmmEpPD'] is not None:
                for item in managed_object['vmmEpPD']:
                    reln_info = {}
                    reln_info['tCl'] = 'fvAEPg'
                    reln_info['tDn'] = item['encapAllocKey']
                    reln_info['type'] = 'Application EPG'
                    reln_info['name'] = self.get_epg_name_from_dn(
                        reln_info['tDn']
                    )
                    info['reln'].append(
                        reln_info
                    )

        info['reln'] = sorted(
            info['reln'],
            key=lambda i: (
                i['tCl'],
                i['tDn']
            )
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_domains_vmm_info(self):
        if self.domain_vmm is not None:
            return self.domain_vmm

        domains_mo = self.get_domain_vmm_mo()
        if domains_mo is None:
            return None

        self.domain_vmm = []
        for managed_object in domains_mo:
            self.domain_vmm.append(
                self.get_domain_vmm_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'vmmDomP.info',
            self.domain_vmm
        )

        return self.domain_vmm

    def match_domain_vmm(self, domain_info, domain_filter):
        if domain_filter is None or len(domain_filter) == 0:
            return True

        for aepg_rule in domain_filter:
            (key, value) = aepg_rule.split(':')
            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, domain_info['name']):
                    return False

            if key == 'aaep':
                key_found = True
                found = False
                for aaep_name in domain_info['aaep_names']:
                    if filter_helper.match_string(value, aaep_name):
                        found = True

                if not found:
                    return False

            if key == 'pool':
                key_found = True
                if not filter_helper.match_string(value, domain_info['vlan']):
                    return False

            if key == 'vlan':
                key_found = True
                if 'vlan_block' in domain_info:
                    found = False
                    for vlan_block in domain_info['vlan_block']:
                        if filter_helper.match_integer(vlan_block, value):
                            found = True

                    if not found:
                        return False

            if key == 'fault':
                key_found = True
                if value == 'any':
                    if not domain_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_domain_vmm',
                        'Unsupported fault filtering value: %s' % (value)
                    )

            if not key_found:
                self.log.error(
                    'match_domain_vmm',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_domains_vmm(
            self,
            domain_filter=None,
            vlan_info=False,
            vlan_usage_info=False,
            node_info=False,
            intf_vlan_info=False,
            controller_info=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_domains = self.get_domains_vmm_info()

        domains = []

        self.get_domain_vmm_controller_mo()
        for domain_info in all_domains:
            if not self.match_domain_vmm(domain_info, domain_filter):
                continue

            if vlan_info:
                domain_info['vlan_info'] = None
                domain_info['vlan_block'] = []
                if domain_info['vlan'] is not None:
                    domain_info['vlan_info'] = self.get_pool_vlan(
                        domain_info['vlan'],
                        vlan_usage_info=vlan_usage_info,
                        domain_name=domain_info['name']
                    )
                    if domain_info['vlan_info'] is not None:
                        for vlan_block in domain_info['vlan_info']['fvnsEncapBlk']:
                            domain_info['vlan_block'].append(
                                '%s-%s' % (
                                    vlan_block['fromVlan'],
                                    vlan_block['toVlan']
                                )
                            )

                if not self.match_domain_vmm(domain_info, domain_filter):
                    continue

            if node_info:
                domain_node_info = self.get_domain_vmm_node(
                    domain_info['name']
                )
                domain_info['node'] = None
                domain_info['interface'] = None
                if domain_node_info is not None:
                    domain_info['node'] = domain_node_info['node']
                    domain_info['interface'] = domain_node_info['interface']

            if intf_vlan_info:
                if domain_info['interface'] is not None:
                    for interface in domain_info['interface']:
                        interface['vlan'] = []
                        interface['operSt'] = '--'
                        interface['operMode'] = '--'

                        if interface['intf_type'] == 'l1PhysIf':
                            interface_info = self.get_interface_phy(
                                interface['pod_id'],
                                interface['node_id'],
                                interface['intf_name'],
                                epg_stats_info=True
                            )
                            if interface_info is not None:
                                interface['operSt'] = interface_info['stats']['operSt']
                                interface['__Output']['operSt'] = interface_info['stats']['__Output']['operSt']
                                interface['operMode'] = interface_info['stats']['operMode']
                                for intf_epg_stats in interface_info['epg_stats']:
                                    if intf_epg_stats['vlan'] is not None:
                                        if intf_epg_stats['vlan']['evlan'] not in interface['vlan']:
                                            interface['vlan'].append(
                                                intf_epg_stats['vlan']['evlan']
                                            )

                                interface['vlan'] = sorted(
                                    interface['vlan']
                                )
                                interface['vlans'] = filter_helper.get_range_from_values(
                                    interface['vlan']
                                )

            if controller_info:
                domain_info['controller'] = self.get_domain_vmm_controllers(
                    domain_vmm_controller_filter=['domain:%s' % (domain_info['name'])]
                )

            if fault_info:
                domain_info['faultInst'] = self.get_domain_vmm_id_fault(
                    domain_info['name'],
                    'faultInst'
                )

            if hfault_info:
                domain_info['faultRecord'] = self.get_domain_vmm_id_fault(
                    domain_info['name'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                domain_info['eventLog'] = self.get_domain_vmm_id_event(
                    domain_info['name'],
                    event_filter=event_filter
                )

            if audit_info:
                domain_info['auditLog'] = self.get_domain_vmm_id_audit(
                    domain_info['name'],
                    audit_filter=audit_filter
                )

            domains.append(domain_info)

        domains = sorted(
            domains,
            key=lambda i: i['name'].lower()
        )

        return domains

    def get_domain_vmm(self, domain_name, vlan_info=False, vlan_usage_info=False):
        domain_filter = ['name:%s' % (domain_name)]
        domains = self.get_domains_vmm(
            domain_filter=domain_filter,
            vlan_info=vlan_info,
            vlan_usage_info=vlan_usage_info
        )
        if domains is None or len(domains) != 1:
            return None
        return domains[0]
