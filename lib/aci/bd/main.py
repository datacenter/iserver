from lib.aci.bd.api import BridgeDomainApi
from lib.aci.bd.info import BridgeDomainInfo
from lib.aci.bd.health.main import BridgeDomainHealth
from lib.aci.bd.igmp.main import BridgeDomainIgmp
from lib.aci.bd.l3out.main import BridgeDomainL3Out
from lib.aci.bd.mld.main import BridgeDomainMld
from lib.aci.bd.retention.main import BridgeDomainRetention
from lib.aci.bd.subnet.main import BridgeDomainSubnet
from lib.aci.bd.vrf.main import BridgeDomainVrf


class BridgeDomain(
        BridgeDomainApi,
        BridgeDomainHealth,
        BridgeDomainIgmp,
        BridgeDomainInfo,
        BridgeDomainL3Out,
        BridgeDomainMld,
        BridgeDomainRetention,
        BridgeDomainSubnet,
        BridgeDomainVrf
        ):
    def __init__(self):
        BridgeDomainApi.__init__(self)
        BridgeDomainHealth.__init__(self)
        BridgeDomainIgmp.__init__(self)
        BridgeDomainInfo.__init__(self)
        BridgeDomainL3Out.__init__(self)
        BridgeDomainMld.__init__(self)
        BridgeDomainRetention.__init__(self)
        BridgeDomainSubnet.__init__(self)
        BridgeDomainVrf.__init__(self)
