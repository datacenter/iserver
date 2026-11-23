from lib.osp.tenant.api import OspTenantApi
from lib.osp.tenant.info import OspTenantInfo


class OspTenant(
        OspTenantApi,
        OspTenantInfo
        ):
    def __init__(self):
        OspTenantApi.__init__(self)
        OspTenantInfo.__init__(self)
