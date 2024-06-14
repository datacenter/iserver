from lib import filter_helper
from lib import ip_helper


class ProtocolArpAdjacencyInfo():
    def __init__(self):
        self.arp_adjacencies = {}

    def get_protocol_arp_adjacency_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['domain_name'] = info['dn'].split('/')[6][4:]
        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        if info['physIfId'] == 'unspecified':
            info['physIfId'] = ''

        info['__Output']['name'] = 'Yellow'
        if info['operSt'] == 'normal':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        return info

    def get_protocol_arp_adjacencies_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.arp_adjacencies:
            return self.arp_adjacencies[key]

        arp_adjacencies_mo = self.get_protocol_arp_adjacencies_mo(pod_id, node_id)
        if arp_adjacencies_mo is not None:
            self.arp_adjacencies[key] = []
            for arp_adjacency_mo in arp_adjacencies_mo:
                self.arp_adjacencies[key].append(
                    self.get_protocol_arp_adjacency_info(
                        arp_adjacency_mo
                    )
                )

        self.log.apic_mo(
            'arpAdjEp.info.%s' % (key),
            self.arp_adjacencies[key]
        )

        return self.arp_adjacencies[key]

    def match_protocol_arp_adjacency(self, arp_adjacency_info, arp_adjacency_filter):
        if arp_adjacency_filter is None or len(arp_adjacency_filter) == 0:
            return True

        for ap_rule in arp_adjacency_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])
            if key == 'name':
                if not filter_helper.match_string(value, arp_adjacency_info['domain_name']):
                    return False

            if key == 'mac':
                if not filter_helper.match_mac(value, arp_adjacency_info['mac']):
                    return False

            if key == 'ip':
                if not filter_helper.match_string(value, arp_adjacency_info['ip']):
                    return False

            if key == 'subnet':
                if not ip_helper.is_ipv4_in_cidr(arp_adjacency_info['ip'], value):
                    return False

        return True

    def get_protocol_arp_adjacencies(self, pod_id, node_id, arp_adjacency_filter=None):
        all_arp_adjacencies = self.get_protocol_arp_adjacencies_info(pod_id, node_id)
        if all_arp_adjacencies is None:
            return None

        arp_adjacencies = []

        for arp_adjacency_info in all_arp_adjacencies:
            if not self.match_protocol_arp_adjacency(arp_adjacency_info, arp_adjacency_filter):
                continue

            arp_adjacencies.append(
                arp_adjacency_info
            )

        arp_adjacencies = sorted(
            arp_adjacencies,
            key=lambda i: i['mac'].lower()
        )

        return arp_adjacencies
