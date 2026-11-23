from lib.aci.domain.phy.event.api import DomainPhyEventApi
from lib.aci.domain.phy.event.info import DomainPhyEventInfo


class DomainPhyEvent(DomainPhyEventApi, DomainPhyEventInfo):
    def __init__(self):
        DomainPhyEventApi.__init__(self)
        DomainPhyEventInfo.__init__(self)
