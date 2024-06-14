from lib.aci.contract.taboo.subject.api import ContractTabooSubjectApi
from lib.aci.contract.taboo.subject.info import ContractTabooSubjectInfo


class ContractTabooSubject(ContractTabooSubjectApi, ContractTabooSubjectInfo):
    def __init__(self):
        ContractTabooSubjectApi.__init__(self)
        ContractTabooSubjectInfo.__init__(self)
