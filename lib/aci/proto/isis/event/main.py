from lib.aci.proto.isis.event.api import ProtocolIsisEventApi
from lib.aci.proto.isis.event.info import ProtocolIsisEventInfo


class ProtocolIsisEvent(ProtocolIsisEventApi, ProtocolIsisEventInfo):
    def __init__(self):
        ProtocolIsisEventApi.__init__(self)
        ProtocolIsisEventInfo.__init__(self)
