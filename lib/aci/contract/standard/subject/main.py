from lib.aci.contract.standard.subject.api import ContractSubjectApi
from lib.aci.contract.standard.subject.info import ContractSubjectInfo


class ContractSubject(ContractSubjectApi, ContractSubjectInfo):
    def __init__(self):
        ContractSubjectApi.__init__(self)
        ContractSubjectInfo.__init__(self)
