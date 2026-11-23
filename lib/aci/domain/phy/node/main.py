from lib.aci.domain.phy.node.api import DomainPhyNodeApi
from lib.aci.domain.phy.node.info import DomainPhyNodeInfo


class DomainPhyNode(DomainPhyNodeApi, DomainPhyNodeInfo):
    def __init__(self):
        DomainPhyNodeApi.__init__(self)
        DomainPhyNodeInfo.__init__(self)
