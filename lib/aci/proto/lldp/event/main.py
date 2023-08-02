from lib.aci.proto.lldp.event.api import ProtocolLldpEventApi
from lib.aci.proto.lldp.event.info import ProtocolLldpEventInfo


class ProtocolLldpEvent(ProtocolLldpEventApi, ProtocolLldpEventInfo):
    def __init__(self):
        ProtocolLldpEventApi.__init__(self)
        ProtocolLldpEventInfo.__init__(self)
