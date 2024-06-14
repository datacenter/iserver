from lib.aci.node.api import NodeApi
from lib.aci.node.info import NodeInfo
from lib.aci.node.policy.profile.main import NodeInterfacePolicyProfile
from lib.aci.node.power.main import NodePower
from lib.aci.node.psu.main import NodePsu
from lib.aci.node.sensor.main import NodeSensor
from lib.aci.node.system.main import NodeSystem
from lib.aci.node.temp.main import NodeTemp


class Node(
    NodeApi,
    NodeInfo,
    NodeInterfacePolicyProfile,
    NodePower,
    NodePsu,
    NodeSensor,
    NodeSystem,
    NodeTemp
    ):
    def __init__(self):
        NodeApi.__init__(self)
        NodeInfo.__init__(self)
        NodeInterfacePolicyProfile.__init__(self)
        NodePower.__init__(self)
        NodePsu.__init__(self)
        NodeSensor.__init__(self)
        NodeSystem.__init__(self)
        NodeTemp.__init__(self)
