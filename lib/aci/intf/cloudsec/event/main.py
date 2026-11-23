from lib.aci.intf.cloudsec.event.api import InterfaceCloudSecEventApi
from lib.aci.intf.cloudsec.event.info import InterfaceCloudSecEventInfo


class InterfaceCloudSecEvent(InterfaceCloudSecEventApi, InterfaceCloudSecEventInfo):
    def __init__(self):
        InterfaceCloudSecEventApi.__init__(self)
        InterfaceCloudSecEventInfo.__init__(self)
