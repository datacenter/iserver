from lib.aci.proto.ipv4.event.api import ProtocolIpv4EventApi
from lib.aci.proto.ipv4.event.info import ProtocolIpv4EventInfo


class ProtocolIpv4Event(ProtocolIpv4EventApi, ProtocolIpv4EventInfo):
    def __init__(self):
        ProtocolIpv4EventApi.__init__(self)
        ProtocolIpv4EventInfo.__init__(self)
