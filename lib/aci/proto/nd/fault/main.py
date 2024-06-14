from lib.aci.proto.nd.fault.api import ProtocolNdFaultApi
from lib.aci.proto.nd.fault.info import ProtocolNdFaultInfo


class ProtocolNdFault(ProtocolNdFaultApi, ProtocolNdFaultInfo):
    def __init__(self):
        ProtocolNdFaultApi.__init__(self)
        ProtocolNdFaultInfo.__init__(self)
