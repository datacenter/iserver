from lib.aci.pg.access.intf.vpc.ports.api import PolicyGroupAccessInterfaceVpcPortApi
from lib.aci.pg.access.intf.vpc.ports.info import PolicyGroupAccessInterfaceVpcPortInfo


class PolicyGroupAccessInterfaceVpcPort(PolicyGroupAccessInterfaceVpcPortApi, PolicyGroupAccessInterfaceVpcPortInfo):
    def __init__(self):
        PolicyGroupAccessInterfaceVpcPortApi.__init__(self)
        PolicyGroupAccessInterfaceVpcPortInfo.__init__(self)
