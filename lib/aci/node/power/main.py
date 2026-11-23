from lib.aci.node.power.api import NodePowerApi
from lib.aci.node.power.info import NodePowerInfo


class NodePower(NodePowerApi, NodePowerInfo):
    def __init__(self):
        NodePowerApi.__init__(self)
        NodePowerInfo.__init__(self)
