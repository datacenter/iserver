from lib.aci.proto.lacp.event.api import ProtocolLacpEventApi
from lib.aci.proto.lacp.event.info import ProtocolLacpEventInfo


class ProtocolLacpEvent(ProtocolLacpEventApi, ProtocolLacpEventInfo):
    def __init__(self):
        ProtocolLacpEventApi.__init__(self)
        ProtocolLacpEventInfo.__init__(self)
