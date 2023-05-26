from lib.aci.intf.virtual_port_channel.member.api import InterfaceVirtualPortChannelMemberApi
from lib.aci.intf.virtual_port_channel.member.info import InterfaceVirtualPortChannelMemberInfo


class InterfaceVirtualPortChannelMember(InterfaceVirtualPortChannelMemberApi, InterfaceVirtualPortChannelMemberInfo):
    def __init__(self):
        InterfaceVirtualPortChannelMemberApi.__init__(self)
        InterfaceVirtualPortChannelMemberInfo.__init__(self)
