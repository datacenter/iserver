from lib import output_helper
from lib import log_helper

from lib.aci.api import Api
from lib.aci.cache import Cache

from lib.aci.ap.main import ApplicationProfile
from lib.aci.bd.main import BridgeDomain
from lib.aci.contract.main import Contract
from lib.aci.domain.main import Domain
from lib.aci.endpoint.main import Endpoint
from lib.aci.epg.main import Epg
from lib.aci.intf.main import Interface
from lib.aci.l2out.main import L2Out
from lib.aci.l3out.main import L3Out
from lib.aci.node.main import Node
from lib.aci.path.main import FabricPath
from lib.aci.pg.main import PolicyGroup
from lib.aci.policy.main import Policy
from lib.aci.pool.main import Pool
from lib.aci.proto.main import Protocol
from lib.aci.tenant import Tenant
from lib.aci.vrf.main import Vrf


class Apic(
        Api,
        ApplicationProfile,
        BridgeDomain,
        Cache,
        Contract,
        Domain,
        Endpoint,
        Epg,
        FabricPath,
        Interface,
        L2Out,
        L3Out,
        Node,
        Policy,
        Pool,
        PolicyGroup,
        Protocol,
        Tenant,
        Vrf
        ):
    def __init__(self, apic_name, username, password, label=None, verbose=False, debug=False, log_id=None, cache_enabled=False):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.log = log_helper.Log(log_id=log_id)

        self.apic_label = label
        Api.__init__(
            self,
            apic_name,
            username,
            password
        )
        Cache.__init__(self, cache_enabled)

        ApplicationProfile.__init__(self)
        BridgeDomain.__init__(self)
        Contract.__init__(self)
        Domain.__init__(self)
        Endpoint.__init__(self)
        Epg.__init__(self)
        FabricPath.__init__(self, log_id=log_id)
        Interface.__init__(self, log_id=log_id)
        L2Out.__init__(self)
        L3Out.__init__(self)
        Node.__init__(self)
        Policy.__init__(self, log_id=log_id)
        Pool.__init__(self)
        PolicyGroup.__init__(self)
        Protocol.__init__(self, log_id=log_id)
        Tenant.__init__(self, log_id=log_id)
        Vrf.__init__(self)
