from lib.aci.intf.macsec.stats.api import InterfaceMacSecStatsApi
from lib.aci.intf.macsec.stats.info import InterfaceMacSecStatsInfo


class InterfaceMacSecStats(InterfaceMacSecStatsApi, InterfaceMacSecStatsInfo):
    def __init__(self):
        InterfaceMacSecStatsApi.__init__(self)
        InterfaceMacSecStatsInfo.__init__(self)
