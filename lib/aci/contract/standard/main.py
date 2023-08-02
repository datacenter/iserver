from lib.aci.contract.standard.api import ContractStandardApi
from lib.aci.contract.standard.info import ContractStandardInfo
from lib.aci.contract.standard.subject.main import ContractSubject
from lib.aci.contract.standard.audit.main import ContractStandardAudit
from lib.aci.contract.standard.event.main import ContractStandardEvent
from lib.aci.contract.standard.fault.main import ContractStandardFault


class ContractStandard(
        ContractStandardApi,
        ContractStandardInfo,
        ContractSubject,
        ContractStandardAudit,
        ContractStandardEvent,
        ContractStandardFault
        ):
    def __init__(self):
        ContractStandardApi.__init__(self)
        ContractStandardInfo.__init__(self)
        ContractSubject.__init__(self)
        ContractStandardAudit.__init__(self)
        ContractStandardEvent.__init__(self)
        ContractStandardFault.__init__(self)
