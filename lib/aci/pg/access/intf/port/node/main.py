from lib.aci.pg.access.intf.port.node.api import PolicyGroupAccessInterfacePortNodeApi
from lib.aci.pg.access.intf.port.node.info import PolicyGroupAccessInterfacePortNodeInfo


class PolicyGroupAccessInterfacePortNode(PolicyGroupAccessInterfacePortNodeApi, PolicyGroupAccessInterfacePortNodeInfo):
    def __init__(self):
        PolicyGroupAccessInterfacePortNodeApi.__init__(self)
        PolicyGroupAccessInterfacePortNodeInfo.__init__(self)
