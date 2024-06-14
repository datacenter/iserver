from lib.aci.domain.l3.fault.api import DomainL3FaultApi
from lib.aci.domain.l3.fault.info import DomainL3FaultInfo


class DomainL3Fault(DomainL3FaultApi, DomainL3FaultInfo):
    def __init__(self):
        DomainL3FaultApi.__init__(self)
        DomainL3FaultInfo.__init__(self)
