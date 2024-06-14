from lib.aci.intf.macsec.event.api import InterfaceMacSecEventApi
from lib.aci.intf.macsec.event.info import InterfaceMacSecEventInfo


class InterfaceMacSecEvent(InterfaceMacSecEventApi, InterfaceMacSecEventInfo):
    def __init__(self):
        InterfaceMacSecEventApi.__init__(self)
        InterfaceMacSecEventInfo.__init__(self)
