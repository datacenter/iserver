from lib.aci.pg.fabric.switch.leaf.main import PolicyGroupFabricSwitchLeaf
from lib.aci.pg.fabric.switch.spine.main import PolicyGroupFabricSwitchSpine


class PolicyGroupFabricSwitch(PolicyGroupFabricSwitchLeaf, PolicyGroupFabricSwitchSpine):
    def __init__(self):
        PolicyGroupFabricSwitchLeaf.__init__(self)
        PolicyGroupFabricSwitchSpine.__init__(self)
