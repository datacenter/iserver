from lib.aci.intf.fcpc.audit.api import InterfaceFcPcAuditApi
from lib.aci.intf.fcpc.audit.info import InterfaceFcPcAuditInfo


class InterfaceFcPcAudit(InterfaceFcPcAuditApi, InterfaceFcPcAuditInfo):
    def __init__(self):
        InterfaceFcPcAuditApi.__init__(self)
        InterfaceFcPcAuditInfo.__init__(self)
