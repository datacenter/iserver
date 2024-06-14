from lib.aci.proto.cdp.event.api import ProtocolCdpEventApi
from lib.aci.proto.cdp.event.info import ProtocolCdpEventInfo


class ProtocolCdpEvent(ProtocolCdpEventApi, ProtocolCdpEventInfo):
    def __init__(self):
        ProtocolCdpEventApi.__init__(self)
        ProtocolCdpEventInfo.__init__(self)
