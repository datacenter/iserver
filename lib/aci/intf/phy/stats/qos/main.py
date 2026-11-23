from lib.aci.intf.phy.stats.qos.api import InterfacePhyQosStatsApi
from lib.aci.intf.phy.stats.qos.info import InterfacePhyQosStatsInfo
from lib.aci.intf.phy.stats.qos.live import InterfacePhyQosStatsLive


class InterfacePhyQosStats(InterfacePhyQosStatsApi, InterfacePhyQosStatsInfo, InterfacePhyQosStatsLive):
    def __init__(self):
        InterfacePhyQosStatsApi.__init__(self)
        InterfacePhyQosStatsInfo.__init__(self)
        InterfacePhyQosStatsLive.__init__(self)
