from lib.aci.contract.standard.event.api import ContractStandardEventApi
from lib.aci.contract.standard.event.info import ContractStandardEventInfo


class ContractStandardEvent(ContractStandardEventApi, ContractStandardEventInfo):
    def __init__(self):
        ContractStandardEventApi.__init__(self)
        ContractStandardEventInfo.__init__(self)
