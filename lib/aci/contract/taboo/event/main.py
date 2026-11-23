from lib.aci.contract.taboo.event.api import ContractTabooEventApi
from lib.aci.contract.taboo.event.info import ContractTabooEventInfo


class ContractTabooEvent(ContractTabooEventApi, ContractTabooEventInfo):
    def __init__(self):
        ContractTabooEventApi.__init__(self)
        ContractTabooEventInfo.__init__(self)
