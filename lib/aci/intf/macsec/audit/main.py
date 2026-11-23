from lib.aci.intf.macsec.audit.api import InterfaceMacSecAuditApi
from lib.aci.intf.macsec.audit.info import InterfaceMacSecAuditInfo


class InterfaceMacSecAudit(InterfaceMacSecAuditApi, InterfaceMacSecAuditInfo):
    def __init__(self):
        InterfaceMacSecAuditApi.__init__(self)
        InterfaceMacSecAuditInfo.__init__(self)
