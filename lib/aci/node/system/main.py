from lib.aci.node.system.api import NodeSystemApi
from lib.aci.node.system.info import NodeSystemInfo


class NodeSystem(NodeSystemApi, NodeSystemInfo):
    def __init__(self):
        NodeSystemApi.__init__(self)
        NodeSystemInfo.__init__(self)
