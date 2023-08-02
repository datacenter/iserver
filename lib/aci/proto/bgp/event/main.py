from lib.aci.proto.bgp.event.api import ProtocolBgpEventApi
from lib.aci.proto.bgp.event.info import ProtocolBgpEventInfo


class ProtocolBgpEvent(ProtocolBgpEventApi, ProtocolBgpEventInfo):
    def __init__(self):
        ProtocolBgpEventApi.__init__(self)
        ProtocolBgpEventInfo.__init__(self)
