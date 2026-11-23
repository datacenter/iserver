from lib.aci.node.sensor.api import NodeSensorApi
from lib.aci.node.sensor.info import NodeSensorInfo


class NodeSensor(NodeSensorApi, NodeSensorInfo):
    def __init__(self):
        NodeSensorApi.__init__(self)
        NodeSensorInfo.__init__(self)
