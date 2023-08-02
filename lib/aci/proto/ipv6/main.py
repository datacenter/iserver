from lib.aci.proto.ipv6.instance.main import ProtocolIpv6Instance
from lib.aci.proto.ipv6.domain.main import ProtocolIpv6Domain
from lib.aci.proto.ipv6.route.main import ProtocolIpv6Route
from lib.aci.proto.ipv6.event.main import ProtocolIpv6Event
from lib.aci.proto.ipv6.fault.main import ProtocolIpv6Fault


class ProtocolIpv6(
        ProtocolIpv6Instance,
        ProtocolIpv6Domain,
        ProtocolIpv6Route,
        ProtocolIpv6Event,
        ProtocolIpv6Fault
        ):
    def __init__(self):
        ProtocolIpv6Instance.__init__(self)
        ProtocolIpv6Domain.__init__(self)
        ProtocolIpv6Route.__init__(self)
        ProtocolIpv6Event.__init__(self)
        ProtocolIpv6Fault.__init__(self)

    def get_protocol_ipv6(
            self,
            pod_id,
            node_id,
            ipv6_filter=None,
            instance_info=False,
            domain_info=False,
            route_info=False,
            fault_info=False,
            hfault_info=False,
            hfault_filter=None,
            event_info=False,
            event_filter=None
            ):
        info = {}

        if instance_info:
            info['instance'] = self.get_protocol_ipv6_instance(
                pod_id,
                node_id
            )

        if domain_info:
            info['domain'] = self.get_protocol_ipv6_domains(
                pod_id,
                node_id,
                ipv6_domain_filter=ipv6_filter
            )
            if instance_info:
                info['instance']['domains'] = len(info['domain'])

        if route_info:
            info['route'] = []
            for domain in info['domain']:
                domain_route = self.get_protocol_ipv6_routes(
                    pod_id,
                    node_id,
                    domain['name'],
                    route_filter=ipv6_filter
                )

                info['route'] = info['route'] + domain_route
                domain['summary'] = self.get_protocol_ipv6_routes_summary(
                    domain_route
                )

            if instance_info:
                info['instance']['routes'] = len(info['route'])
                info['instance']['summary'] = self.get_protocol_ipv6_routes_summary(
                    info['route']
                )

        # if domain_info:
        #     info['domain'] = self.get_protocol_arp_domains(
        #         pod_id,
        #         node_id,
        #         arp_domain_filter=arp_domain_filter,
        #         adjacency_info=adjacency_info
        #     )

        # if adjacency_info:
        #     info['adjacency'] = []
        #     for domain in info['domain']:
        #         info['adjacency'] = info['adjacency'] + domain['adjacency']

        # if interface_info:
        #     info['interface'] = self.get_protocol_arp_domains_interface_summary(
        #         info['domain']
        #     )

        if fault_info:
            info['faultInst'] = self.get_protocol_ipv6_fault(
                pod_id,
                node_id
            )

        if hfault_info:
            all_faults = self.get_protocol_ipv6_fault_record(
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
            all_events = self.get_protocol_ipv6_event(
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
