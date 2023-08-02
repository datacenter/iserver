from lib.aci.intf.loopback.audit.api import InterfaceLoopbackAuditApi
from lib.aci.intf.loopback.audit.info import InterfaceLoopbackAuditInfo


class InterfaceLoopbackAudit(InterfaceLoopbackAuditApi, InterfaceLoopbackAuditInfo):
    def __init__(self):
        InterfaceLoopbackAuditApi.__init__(self)
        InterfaceLoopbackAuditInfo.__init__(self)
