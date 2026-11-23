from lib.aci.domain.vmm.audit.api import DomainVmmAuditApi
from lib.aci.domain.vmm.audit.info import DomainVmmAuditInfo


class DomainVmmAudit(DomainVmmAuditApi, DomainVmmAuditInfo):
    def __init__(self):
        DomainVmmAuditApi.__init__(self)
        DomainVmmAuditInfo.__init__(self)
