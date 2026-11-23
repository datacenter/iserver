from lib.aci.intf.fcpc.fault.api import InterfaceFcPcFaultApi
from lib.aci.intf.fcpc.fault.info import InterfaceFcPcFaultInfo


class InterfaceFcPcFault(InterfaceFcPcFaultApi, InterfaceFcPcFaultInfo):
    def __init__(self):
        InterfaceFcPcFaultApi.__init__(self)
        InterfaceFcPcFaultInfo.__init__(self)
