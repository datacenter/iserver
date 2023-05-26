from lib.aci.intf.cloudsec.api import InterfaceCloudSecApi
from lib.aci.intf.cloudsec.info import InterfaceCloudSecInfo


class InterfaceCloudSec(InterfaceCloudSecApi, InterfaceCloudSecInfo):
    def __init__(self):
        InterfaceCloudSecApi.__init__(self)
        InterfaceCloudSecInfo.__init__(self)
