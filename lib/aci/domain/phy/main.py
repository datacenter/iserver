from lib.aci.domain.phy.api import DomainPhyApi
from lib.aci.domain.phy.info import DomainPhyInfo
from lib.aci.domain.phy.audit.main import DomainPhyAudit
from lib.aci.domain.phy.event.main import DomainPhyEvent
from lib.aci.domain.phy.fault.main import DomainPhyFault
from lib.aci.domain.phy.node.main import DomainPhyNode


class DomainPhy(
        DomainPhyApi,
        DomainPhyInfo,
        DomainPhyAudit,
        DomainPhyEvent,
        DomainPhyFault,
        DomainPhyNode
        ):
    def __init__(self):
        DomainPhyApi.__init__(self)
        DomainPhyInfo.__init__(self)
        DomainPhyAudit.__init__(self)
        DomainPhyEvent.__init__(self)
        DomainPhyFault.__init__(self)
        DomainPhyNode.__init__(self)
