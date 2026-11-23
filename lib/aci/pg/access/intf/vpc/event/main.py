from lib.aci.pg.access.intf.vpc.event.api import PolicyGroupAccessInterfaceVpcEventApi
from lib.aci.pg.access.intf.vpc.event.info import PolicyGroupAccessInterfaceVpcEventInfo


class PolicyGroupAccessInterfaceVpcEvent(PolicyGroupAccessInterfaceVpcEventApi, PolicyGroupAccessInterfaceVpcEventInfo):
    def __init__(self):
        PolicyGroupAccessInterfaceVpcEventApi.__init__(self)
        PolicyGroupAccessInterfaceVpcEventInfo.__init__(self)
