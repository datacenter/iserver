from lib import output_helper

from lib.aci.ap.output import ApplicationProfileOutput
from lib.aci.bd.output import BridgeDomainOutput
from lib.aci.contract.output import ContractOutput
from lib.aci.domain.output import DomainOutput
from lib.aci.endpoint.output import EndpointOutput
from lib.aci.epg.output import EpgOutput
from lib.aci.intf.output import InterfaceOutput
from lib.aci.l2out.output import L2OutOutput
from lib.aci.l3out.output import L3OutOutput
from lib.aci.node.output import NodeOutput
from lib.aci.pg.output import PolicyGroupOutput
from lib.aci.policy.output import PolicyOutput
from lib.aci.pool.output import PoolOutput
from lib.aci.proto.output import ProtocolOutput
from lib.aci.tenant.output import TenantOutput
from lib.aci.vrf.output import VrfOutput


class ApicOutput(
    ApplicationProfileOutput,
    BridgeDomainOutput,
    ContractOutput,
    DomainOutput,
    EndpointOutput,
    EpgOutput,
    InterfaceOutput,
    L2OutOutput,
    L3OutOutput,
    NodeOutput,
    PolicyGroupOutput,
    PolicyOutput,
    PoolOutput,
    ProtocolOutput,
    TenantOutput,
    VrfOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.is_apic = True

        ApplicationProfileOutput.__init__(self)
        BridgeDomainOutput.__init__(self)
        ContractOutput.__init__(self)
        DomainOutput.__init__(self)
        EndpointOutput.__init__(self)
        EpgOutput.__init__(self)
        InterfaceOutput.__init__(self)
        L2OutOutput.__init__(self)
        L3OutOutput.__init__(self)
        NodeOutput.__init__(self)
        PolicyGroupOutput.__init__(self)
        PolicyOutput.__init__(self)
        PoolOutput.__init__(self)
        ProtocolOutput.__init__(self)
        TenantOutput.__init__(self)
        VrfOutput.__init__(self)

    def set_apic_off(self):
        self.is_apic = False
