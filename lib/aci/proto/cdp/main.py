from lib.aci.proto.cdp.instance.main import ProtocolCdpInstance
from lib.aci.proto.cdp.interface.main import ProtocolCdpInterface
from lib.aci.proto.cdp.neighbor.main import ProtocolCdpNeighbor
from lib.aci.proto.cdp.event.main import ProtocolCdpEvent


class ProtocolCdp(
        ProtocolCdpInstance,
        ProtocolCdpNeighbor,
        ProtocolCdpInterface,
        ProtocolCdpEvent
        ):
    def __init__(self):
        ProtocolCdpInstance.__init__(self)
        ProtocolCdpInterface.__init__(self)
        ProtocolCdpNeighbor.__init__(self)
        ProtocolCdpEvent.__init__(self)

    def get_protocol_cdp(
            self,
            pod_id,
            node_id,
            cdp_filter=None,
            instance_info=False,
            nei_info=False,
            interface_info=False,
            event_info=False,
            event_filter=None
            ):
        info = {}

        if instance_info:
            info['instance'] = self.get_protocol_cdp_instance(
                pod_id=pod_id,
                node_id=node_id
            )

        if nei_info:
            info['neighbors'] = self.get_protocol_cdp_neighbors(
                pod_id,
                node_id,
                cdp_neighbor_filter=cdp_filter
            )

            if instance_info:
                info['instance']['neighborCount'] = len(info['neighbors'])

        if interface_info:
            info['interfaces'] = self.get_protocol_cdp_interfaces(
                pod_id,
                node_id,
                cdp_interface_filter=cdp_filter
            )

            if nei_info:
                info['interfaces'] = self.add_protocol_cdp_interface_neighbor_info(
                    info['interfaces'],
                    info['neighbors'],
                    remove_no_neighbors=True
                )

            if instance_info:
                info['instance']['activeInterfaceCount'] = self.get_cdp_active_interface_count(
                    info['interfaces']
                )

        if event_info:
            all_events = self.get_protocol_cdp_event(
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

        self.log.apic_mo(
            'cdp.info.%s.%s' % (
                pod_id,
                node_id
            ),
            info
        )

        return info
