from lib.aci.proto.bgp.domain.main import ProtocolBgpDomain
from lib.aci.proto.bgp.instance.main import ProtocolBgpInstance
from lib.aci.proto.bgp.neighbor.main import ProtocolBgpNeighbor


class ProtocolBgp(ProtocolBgpDomain, ProtocolBgpInstance, ProtocolBgpNeighbor):
    def __init__(self):
        ProtocolBgpDomain.__init__(self)
        ProtocolBgpInstance.__init__(self)
        ProtocolBgpNeighbor.__init__(self)

    def get_protocol_bgp(self, pod_id, node_id, bgp_filter=None, stats_info=False, prefix_info=False):
        info = {}

        info['instance'] = self.get_protocol_bgp_instance(
            pod_id,
            node_id
        )

        if info['instance'] is None:
            return None

        info['domains'] = self.get_protocol_bgp_domains(
            pod_id,
            node_id,
            bgp_domain_filter=bgp_filter
        )

        info['neighbors'] = self.get_protocol_bgp_neighbors(
            pod_id,
            node_id,
            bgp_neighbor_filter=bgp_filter,
            stats_info=stats_info,
            prefix_info=prefix_info
        )

        info['instance']['summary'] = self.get_protocol_bgp_instance_summary(
            info
        )
        info['instance'] = self.my_output.merge_output(
            info['instance']
        )

        return info
