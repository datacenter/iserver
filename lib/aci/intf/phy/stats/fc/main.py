from lib.aci.intf.phy.stats.fc.api import InterfacePhyFcStatsApi
from lib.aci.intf.phy.stats.fc.info import InterfacePhyFcStatsInfo


class InterfacePhyFcStats(InterfacePhyFcStatsApi, InterfacePhyFcStatsInfo):
    def __init__(self):
        InterfacePhyFcStatsApi.__init__(self)
        InterfacePhyFcStatsInfo.__init__(self)
