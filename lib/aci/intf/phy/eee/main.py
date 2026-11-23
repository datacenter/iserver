from lib.aci.intf.phy.eee.api import InterfacePhyEeeApi
from lib.aci.intf.phy.eee.info import InterfacePhyEeeInfo


class InterfacePhyEee(InterfacePhyEeeApi, InterfacePhyEeeInfo):
    def __init__(self):
        InterfacePhyEeeApi.__init__(self)
        InterfacePhyEeeInfo.__init__(self)
