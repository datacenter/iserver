from lib.aci.contract.filter.fault.api import ContractFilterFaultApi
from lib.aci.contract.filter.fault.info import ContractFilterFaultInfo


class ContractFilterFault(ContractFilterFaultApi, ContractFilterFaultInfo):
    def __init__(self):
        ContractFilterFaultApi.__init__(self)
        ContractFilterFaultInfo.__init__(self)
