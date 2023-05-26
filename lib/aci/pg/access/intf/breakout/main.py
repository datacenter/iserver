from lib.aci.pg.access.intf.breakout.api import PolicyGroupAccessInterfaceBreakoutApi
from lib.aci.pg.access.intf.breakout.info import PolicyGroupAccessInterfaceBreakoutInfo


class PolicyGroupAccessInterfaceBreakout(PolicyGroupAccessInterfaceBreakoutApi, PolicyGroupAccessInterfaceBreakoutInfo):
    def __init__(self):
        PolicyGroupAccessInterfaceBreakoutApi.__init__(self)
        PolicyGroupAccessInterfaceBreakoutInfo.__init__(self)
