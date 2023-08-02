from lib import filter_helper


class ProtocolIpv6DomainInfo():
    def __init__(self):
        self.ipv6_domains = {}

    def get_protocol_ipv6_domain_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        info['__Output']['name'] = 'Yellow'

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_protocol_ipv6_domains_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.ipv6_domains:
            return self.ipv6_domains[key]

        ipv6_domains_mo = self.get_protocol_ipv6_domains_mo(pod_id, node_id)
        if ipv6_domains_mo is not None:
            self.ipv6_domains[key] = []
            for ipv6_domain_mo in ipv6_domains_mo:
                self.ipv6_domains[key].append(
                    self.get_protocol_ipv6_domain_info(
                        ipv6_domain_mo
                    )
                )

        return self.ipv6_domains[key]

    def match_protocol_ipv6_domain(self, ipv6_domain_info, ipv6_domain_filter):
        if ipv6_domain_filter is None or len(ipv6_domain_filter) == 0:
            return True

        for ap_rule in ipv6_domain_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'vrf':
                if not filter_helper.match_tenant_name(value, ipv6_domain_info['name'], delimiter=':'):
                    return False

        return True

    def get_protocol_ipv6_domains(self, pod_id, node_id, ipv6_domain_filter=None):
        all_ipv6_domains = self.get_protocol_ipv6_domains_info(pod_id, node_id)
        if all_ipv6_domains is None:
            return None

        ipv6_domains = []

        for ipv6_domain_info in all_ipv6_domains:
            if not self.match_protocol_ipv6_domain(ipv6_domain_info, ipv6_domain_filter):
                continue

            ipv6_domains.append(
                ipv6_domain_info
            )

        ipv6_domains = sorted(
            ipv6_domains,
            key=lambda i: i['name'].lower()
        )

        return ipv6_domains
