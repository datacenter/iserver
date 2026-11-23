from lib import filter_helper


class ProtocolHsrpDomainInfo():
    def __init__(self):
        self.hsrp_domains = {}

    def add_protocol_hsrp_domain_interface_info(self, domains, interfaces):
        for domain in domains:
            domain['interfacesCount'] = 0

            for interface in interfaces:
                if interface['domainName'] == domain['name']:
                    domain['interfacesCount'] = domain['interfacesCount'] + 1

        return domains

    def get_protocol_hsrp_domain_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['__Output']['name'] = 'Yellow'

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
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

    def get_protocol_hsrp_domains_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.hsrp_domains:
            return self.hsrp_domains[key]

        hsrp_domains_mo = self.get_protocol_hsrp_domains_mo(pod_id, node_id)
        if hsrp_domains_mo is not None:
            self.hsrp_domains[key] = []
            for hsrp_domain_mo in hsrp_domains_mo:
                self.hsrp_domains[key].append(
                    self.get_protocol_hsrp_domain_info(
                        hsrp_domain_mo
                    )
                )

        return self.hsrp_domains[key]

    def match_protocol_hsrp_domain(self, hsrp_domain_info, hsrp_domain_filter):
        if hsrp_domain_filter is None or len(hsrp_domain_filter) == 0:
            return True

        for ap_rule in hsrp_domain_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'vrf':
                if not filter_helper.match_string(value, hsrp_domain_info['name']):
                    return False

        return True

    def get_protocol_hsrp_domains(self, pod_id, node_id, hsrp_domain_filter=None):
        all_hsrp_domains = self.get_protocol_hsrp_domains_info(pod_id, node_id)
        if all_hsrp_domains is None:
            return None

        hsrp_domains = []

        for hsrp_domain_info in all_hsrp_domains:
            if not self.match_protocol_hsrp_domain(hsrp_domain_info, hsrp_domain_filter):
                continue

            hsrp_domains.append(
                hsrp_domain_info
            )

        hsrp_domains = sorted(
            hsrp_domains,
            key=lambda i: i['name'].lower()
        )

        return hsrp_domains
