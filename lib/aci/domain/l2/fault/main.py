from lib.aci.domain.l2.fault.api import DomainL2FaultApi
from lib.aci.domain.l2.fault.info import DomainL2FaultInfo


class DomainL2Fault(DomainL2FaultApi, DomainL2FaultInfo):
    def __init__(self):
        DomainL2FaultApi.__init__(self)
        DomainL2FaultInfo.__init__(self)
