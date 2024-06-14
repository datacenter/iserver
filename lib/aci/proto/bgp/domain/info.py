from lib import filter_helper


class ProtocolBgpDomainInfo():
    def __init__(self):
        self.bgp_domains = {}

    def get_protocol_bgp_domain_info(self, managed_object):
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

        if info['numPeers'] == '0':
            info['isPeer'] = False
        else:
            info['isPeer'] = True
            info['__Output']['numPeers'] = 'Blue'

        info['peerSummary'] = '%s/%s' % (
            info['numEstPeers'],
            info['numPeers']
        )

        if info['numEstPeers'] != '0':
            if info['numPeers'] == info['numEstPeers']:
                info['__Output']['peerSummary'] = 'Green'
                info['__Output']['numEstPeers'] = 'Green'
            else:
                info['__Output']['peerSummary'] = 'Red'
                info['__Output']['numEstPeers'] = 'Red'

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

    def get_protocol_bgp_domains_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bgp_domains:
            return self.bgp_domains[key]

        bgp_domains_mo = self.get_protocol_bgp_domains_mo(pod_id, node_id)
        if bgp_domains_mo is not None:
            self.bgp_domains[key] = []
            for bgp_domain_mo in bgp_domains_mo:
                self.bgp_domains[key].append(
                    self.get_protocol_bgp_domain_info(
                        bgp_domain_mo
                    )
                )

        return self.bgp_domains[key]

    def match_protocol_bgp_domain(self, bgp_domain_info, bgp_domain_filter):
        if bgp_domain_filter is None or len(bgp_domain_filter) == 0:
            return True

        for ap_rule in bgp_domain_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'vrf':
                if not filter_helper.match_string(value, bgp_domain_info['name']):
                    return False

        return True

    def get_protocol_bgp_domains(self, pod_id, node_id, bgp_domain_filter=None):
        all_bgp_domains = self.get_protocol_bgp_domains_info(pod_id, node_id)
        if all_bgp_domains is None:
            return None

        bgp_domains = []

        for bgp_domain_info in all_bgp_domains:
            if not self.match_protocol_bgp_domain(bgp_domain_info, bgp_domain_filter):
                continue

            bgp_domains.append(
                bgp_domain_info
            )

        bgp_domains = sorted(
            bgp_domains,
            key=lambda i: i['name'].lower()
        )

        return bgp_domains
