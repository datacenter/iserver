from lib.aci.proto.ipv4.route.api import ProtocolIpv4RouteApi
from lib.aci.proto.ipv4.route.info import ProtocolIpv4RouteInfo


class ProtocolIpv4Route(ProtocolIpv4RouteApi, ProtocolIpv4RouteInfo):
    def __init__(self):
        ProtocolIpv4RouteApi.__init__(self)
        ProtocolIpv4RouteInfo.__init__(self)
