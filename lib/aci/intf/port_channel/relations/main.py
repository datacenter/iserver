from lib.aci.intf.port_channel.relations.api import InterfacePortChannelRelationsApi
from lib.aci.intf.port_channel.relations.info import InterfacePortChannelRelationsInfo


class InterfacePortChannelRelations(InterfacePortChannelRelationsApi, InterfacePortChannelRelationsInfo):
    def __init__(self):
        InterfacePortChannelRelationsApi.__init__(self)
        InterfacePortChannelRelationsInfo.__init__(self)
