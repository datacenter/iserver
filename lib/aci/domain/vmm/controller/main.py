from lib.aci.domain.vmm.controller.api import DomainVmmControllerApi
from lib.aci.domain.vmm.controller.info import DomainVmmControllerInfo


class DomainVmmController(DomainVmmControllerApi, DomainVmmControllerInfo):
    def __init__(self):
        DomainVmmControllerApi.__init__(self)
        DomainVmmControllerInfo.__init__(self)
