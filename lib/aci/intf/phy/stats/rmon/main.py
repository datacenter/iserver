from lib.aci.intf.phy.stats.rmon.api import InterfacePhyRmonStatsApi
from lib.aci.intf.phy.stats.rmon.info import InterfacePhyRmonStatsInfo


class InterfacePhyRmonStats(InterfacePhyRmonStatsApi, InterfacePhyRmonStatsInfo):
    def __init__(self):
        InterfacePhyRmonStatsApi.__init__(self)
        InterfacePhyRmonStatsInfo.__init__(self)
