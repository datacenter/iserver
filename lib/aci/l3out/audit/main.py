from lib.aci.l3out.audit.api import L3OutAuditApi
from lib.aci.l3out.audit.info import L3OutAuditInfo


class L3OutAudit(L3OutAuditApi, L3OutAuditInfo):
    def __init__(self):
        L3OutAuditApi.__init__(self)
        L3OutAuditInfo.__init__(self)
