from lib.aci.intf.lacp.stats.api import InterfaceLacpStatsApi
from lib.aci.intf.lacp.stats.info import InterfaceLacpStatsInfo


class InterfaceLacpStats(InterfaceLacpStatsApi, InterfaceLacpStatsInfo):
    def __init__(self):
        InterfaceLacpStatsApi.__init__(self)
        InterfaceLacpStatsInfo.__init__(self)
