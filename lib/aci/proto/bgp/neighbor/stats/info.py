class ProtocolBgpNeighborStatsInfo():
    def __init__(self):
        pass

    def get_protocol_bgp_neighbor_stats_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_protocol_bgp_neighbor_stats(self, pod_id, node_id, bgp_domain_name, bgp_peer_addr, bgp_state_addr):
        managed_object = self.get_protocol_bgp_neighbor_stats_mo(
            pod_id,
            node_id,
            bgp_domain_name,
            bgp_peer_addr,
            bgp_state_addr
        )
        if managed_object is None or len(managed_object) == 0:
            return None

        return self.get_protocol_bgp_neighbor_stats_info(managed_object)
