from lib.aci.domain.phy.api import DomainPhyApi
from lib.aci.domain.phy.info import DomainPhyInfo
from lib.aci.domain.phy.create import DomainPhyCreate
from lib.aci.domain.phy.delete import DomainPhyDelete
from lib.aci.domain.phy.update import DomainPhyUpdate
from lib.aci.domain.phy.audit.main import DomainPhyAudit
from lib.aci.domain.phy.event.main import DomainPhyEvent
from lib.aci.domain.phy.fault.main import DomainPhyFault
from lib.aci.domain.phy.node.main import DomainPhyNode


class DomainPhy(
        DomainPhyApi,
        DomainPhyInfo,
        DomainPhyCreate,
        DomainPhyDelete,
        DomainPhyUpdate,
        DomainPhyAudit,
        DomainPhyEvent,
        DomainPhyFault,
        DomainPhyNode
        ):
    def __init__(self):
        DomainPhyApi.__init__(self)
        DomainPhyInfo.__init__(self)
        DomainPhyCreate.__init__(self)
        DomainPhyDelete.__init__(self)
        DomainPhyUpdate.__init__(self)
        DomainPhyAudit.__init__(self)
        DomainPhyEvent.__init__(self)
        DomainPhyFault.__init__(self)
        DomainPhyNode.__init__(self)
