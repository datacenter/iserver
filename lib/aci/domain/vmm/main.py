from lib.aci.domain.vmm.api import DomainVmmApi
from lib.aci.domain.vmm.info import DomainVmmInfo
from lib.aci.domain.vmm.audit.main import DomainVmmAudit
from lib.aci.domain.vmm.controller.main import DomainVmmController
from lib.aci.domain.vmm.epg.main import DomainVmmEpg
from lib.aci.domain.vmm.event.main import DomainVmmEvent
from lib.aci.domain.vmm.fault.main import DomainVmmFault
from lib.aci.domain.vmm.node.main import DomainVmmNode


class DomainVmm(
        DomainVmmApi,
        DomainVmmInfo,
        DomainVmmAudit,
        DomainVmmController,
        DomainVmmEpg,
        DomainVmmEvent,
        DomainVmmFault,
        DomainVmmNode
        ):
    def __init__(self):
        DomainVmmApi.__init__(self)
        DomainVmmInfo.__init__(self)
        DomainVmmAudit.__init__(self)
        DomainVmmController.__init__(self)
        DomainVmmEpg.__init__(self)
        DomainVmmEvent.__init__(self)
        DomainVmmFault.__init__(self)
        DomainVmmNode.__init__(self)
