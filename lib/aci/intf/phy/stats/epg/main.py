from lib.aci.intf.phy.stats.epg.api import InterfacePhyEpgStatsApi
from lib.aci.intf.phy.stats.epg.info import InterfacePhyEpgStatsInfo


class InterfacePhyEpgStats(InterfacePhyEpgStatsApi, InterfacePhyEpgStatsInfo):
    def __init__(self):
        InterfacePhyEpgStatsApi.__init__(self)
        InterfacePhyEpgStatsInfo.__init__(self)
