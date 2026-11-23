from lib.aci.proto.bgp.neighbor.stats.main import ProtocolBgpNeighborStats
from lib.aci.proto.bgp.neighbor.api import ProtocolBgpNeighborApi
from lib.aci.proto.bgp.neighbor.info import ProtocolBgpNeighborInfo


class ProtocolBgpNeighbor(ProtocolBgpNeighborApi, ProtocolBgpNeighborInfo, ProtocolBgpNeighborStats):
    def __init__(self):
        ProtocolBgpNeighborApi.__init__(self)
        ProtocolBgpNeighborInfo.__init__(self)
        ProtocolBgpNeighborStats.__init__(self)
