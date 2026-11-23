from lib.aci.intf.management.audit.api import InterfaceMgmtAuditApi
from lib.aci.intf.management.audit.info import InterfaceMgmtAuditInfo


class InterfaceMgmtAudit(InterfaceMgmtAuditApi, InterfaceMgmtAuditInfo):
    def __init__(self):
        InterfaceMgmtAuditApi.__init__(self)
        InterfaceMgmtAuditInfo.__init__(self)
