from lib.aci.proto.cdp.instance.main import ProtocolCdpInstance
from lib.aci.proto.cdp.interface.main import ProtocolCdpInterface
from lib.aci.proto.cdp.neighbor.main import ProtocolCdpNeighbor


class ProtocolCdp(ProtocolCdpInstance, ProtocolCdpNeighbor, ProtocolCdpInterface):
    def __init__(self):
        ProtocolCdpInstance.__init__(self)
        ProtocolCdpInterface.__init__(self)
        ProtocolCdpNeighbor.__init__(self)

    def get_protocol_cdp(self, pod_id, node_id, cdp_filter=None, include_instance=True, include_neighbors=True, include_interfaces=True):
        info = {}

        if include_instance:
            info['instance'] = self.get_protocol_cdp_instance(
                pod_id=pod_id,
                node_id=node_id
            )

        if include_neighbors:
            info['neighbors'] = self.get_protocol_cdp_neighbors(
                pod_id,
                node_id,
                cdp_neighbor_filter=cdp_filter
            )

            if include_instance:
                info['instance']['neighborCount'] = len(info['neighbors'])

        if include_interfaces:
            info['interfaces'] = self.get_protocol_cdp_interfaces(
                pod_id,
                node_id,
                cdp_interface_filter=cdp_filter
            )

            if include_neighbors:
                info['interfaces'] = self.add_protocol_cdp_interface_neighbor_info(
                    info['interfaces'],
                    info['neighbors'],
                    remove_no_neighbors=True
                )

            if include_instance:
                info['instance']['activeInterfaceCount'] = self.get_cdp_active_interface_count(
                    info['interfaces']
                )

        self.log.apic_mo(
            'cdp.info.%s.%s' % (
                pod_id,
                node_id
            ),
            info
        )

        return info
