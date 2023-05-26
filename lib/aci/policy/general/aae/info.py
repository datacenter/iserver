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

        if managed_object['infraProvAcc'] is None:
            info['infraVlanEnabled'] = False
            info['infraVlanEnabledTick'] = '\u2717'
            info['__Output']['infraVlanEnabledTick'] = 'Red'
        else:
            info['infraVlanEnabled'] = True
            info['infraVlanEnabledTick'] = '\u2713'
            info['__Output']['infraVlanEnabledTick'] = 'Green'

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

        return True

    def get_policy_global_aae(self, policy_global_aae_filter=None):
        policy_global_aae = []

        if not self.initialize_policy_global_aae():
            self.log.error(
                'get_policy_global_aae',
                'Initialization failed'
            )
            return policy_global_aae

        for managed_object in self.mo_policy_global_aae:
            policy_global_aae_info = self.get_policy_global_aae_info(
                managed_object
            )

            if not self.match_policy_global_aae(policy_global_aae_info, policy_global_aae_filter):
                continue

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
