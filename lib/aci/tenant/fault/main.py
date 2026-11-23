from lib.aci.tenant.fault.api import TenantFaultApi
from lib.aci.tenant.fault.info import TenantFaultInfo


class TenantFault(TenantFaultApi, TenantFaultInfo):
    def __init__(self):
        TenantFaultApi.__init__(self)
        TenantFaultInfo.__init__(self)
