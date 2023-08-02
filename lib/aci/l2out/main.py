from lib.aci.l2out.api import L2OutApi
from lib.aci.l2out.info import L2OutInfo
from lib.aci.l2out.audit.main import L2OutAudit
from lib.aci.l2out.event.main import L2OutEvent
from lib.aci.l2out.fault.main import L2OutFault
from lib.aci.l2out.node.main import L2OutNode


class L2Out(
        L2OutApi,
        L2OutInfo,
        L2OutAudit,
        L2OutEvent,
        L2OutFault,
        L2OutNode
        ):
    def __init__(self):
        L2OutApi.__init__(self)
        L2OutInfo.__init__(self)
        L2OutAudit.__init__(self)
        L2OutEvent.__init__(self)
        L2OutFault.__init__(self)
        L2OutNode.__init__(self)
