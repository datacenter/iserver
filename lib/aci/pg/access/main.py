from lib.aci.pg.access.intf.main import PolicyGroupAccessInterface
from lib.aci.pg.access.switch.main import PolicyGroupAccessSwitch


class PolicyGroupAccess(PolicyGroupAccessInterface, PolicyGroupAccessSwitch):
    def __init__(self):
        PolicyGroupAccessInterface.__init__(self)
        PolicyGroupAccessSwitch.__init__(self)
