from lib.aci.domain.vmm.node.api import DomainVmmNodeApi
from lib.aci.domain.vmm.node.info import DomainVmmNodeInfo


class DomainVmmNode(DomainVmmNodeApi, DomainVmmNodeInfo):
    def __init__(self):
        DomainVmmNodeApi.__init__(self)
        DomainVmmNodeInfo.__init__(self)
