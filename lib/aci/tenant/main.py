from lib.aci.tenant.api import TenantApi
from lib.aci.tenant.info import TenantInfo


class Tenant(TenantApi, TenantInfo):
    def __init__(self):
        TenantApi.__init__(self)
        TenantInfo.__init__(self)
