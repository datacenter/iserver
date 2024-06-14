from lib.aci.bd.node.api import BridgeDomainNodeApi
from lib.aci.bd.node.info import BridgeDomainNodeInfo


class BridgeDomainNode(BridgeDomainNodeApi, BridgeDomainNodeInfo):
    def __init__(self):
        BridgeDomainNodeApi.__init__(self)
        BridgeDomainNodeInfo.__init__(self)
