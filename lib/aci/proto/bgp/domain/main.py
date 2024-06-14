from lib.aci.proto.bgp.domain.api import ProtocolBgpDomainApi
from lib.aci.proto.bgp.domain.info import ProtocolBgpDomainInfo


class ProtocolBgpDomain(ProtocolBgpDomainApi, ProtocolBgpDomainInfo):
    def __init__(self):
        ProtocolBgpDomainApi.__init__(self)
        ProtocolBgpDomainInfo.__init__(self)
