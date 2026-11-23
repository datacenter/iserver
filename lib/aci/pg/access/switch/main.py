from lib.aci.pg.access.switch.leaf.main import PolicyGroupAccessSwitchLeaf
from lib.aci.pg.access.switch.spine.main import PolicyGroupAccessSwitchSpine


class PolicyGroupAccessSwitch(PolicyGroupAccessSwitchLeaf, PolicyGroupAccessSwitchSpine):
    def __init__(self):
        PolicyGroupAccessSwitchLeaf.__init__(self)
        PolicyGroupAccessSwitchSpine.__init__(self)
