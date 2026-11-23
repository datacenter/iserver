from lib.aci.intf.macsec.tx.main import InterfaceMacSecTx
from lib.aci.intf.macsec.rx.main import InterfaceMacSecRx
from lib.aci.intf.macsec.stats.main import InterfaceMacSecStats
from lib.aci.intf.macsec.castats.main import InterfaceMacSecCaStats
from lib.aci.intf.macsec.api import InterfaceMacSecApi
from lib.aci.intf.macsec.info import InterfaceMacSecInfo
from lib.aci.intf.macsec.audit.main import InterfaceMacSecAudit
from lib.aci.intf.macsec.event.main import InterfaceMacSecEvent
from lib.aci.intf.macsec.fault.main import InterfaceMacSecFault


class InterfaceMacSec(
        InterfaceMacSecTx,
        InterfaceMacSecRx,
        InterfaceMacSecStats,
        InterfaceMacSecCaStats,
        InterfaceMacSecApi,
        InterfaceMacSecInfo,
        InterfaceMacSecAudit,
        InterfaceMacSecEvent,
        InterfaceMacSecFault
        ):
    def __init__(self):
        InterfaceMacSecRx.__init__(self)
        InterfaceMacSecTx.__init__(self)
        InterfaceMacSecStats.__init__(self)
        InterfaceMacSecCaStats.__init__(self)
        InterfaceMacSecApi.__init__(self)
        InterfaceMacSecInfo.__init__(self)
        InterfaceMacSecAudit.__init__(self)
        InterfaceMacSecEvent.__init__(self)
        InterfaceMacSecFault.__init__(self)
