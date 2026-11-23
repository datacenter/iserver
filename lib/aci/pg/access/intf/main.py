from lib.aci.pg.access.intf.breakout.main import PolicyGroupAccessInterfaceBreakout
from lib.aci.pg.access.intf.fc.main import PolicyGroupAccessInterfaceFc
from lib.aci.pg.access.intf.fcpc.main import PolicyGroupAccessInterfaceFcPc
from lib.aci.pg.access.intf.override.main import PolicyGroupAccessInterfaceOverride
from lib.aci.pg.access.intf.pc.main import PolicyGroupAccessInterfacePc
from lib.aci.pg.access.intf.port.main import PolicyGroupAccessInterfacePort
from lib.aci.pg.access.intf.spine.main import PolicyGroupAccessInterfaceSpine
from lib.aci.pg.access.intf.vpc.main import PolicyGroupAccessInterfaceVpc


class PolicyGroupAccessInterface(
    PolicyGroupAccessInterfaceBreakout,
    PolicyGroupAccessInterfaceFc,
    PolicyGroupAccessInterfaceFcPc,
    PolicyGroupAccessInterfaceOverride,
    PolicyGroupAccessInterfacePc,
    PolicyGroupAccessInterfacePort,
    PolicyGroupAccessInterfaceSpine,
    PolicyGroupAccessInterfaceVpc
    ):
    def __init__(self):
        PolicyGroupAccessInterfaceBreakout.__init__(self)
        PolicyGroupAccessInterfaceFc.__init__(self)
        PolicyGroupAccessInterfaceFcPc.__init__(self)
        PolicyGroupAccessInterfaceOverride.__init__(self)
        PolicyGroupAccessInterfacePc.__init__(self)
        PolicyGroupAccessInterfacePort.__init__(self)
        PolicyGroupAccessInterfaceSpine.__init__(self)
        PolicyGroupAccessInterfaceVpc.__init__(self)
