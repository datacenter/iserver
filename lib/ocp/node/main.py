from lib.ocp.node.info import OcpNodeInfo
from lib.ocp.node.linux import OcpNodeLinux
from lib.ocp.node.sriov import OcpNodeSriov


class OcpNode(
        OcpNodeInfo,
        OcpNodeLinux,
        OcpNodeSriov
        ):
    def __init__(self):
        OcpNodeInfo.__init__(self)
        OcpNodeLinux.__init__(self)
        OcpNodeSriov.__init__(self)
