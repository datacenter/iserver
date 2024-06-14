from lib.aci.intf.phy.event.api import InterfacePhyEventApi
from lib.aci.intf.phy.event.info import InterfacePhyEventInfo


class InterfacePhyEvent(InterfacePhyEventApi, InterfacePhyEventInfo):
    def __init__(self):
        InterfacePhyEventApi.__init__(self)
        InterfacePhyEventInfo.__init__(self)
