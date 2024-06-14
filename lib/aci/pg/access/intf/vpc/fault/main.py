from lib.aci.pg.access.intf.vpc.fault.api import PolicyGroupAccessInterfaceVpcFaultApi
from lib.aci.pg.access.intf.vpc.fault.info import PolicyGroupAccessInterfaceVpcFaultInfo


class PolicyGroupAccessInterfaceVpcFault(PolicyGroupAccessInterfaceVpcFaultApi, PolicyGroupAccessInterfaceVpcFaultInfo):
    def __init__(self):
        PolicyGroupAccessInterfaceVpcFaultApi.__init__(self)
        PolicyGroupAccessInterfaceVpcFaultInfo.__init__(self)
