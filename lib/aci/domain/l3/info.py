from lib import filter_helper


class DomainL3Info():
    def __init__(self):
        self.domain_l3 = None

    def get_domain_l3_info(self, managed_object):
        keys = [
            'dn',
            'name'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

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

    def get_domains_l3_info(self):
        if self.domain_l3 is not None:
            return self.domain_l3

        domains_mo = self.get_domain_l3_mo()
        if domains_mo is None:
            return None

        self.domain_l3 = []
        for managed_object in domains_mo:
            self.domain_l3.append(
                self.get_domain_l3_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'l3extDomP.info',
            self.domain_l3
        )

        return self.domain_l3

    def match_domain_l3(self, domain_info, domain_filter):
        if domain_filter is None or len(domain_filter) == 0:
            return True

        for aepg_rule in domain_filter:
            (key, value) = aepg_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, domain_info['name']):
                    return False

        return True

    def get_domains_l3(self, domain_filter=None, vlan_info=False):
        all_domains = self.get_domains_l3_info()

        domains = []

        for domain_info in all_domains:
            if not self.match_domain_l3(domain_info, domain_filter):
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
