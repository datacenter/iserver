from lib.aci.intf.tunnel.audit.api import InterfaceTunnelAuditApi
from lib.aci.intf.tunnel.audit.info import InterfaceTunnelAuditInfo


class InterfaceTunnelAudit(InterfaceTunnelAuditApi, InterfaceTunnelAuditInfo):
    def __init__(self):
        InterfaceTunnelAuditApi.__init__(self)
        InterfaceTunnelAuditInfo.__init__(self)
