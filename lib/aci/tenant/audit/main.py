from lib.aci.tenant.audit.api import TenantAuditApi
from lib.aci.tenant.audit.info import TenantAuditInfo


class TenantAudit(TenantAuditApi, TenantAuditInfo):
    def __init__(self):
        TenantAuditApi.__init__(self)
        TenantAuditInfo.__init__(self)
