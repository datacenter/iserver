from lib.aci.pg.access.intf.vpc.node.api import PolicyGroupAccessInterfaceVpcNodeApi
from lib.aci.pg.access.intf.vpc.node.info import PolicyGroupAccessInterfaceVpcNodeInfo


class PolicyGroupAccessInterfaceVpcNode(PolicyGroupAccessInterfaceVpcNodeApi, PolicyGroupAccessInterfaceVpcNodeInfo):
    def __init__(self):
        PolicyGroupAccessInterfaceVpcNodeApi.__init__(self)
        PolicyGroupAccessInterfaceVpcNodeInfo.__init__(self)
