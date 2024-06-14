from lib import output_helper
from lib import log_helper
from lib import context

from lib.aci import settings

from lib.aci.api import Api
from lib.aci.cache import Cache
from lib.aci.common import Common
from lib.aci.ws import WebSocket

from lib.aci.ap.main import ApplicationProfile
from lib.aci.bd.main import BridgeDomain
from lib.aci.context import Context
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
from lib.aci.server.main import Server
from lib.aci.system.main import System
from lib.aci.tenant.main import Tenant
from lib.aci.vrf.main import Vrf


class Apic(
        Api,
        ApplicationProfile,
        BridgeDomain,
        Cache,
        Common,
        Context,
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
        Server,
        System,
        Tenant,
        Vrf,
        WebSocket
        ):
    def __init__(self, apic_ip, apic_port, username, password, apic_name=None, verbose=False, debug=False, log_id=None, no_cache=False):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.log = log_helper.Log(log_id=log_id)

        self.context_handler = context.Context(log_id=log_id)
        self.apic_name = apic_name
        self.apic_settings = None
        if apic_name is not None:
            settings_handler = settings.ApicSettings()
            self.apic_settings = settings_handler.get_apic_controller(
                apic_name
            )

        Api.__init__(
            self,
            apic_ip,
            apic_port,
            username,
            password
        )
        Cache.__init__(self, self.apic_name, no_cache=no_cache)
        Common.__init__(self)
        Context.__init__(self)
        WebSocket.__init__(
            self,
            apic_ip,
            debug=debug
        )

        ApplicationProfile.__init__(self)
        BridgeDomain.__init__(self)
        Contract.__init__(self)
        Domain.__init__(self)
        Endpoint.__init__(self)
        Epg.__init__(self)
        FabricPath.__init__(self)
        Interface.__init__(self)
        L2Out.__init__(self)
        L3Out.__init__(self)
        Node.__init__(self)
        Policy.__init__(self)
        Pool.__init__(self)
        PolicyGroup.__init__(self)
        Protocol.__init__(self)
        Server.__init__(self)
        System.__init__(self)
        Tenant.__init__(self)
        Vrf.__init__(self)

    def get_apic_name(self):
        if self.apic_name is None:
            return self.apic_ip
        return self.apic_name
