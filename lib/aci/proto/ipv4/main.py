from lib.aci.proto.ipv4.domain.main import ProtocolIpv4Domain
from lib.aci.proto.ipv4.route.main import ProtocolIpv4Route


class ProtocolIpv4(ProtocolIpv4Domain, ProtocolIpv4Route):
    def __init__(self):
        ProtocolIpv4Domain.__init__(self)
        ProtocolIpv4Route.__init__(self)
