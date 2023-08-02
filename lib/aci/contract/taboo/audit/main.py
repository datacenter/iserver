from lib.aci.contract.taboo.audit.api import ContractTabooAuditApi
from lib.aci.contract.taboo.audit.info import ContractTabooAuditInfo


class ContractTabooAudit(ContractTabooAuditApi, ContractTabooAuditInfo):
    def __init__(self):
        ContractTabooAuditApi.__init__(self)
        ContractTabooAuditInfo.__init__(self)
