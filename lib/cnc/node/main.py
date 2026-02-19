from lib.cnc.node.api import NodeApi
from lib.cnc.node.info import NodeInfo


class Node(
    NodeApi,
    NodeInfo
    ):
    def __init__(self):
        NodeApi.__init__(self)
        NodeInfo.__init__(self)
