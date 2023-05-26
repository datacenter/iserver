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
                                if user_item['name'] == '%s_cred' % (item['name']):
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
            if key == 'name':
                if not filter_helper.match_string(value, domain_info['name']):
                    return False

        return True

    def get_domains_vmm(self, domain_filter=None, vlan_info=False):
        all_domains = self.get_domains_vmm_info()

        domains = []

        for domain_info in all_domains:
            if not self.match_domain_vmm(domain_info, domain_filter):
                continue

            if vlan_info:
                domain_info['vlan_info'] = None
                if domain_info['vlan'] is not None:
                    domain_info['vlan_info'] = self.get_pool_vlan(
                        domain_info['vlan']
                    )

            domains.append(domain_info)

        domains = sorted(
            domains,
            key=lambda i: i['name'].lower()
        )

        return domains
