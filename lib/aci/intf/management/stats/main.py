from lib.aci.intf.management.stats.api import InterfaceManagementStatsApi
from lib.aci.intf.management.stats.info import InterfaceManagementStatsInfo


class InterfaceManagementStats(InterfaceManagementStatsApi, InterfaceManagementStatsInfo):
    def __init__(self):
        InterfaceManagementStatsApi.__init__(self)
        InterfaceManagementStatsInfo.__init__(self)
