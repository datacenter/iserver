from lib.aci.proto.hsrp.event.api import ProtocolHsrpEventApi
from lib.aci.proto.hsrp.event.info import ProtocolHsrpEventInfo


class ProtocolHsrpEvent(ProtocolHsrpEventApi, ProtocolHsrpEventInfo):
    def __init__(self):
        ProtocolHsrpEventApi.__init__(self)
        ProtocolHsrpEventInfo.__init__(self)
