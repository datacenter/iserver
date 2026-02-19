from lib.ocp.task.helm.main import OcpTaskHelm
from lib.ocp.task.node.main import OcpTaskNode


class OcpTask(
        OcpTaskHelm,
        OcpTaskNode
        ):
    def __init__(self):
        OcpTaskHelm.__init__(self)
        OcpTaskNode.__init__(self)
