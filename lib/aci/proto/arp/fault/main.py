from lib.aci.proto.arp.fault.api import ProtocolArpFaultApi
from lib.aci.proto.arp.fault.info import ProtocolArpFaultInfo


class ProtocolArpFault(ProtocolArpFaultApi, ProtocolArpFaultInfo):
    def __init__(self):
        ProtocolArpFaultApi.__init__(self)
        ProtocolArpFaultInfo.__init__(self)
