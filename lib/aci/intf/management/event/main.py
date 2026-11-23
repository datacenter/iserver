from lib.aci.intf.management.event.api import InterfaceManagementEventApi
from lib.aci.intf.management.event.info import InterfaceManagementEventInfo


class InterfaceManagementEvent(InterfaceManagementEventApi, InterfaceManagementEventInfo):
    def __init__(self):
        InterfaceManagementEventApi.__init__(self)
        InterfaceManagementEventInfo.__init__(self)
