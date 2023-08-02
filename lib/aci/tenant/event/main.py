from lib.aci.tenant.event.api import TenantEventApi
from lib.aci.tenant.event.info import TenantEventInfo


class TenantEvent(TenantEventApi, TenantEventInfo):
    def __init__(self):
        TenantEventApi.__init__(self)
        TenantEventInfo.__init__(self)
