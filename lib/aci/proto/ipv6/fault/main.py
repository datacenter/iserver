from lib.aci.proto.ipv6.fault.api import ProtocolIpv6FaultApi
from lib.aci.proto.ipv6.fault.info import ProtocolIpv6FaultInfo


class ProtocolIpv6Fault(ProtocolIpv6FaultApi, ProtocolIpv6FaultInfo):
    def __init__(self):
        ProtocolIpv6FaultApi.__init__(self)
        ProtocolIpv6FaultInfo.__init__(self)
