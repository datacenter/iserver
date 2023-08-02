from lib.aci.contract.standard.main import ContractStandard
from lib.aci.contract.filter.main import ContractFilter
from lib.aci.contract.taboo.main import ContractTaboo


class Contract(
        ContractStandard,
        ContractFilter,
        ContractTaboo,
        ):
    def __init__(self):
        ContractStandard.__init__(self)
        ContractFilter.__init__(self)
        ContractTaboo.__init__(self)
