from lib.aci.contract.api import ContractApi
from lib.aci.contract.info import ContractInfo
from lib.aci.contract.filter.main import Filter
from lib.aci.contract.subject.main import Subject
from lib.aci.contract.taboo.main import Taboo
from lib.aci.contract.taboo_subject.main import TabooSubject


class Contract(ContractApi, ContractInfo, Filter, Subject, Taboo, TabooSubject):
    def __init__(self):
        ContractApi.__init__(self)
        ContractInfo.__init__(self)
        Filter.__init__(self)
        Subject.__init__(self)
        Taboo.__init__(self)
        TabooSubject.__init__(self)
