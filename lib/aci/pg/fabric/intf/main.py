from lib.aci.pg.fabric.intf.leaf.main import PolicyGroupFabricInterfaceLeaf
from lib.aci.pg.fabric.intf.spine.main import PolicyGroupFabricInterfaceSpine


class PolicyGroupFabricInterface(PolicyGroupFabricInterfaceLeaf, PolicyGroupFabricInterfaceSpine):
    def __init__(self):
        PolicyGroupFabricInterfaceLeaf.__init__(self)
        PolicyGroupFabricInterfaceSpine.__init__(self)
