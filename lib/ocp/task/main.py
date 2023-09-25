from lib.ocp.task.node.main import OcpTaskNode
from lib.ocp.task.ssh import OcpTaskSsh


class OcpTask(
        OcpTaskNode,
        OcpTaskSsh
        ):
    def __init__(self):
        OcpTaskNode.__init__(self)
        OcpTaskSsh.__init__(self)
