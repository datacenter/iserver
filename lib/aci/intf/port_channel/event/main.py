from lib.aci.intf.port_channel.event.api import InterfacePortChannelEventApi
from lib.aci.intf.port_channel.event.info import InterfacePortChannelEventInfo


class InterfacePortChannelEvent(InterfacePortChannelEventApi, InterfacePortChannelEventInfo):
    def __init__(self):
        InterfacePortChannelEventApi.__init__(self)
        InterfacePortChannelEventInfo.__init__(self)
