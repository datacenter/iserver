from lib.aci.proto.hsrp.fault.api import ProtocolHsrpFaultApi
from lib.aci.proto.hsrp.fault.info import ProtocolHsrpFaultInfo


class ProtocolHsrpFault(ProtocolHsrpFaultApi, ProtocolHsrpFaultInfo):
    def __init__(self):
        ProtocolHsrpFaultApi.__init__(self)
        ProtocolHsrpFaultInfo.__init__(self)
