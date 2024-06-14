from lib.aci.proto.nd.neighbor.api import ProtocolNdNeighborApi
from lib.aci.proto.nd.neighbor.info import ProtocolNdNeighborInfo


class ProtocolNdNeighbor(ProtocolNdNeighborApi, ProtocolNdNeighborInfo):
    def __init__(self):
        ProtocolNdNeighborApi.__init__(self)
        ProtocolNdNeighborInfo.__init__(self)
