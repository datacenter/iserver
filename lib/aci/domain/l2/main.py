from lib.aci.domain.l2.api import DomainL2Api
from lib.aci.domain.l2.info import DomainL2Info


class DomainL2(DomainL2Api, DomainL2Info):
    def __init__(self):
        DomainL2Api.__init__(self)
        DomainL2Info.__init__(self)
