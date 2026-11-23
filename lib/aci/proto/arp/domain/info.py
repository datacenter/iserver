from lib import filter_helper


class ProtocolArpDomainInfo():
    def __init__(self):
        self.arp_domains = {}

    def get_protocol_arp_domains_interface_summary(self, domains):
        interface = {}

        for domain in domains:
            pod_node_name = domain['pod_node_name']
            if 'adjacency' in domain and domain['adjacency'] is not None:
                for adjacency in domain['adjacency']:
                    if adjacency['ifId'] not in interface:
                        interface[adjacency['ifId']] = 0

                    interface[adjacency['ifId']] = interface[adjacency['ifId']] + 1

        interface_list = []
        for intf in interface:
            entry = {}
            entry['pod_node_name'] = pod_node_name
            entry['interface'] = intf
            entry['count'] = interface[intf]
            interface_list.append(entry)

        interface_list = sorted(
            interface_list,
            key=lambda i: (
                i['pod_node_name'],
                i['interface'].lower()
            )
        )
        return interface_list

    def get_protocol_arp_domain_info(self, managed_object):
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

    def get_protocol_arp_domains_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.arp_domains:
            return self.arp_domains[key]

        arp_domains_mo = self.get_protocol_arp_domains_mo(pod_id, node_id)
        if arp_domains_mo is not None:
            self.arp_domains[key] = []
            for arp_domain_mo in arp_domains_mo:
                self.arp_domains[key].append(
                    self.get_protocol_arp_domain_info(
                        arp_domain_mo
                    )
                )

        return self.arp_domains[key]

    def match_protocol_arp_domain(self, arp_domain_info, arp_domain_filter):
        if arp_domain_filter is None or len(arp_domain_filter) == 0:
            return True

        for ap_rule in arp_domain_filter:
            (key, value) = ap_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, arp_domain_info['name']):
                    return False

        return True

    def get_protocol_arp_adjacency_filter(self, arp_domain_info, arp_domain_filter):
        if arp_domain_filter is None:
            return None

        arp_adjacency_filter = ['name:%s' % (arp_domain_info['name'])]
        for rule in arp_domain_filter:
            if rule.split(':')[0] == 'name':
                continue

            arp_adjacency_filter.append(
                rule
            )

        return arp_adjacency_filter

    def get_protocol_arp_domains(self, pod_id, node_id, arp_domain_filter=None, adjacency_info=False):
        all_arp_domains = self.get_protocol_arp_domains_info(pod_id, node_id)
        if all_arp_domains is None:
            return None

        arp_domains = []

        for arp_domain_info in all_arp_domains:
            if not self.match_protocol_arp_domain(arp_domain_info, arp_domain_filter):
                continue

            if adjacency_info:
                arp_domain_info['adjacency'] = self.get_protocol_arp_adjacencies(
                    pod_id,
                    node_id,
                    arp_adjacency_filter=self.get_protocol_arp_adjacency_filter(
                        arp_domain_info,
                        arp_domain_filter
                    )
                )

                arp_domain_info['adjacency_count'] = 0
                if arp_domain_info['adjacency'] is not None:
                    arp_domain_info['adjacency_count'] = len(arp_domain_info['adjacency'])

            arp_domains.append(
                arp_domain_info
            )

        arp_domains = sorted(
            arp_domains,
            key=lambda i: i['name'].lower()
        )

        return arp_domains
