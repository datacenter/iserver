from lib import filter_helper


class PolicyGeneralAaeInfo():
    def __init__(self):
        pass

    def get_policy_global_aae_domain_info(self, managed_object):
        keys = [
            'forceResolve',
            'state',
            'tCl',
            'tDn'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['domainType'] = self.get_domain_type_from_tcl(
            managed_object['tCl']
        )

        info['domainName'] = managed_object['tDn']
        if info['tCl'] == 'vmmDomP':
            # "tDn": "uni/vmmp-VMware/dom-EU-SPDC-CDC-22"
            info['domainName'] = managed_object['tDn'].split('/')[2][4:]

        if info['tCl'] == 'l3extDomP':
            # "tDn": "uni/l3dom-vEPC_ESX"
            info['domainName'] = managed_object['tDn'].split('/')[1][6:]

        if info['tCl'] == 'physDomP':
            # "tDn": "uni/phys-ESX-CDC-22_PhysDom"
            info['domainName'] = managed_object['tDn'].split('/')[1][5:]

        if info['tCl'] == 'l2extDomP':
            # "tDn": "uni/l2dom-Infra_L2dom"
            info['domainName'] = managed_object['tDn'].split('/')[1][6:]

        return info

    def extend_policy_global_aae_domain_info(self, policy_global_aae_info):
        for domain_info in policy_global_aae_info['infraRsDomP']:
            if domain_info['tCl'] == 'physDomP':
                domain_info['info'] = self.get_domain_phy(
                    domain_info['domainName'],
                    vlan_info=True
                )
                continue

            if domain_info['tCl'] == 'vmmDomP':
                domain_info['info'] = self.get_domain_vmm(
                    domain_info['domainName'],
                    vlan_info=True
                )
                continue

            if domain_info['tCl'] == 'l2extDomP':
                domain_info['info'] = self.get_domain_l2(
                    domain_info['domainName'],
                    vlan_info=True
                )
                continue

            if domain_info['tCl'] == 'l3extDomP':
                domain_info['info'] = self.get_domain_l3(
                    domain_info['domainName'],
                    vlan_info=True
                )
                continue

            domain_info['info'] = None
            self.log.error(
                'extend_policy_global_aae_domain_info',
                'Unsupported domain: %s' % (domain_info['tCl'])
            )

        policy_global_aae_info['vlanPool'] = []
        policy_global_aae_info['vlanBlock'] = []
        for domain_info in policy_global_aae_info['infraRsDomP']:
            if domain_info['info'] is not None:
                if domain_info['info']['vlan'] not in policy_global_aae_info['vlanPool']:
                    policy_global_aae_info['vlanPool'].append(
                        domain_info['info']['vlan']
                    )
                    if domain_info['info']['vlan_info'] is not None:
                        for vlan_range in domain_info['info']['vlan_info']['fvnsEncapBlk']:
                            policy_global_aae_info['vlanBlock'].append(
                                vlan_range['blockInfo']
                            )

        policy_global_aae_info['vlanPool'] = sorted(
            policy_global_aae_info['vlanPool']
        )
        policy_global_aae_info['vlanBlock'] = sorted(
            policy_global_aae_info['vlanBlock']
        )

        return policy_global_aae_info

    def get_policy_global_aae_epg_info(self, managed_object):
        keys = [
            'dn',
            'encap',
            'mode',
            'primaryEncap',
            'state',
            'tCl',
            'tDn'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['epgName'] = None
        if info['tCl'] == 'fvAEPg':
            info['epgName'] = self.get_epg_name_from_dn(
                managed_object['tDn']
            )

        info['epgEncap'] = None
        if info['epgName'] is not None:
            if info['encap'] is not None and len(info['encap']) > 0:
                info['epgEncap'] = '%s (%s)' % (
                    info['epgName'],
                    info['encap']
                )

        return info

    def get_policy_global_aae_policy_group_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['dn'] = managed_object['tDn']
        info['type'] = managed_object['tCl']
        info['typeName'] = self.get_policy_type_from_tcl(
            managed_object['tCl']
        )

        info['name'] = managed_object['tDn']
        if info['type'] == 'infraSpAccPortGrp':
            # "tDn": "uni/infra/funcprof/spaccportgrp-multipodL3Out_policyGroup"
            info['name'] = managed_object['tDn'].split('/')[3][13:]

        if info['type'] == 'infraAccPortGrp':
            # "tDn": "uni/infra/funcprof/accportgrp-ESX-CDC-22_PolGrp"
            info['name'] = managed_object['tDn'].split('/')[3][11:]

        if info['type'] == 'infraAccBndlGrp':
            # "tDn": "uni/infra/funcprof/accbundle-k8s_esx72_PolGrp"
            info['name'] = managed_object['tDn'].split('/')[3][10:]

        if info['type'] not in ['infraSpAccPortGrp', 'infraAccPortGrp', 'infraAccBndlGrp']:
            self.log.error(
                'get_policy_global_aae_policy_group_info',
                'Unsupported: %s' % (managed_object['tDn'])
            )

        return info

    def get_policy_global_aae_info(self, managed_object):
        keys = [
            'descr',
            'dn',
            'name'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['infraRtAttEntP'] = []
        for policy_group_mo in managed_object['infraRtAttEntP']:
            info['infraRtAttEntP'].append(
                self.get_policy_global_aae_policy_group_info(
                    policy_group_mo
                )
            )
        info['infraRtAttEntP'] = sorted(
            info['infraRtAttEntP'],
            key=lambda i: i['name']
        )

        info['infraRsDomP'] = []
        for domain_mo in managed_object['infraRsDomP']:
            info['infraRsDomP'].append(
                self.get_policy_global_aae_domain_info(
                    domain_mo
                )
            )

        info['infraRsDomP'] = sorted(
            info['infraRsDomP'],
            key=lambda i: i['domainName']
        )

        info['infraRsFuncToEpg'] = []
        for epg_mo in managed_object['infraRsFuncToEpg']:
            info['infraRsFuncToEpg'].append(
                self.get_policy_global_aae_epg_info(
                    epg_mo
                )
            )

        if managed_object['infraProvAcc'] is None:
            info['infraVlanEnabled'] = False
            info['infraVlanEnabledTick'] = '\u2717'
            info['__Output']['infraVlanEnabledTick'] = 'Red'
        else:
            info['infraVlanEnabled'] = True
            info['infraVlanEnabledTick'] = '\u2713'
            info['__Output']['infraVlanEnabledTick'] = 'Green'

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def match_policy_global_aae(self, policy_global_aae_info, policy_global_aae_filter):
        if policy_global_aae_filter is None or len(policy_global_aae_filter) == 0:
            return True

        for aepg_rule in policy_global_aae_filter:
            (key, value) = aepg_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, policy_global_aae_info['name']):
                    return False

            if key == 'dn':
                if not filter_helper.match_string(value, policy_global_aae_info['dn']):
                    return False

            if key == 'fault':
                if value == 'any':
                    if not policy_global_aae_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_policy_global_aae',
                        'Unsupported fault filtering value: %s' % (value)
                    )

        return True

    def get_policy_global_aae(
            self,
            policy_global_aae_filter=None,
            domain_info=False,
            node_info=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_policies = self.get_policy_global_aae_mo()
        if all_policies is None:
            return None

        policy_global_aae = []

        for managed_object in all_policies:
            policy_global_aae_info = self.get_policy_global_aae_info(
                managed_object
            )

            if not self.match_policy_global_aae(policy_global_aae_info, policy_global_aae_filter):
                continue

            if domain_info:
                policy_global_aae_info = self.extend_policy_global_aae_domain_info(
                    policy_global_aae_info
                )

            if node_info:
                domain_node_info = self.get_policy_global_aae_node(
                    policy_global_aae_info['name']
                )
                policy_global_aae_info['node'] = None
                policy_global_aae_info['interface'] = None
                if domain_node_info is not None:
                    policy_global_aae_info['node'] = domain_node_info['node']
                    policy_global_aae_info['interface'] = domain_node_info['interface']

            if fault_info:
                policy_global_aae_info['faultInst'] = self.get_policy_global_aae_id_fault(
                    policy_global_aae_info['name'],
                    'faultInst'
                )

            if hfault_info:
                policy_global_aae_info['faultRecord'] = self.get_policy_global_aae_id_fault(
                    policy_global_aae_info['name'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                policy_global_aae_info['eventLog'] = self.get_policy_global_aae_id_event(
                    policy_global_aae_info['name'],
                    event_filter=event_filter
                )

            if audit_info:
                policy_global_aae_info['auditLog'] = self.get_policy_global_aae_id_audit(
                    policy_global_aae_info['name'],
                    audit_filter=audit_filter
                )

            policy_global_aae.append(policy_global_aae_info)

        policy_global_aae = sorted(
            policy_global_aae,
            key=lambda i: i['name'].lower()
        )

        self.log.apic_mo(
            'infraAttEntityP.info',
            policy_global_aae
        )

        return policy_global_aae
