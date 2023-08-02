class ProtocolLldpInfo():
    def __init__(self):
        pass

    def get_protocol_lldp(
            self,
            pod_id,
            node_id,
            adjacency_filter=None,
            instance_info=True,
            stats_info=True,
            adjacency_info=True,
            fault_info=False,
            hfault_info=False,
            hfault_filter=None,
            event_info=False,
            event_filter=None
            ):
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

        if fault_info:
            info['faultInst'] = self.get_protocol_lldp_fault(
                pod_id,
                node_id
            )
            if adjacency_info:
                for adjacency in info['adjacency']:
                    adjacency['faultInst'] = self.get_protocol_lldp_adjacency_fault(
                        pod_id,
                        node_id,
                        adjacency['interface_id'],
                        'faultInst'
                    )

        if hfault_info:
            info['faultRecord'] = self.get_protocol_lldp_fault(
                pod_id,
                node_id
            )
            if adjacency_info:
                for adjacency in info['adjacency']:
                    adjacency['faultRecord'] = self.get_protocol_lldp_adjacency_fault(
                        pod_id,
                        node_id,
                        adjacency['interface_id'],
                        'faultRecord',
                        fault_filter=hfault_filter
                    )

        if event_info:
            info['eventLog'] = self.get_protocol_lldp_event(
                pod_id,
                node_id
            )
            if adjacency_info:
                for adjacency in info['adjacency']:
                    adjacency['eventLog'] = self.get_protocol_lldp_adjacency_event(
                        pod_id,
                        node_id,
                        adjacency['interface_id'],
                        event_filter=event_filter
                    )

        return info
