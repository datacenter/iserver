from lib.aci.intf.fc.audit.api import InterfaceFcAuditApi
from lib.aci.intf.fc.audit.info import InterfaceFcAuditInfo


class InterfaceFcAudit(InterfaceFcAuditApi, InterfaceFcAuditInfo):
    def __init__(self):
        InterfaceFcAuditApi.__init__(self)
        InterfaceFcAuditInfo.__init__(self)
