from lib.aci.intf.phy.stats.ether.api import InterfacePhyEtherStatsApi
from lib.aci.intf.phy.stats.ether.info import InterfacePhyEtherStatsInfo


class InterfacePhyEtherStats(InterfacePhyEtherStatsApi, InterfacePhyEtherStatsInfo):
    def __init__(self):
        InterfacePhyEtherStatsApi.__init__(self)
        InterfacePhyEtherStatsInfo.__init__(self)
