from lib.aci.proto.nd.domain.api import ProtocolNdDomainApi
from lib.aci.proto.nd.domain.info import ProtocolNdDomainInfo


class ProtocolNdDomain(ProtocolNdDomainApi, ProtocolNdDomainInfo):
    def __init__(self):
        ProtocolNdDomainApi.__init__(self)
        ProtocolNdDomainInfo.__init__(self)
