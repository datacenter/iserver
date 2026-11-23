from lib.aci.intf.vfc.api import InterfaceVfcApi
from lib.aci.intf.vfc.info import InterfaceVfcInfo
from lib.aci.intf.vfc.event.main import InterfaceVfcEvent
from lib.aci.intf.vfc.fault.main import InterfaceVfcFault


class InterfaceVfc(
        InterfaceVfcApi,
        InterfaceVfcInfo,
        InterfaceVfcEvent,
        InterfaceVfcFault
        ):
    def __init__(self):
        InterfaceVfcApi.__init__(self)
        InterfaceVfcInfo.__init__(self)
        InterfaceVfcEvent.__init__(self)
        InterfaceVfcFault.__init__(self)
