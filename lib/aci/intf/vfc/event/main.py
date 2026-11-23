from lib.aci.intf.vfc.event.api import InterfaceVfcEventApi
from lib.aci.intf.vfc.event.info import InterfaceVfcEventInfo


class InterfaceVfcEvent(InterfaceVfcEventApi, InterfaceVfcEventInfo):
    def __init__(self):
        InterfaceVfcEventApi.__init__(self)
        InterfaceVfcEventInfo.__init__(self)
