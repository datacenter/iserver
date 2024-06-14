from lib.ocp.task.chrony.main import OcpTaskChrony
from lib.ocp.task.container_policy.main import OcpTaskContainerPolicy
from lib.ocp.task.node.main import OcpTaskNode
from lib.ocp.task.ssh import OcpTaskSsh


class OcpTask(
        OcpTaskChrony,
        OcpTaskContainerPolicy,
        OcpTaskNode,
        OcpTaskSsh
        ):
    def __init__(self):
        OcpTaskChrony.__init__(self)
        OcpTaskContainerPolicy.__init__(self)
        OcpTaskNode.__init__(self)
        OcpTaskSsh.__init__(self)
