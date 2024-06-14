from lib.aci.intf.virtual_port_channel.fault.api import InterfaceVirtualPortChannelFaultApi
from lib.aci.intf.virtual_port_channel.fault.info import InterfaceVirtualPortChannelFaultInfo


class InterfaceVirtualPortChannelFault(InterfaceVirtualPortChannelFaultApi, InterfaceVirtualPortChannelFaultInfo):
    def __init__(self):
        InterfaceVirtualPortChannelFaultApi.__init__(self)
        InterfaceVirtualPortChannelFaultInfo.__init__(self)
