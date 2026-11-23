from lib.aci.intf.svi.api import InterfaceSviApi
from lib.aci.intf.svi.info import InterfaceSviInfo
from lib.aci.intf.svi.audit.main import InterfaceSviAudit
from lib.aci.intf.svi.event.main import InterfaceSviEvent
from lib.aci.intf.svi.fault.main import InterfaceSviFault


class InterfaceSvi(
        InterfaceSviApi,
        InterfaceSviInfo,
        InterfaceSviAudit,
        InterfaceSviEvent,
        InterfaceSviFault
        ):
    def __init__(self):
        InterfaceSviApi.__init__(self)
        InterfaceSviInfo.__init__(self)
        InterfaceSviAudit.__init__(self)
        InterfaceSviEvent.__init__(self)
        InterfaceSviFault.__init__(self)
