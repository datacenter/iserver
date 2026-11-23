from lib.aci.intf.phy.fault.api import InterfacePhyFaultApi
from lib.aci.intf.phy.fault.info import InterfacePhyFaultInfo


class InterfacePhyFault(InterfacePhyFaultApi, InterfacePhyFaultInfo):
    def __init__(self):
        InterfacePhyFaultApi.__init__(self)
        InterfacePhyFaultInfo.__init__(self)
