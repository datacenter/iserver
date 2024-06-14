from lib.aci.contract.filter.audit.api import ContractFilterAuditApi
from lib.aci.contract.filter.audit.info import ContractFilterAuditInfo


class ContractFilterAudit(ContractFilterAuditApi, ContractFilterAuditInfo):
    def __init__(self):
        ContractFilterAuditApi.__init__(self)
        ContractFilterAuditInfo.__init__(self)
