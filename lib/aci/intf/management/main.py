from lib.aci.intf.fault_counts.main import InterfaceFaultCounts
from lib.aci.intf.management.state.main import InterfaceManagementState
from lib.aci.intf.management.stats.main import InterfaceManagementStats
from lib.aci.intf.management.api import InterfaceMgmtApi
from lib.aci.intf.management.info import InterfaceMgmtInfo


class InterfaceMgmt(InterfaceFaultCounts, InterfaceManagementState, InterfaceManagementStats, InterfaceMgmtApi, InterfaceMgmtInfo):
    def __init__(self):
        InterfaceFaultCounts.__init__(self)
        InterfaceManagementState.__init__(self)
        InterfaceManagementStats.__init__(self)
        InterfaceMgmtApi.__init__(self)
        InterfaceMgmtInfo.__init__(self)
