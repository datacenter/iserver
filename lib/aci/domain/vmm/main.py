from lib.aci.domain.vmm.api import DomainVmmApi
from lib.aci.domain.vmm.info import DomainVmmInfo
from lib.aci.domain.vmm.epg.main import DomainVmmEpg


class DomainVmm(DomainVmmApi, DomainVmmInfo, DomainVmmEpg):
    def __init__(self):
        DomainVmmApi.__init__(self)
        DomainVmmInfo.__init__(self)
        DomainVmmEpg.__init__(self)
