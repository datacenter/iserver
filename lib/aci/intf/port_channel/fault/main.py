from lib.aci.intf.port_channel.fault.api import InterfacePortChannelFaultApi
from lib.aci.intf.port_channel.fault.info import InterfacePortChannelFaultInfo


class InterfacePortChannelFault(InterfacePortChannelFaultApi, InterfacePortChannelFaultInfo):
    def __init__(self):
        InterfacePortChannelFaultApi.__init__(self)
        InterfacePortChannelFaultInfo.__init__(self)
