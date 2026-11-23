from lib.aci.domain.l2.api import DomainL2Api
from lib.aci.domain.l2.info import DomainL2Info
from lib.aci.domain.l2.audit.main import DomainL2Audit
from lib.aci.domain.l2.event.main import DomainL2Event
from lib.aci.domain.l2.fault.main import DomainL2Fault
from lib.aci.domain.l2.node.main import DomainL2Node


class DomainL2(
        DomainL2Api,
        DomainL2Info,
        DomainL2Audit,
        DomainL2Event,
        DomainL2Fault,
        DomainL2Node
        ):
    def __init__(self):
        DomainL2Api.__init__(self)
        DomainL2Info.__init__(self)
        DomainL2Audit.__init__(self)
        DomainL2Event.__init__(self)
        DomainL2Fault.__init__(self)
        DomainL2Node.__init__(self)
