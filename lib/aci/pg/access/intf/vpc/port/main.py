from lib.aci.pg.access.intf.vpc.port.api import PolicyGroupAccessInterfaceVpcPortApi
from lib.aci.pg.access.intf.vpc.port.info import PolicyGroupAccessInterfaceVpcPortInfo


class PolicyGroupAccessInterfaceVpcPort(PolicyGroupAccessInterfaceVpcPortApi, PolicyGroupAccessInterfaceVpcPortInfo):
    def __init__(self):
        PolicyGroupAccessInterfaceVpcPortApi.__init__(self)
        PolicyGroupAccessInterfaceVpcPortInfo.__init__(self)
