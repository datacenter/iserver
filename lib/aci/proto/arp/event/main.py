from lib.aci.proto.arp.event.api import ProtocolArpEventApi
from lib.aci.proto.arp.event.info import ProtocolArpEventInfo


class ProtocolArpEvent(ProtocolArpEventApi, ProtocolArpEventInfo):
    def __init__(self):
        ProtocolArpEventApi.__init__(self)
        ProtocolArpEventInfo.__init__(self)
