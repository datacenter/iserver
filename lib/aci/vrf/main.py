from lib.aci.vrf.api import VrfApi
from lib.aci.vrf.info import VrfInfo
from lib.aci.vrf.audit.main import VrfAudit
from lib.aci.vrf.event.main import VrfEvent
from lib.aci.vrf.fault.main import VrfFault
from lib.aci.vrf.node.main import VrfNode


class Vrf(
        VrfApi,
        VrfInfo,
        VrfAudit,
        VrfEvent,
        VrfFault,
        VrfNode
        ):
    def __init__(self):
        VrfApi.__init__(self)
        VrfInfo.__init__(self)
        VrfAudit.__init__(self)
        VrfEvent.__init__(self)
        VrfFault.__init__(self)
        VrfNode.__init__(self)