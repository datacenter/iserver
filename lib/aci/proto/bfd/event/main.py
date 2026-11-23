from lib.aci.proto.bfd.event.api import ProtocolBfdEventApi
from lib.aci.proto.bfd.event.info import ProtocolBfdEventInfo


class ProtocolBfdEvent(ProtocolBfdEventApi, ProtocolBfdEventInfo):
    def __init__(self):
        ProtocolBfdEventApi.__init__(self)
        ProtocolBfdEventInfo.__init__(self)
