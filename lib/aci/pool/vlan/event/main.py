from lib.aci.pool.vlan.event.api import PoolVlanEventApi
from lib.aci.pool.vlan.event.info import PoolVlanEventInfo


class PoolVlanEvent(PoolVlanEventApi, PoolVlanEventInfo):
    def __init__(self):
        PoolVlanEventApi.__init__(self)
        PoolVlanEventInfo.__init__(self)
