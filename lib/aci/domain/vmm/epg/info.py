from lib import filter_helper


class DomainVmmEpgInfo():
    def __init__(self):
        self.domain_vmm_epg = None

    def get_domain_vmm_epg_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        info['vlanId'] = int(info['encap'][5:])

        if info['allocMode'] == 'dynamic':
            info['tenant'] = info['encapAllocKey'].split('/')[1][3:]
            info['appName'] = info['encapAllocKey'].split('/')[2][3:]
            info['epgName'] = info['encapAllocKey'].split('/')[3][4:]
            info['tenantAppEpg'] = '%s/%s/%s' % (
                info['tenant'],
                info['appName'],
                info['epgName']
            )

        if info['allocMode'] == 'static':
            info['tenant'] = ''
            info['appName'] = ''
            info['epgName'] = ''
            info['tenantAppEpg'] = 'static allocation'

        info['domainType'] = 'VMM Domain'
        info['domainName'] = None

        if info['domainName'] is None and 'dn' in info:
            info['domainName'] = '%s/%s' % (
                info['dn'].split('/')[1][5:],
                info['dn'].split('/')[2][4:]
            )

        if info['domainName'] is None and 'idConsumerDn' in info:
            if len(info['idConsumerDn']) > 0:
                info['domainName'] = '%s/%s' % (
                    info['idConsumerDn'].split('/')[1][5:],
                    info['idConsumerDn'].split('/')[2][4:]
                )

        return info

    def get_domain_vmm_epg_infos(self):
        if self.domain_vmm_epg is not None:
            return self.domain_vmm_epg

        managed_objects = self.get_domain_vmm_epg_mo()
        if managed_objects is None:
            return None

        self.domain_vmm_epg = []
        for managed_object in managed_objects:
            self.domain_vmm_epg.append(
                self.get_domain_vmm_epg_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'vmmEpPD.info',
            self.domain_vmm_epg
        )

        return self.domain_vmm_epg

    def match_domain_vmm_epg(self, domain_vmm_epg_info, domain_vmm_epg_filter):
        if domain_vmm_epg_filter is None or len(domain_vmm_epg_filter) == 0:
            return True

        range_defined = False
        range_match = False

        for aepg_rule in domain_vmm_epg_filter:
            (key, value) = aepg_rule.split(':')
            if key == 'pool':
                if not filter_helper.match_string(value, domain_vmm_epg_info['encapCtx']):
                    return False

            if key == 'range':
                range_defined = True
                (vlan_from, vlan_to) = value.split(',')
                vlan_id = domain_vmm_epg_info['encap'][5:]
                if int(vlan_from) <= int(vlan_id) <= int(vlan_to):
                    range_match = True

        if range_defined and not range_match:
            return False

        return True

    def get_domain_vmm_epgs(self, domain_vmm_epg_filter=None):
        all_epgs = self.get_domain_vmm_epg_infos()
        if all_epgs is None:
            return None

        epgs = []

        for domain_vmm_epg_info in all_epgs:
            if not self.match_domain_vmm_epg(domain_vmm_epg_info, domain_vmm_epg_filter):
                continue

            epgs.append(domain_vmm_epg_info)

        epgs = sorted(
            epgs,
            key=lambda i: i['vlanId']
        )

        return epgs
