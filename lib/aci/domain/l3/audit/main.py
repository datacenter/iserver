from lib.aci.domain.l3.audit.api import DomainL3AuditApi
from lib.aci.domain.l3.audit.info import DomainL3AuditInfo


class DomainL3Audit(DomainL3AuditApi, DomainL3AuditInfo):
    def __init__(self):
        DomainL3AuditApi.__init__(self)
        DomainL3AuditInfo.__init__(self)
