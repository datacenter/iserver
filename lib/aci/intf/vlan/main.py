from lib.aci.intf.vlan.api import InterfaceVlanStatsApi
from lib.aci.intf.vlan.info import InterfaceVlanStatsInfo


class InterfaceVlanStats(InterfaceVlanStatsApi, InterfaceVlanStatsInfo):
    def __init__(self):
        InterfaceVlanStatsApi.__init__(self)
        InterfaceVlanStatsInfo.__init__(self)
