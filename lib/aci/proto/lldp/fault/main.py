from lib.aci.proto.lldp.fault.api import ProtocolLldpFaultApi
from lib.aci.proto.lldp.fault.info import ProtocolLldpFaultInfo


class ProtocolLldpFault(ProtocolLldpFaultApi, ProtocolLldpFaultInfo):
    def __init__(self):
        ProtocolLldpFaultApi.__init__(self)
        ProtocolLldpFaultInfo.__init__(self)
