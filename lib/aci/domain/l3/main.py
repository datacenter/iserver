from lib.aci.domain.l3.api import DomainL3Api
from lib.aci.domain.l3.info import DomainL3Info


class DomainL3(DomainL3Api, DomainL3Info):
    def __init__(self):
        DomainL3Api.__init__(self)
        DomainL3Info.__init__(self)
