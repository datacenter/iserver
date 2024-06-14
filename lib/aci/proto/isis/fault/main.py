from lib.aci.proto.isis.fault.api import ProtocolIsisFaultApi
from lib.aci.proto.isis.fault.info import ProtocolIsisFaultInfo


class ProtocolIsisFault(ProtocolIsisFaultApi, ProtocolIsisFaultInfo):
    def __init__(self):
        ProtocolIsisFaultApi.__init__(self)
        ProtocolIsisFaultInfo.__init__(self)
