from lib.aci.pg.access.main import PolicyGroupAccess
from lib.aci.pg.fabric.main import PolicyGroupFabric


class PolicyGroup(
    PolicyGroupAccess,
    PolicyGroupFabric
    ):
    def __init__(self):
        PolicyGroupAccess.__init__(self)
        PolicyGroupFabric.__init__(self)
