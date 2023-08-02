from lib.aci.intf.cloudsec.fault.api import InterfaceCloudSecFaultApi
from lib.aci.intf.cloudsec.fault.info import InterfaceCloudSecFaultInfo


class InterfaceCloudSecFault(InterfaceCloudSecFaultApi, InterfaceCloudSecFaultInfo):
    def __init__(self):
        InterfaceCloudSecFaultApi.__init__(self)
        InterfaceCloudSecFaultInfo.__init__(self)
