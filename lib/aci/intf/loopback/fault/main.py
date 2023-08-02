from lib.aci.intf.loopback.fault.api import InterfaceLoopbackFaultApi
from lib.aci.intf.loopback.fault.info import InterfaceLoopbackFaultInfo


class InterfaceLoopbackFault(InterfaceLoopbackFaultApi, InterfaceLoopbackFaultInfo):
    def __init__(self):
        InterfaceLoopbackFaultApi.__init__(self)
        InterfaceLoopbackFaultInfo.__init__(self)
