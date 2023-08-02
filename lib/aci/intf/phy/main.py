from lib.aci.intf.phy.cap.main import InterfacePhyCap
from lib.aci.intf.phy.eee.main import InterfacePhyEee
from lib.aci.intf.phy.load.main import InterfacePhyLoad
from lib.aci.intf.phy.pc.main import InterfacePhyPc
from lib.aci.intf.phy.stats.main import InterfacePhyStats
from lib.aci.intf.phy.api import InterfacePhyApi
from lib.aci.intf.phy.info import InterfacePhyInfo
from lib.aci.intf.phy.audit.main import InterfacePhyAudit
from lib.aci.intf.phy.event.main import InterfacePhyEvent
from lib.aci.intf.phy.fault.main import InterfacePhyFault


class InterfacePhy(
        InterfacePhyCap,
        InterfacePhyEee,
        InterfacePhyLoad,
        InterfacePhyPc,
        InterfacePhyStats,
        InterfacePhyApi,
        InterfacePhyInfo,
        InterfacePhyAudit,
        InterfacePhyEvent,
        InterfacePhyFault
        ):
    def __init__(self):
        InterfacePhyCap.__init__(self)
        InterfacePhyEee.__init__(self)
        InterfacePhyLoad.__init__(self)
        InterfacePhyPc.__init__(self)
        InterfacePhyStats.__init__(self)
        InterfacePhyApi.__init__(self)
        InterfacePhyInfo.__init__(self)
        InterfacePhyAudit.__init__(self)
        InterfacePhyEvent.__init__(self)
        InterfacePhyFault.__init__(self)
