from lib.aci.domain.l3.event.api import DomainL3EventApi
from lib.aci.domain.l3.event.info import DomainL3EventInfo


class DomainL3Event(DomainL3EventApi, DomainL3EventInfo):
    def __init__(self):
        DomainL3EventApi.__init__(self)
        DomainL3EventInfo.__init__(self)
