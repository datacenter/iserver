from lib.aci.intf.loopback.api import InterfaceLoopbackApi
from lib.aci.intf.loopback.info import InterfaceLoopbackInfo


class InterfaceLoopback(InterfaceLoopbackApi, InterfaceLoopbackInfo):
    def __init__(self):
        InterfaceLoopbackApi.__init__(self)
        InterfaceLoopbackInfo.__init__(self)
