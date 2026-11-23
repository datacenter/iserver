from lib.aci.intf.phy.audit.api import InterfacePhyAuditApi
from lib.aci.intf.phy.audit.info import InterfacePhyAuditInfo


class InterfacePhyAudit(InterfacePhyAuditApi, InterfacePhyAuditInfo):
    def __init__(self):
        InterfacePhyAuditApi.__init__(self)
        InterfacePhyAuditInfo.__init__(self)
