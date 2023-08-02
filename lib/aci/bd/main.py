from lib.aci.bd.api import BridgeDomainApi
from lib.aci.bd.info import BridgeDomainInfo
from lib.aci.bd.igmp.main import BridgeDomainIgmp
from lib.aci.bd.l3out.main import BridgeDomainL3Out
from lib.aci.bd.mld.main import BridgeDomainMld
from lib.aci.bd.retention.main import BridgeDomainRetention
from lib.aci.bd.subnet.main import BridgeDomainSubnet
from lib.aci.bd.vrf.main import BridgeDomainVrf
from lib.aci.bd.audit.main import BridgeDomainAudit
from lib.aci.bd.event.main import BridgeDomainEvent
from lib.aci.bd.fault.main import BridgeDomainFault
from lib.aci.bd.node.main import BridgeDomainNode


class BridgeDomain(
        BridgeDomainApi,
        BridgeDomainIgmp,
        BridgeDomainInfo,
        BridgeDomainL3Out,
        BridgeDomainMld,
        BridgeDomainRetention,
        BridgeDomainSubnet,
        BridgeDomainVrf,
        BridgeDomainAudit,
        BridgeDomainEvent,
        BridgeDomainFault,
        BridgeDomainNode
        ):
    def __init__(self):
        BridgeDomainApi.__init__(self)
        BridgeDomainIgmp.__init__(self)
        BridgeDomainInfo.__init__(self)
        BridgeDomainL3Out.__init__(self)
        BridgeDomainMld.__init__(self)
        BridgeDomainRetention.__init__(self)
        BridgeDomainSubnet.__init__(self)
        BridgeDomainVrf.__init__(self)
        BridgeDomainAudit.__init__(self)
        BridgeDomainEvent.__init__(self)
        BridgeDomainFault.__init__(self)
        BridgeDomainNode.__init__(self)
