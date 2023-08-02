from lib.aci.ap.audit.api import ApplicationProfileAuditApi
from lib.aci.ap.audit.info import ApplicationProfileAuditInfo


class ApplicationProfileAudit(ApplicationProfileAuditApi, ApplicationProfileAuditInfo):
    def __init__(self):
        ApplicationProfileAuditApi.__init__(self)
        ApplicationProfileAuditInfo.__init__(self)
