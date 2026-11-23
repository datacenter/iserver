from lib.aci.l2out.audit.api import L2OutAuditApi
from lib.aci.l2out.audit.info import L2OutAuditInfo


class L2OutAudit(L2OutAuditApi, L2OutAuditInfo):
    def __init__(self):
        L2OutAuditApi.__init__(self)
        L2OutAuditInfo.__init__(self)
