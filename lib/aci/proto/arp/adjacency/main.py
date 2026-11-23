from lib.aci.proto.arp.adjacency.api import ProtocolArpAdjacencyApi
from lib.aci.proto.arp.adjacency.info import ProtocolArpAdjacencyInfo


class ProtocolArpAdjacency(ProtocolArpAdjacencyApi, ProtocolArpAdjacencyInfo):
    def __init__(self):
        ProtocolArpAdjacencyApi.__init__(self)
        ProtocolArpAdjacencyInfo.__init__(self)
