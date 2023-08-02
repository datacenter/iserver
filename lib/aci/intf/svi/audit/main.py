from lib.aci.intf.svi.audit.api import InterfaceSviAuditApi
from lib.aci.intf.svi.audit.info import InterfaceSviAuditInfo


class InterfaceSviAudit(InterfaceSviAuditApi, InterfaceSviAuditInfo):
    def __init__(self):
        InterfaceSviAuditApi.__init__(self)
        InterfaceSviAuditInfo.__init__(self)
