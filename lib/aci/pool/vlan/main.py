from lib.aci.pool.vlan.api import PoolVlanApi
from lib.aci.pool.vlan.info import PoolVlanInfo
from lib.aci.pool.vlan.output import PoolVlanOutput


class PoolVlan(PoolVlanApi, PoolVlanInfo, PoolVlanOutput):
    def __init__(self):
        PoolVlanApi.__init__(self)
        PoolVlanInfo.__init__(self)
        PoolVlanOutput.__init__(self)
