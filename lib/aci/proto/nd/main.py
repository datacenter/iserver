from lib.aci.proto.nd.instance.main import ProtocolNdInstance
from lib.aci.proto.nd.domain.main import ProtocolNdDomain
from lib.aci.proto.nd.interface.main import ProtocolNdInterface
from lib.aci.proto.nd.neighbor.main import ProtocolNdNeighbor


class ProtocolNd(ProtocolNdInstance, ProtocolNdDomain, ProtocolNdInterface, ProtocolNdNeighbor):
    def __init__(self):
        ProtocolNdInstance.__init__(self)
        ProtocolNdDomain.__init__(self)
        ProtocolNdInterface.__init__(self)
        ProtocolNdNeighbor.__init__(self)

    def get_protocol_nd(self, pod_id, node_id):
        info = {}

        info['instance'] = self.get_protocol_nd_instance_info(
            pod_id=pod_id,
            node_id=node_id
        )

        info['domains'] = self.get_protocol_nd_domain_info(
            pod_id,
            node_id
        )

        info['neighbors'] = self.get_protocol_nd_neighbors_info(
            pod_id,
            node_id
        )

        info['domains'] = self.add_protocol_nd_domain_neighbor_info(
            info['domains'],
            info['neighbors']
        )

        info['interfaces'] = self.get_protocol_nd_interfaces_info(
            pod_id,
            node_id
        )

        info['domains'] = self.add_protocol_nd_domain_interface_info(
            info['domains'],
            info['interfaces']
        )

        info['interfaces'] = self.add_protocol_nd_interface_neighbor_info(
            info['interfaces'],
            info['neighbors'],
            remove_no_neighbors=True
        )

        info['instance']['neighborCount'] = len(info['neighbors'])

        info['instance']['activeInterfaceCount'] = self.get_nd_active_interface_count(
            info['interfaces']
        )

        return info
