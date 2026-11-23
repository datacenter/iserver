from lib.aci.intf.fault_counts.main import InterfaceFaultCounts
from lib.aci.intf.management.state.main import InterfaceManagementState
from lib.aci.intf.management.stats.main import InterfaceManagementStats
from lib.aci.intf.management.api import InterfaceMgmtApi
from lib.aci.intf.management.info import InterfaceMgmtInfo
from lib.aci.intf.management.audit.main import InterfaceMgmtAudit
from lib.aci.intf.management.event.main import InterfaceManagementEvent
from lib.aci.intf.management.fault.main import InterfaceManagementFault


class InterfaceMgmt(
        InterfaceFaultCounts,
        InterfaceManagementState,
        InterfaceManagementStats,
        InterfaceMgmtApi,
        InterfaceMgmtInfo,
        InterfaceMgmtAudit,
        InterfaceManagementEvent,
        InterfaceManagementFault
        ):
    def __init__(self):
        InterfaceFaultCounts.__init__(self)
        InterfaceManagementState.__init__(self)
        InterfaceManagementStats.__init__(self)
        InterfaceMgmtApi.__init__(self)
        InterfaceMgmtInfo.__init__(self)
        InterfaceMgmtAudit.__init__(self)
        InterfaceManagementEvent.__init__(self)
        InterfaceManagementFault.__init__(self)
