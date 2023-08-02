from lib.aci.l3out.node.api import L3OutNodeApi
from lib.aci.l3out.node.info import L3OutNodeInfo


class L3OutNode(L3OutNodeApi, L3OutNodeInfo):
    def __init__(self):
        L3OutNodeApi.__init__(self)
        L3OutNodeInfo.__init__(self)
