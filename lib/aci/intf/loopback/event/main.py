from lib.aci.intf.loopback.event.api import InterfaceLoopbackEventApi
from lib.aci.intf.loopback.event.info import InterfaceLoopbackEventInfo


class InterfaceLoopbackEvent(InterfaceLoopbackEventApi, InterfaceLoopbackEventInfo):
    def __init__(self):
        InterfaceLoopbackEventApi.__init__(self)
        InterfaceLoopbackEventInfo.__init__(self)
