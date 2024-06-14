from lib.aci.intf.tunnel.api import InterfaceTunnelApi
from lib.aci.intf.tunnel.info import InterfaceTunnelInfo
from lib.aci.intf.tunnel.audit.main import InterfaceTunnelAudit
from lib.aci.intf.tunnel.event.main import InterfaceTunnelEvent
from lib.aci.intf.tunnel.fault.main import InterfaceTunnelFault


class InterfaceTunnel(
        InterfaceTunnelApi,
        InterfaceTunnelInfo,
        InterfaceTunnelAudit,
        InterfaceTunnelEvent,
        InterfaceTunnelFault
        ):
    def __init__(self):
        InterfaceTunnelApi.__init__(self)
        InterfaceTunnelInfo.__init__(self)
        InterfaceTunnelAudit.__init__(self)
        InterfaceTunnelEvent.__init__(self)
        InterfaceTunnelFault.__init__(self)
