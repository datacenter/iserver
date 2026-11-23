from lib.aci.vrf.node.api import VrfNodeApi
from lib.aci.vrf.node.info import VrfNodeInfo


class VrfNode(VrfNodeApi, VrfNodeInfo):
    def __init__(self):
        VrfNodeApi.__init__(self)
        VrfNodeInfo.__init__(self)
