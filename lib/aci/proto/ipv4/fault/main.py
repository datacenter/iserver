from lib.aci.proto.ipv4.fault.api import ProtocolIpv4FaultApi
from lib.aci.proto.ipv4.fault.info import ProtocolIpv4FaultInfo


class ProtocolIpv4Fault(ProtocolIpv4FaultApi, ProtocolIpv4FaultInfo):
    def __init__(self):
        ProtocolIpv4FaultApi.__init__(self)
        ProtocolIpv4FaultInfo.__init__(self)
