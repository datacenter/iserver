from lib.aci.intf.adjacency.lacp.api import InterfaceAdjacencyLacpApi
from lib.aci.intf.adjacency.lacp.info import InterfaceAdjacencyLacpInfo


class InterfaceAdjacencyLacp(InterfaceAdjacencyLacpApi, InterfaceAdjacencyLacpInfo):
    def __init__(self):
        InterfaceAdjacencyLacpApi.__init__(self)
        InterfaceAdjacencyLacpInfo.__init__(self)
