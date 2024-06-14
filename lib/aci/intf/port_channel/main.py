from lib.aci.intf.port_channel.members.main import InterfacePortChannelMembers
from lib.aci.intf.port_channel.relations.main import InterfacePortChannelRelations
from lib.aci.intf.port_channel.api import InterfacePortChannelApi
from lib.aci.intf.port_channel.info import InterfacePortChannelInfo
from lib.aci.intf.port_channel.audit.main import InterfacePortChannelAudit
from lib.aci.intf.port_channel.event.main import InterfacePortChannelEvent
from lib.aci.intf.port_channel.fault.main import InterfacePortChannelFault


class InterfacePortChannel(
        InterfacePortChannelApi,
        InterfacePortChannelInfo,
        InterfacePortChannelMembers,
        InterfacePortChannelRelations,
        InterfacePortChannelAudit,
        InterfacePortChannelEvent,
        InterfacePortChannelFault
        ):
    def __init__(self):
        InterfacePortChannelMembers.__init__(self)
        InterfacePortChannelRelations.__init__(self)
        InterfacePortChannelApi.__init__(self)
        InterfacePortChannelInfo.__init__(self)
        InterfacePortChannelAudit.__init__(self)
        InterfacePortChannelEvent.__init__(self)
        InterfacePortChannelFault.__init__(self)
