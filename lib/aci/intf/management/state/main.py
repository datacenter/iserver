from lib.aci.intf.management.state.api import InterfaceManagementStateApi
from lib.aci.intf.management.state.info import InterfaceManagementStateInfo


class InterfaceManagementState(InterfaceManagementStateApi, InterfaceManagementStateInfo):
    def __init__(self):
        InterfaceManagementStateApi.__init__(self)
        InterfaceManagementStateInfo.__init__(self)
