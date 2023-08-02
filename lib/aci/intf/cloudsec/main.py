from lib.aci.intf.cloudsec.api import InterfaceCloudSecApi
from lib.aci.intf.cloudsec.info import InterfaceCloudSecInfo
from lib.aci.intf.cloudsec.audit.main import InterfaceCloudSecAudit
from lib.aci.intf.cloudsec.event.main import InterfaceCloudSecEvent
from lib.aci.intf.cloudsec.fault.main import InterfaceCloudSecFault


class InterfaceCloudSec(
        InterfaceCloudSecApi,
        InterfaceCloudSecInfo,
        InterfaceCloudSecAudit,
        InterfaceCloudSecEvent,
        InterfaceCloudSecFault
        ):
    def __init__(self):
        InterfaceCloudSecApi.__init__(self)
        InterfaceCloudSecInfo.__init__(self)
        InterfaceCloudSecAudit.__init__(self)
        InterfaceCloudSecEvent.__init__(self)
        InterfaceCloudSecFault.__init__(self)
