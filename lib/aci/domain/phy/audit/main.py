from lib.aci.domain.phy.audit.api import DomainPhyAuditApi
from lib.aci.domain.phy.audit.info import DomainPhyAuditInfo


class DomainPhyAudit(DomainPhyAuditApi, DomainPhyAuditInfo):
    def __init__(self):
        DomainPhyAuditApi.__init__(self)
        DomainPhyAuditInfo.__init__(self)
