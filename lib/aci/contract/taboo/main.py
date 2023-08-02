from lib.aci.contract.taboo.api import ContractTabooApi
from lib.aci.contract.taboo.info import ContractTabooInfo
from lib.aci.contract.taboo.subject.main import ContractTabooSubject
from lib.aci.contract.taboo.audit.main import ContractTabooAudit
from lib.aci.contract.taboo.event.main import ContractTabooEvent
from lib.aci.contract.taboo.fault.main import ContractTabooFault


class ContractTaboo(
        ContractTabooApi,
        ContractTabooInfo,
        ContractTabooSubject,
        ContractTabooAudit,
        ContractTabooEvent,
        ContractTabooFault
        ):
    def __init__(self):
        ContractTabooApi.__init__(self)
        ContractTabooInfo.__init__(self)
        ContractTabooSubject.__init__(self)
        ContractTabooAudit.__init__(self)
        ContractTabooEvent.__init__(self)
        ContractTabooFault.__init__(self)
