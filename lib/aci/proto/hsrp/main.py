from lib.aci.proto.hsrp.instance.main import ProtocolHsrpInstance
from lib.aci.proto.hsrp.domain.main import ProtocolHsrpDomain
from lib.aci.proto.hsrp.interface.main import ProtocolHsrpInterface


class ProtocolHsrp(ProtocolHsrpInstance, ProtocolHsrpDomain, ProtocolHsrpInterface):
    def __init__(self):
        ProtocolHsrpInstance.__init__(self)
        ProtocolHsrpDomain.__init__(self)
        ProtocolHsrpInterface.__init__(self)

    def get_protocol_hsrp(self, pod_id, node_id, hsrp_filter=None):
        info = {}

        info['instance'] = self.get_protocol_hsrp_instance(
            pod_id=pod_id,
            node_id=node_id
        )

        if info['instance'] is None:
            return None

        info['domains'] = self.get_protocol_hsrp_domains(
            pod_id=pod_id,
            node_id=node_id,
            hsrp_domain_filter=hsrp_filter
        )

        info['interfaces'] = self.get_protocol_hsrp_interfaces(
            pod_id=pod_id,
            node_id=node_id,
            hsrp_interface_filter=hsrp_filter
        )

        info['domains'] = self.add_protocol_hsrp_domain_interface_info(
            info['domains'],
            info['interfaces']
        )

        return info
