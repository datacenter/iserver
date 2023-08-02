from lib.aci.proto.bgp.domain.main import ProtocolBgpDomain
from lib.aci.proto.bgp.instance.main import ProtocolBgpInstance
from lib.aci.proto.bgp.neighbor.main import ProtocolBgpNeighbor
from lib.aci.proto.bgp.event.main import ProtocolBgpEvent
from lib.aci.proto.bgp.fault.main import ProtocolBgpFault


class ProtocolBgp(
        ProtocolBgpDomain,
        ProtocolBgpInstance,
        ProtocolBgpNeighbor,
        ProtocolBgpEvent,
        ProtocolBgpFault
        ):
    def __init__(self):
        ProtocolBgpDomain.__init__(self)
        ProtocolBgpInstance.__init__(self)
        ProtocolBgpNeighbor.__init__(self)
        ProtocolBgpEvent.__init__(self)
        ProtocolBgpFault.__init__(self)

    def get_protocol_bgp(
            self,
            pod_id,
            node_id,
            bgp_filter=None,
            instance_info=False,
            domain_info=False,
            neighbor_info=False,
            stats_info=False,
            prefix_info=False,
            fault_info=False,
            hfault_info=False,
            hfault_filter=None,
            event_info=False,
            event_filter=None
            ):
        info = {}

        if instance_info:
            info['instance'] = self.get_protocol_bgp_instance(
                pod_id,
                node_id
            )

        if domain_info:
            info['domain'] = self.get_protocol_bgp_domains(
                pod_id,
                node_id,
                bgp_domain_filter=bgp_filter
            )

        if neighbor_info:
            info['neighbor'] = self.get_protocol_bgp_neighbors(
                pod_id,
                node_id,
                bgp_neighbor_filter=bgp_filter,
                stats_info=stats_info,
                prefix_info=prefix_info
            )

        if instance_info and domain_info and neighbor_info:
            info['instance']['summary'] = self.get_protocol_bgp_instance_summary(
                info
            )
            info['instance'] = self.my_output.merge_output(
                info['instance']
            )

        if fault_info:
            info['faultInst'] = self.get_protocol_bgp_fault(
                pod_id,
                node_id
            )

        if hfault_info:
            all_faults = self.get_protocol_bgp_fault_record(
                pod_id,
                node_id
            )
            info['faultRecord'] = []
            for fault in all_faults:
                if not self.match_system_fault(fault, hfault_filter, exclude_cleared=False):
                    continue

                info['faultRecord'].append(
                    fault
                )

        if event_info:
            all_events = self.get_protocol_bgp_event(
                pod_id,
                node_id
            )
            info['eventLog'] = []
            for event in all_events:
                if not self.match_system_fault(event, event_filter, exclude_cleared=False):
                    continue

                info['eventLog'].append(
                    event
                )

        return info
