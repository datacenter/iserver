from lib.aci.intf.vfc.audit.api import InterfaceVfcAuditApi
from lib.aci.intf.vfc.audit.info import InterfaceVfcAuditInfo


class InterfaceVfcAudit(InterfaceVfcAuditApi, InterfaceVfcAuditInfo):
    def __init__(self):
        InterfaceVfcAuditApi.__init__(self)
        InterfaceVfcAuditInfo.__init__(self)
