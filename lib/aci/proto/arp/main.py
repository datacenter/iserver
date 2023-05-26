from lib.aci.proto.arp.adjacency.main import ProtocolArpAdjacency
from lib.aci.proto.arp.domain.main import ProtocolArpDomain


class ProtocolArp(ProtocolArpAdjacency, ProtocolArpDomain):
    def __init__(self):
        ProtocolArpAdjacency.__init__(self)
        ProtocolArpDomain.__init__(self)

    def get_protocol_arp(self, pod_id, node_id, arp_domain_filter=None, adjacency_info=False, interface_info=False):
        info = {}

        info['domains'] = self.get_protocol_arp_domains(
            pod_id,
            node_id,
            arp_domain_filter=arp_domain_filter,
            adjacency_info=adjacency_info
        )

        if adjacency_info:
            info['adjacency'] = []
            for domain in info['domains']:
                info['adjacency'] = info['adjacency'] + domain['adjacency']

        if interface_info:
            info['interface'] = self.get_protocol_arp_domains_interface_summary(
                info['domains']
            )

        return info
