from lib.aci.intf.virtual_port_channel.member.main import InterfaceVirtualPortChannelMember
from lib.aci.intf.virtual_port_channel.api import InterfaceVirtualPortChannelApi
from lib.aci.intf.virtual_port_channel.info import InterfaceVirtualPortChannelInfo


class InterfaceVirtualPortChannel(InterfaceVirtualPortChannelMember, InterfaceVirtualPortChannelApi, InterfaceVirtualPortChannelInfo):
    def __init__(self):
        InterfaceVirtualPortChannelMember.__init__(self)
        InterfaceVirtualPortChannelApi.__init__(self)
        InterfaceVirtualPortChannelInfo.__init__(self)
