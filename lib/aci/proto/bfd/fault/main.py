from lib.aci.proto.bfd.fault.api import ProtocolBfdFaultApi
from lib.aci.proto.bfd.fault.info import ProtocolBfdFaultInfo


class ProtocolBfdFault(ProtocolBfdFaultApi, ProtocolBfdFaultInfo):
    def __init__(self):
        ProtocolBfdFaultApi.__init__(self)
        ProtocolBfdFaultInfo.__init__(self)
