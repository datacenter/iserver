from lib.aci.domain.l2.event.api import DomainL2EventApi
from lib.aci.domain.l2.event.info import DomainL2EventInfo


class DomainL2Event(DomainL2EventApi, DomainL2EventInfo):
    def __init__(self):
        DomainL2EventApi.__init__(self)
        DomainL2EventInfo.__init__(self)
