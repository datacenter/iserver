from lib.aci.intf.vfc.fault.api import InterfaceVfcFaultApi
from lib.aci.intf.vfc.fault.info import InterfaceVfcFaultInfo


class InterfaceVfcFault(InterfaceVfcFaultApi, InterfaceVfcFaultInfo):
    def __init__(self):
        InterfaceVfcFaultApi.__init__(self)
        InterfaceVfcFaultInfo.__init__(self)
