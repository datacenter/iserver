from lib.aci.tenant.api import TenantApi
from lib.aci.tenant.info import TenantInfo
from lib.aci.tenant.audit.main import TenantAudit
from lib.aci.tenant.event.main import TenantEvent
from lib.aci.tenant.fault.main import TenantFault


class Tenant(
        TenantApi,
        TenantInfo,
        TenantAudit,
        TenantEvent,
        TenantFault
        ):
    def __init__(self):
        TenantApi.__init__(self)
        TenantInfo.__init__(self)
        TenantAudit.__init__(self)
        TenantEvent.__init__(self)
        TenantFault.__init__(self)
