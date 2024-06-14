from lib.aci.l2out.node.api import L2OutNodeApi
from lib.aci.l2out.node.info import L2OutNodeInfo


class L2OutNode(L2OutNodeApi, L2OutNodeInfo):
    def __init__(self):
        L2OutNodeApi.__init__(self)
        L2OutNodeInfo.__init__(self)
