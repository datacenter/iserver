from lib.aci.proto.isis.domain.main import ProtocolIsisDomain
from lib.aci.proto.isis.instance.main import ProtocolIsisInstance
from lib.aci.proto.isis.interface.main import ProtocolIsisInterface
from lib.aci.proto.isis.lsp.main import ProtocolIsisLsp
from lib.aci.proto.isis.neighbor.main import ProtocolIsisNeighbor
from lib.aci.proto.isis.route.main import ProtocolIsisRoute
from lib.aci.proto.isis.tree.main import ProtocolIsisTree
from lib.aci.proto.isis.tunnel.main import ProtocolIsisTunnel
from lib.aci.proto.isis.event.main import ProtocolIsisEvent
from lib.aci.proto.isis.fault.main import ProtocolIsisFault


class ProtocolIsis(
        ProtocolIsisDomain,
        ProtocolIsisInterface,
        ProtocolIsisInstance,
        ProtocolIsisLsp,
        ProtocolIsisNeighbor,
        ProtocolIsisRoute,
        ProtocolIsisTree,
        ProtocolIsisTunnel,
        ProtocolIsisEvent,
        ProtocolIsisFault
        ):
    def __init__(self):
        ProtocolIsisDomain.__init__(self)
        ProtocolIsisInstance.__init__(self)
        ProtocolIsisInterface.__init__(self)
        ProtocolIsisLsp.__init__(self)
        ProtocolIsisNeighbor.__init__(self)
        ProtocolIsisRoute.__init__(self)
        ProtocolIsisTree.__init__(self)
        ProtocolIsisTunnel.__init__(self)
        ProtocolIsisEvent.__init__(self)
        ProtocolIsisFault.__init__(self)

    def get_protocol_isis(
            self,
            pod_id,
            node_id,
            isis_domain_filter=None,
            instance_info=False,
            domain_info=False,
            tunnel_info=False,
            lsp_info=False,
            interface_info=False,
            neighbor_info=False,
            tree_info=False,
            route_info=False,
            fault_info=False,
            hfault_info=False,
            hfault_filter=None,
            event_info=False,
            event_filter=None
            ):
        info = {}

        if instance_info:
            info['instance'] = self.get_protocol_isis_instance(
                pod_id=pod_id,
                node_id=node_id
            )

        if domain_info:
            info['domain'] = self.get_protocol_isis_domains(
                pod_id,
                node_id,
                isis_domain_filter=isis_domain_filter,
                tunnel_info=tunnel_info,
                lsp_info=lsp_info,
                interface_info=interface_info,
                neighbor_info=neighbor_info,
                tree_info=tree_info,
                route_info=route_info
            )

            if instance_info:
                info['instance']['domainCount'] = len(info['domain'])

        if fault_info:
            info['faultInst'] = self.get_protocol_isis_fault(
                pod_id,
                node_id
            )

        if hfault_info:
            all_faults = self.get_protocol_isis_fault_record(
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
            all_events = self.get_protocol_isis_event(
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
