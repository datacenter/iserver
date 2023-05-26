from lib.aci.intf.adjacency.lldp.api import InterfaceAdjacencyLldpApi
from lib.aci.intf.adjacency.lldp.info import InterfaceAdjacencyLldpInfo


class InterfaceAdjacencyLldp(InterfaceAdjacencyLldpApi, InterfaceAdjacencyLldpInfo):
    def __init__(self):
        InterfaceAdjacencyLldpApi.__init__(self)
        InterfaceAdjacencyLldpInfo.__init__(self)
