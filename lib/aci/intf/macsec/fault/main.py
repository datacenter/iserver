from lib.aci.intf.macsec.fault.api import InterfaceMacSecFaultApi
from lib.aci.intf.macsec.fault.info import InterfaceMacSecFaultInfo


class InterfaceMacSecFault(InterfaceMacSecFaultApi, InterfaceMacSecFaultInfo):
    def __init__(self):
        InterfaceMacSecFaultApi.__init__(self)
        InterfaceMacSecFaultInfo.__init__(self)
