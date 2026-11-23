from lib.aci.domain.vmm.fault.api import DomainVmmFaultApi
from lib.aci.domain.vmm.fault.info import DomainVmmFaultInfo


class DomainVmmFault(DomainVmmFaultApi, DomainVmmFaultInfo):
    def __init__(self):
        DomainVmmFaultApi.__init__(self)
        DomainVmmFaultInfo.__init__(self)
