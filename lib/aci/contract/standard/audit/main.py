from lib.aci.contract.standard.audit.api import ContractStandardAuditApi
from lib.aci.contract.standard.audit.info import ContractStandardAuditInfo


class ContractStandardAudit(ContractStandardAuditApi, ContractStandardAuditInfo):
    def __init__(self):
        ContractStandardAuditApi.__init__(self)
        ContractStandardAuditInfo.__init__(self)
