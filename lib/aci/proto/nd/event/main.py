from lib.aci.proto.nd.event.api import ProtocolNdEventApi
from lib.aci.proto.nd.event.info import ProtocolNdEventInfo


class ProtocolNdEvent(ProtocolNdEventApi, ProtocolNdEventInfo):
    def __init__(self):
        ProtocolNdEventApi.__init__(self)
        ProtocolNdEventInfo.__init__(self)
