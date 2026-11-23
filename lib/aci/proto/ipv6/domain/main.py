from lib.aci.proto.ipv6.domain.api import ProtocolIpv6DomainApi
from lib.aci.proto.ipv6.domain.info import ProtocolIpv6DomainInfo


class ProtocolIpv6Domain(ProtocolIpv6DomainApi, ProtocolIpv6DomainInfo):
    def __init__(self):
        ProtocolIpv6DomainApi.__init__(self)
        ProtocolIpv6DomainInfo.__init__(self)
