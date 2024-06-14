from lib.aci.contract.filter.event.api import ContractFilterEventApi
from lib.aci.contract.filter.event.info import ContractFilterEventInfo


class ContractFilterEvent(ContractFilterEventApi, ContractFilterEventInfo):
    def __init__(self):
        ContractFilterEventApi.__init__(self)
        ContractFilterEventInfo.__init__(self)
