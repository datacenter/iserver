from lib.aci.pool.vlan.audit.api import PoolVlanAuditApi
from lib.aci.pool.vlan.audit.info import PoolVlanAuditInfo


class PoolVlanAudit(PoolVlanAuditApi, PoolVlanAuditInfo):
    def __init__(self):
        PoolVlanAuditApi.__init__(self)
        PoolVlanAuditInfo.__init__(self)
