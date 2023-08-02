from lib.aci.intf.tunnel.fault.api import InterfaceTunnelFaultApi
from lib.aci.intf.tunnel.fault.info import InterfaceTunnelFaultInfo


class InterfaceTunnelFault(InterfaceTunnelFaultApi, InterfaceTunnelFaultInfo):
    def __init__(self):
        InterfaceTunnelFaultApi.__init__(self)
        InterfaceTunnelFaultInfo.__init__(self)
