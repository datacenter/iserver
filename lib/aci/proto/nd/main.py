from lib.aci.proto.nd.instance.main import ProtocolNdInstance
from lib.aci.proto.nd.domain.main import ProtocolNdDomain
from lib.aci.proto.nd.interface.main import ProtocolNdInterface
from lib.aci.proto.nd.neighbor.main import ProtocolNdNeighbor
from lib.aci.proto.nd.event.main import ProtocolNdEvent
from lib.aci.proto.nd.fault.main import ProtocolNdFault


class ProtocolNd(
        ProtocolNdInstance,
        ProtocolNdDomain,
        ProtocolNdInterface,
        ProtocolNdNeighbor,
        ProtocolNdEvent,
        ProtocolNdFault
        ):
    def __init__(self):
        ProtocolNdInstance.__init__(self)
        ProtocolNdDomain.__init__(self)
        ProtocolNdInterface.__init__(self)
        ProtocolNdNeighbor.__init__(self)
        ProtocolNdEvent.__init__(self)
        ProtocolNdFault.__init__(self)

    def get_protocol_nd(
            self,
            pod_id,
            node_id,
            instance_info=False,
            domain_info=False,
            neighbor_info=False,
            interface_info=False,
            fault_info=False,
            hfault_info=False,
            hfault_filter=None,
            event_info=False,
            event_filter=None
            ):
        info = {}

        if instance_info:
            info['instance'] = self.get_protocol_nd_instance_info(
                pod_id=pod_id,
                node_id=node_id
            )

        if domain_info:
            info['domain'] = self.get_protocol_nd_domain_info(
                pod_id,
                node_id
            )

        if neighbor_info:
            info['neighbor'] = self.get_protocol_nd_neighbors_info(
                pod_id,
                node_id
            )
            if domain_info:
                info['domain'] = self.add_protocol_nd_domain_neighbor_info(
                    info['domain'],
                    info['neighbor']
                )

            if instance_info:
                info['instance']['neighborCount'] = len(info['neighbor'])

        if interface_info:
            info['interface'] = self.get_protocol_nd_interfaces_info(
                pod_id,
                node_id
            )

            if interface_info:
                info['domain'] = self.add_protocol_nd_domain_interface_info(
                    info['domain'],
                    info['interface']
                )

            if neighbor_info:
                info['interface'] = self.add_protocol_nd_interface_neighbor_info(
                    info['interface'],
                    info['neighbor'],
                    remove_no_neighbors=False
                )

            if instance_info:
                info['instance']['activeInterfaceCount'] = self.get_nd_active_interface_count(
                    info['interface']
                )

        if fault_info:
            info['faultInst'] = self.get_protocol_nd_fault(
                pod_id,
                node_id
            )

        if hfault_info:
            all_faults = self.get_protocol_nd_fault_record(
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
            all_events = self.get_protocol_nd_event(
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
