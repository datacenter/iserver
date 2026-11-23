from lib.aci.pool.vlan.fault.api import PoolVlanFaultApi
from lib.aci.pool.vlan.fault.info import PoolVlanFaultInfo


class PoolVlanFault(PoolVlanFaultApi, PoolVlanFaultInfo):
    def __init__(self):
        PoolVlanFaultApi.__init__(self)
        PoolVlanFaultInfo.__init__(self)
