from lib.aci.intf.management.fault.api import InterfaceManagementFaultApi
from lib.aci.intf.management.fault.info import InterfaceManagementFaultInfo


class InterfaceManagementFault(InterfaceManagementFaultApi, InterfaceManagementFaultInfo):
    def __init__(self):
        InterfaceManagementFaultApi.__init__(self)
        InterfaceManagementFaultInfo.__init__(self)
