from lib.aci.proto.ipv6.route.api import ProtocolIpv6RouteApi
from lib.aci.proto.ipv6.route.info import ProtocolIpv6RouteInfo


class ProtocolIpv6Route(ProtocolIpv6RouteApi, ProtocolIpv6RouteInfo):
    def __init__(self):
        ProtocolIpv6RouteApi.__init__(self)
        ProtocolIpv6RouteInfo.__init__(self)
