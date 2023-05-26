from lib.aci.intf.adjacency.cdp.api import InterfaceAdjacencyCdpApi
from lib.aci.intf.adjacency.cdp.info import InterfaceAdjacencyCdpInfo


class InterfaceAdjacencyCdp(InterfaceAdjacencyCdpApi, InterfaceAdjacencyCdpInfo):
    def __init__(self):
        InterfaceAdjacencyCdpApi.__init__(self)
        InterfaceAdjacencyCdpInfo.__init__(self)
