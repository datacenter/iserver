from lib.aci.intf.tunnel.event.api import InterfaceTunnelEventApi
from lib.aci.intf.tunnel.event.info import InterfaceTunnelEventInfo


class InterfaceTunnelEvent(InterfaceTunnelEventApi, InterfaceTunnelEventInfo):
    def __init__(self):
        InterfaceTunnelEventApi.__init__(self)
        InterfaceTunnelEventInfo.__init__(self)
