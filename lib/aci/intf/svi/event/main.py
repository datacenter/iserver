from lib.aci.intf.svi.event.api import InterfaceSviEventApi
from lib.aci.intf.svi.event.info import InterfaceSviEventInfo


class InterfaceSviEvent(InterfaceSviEventApi, InterfaceSviEventInfo):
    def __init__(self):
        InterfaceSviEventApi.__init__(self)
        InterfaceSviEventInfo.__init__(self)
