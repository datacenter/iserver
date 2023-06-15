class ProtocolLldpInfo():
    def __init__(self):
        pass

    def get_protocol_lldp(self, pod_id, node_id, adjacency_filter=None, instance_info=True, stats_info=True, adjacency_info=True):
        info = {}

        if instance_info:
            info['instance'] = self.get_protocol_lldp_instance(
                pod_id,
                node_id
            )

        if stats_info:
            info['stats'] = self.get_protocol_lldp_stats(
                pod_id,
                node_id
            )

        if adjacency_info:
            info['adjacency'] = self.get_lldp_adjacency_endpoint(
                pod_id,
                node_id,
                adjacency_filter=adjacency_filter
            )

            if instance_info:
                info['instance']['adjacencyCount'] = len(info['adjacency'])

            if stats_info:
                info['instance']['__Output']['errorsTick'] = info['stats']['__Output']['errorsTick']
                info['instance']['errorsTick'] = info['stats']['errorsTick']

        return info
