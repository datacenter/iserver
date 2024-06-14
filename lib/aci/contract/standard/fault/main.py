from lib.aci.contract.standard.fault.api import ContractStandardFaultApi
from lib.aci.contract.standard.fault.info import ContractStandardFaultInfo


class ContractStandardFault(ContractStandardFaultApi, ContractStandardFaultInfo):
    def __init__(self):
        ContractStandardFaultApi.__init__(self)
        ContractStandardFaultInfo.__init__(self)
