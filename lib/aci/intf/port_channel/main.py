from lib.aci.intf.port_channel.members.main import InterfacePortChannelMembers
from lib.aci.intf.port_channel.relations.main import InterfacePortChannelRelations
from lib.aci.intf.port_channel.api import InterfacePortChannelApi
from lib.aci.intf.port_channel.info import InterfacePortChannelInfo


class InterfacePortChannel(InterfacePortChannelApi, InterfacePortChannelInfo, InterfacePortChannelMembers, InterfacePortChannelRelations):
    def __init__(self):
        InterfacePortChannelMembers.__init__(self)
        InterfacePortChannelRelations.__init__(self)
        InterfacePortChannelApi.__init__(self)
        InterfacePortChannelInfo.__init__(self)
