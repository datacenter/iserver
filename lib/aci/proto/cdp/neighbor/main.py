from lib.aci.proto.cdp.neighbor.api import ProtocolCdpNeighborApi
from lib.aci.proto.cdp.neighbor.info import ProtocolCdpNeighborInfo


class ProtocolCdpNeighbor(ProtocolCdpNeighborApi, ProtocolCdpNeighborInfo):
    def __init__(self):
        ProtocolCdpNeighborApi.__init__(self)
        ProtocolCdpNeighborInfo.__init__(self)
