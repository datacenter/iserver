from lib.aci.domain.vmm.event.api import DomainVmmEventApi
from lib.aci.domain.vmm.event.info import DomainVmmEventInfo


class DomainVmmEvent(DomainVmmEventApi, DomainVmmEventInfo):
    def __init__(self):
        DomainVmmEventApi.__init__(self)
        DomainVmmEventInfo.__init__(self)
