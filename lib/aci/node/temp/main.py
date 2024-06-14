from lib.aci.node.temp.api import NodeTempApi
from lib.aci.node.temp.info import NodeTempInfo


class NodeTemp(NodeTempApi, NodeTempInfo):
    def __init__(self):
        NodeTempApi.__init__(self)
        NodeTempInfo.__init__(self)
