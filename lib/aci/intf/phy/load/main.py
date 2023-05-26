from lib.aci.intf.phy.load.api import InterfacePhyLoadApi
from lib.aci.intf.phy.load.info import InterfacePhyLoadInfo


class InterfacePhyLoad(InterfacePhyLoadApi, InterfacePhyLoadInfo):
    def __init__(self):
        InterfacePhyLoadApi.__init__(self)
        InterfacePhyLoadInfo.__init__(self)
