from lib.aci.proto.bgp.neighbor.stats.api import ProtocolBgpNeighborStatsApi
from lib.aci.proto.bgp.neighbor.stats.info import ProtocolBgpNeighborStatsInfo


class ProtocolBgpNeighborStats(ProtocolBgpNeighborStatsApi, ProtocolBgpNeighborStatsInfo):
    def __init__(self):
        ProtocolBgpNeighborStatsApi.__init__(self)
        ProtocolBgpNeighborStatsInfo.__init__(self)
