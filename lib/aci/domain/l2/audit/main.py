from lib.aci.domain.l2.audit.api import DomainL2AuditApi
from lib.aci.domain.l2.audit.info import DomainL2AuditInfo


class DomainL2Audit(DomainL2AuditApi, DomainL2AuditInfo):
    def __init__(self):
        DomainL2AuditApi.__init__(self)
        DomainL2AuditInfo.__init__(self)
