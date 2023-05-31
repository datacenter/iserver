from lib import filter_helper


class DomainAaaInfo():
    def __init__(self):
        pass

    def get_domain_aaa_info(self, managed_object):
        keys = [
            'descr',
            'dn',
            'name',
            'restrictedRbacDomain',
            'status'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def match_domain_aaa(self, domain_info, domain_filter):
        if domain_filter is None or len(domain_filter) == 0:
            return True

        for aepg_rule in domain_filter:
            (key, value) = aepg_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, domain_info['name']):
                    return False

            if key == 'dn':
                if not filter_helper.match_string(value, domain_info['dn']):
                    return False

            if key == 'system':
                keys = ['mgmt', 'all', 'common']
                if value == 'true':
                    if domain_info['name'] not in keys:
                        return False

                if value == 'false':
                    if domain_info['name'] in keys:
                        return False

        return True

    def get_domains_aaa(self, domain_filter=None):
        all_domains = self.get_domain_aaa_mo()
        if all_domains is None:
            return None

        domain_aaa = []

        for managed_object in all_domains:
            domain_info = self.get_domain_aaa_info(
                managed_object
            )

            if not self.match_domain_aaa(domain_info, domain_filter):
                continue

            domain_aaa.append(domain_info)

        domain_aaa = sorted(
            domain_aaa,
            key=lambda i: i['name'].lower()
        )

        self.log.apic_mo(
            'aaaDomain.info',
            domain_aaa
        )

        return domain_aaa
