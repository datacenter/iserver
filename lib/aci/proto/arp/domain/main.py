from lib.aci.proto.arp.domain.api import ProtocolArpDomainApi
from lib.aci.proto.arp.domain.info import ProtocolArpDomainInfo


class ProtocolArpDomain(ProtocolArpDomainApi, ProtocolArpDomainInfo):
    def __init__(self):
        ProtocolArpDomainApi.__init__(self)
        ProtocolArpDomainInfo.__init__(self)
