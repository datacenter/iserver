from lib.aci.pg.fabric.intf.main import PolicyGroupFabricInterface
from lib.aci.pg.fabric.module.main import PolicyGroupFabricModule
from lib.aci.pg.fabric.switch.main import PolicyGroupFabricSwitch


class PolicyGroupFabric(PolicyGroupFabricInterface, PolicyGroupFabricModule, PolicyGroupFabricSwitch):
    def __init__(self):
        PolicyGroupFabricInterface.__init__(self)
        PolicyGroupFabricModule.__init__(self)
        PolicyGroupFabricSwitch.__init__(self)
