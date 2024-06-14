from lib.aci.domain.l3.api import DomainL3Api
from lib.aci.domain.l3.info import DomainL3Info
from lib.aci.domain.l3.audit.main import DomainL3Audit
from lib.aci.domain.l3.event.main import DomainL3Event
from lib.aci.domain.l3.fault.main import DomainL3Fault
from lib.aci.domain.l3.node.main import DomainL3Node


class DomainL3(
        DomainL3Api,
        DomainL3Info,
        DomainL3Audit,
        DomainL3Event,
        DomainL3Fault,
        DomainL3Node
        ):
    def __init__(self):
        DomainL3Api.__init__(self)
        DomainL3Info.__init__(self)
        DomainL3Audit.__init__(self)
        DomainL3Event.__init__(self)
        DomainL3Fault.__init__(self)
        DomainL3Node.__init__(self)
