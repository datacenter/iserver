from lib.aci.proto.bgp.fault.api import ProtocolBgpFaultApi
from lib.aci.proto.bgp.fault.info import ProtocolBgpFaultInfo


class ProtocolBgpFault(ProtocolBgpFaultApi, ProtocolBgpFaultInfo):
    def __init__(self):
        ProtocolBgpFaultApi.__init__(self)
        ProtocolBgpFaultInfo.__init__(self)
