from lib.aci.proto.ipv6.event.api import ProtocolIpv6EventApi
from lib.aci.proto.ipv6.event.info import ProtocolIpv6EventInfo


class ProtocolIpv6Event(ProtocolIpv6EventApi, ProtocolIpv6EventInfo):
    def __init__(self):
        ProtocolIpv6EventApi.__init__(self)
        ProtocolIpv6EventInfo.__init__(self)
