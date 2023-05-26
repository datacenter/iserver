from lib.aci.proto.isis.domain.api import ProtocolIsisDomainApi
from lib.aci.proto.isis.domain.info import ProtocolIsisDomainInfo


class ProtocolIsisDomain(ProtocolIsisDomainApi, ProtocolIsisDomainInfo):
    def __init__(self):
        ProtocolIsisDomainApi.__init__(self)
        ProtocolIsisDomainInfo.__init__(self)
