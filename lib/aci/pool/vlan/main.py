from lib.aci.pool.vlan.api import PoolVlanApi
from lib.aci.pool.vlan.info import PoolVlanInfo


class PoolVlan(PoolVlanApi, PoolVlanInfo):
    def __init__(self):
        PoolVlanApi.__init__(self)
        PoolVlanInfo.__init__(self)
