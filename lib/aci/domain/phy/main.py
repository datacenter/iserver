from lib.aci.domain.phy.api import DomainPhyApi
from lib.aci.domain.phy.info import DomainPhyInfo


class DomainPhy(DomainPhyApi, DomainPhyInfo):
    def __init__(self):
        DomainPhyApi.__init__(self)
        DomainPhyInfo.__init__(self)
