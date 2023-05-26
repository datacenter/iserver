from lib.aci.intf.phy.cap.api import InterfacePhyCapApi
from lib.aci.intf.phy.cap.info import InterfacePhyCapInfo


class InterfacePhyCap(InterfacePhyCapApi, InterfacePhyCapInfo):
    def __init__(self):
        InterfacePhyCapApi.__init__(self)
        InterfacePhyCapInfo.__init__(self)
