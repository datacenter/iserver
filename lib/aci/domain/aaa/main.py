from lib.aci.domain.aaa.api import DomainAaaApi
from lib.aci.domain.aaa.info import DomainAaaInfo


class DomainAaa(DomainAaaApi, DomainAaaInfo):
    def __init__(self):
        DomainAaaApi.__init__(self)
        DomainAaaInfo.__init__(self)
