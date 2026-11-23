from lib.aci.pg.fabric.module.leaf.main import PolicyGroupFabricModuleLeaf
from lib.aci.pg.fabric.module.spine.main import PolicyGroupFabricModuleSpine


class PolicyGroupFabricModule(PolicyGroupFabricModuleLeaf, PolicyGroupFabricModuleSpine):
    def __init__(self):
        PolicyGroupFabricModuleLeaf.__init__(self)
        PolicyGroupFabricModuleSpine.__init__(self)
