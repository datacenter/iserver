from lib.aci.intf.virtual_port_channel.member.main import InterfaceVirtualPortChannelMember
from lib.aci.intf.virtual_port_channel.api import InterfaceVirtualPortChannelApi
from lib.aci.intf.virtual_port_channel.info import InterfaceVirtualPortChannelInfo
from lib.aci.intf.virtual_port_channel.audit.main import InterfaceVirtualPortChannelAudit
from lib.aci.intf.virtual_port_channel.event.main import InterfaceVirtualPortChannelEvent
from lib.aci.intf.virtual_port_channel.fault.main import InterfaceVirtualPortChannelFault


class InterfaceVirtualPortChannel(
        InterfaceVirtualPortChannelMember,
        InterfaceVirtualPortChannelApi,
        InterfaceVirtualPortChannelInfo,
        InterfaceVirtualPortChannelAudit,
        InterfaceVirtualPortChannelEvent,
        InterfaceVirtualPortChannelFault
        ):
    def __init__(self):
        InterfaceVirtualPortChannelMember.__init__(self)
        InterfaceVirtualPortChannelApi.__init__(self)
        InterfaceVirtualPortChannelInfo.__init__(self)
        InterfaceVirtualPortChannelAudit.__init__(self)
        InterfaceVirtualPortChannelEvent.__init__(self)
        InterfaceVirtualPortChannelFault.__init__(self)
