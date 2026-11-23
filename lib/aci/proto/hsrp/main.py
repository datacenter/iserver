from lib.aci.proto.hsrp.instance.main import ProtocolHsrpInstance
from lib.aci.proto.hsrp.domain.main import ProtocolHsrpDomain
from lib.aci.proto.hsrp.interface.main import ProtocolHsrpInterface
from lib.aci.proto.hsrp.event.main import ProtocolHsrpEvent
from lib.aci.proto.hsrp.fault.main import ProtocolHsrpFault


class ProtocolHsrp(
        ProtocolHsrpInstance,
        ProtocolHsrpDomain,
        ProtocolHsrpInterface,
        ProtocolHsrpEvent,
        ProtocolHsrpFault
        ):
    def __init__(self):
        ProtocolHsrpInstance.__init__(self)
        ProtocolHsrpDomain.__init__(self)
        ProtocolHsrpInterface.__init__(self)
        ProtocolHsrpEvent.__init__(self)
        ProtocolHsrpFault.__init__(self)

    def get_protocol_hsrp(
            self,
            pod_id,
            node_id,
            hsrp_filter=None,
            instance_info=False,
            domain_info=False,
            interface_info=False,
            fault_info=False,
            hfault_info=False,
            hfault_filter=None,
            event_info=False,
            event_filter=None
            ):
        info = {}

        if instance_info:
            info['instance'] = self.get_protocol_hsrp_instance(
                pod_id=pod_id,
                node_id=node_id
            )

        if domain_info:
            info['domains'] = self.get_protocol_hsrp_domains(
                pod_id=pod_id,
                node_id=node_id,
                hsrp_domain_filter=hsrp_filter
            )

        if interface_info:
            info['interfaces'] = self.get_protocol_hsrp_interfaces(
                pod_id=pod_id,
                node_id=node_id,
                hsrp_interface_filter=hsrp_filter
            )

            if domain_info:
                info['domains'] = self.add_protocol_hsrp_domain_interface_info(
                    info['domains'],
                    info['interfaces']
                )

        if fault_info:
            info['faultInst'] = self.get_protocol_hsrp_fault(
                pod_id,
                node_id
            )

        if hfault_info:
            all_faults = self.get_protocol_hsrp_fault_record(
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
            all_events = self.get_protocol_hsrp_event(
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
