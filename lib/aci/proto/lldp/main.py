from lib.aci.proto.lldp.instance.main import ProtocolLldpInstance
from lib.aci.proto.lldp.stats.main import ProtocolLldpStats


class ProtocolLldp(ProtocolLldpInstance, ProtocolLldpStats):
    def __init__(self):
        ProtocolLldpInstance.__init__(self)
        ProtocolLldpStats.__init__(self)

    def get_protocol_lldp(self, pod_id, node_id, lldp_filter=None, include_instance=True, include_stats=True, include_adjacency=True):
        info = {}

        if include_instance:
            info['instance'] = self.get_protocol_lldp_instance(
                pod_id,
                node_id
            )

        if include_stats:
            info['stats'] = self.get_protocol_lldp_stats(
                pod_id,
                node_id
            )

        if include_adjacency:
            info['adjacency'] = self.get_lldp_adjacency_endpoint(
                pod_id,
                node_id,
                lldp_filter=lldp_filter
            )

            if include_instance:
                info['instance']['adjacencyCount'] = len(info['adjacency'])

        return info
