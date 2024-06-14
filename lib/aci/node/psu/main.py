from lib.aci.node.psu.api import NodePsuApi
from lib.aci.node.psu.info import NodePsuInfo


class NodePsu(NodePsuApi, NodePsuInfo):
    def __init__(self):
        NodePsuApi.__init__(self)
        NodePsuInfo.__init__(self)
