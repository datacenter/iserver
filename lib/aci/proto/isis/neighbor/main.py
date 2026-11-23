from lib.aci.proto.isis.neighbor.api import ProtocolIsisNeighborApi
from lib.aci.proto.isis.neighbor.info import ProtocolIsisNeighborInfo


class ProtocolIsisNeighbor(ProtocolIsisNeighborApi, ProtocolIsisNeighborInfo):
    def __init__(self):
        ProtocolIsisNeighborApi.__init__(self)
        ProtocolIsisNeighborInfo.__init__(self)
