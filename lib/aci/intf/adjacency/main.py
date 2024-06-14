from lib.aci.intf.adjacency.cdp.main import InterfaceAdjacencyCdp
from lib.aci.intf.adjacency.lacp.main import InterfaceAdjacencyLacp
from lib.aci.intf.adjacency.lldp.main import InterfaceAdjacencyLldp


class InterfaceAdjacency(InterfaceAdjacencyCdp, InterfaceAdjacencyLacp, InterfaceAdjacencyLldp):
    def __init__(self):
        InterfaceAdjacencyCdp.__init__(self)
        InterfaceAdjacencyLacp.__init__(self)
        InterfaceAdjacencyLldp.__init__(self)
