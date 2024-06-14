from lib.aci.ap.api import ApplicationProfileApi
from lib.aci.ap.info import ApplicationProfileInfo
from lib.aci.ap.audit.main import ApplicationProfileAudit
from lib.aci.ap.event.main import ApplicationProfileEvent
from lib.aci.ap.fault.main import ApplicationProfileFault
from lib.aci.ap.node.main import ApplicationProfileNode


class ApplicationProfile(
        ApplicationProfileApi,
        ApplicationProfileInfo,
        ApplicationProfileAudit,
        ApplicationProfileEvent,
        ApplicationProfileFault,
        ApplicationProfileNode
        ):
    def __init__(self):
        ApplicationProfileApi.__init__(self)
        ApplicationProfileInfo.__init__(self)
        ApplicationProfileAudit.__init__(self)
        ApplicationProfileEvent.__init__(self)
        ApplicationProfileFault.__init__(self)
        ApplicationProfileNode.__init__(self)
