from lib.aci.domain.phy.fault.api import DomainPhyFaultApi
from lib.aci.domain.phy.fault.info import DomainPhyFaultInfo


class DomainPhyFault(DomainPhyFaultApi, DomainPhyFaultInfo):
    def __init__(self):
        DomainPhyFaultApi.__init__(self)
        DomainPhyFaultInfo.__init__(self)
