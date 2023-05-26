from lib.aci.pg.access.intf.vpc.node.main import PolicyGroupAccessInterfaceVpcNode
from lib.aci.pg.access.intf.vpc.port.main import PolicyGroupAccessInterfaceVpcPort
from lib.aci.pg.access.intf.vpc.api import PolicyGroupAccessInterfaceVpcApi
from lib.aci.pg.access.intf.vpc.info import PolicyGroupAccessInterfaceVpcInfo


class PolicyGroupAccessInterfaceVpc(PolicyGroupAccessInterfaceVpcNode, PolicyGroupAccessInterfaceVpcPort, PolicyGroupAccessInterfaceVpcApi, PolicyGroupAccessInterfaceVpcInfo):
    def __init__(self):
        PolicyGroupAccessInterfaceVpcNode.__init__(self)
        PolicyGroupAccessInterfaceVpcPort.__init__(self)
        PolicyGroupAccessInterfaceVpcApi.__init__(self)
        PolicyGroupAccessInterfaceVpcInfo.__init__(self)
