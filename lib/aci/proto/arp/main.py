from lib.aci.proto.arp.instance.main import ProtocolArpInstance
from lib.aci.proto.arp.domain.main import ProtocolArpDomain
from lib.aci.proto.arp.adjacency.main import ProtocolArpAdjacency
from lib.aci.proto.arp.event.main import ProtocolArpEvent
from lib.aci.proto.arp.fault.main import ProtocolArpFault


class ProtocolArp(
        ProtocolArpInstance,
        ProtocolArpDomain,
        ProtocolArpAdjacency,
        ProtocolArpEvent,
        ProtocolArpFault
        ):
    def __init__(self):
        ProtocolArpInstance.__init__(self)
        ProtocolArpDomain.__init__(self)
        ProtocolArpAdjacency.__init__(self)
        ProtocolArpEvent.__init__(self)
        ProtocolArpFault.__init__(self)

    def get_protocol_arp(
            self,
            pod_id,
            node_id,
            arp_domain_filter=None,
            instance_info=False,
            domain_info=False,
            adjacency_info=False,
            interface_info=False,
            fault_info=False,
            hfault_info=False,
            hfault_filter=None,
            event_info=False,
            event_filter=None
            ):
        info = {}

        if instance_info:
            info['instance'] = self.get_protocol_arp_instance(
                pod_id,
                node_id
            )

        if domain_info:
            info['domain'] = self.get_protocol_arp_domains(
                pod_id,
                node_id,
                arp_domain_filter=arp_domain_filter,
                adjacency_info=adjacency_info
            )

        if adjacency_info:
            info['adjacency'] = []
            for domain in info['domain']:
                info['adjacency'] = info['adjacency'] + domain['adjacency']

        if interface_info:
            info['interface'] = self.get_protocol_arp_domains_interface_summary(
                info['domain']
            )

        if fault_info:
            info['faultInst'] = self.get_protocol_arp_fault(
                pod_id,
                node_id
            )

        if hfault_info:
            all_faults = self.get_protocol_arp_fault_record(
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
            all_events = self.get_protocol_arp_event(
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
