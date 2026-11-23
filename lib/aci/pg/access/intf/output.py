from lib.aci.pg.access.intf.port.output import PolicyGroupAccessInterfacePortOutput
from lib.aci.pg.access.intf.vpc.output import PolicyGroupAccessInterfaceVpcOutput
from lib.aci.pg.access.intf.breakout.output import PolicyGroupAccessInterfaceBreakoutOutput


class PolicyGroupAccessInterfaceOutput(
    PolicyGroupAccessInterfacePortOutput,
    PolicyGroupAccessInterfaceVpcOutput,
    PolicyGroupAccessInterfaceBreakoutOutput
    ):
    def __init__(self):
        PolicyGroupAccessInterfacePortOutput.__init__(self)
        PolicyGroupAccessInterfaceVpcOutput.__init__(self)
        PolicyGroupAccessInterfaceBreakoutOutput.__init__(self)
