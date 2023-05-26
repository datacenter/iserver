from lib.aci.proto.ipv6.domain.main import ProtocolIpv6Domain
from lib.aci.proto.ipv6.route.main import ProtocolIpv6Route


class ProtocolIpv6(ProtocolIpv6Domain, ProtocolIpv6Route):
    def __init__(self):
        ProtocolIpv6Domain.__init__(self)
        ProtocolIpv6Route.__init__(self)
