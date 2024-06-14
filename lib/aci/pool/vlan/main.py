from lib.aci.pool.vlan.api import PoolVlanApi
from lib.aci.pool.vlan.info import PoolVlanInfo
from lib.aci.pool.vlan.audit.main import PoolVlanAudit
from lib.aci.pool.vlan.event.main import PoolVlanEvent
from lib.aci.pool.vlan.fault.main import PoolVlanFault


class PoolVlan(
        PoolVlanApi,
        PoolVlanInfo,
        PoolVlanAudit,
        PoolVlanEvent,
        PoolVlanFault
        ):
    def __init__(self):
        PoolVlanApi.__init__(self)
        PoolVlanInfo.__init__(self)
        PoolVlanAudit.__init__(self)
        PoolVlanEvent.__init__(self)
        PoolVlanFault.__init__(self)
