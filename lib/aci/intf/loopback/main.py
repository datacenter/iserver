from lib.aci.intf.loopback.api import InterfaceLoopbackApi
from lib.aci.intf.loopback.info import InterfaceLoopbackInfo
from lib.aci.intf.loopback.audit.main import InterfaceLoopbackAudit
from lib.aci.intf.loopback.event.main import InterfaceLoopbackEvent
from lib.aci.intf.loopback.fault.main import InterfaceLoopbackFault


class InterfaceLoopback(
        InterfaceLoopbackApi,
        InterfaceLoopbackInfo,
        InterfaceLoopbackAudit,
        InterfaceLoopbackEvent,
        InterfaceLoopbackFault
        ):
    def __init__(self):
        InterfaceLoopbackApi.__init__(self)
        InterfaceLoopbackInfo.__init__(self)
        InterfaceLoopbackAudit.__init__(self)
        InterfaceLoopbackEvent.__init__(self)
        InterfaceLoopbackFault.__init__(self)
