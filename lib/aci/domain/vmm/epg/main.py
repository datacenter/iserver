from lib.aci.domain.vmm.epg.api import DomainVmmEpgApi
from lib.aci.domain.vmm.epg.info import DomainVmmEpgInfo


class DomainVmmEpg(DomainVmmEpgApi, DomainVmmEpgInfo):
    def __init__(self):
        DomainVmmEpgApi.__init__(self)
        DomainVmmEpgInfo.__init__(self)
