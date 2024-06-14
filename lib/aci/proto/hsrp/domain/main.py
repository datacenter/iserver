from lib.aci.proto.hsrp.domain.api import ProtocolHsrpDomainApi
from lib.aci.proto.hsrp.domain.info import ProtocolHsrpDomainInfo


class ProtocolHsrpDomain(ProtocolHsrpDomainApi, ProtocolHsrpDomainInfo):
    def __init__(self):
        ProtocolHsrpDomainApi.__init__(self)
        ProtocolHsrpDomainInfo.__init__(self)
