from lib.aci.contract.standard.output import ContractStandardOutput
from lib.aci.contract.filter.output import ContractFilterOutput
from lib.aci.contract.taboo.output import ContractTabooOutput


class ContractOutput(ContractStandardOutput, ContractFilterOutput, ContractTabooOutput):
    def __init__(self):
        ContractStandardOutput.__init__(self)
        ContractFilterOutput.__init__(self)
        ContractTabooOutput.__init__(self)
