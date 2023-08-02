from lib.aci.bd.audit.api import BridgeDomainAuditApi
from lib.aci.bd.audit.info import BridgeDomainAuditInfo


class BridgeDomainAudit(BridgeDomainAuditApi, BridgeDomainAuditInfo):
    def __init__(self):
        BridgeDomainAuditApi.__init__(self)
        BridgeDomainAuditInfo.__init__(self)
