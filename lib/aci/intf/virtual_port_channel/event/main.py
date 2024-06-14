from lib.aci.intf.virtual_port_channel.event.api import InterfaceVirtualPortChannelEventApi
from lib.aci.intf.virtual_port_channel.event.info import InterfaceVirtualPortChannelEventInfo


class InterfaceVirtualPortChannelEvent(InterfaceVirtualPortChannelEventApi, InterfaceVirtualPortChannelEventInfo):
    def __init__(self):
        InterfaceVirtualPortChannelEventApi.__init__(self)
        InterfaceVirtualPortChannelEventInfo.__init__(self)
