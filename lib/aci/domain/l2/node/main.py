from lib.aci.domain.l2.node.api import DomainL2NodeApi
from lib.aci.domain.l2.node.info import DomainL2NodeInfo


class DomainL2Node(DomainL2NodeApi, DomainL2NodeInfo):
    def __init__(self):
        DomainL2NodeApi.__init__(self)
        DomainL2NodeInfo.__init__(self)
