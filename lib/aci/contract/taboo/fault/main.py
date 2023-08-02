from lib.aci.contract.taboo.fault.api import ContractTabooFaultApi
from lib.aci.contract.taboo.fault.info import ContractTabooFaultInfo


class ContractTabooFault(ContractTabooFaultApi, ContractTabooFaultInfo):
    def __init__(self):
        ContractTabooFaultApi.__init__(self)
        ContractTabooFaultInfo.__init__(self)
