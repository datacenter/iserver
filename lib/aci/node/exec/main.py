from lib.aci.node.exec.run import NodeExecRun
from lib.aci.node.exec.vlan import NodeExecVlan


class NodeExec(
        NodeExecRun,
        NodeExecVlan
    ):
    def __init__(self):
        NodeExecRun.__init__(self)
        NodeExecVlan.__init__(self)
