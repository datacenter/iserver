from lib.aci.l3out.api import L3OutApi
from lib.aci.l3out.bgp import L3OutBgp
from lib.aci.l3out.domain import L3OutDomain
from lib.aci.l3out.eigrp import L3OutEigrp
from lib.aci.l3out.epg import L3OutEpg
from lib.aci.l3out.info import L3OutInfo
from lib.aci.l3out.logical_node_profile.main import L3OutLogicalNodeProfile
from lib.aci.l3out.ospf import L3OutOspf
from lib.aci.l3out.pim import L3OutPim
from lib.aci.l3out.vrf import L3OutVrf
from lib.aci.l3out.audit.main import L3OutAudit
from lib.aci.l3out.event.main import L3OutEvent
from lib.aci.l3out.fault.main import L3OutFault
from lib.aci.l3out.node.main import L3OutNode


class L3Out(
        L3OutApi,
        L3OutBgp,
        L3OutDomain,
        L3OutEigrp,
        L3OutEpg,
        L3OutInfo,
        L3OutLogicalNodeProfile,
        L3OutOspf,
        L3OutPim,
        L3OutVrf,
        L3OutAudit,
        L3OutEvent,
        L3OutFault,
        L3OutNode
        ):
    def __init__(self):
        L3OutApi.__init__(self)
        L3OutBgp.__init__(self)
        L3OutDomain.__init__(self)
        L3OutEigrp.__init__(self)
        L3OutEpg.__init__(self)
        L3OutInfo.__init__(self)
        L3OutLogicalNodeProfile.__init__(self)
        L3OutOspf.__init__(self)
        L3OutPim.__init__(self)
        L3OutVrf.__init__(self)
        L3OutAudit.__init__(self)
        L3OutEvent.__init__(self)
        L3OutFault.__init__(self)
        L3OutNode.__init__(self)
