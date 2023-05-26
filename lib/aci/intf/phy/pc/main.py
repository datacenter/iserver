from lib.aci.intf.phy.pc.api import InterfacePhyPcApi
from lib.aci.intf.phy.pc.info import InterfacePhyPcInfo


class InterfacePhyPc(InterfacePhyPcApi, InterfacePhyPcInfo):
    def __init__(self):
        InterfacePhyPcApi.__init__(self)
        InterfacePhyPcInfo.__init__(self)
