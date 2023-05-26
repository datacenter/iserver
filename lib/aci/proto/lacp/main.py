from lib.aci.proto.lacp.instance.main import ProtocolLacpInstance
from lib.aci.proto.lacp.interface.main import ProtocolLacpInterface


class ProtocolLacp(ProtocolLacpInstance, ProtocolLacpInterface):
    def __init__(self):
        ProtocolLacpInstance.__init__(self)
        ProtocolLacpInterface.__init__(self)

    def get_protocol_lacp(self, pod_id, node_id):
        info = {}

        info['instance'] = self.get_protocol_lacp_instance(
            pod_id,
            node_id
        )

        info['interfaces'] = self.get_interface_port_channel(
            pod_id,
            node_id
        )

        lacp_interfaces = self.get_interface_lacp(
            pod_id,
            node_id,
            adjacency_info=True
        )

        for interface in info['interfaces']:
            interface['lacp'] = []
            for lacp_interface in lacp_interfaces:
                if lacp_interface['id'] in interface['state']['portId']:
                    interface['lacp'].append(
                        lacp_interface
                    )

        info['instance']['summary'] = self.get_interface_port_channel_summary(
            pod_id,
            node_id
        )
        for key in info['instance']['summary']['__Output']:
            info['instance']['__Output']['summary.%s' % (key)] = info['instance']['summary']['__Output'][key]

        return info
