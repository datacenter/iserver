from lib.aci.proto.ipv4.domain.api import ProtocolIpv4DomainApi
from lib.aci.proto.ipv4.domain.info import ProtocolIpv4DomainInfo


class ProtocolIpv4Domain(ProtocolIpv4DomainApi, ProtocolIpv4DomainInfo):
    def __init__(self):
        ProtocolIpv4DomainApi.__init__(self)
        ProtocolIpv4DomainInfo.__init__(self)
