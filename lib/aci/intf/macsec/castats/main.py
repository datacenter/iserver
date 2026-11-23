from lib.aci.intf.macsec.castats.api import InterfaceMacSecCaStatsApi
from lib.aci.intf.macsec.castats.info import InterfaceMacSecCaStatsInfo


class InterfaceMacSecCaStats(InterfaceMacSecCaStatsApi, InterfaceMacSecCaStatsInfo):
    def __init__(self):
        InterfaceMacSecCaStatsApi.__init__(self)
        InterfaceMacSecCaStatsInfo.__init__(self)
