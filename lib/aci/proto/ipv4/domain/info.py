from lib import filter_helper


class ProtocolIpv4DomainInfo():
    def __init__(self):
        self.ipv4_domains = {}

    def get_protocol_ipv4_domain_info(self, managed_object):
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

    def get_protocol_ipv4_domains_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.ipv4_domains:
            return self.ipv4_domains[key]

        ipv4_domains_mo = self.get_protocol_ipv4_domains_mo(pod_id, node_id)
        if ipv4_domains_mo is not None:
            self.ipv4_domains[key] = []
            for ipv4_domain_mo in ipv4_domains_mo:
                self.ipv4_domains[key].append(
                    self.get_protocol_ipv4_domain_info(
                        ipv4_domain_mo
                    )
                )

        return self.ipv4_domains[key]

    def match_protocol_ipv4_domain(self, ipv4_domain_info, ipv4_domain_filter):
        if ipv4_domain_filter is None or len(ipv4_domain_filter) == 0:
            return True

        for ap_rule in ipv4_domain_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'vrf':
                if not filter_helper.match_tenant_name(value, ipv4_domain_info['name'], delimiter=':'):
                    return False

        return True

    def get_protocol_ipv4_domains(self, pod_id, node_id, ipv4_domain_filter=None):
        all_ipv4_domains = self.get_protocol_ipv4_domains_info(pod_id, node_id)
        if all_ipv4_domains is None:
            return None

        ipv4_domains = []

        for ipv4_domain_info in all_ipv4_domains:
            if not self.match_protocol_ipv4_domain(ipv4_domain_info, ipv4_domain_filter):
                continue

            ipv4_domains.append(
                ipv4_domain_info
            )

        ipv4_domains = sorted(
            ipv4_domains,
            key=lambda i: i['name'].lower()
        )

        return ipv4_domains
