from lib.aci.intf.tunnel.api import InterfaceTunnelApi
from lib.aci.intf.tunnel.info import InterfaceTunnelInfo


class InterfaceTunnel(InterfaceTunnelApi, InterfaceTunnelInfo):
    def __init__(self):
        InterfaceTunnelApi.__init__(self)
        InterfaceTunnelInfo.__init__(self)
