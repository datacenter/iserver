from lib.aci.intf.fc.fault.api import InterfaceFcFaultApi
from lib.aci.intf.fc.fault.info import InterfaceFcFaultInfo


class InterfaceFcFault(InterfaceFcFaultApi, InterfaceFcFaultInfo):
    def __init__(self):
        InterfaceFcFaultApi.__init__(self)
        InterfaceFcFaultInfo.__init__(self)
