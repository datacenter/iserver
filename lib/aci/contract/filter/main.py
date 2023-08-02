from lib.aci.contract.filter.api import ContractFilterApi
from lib.aci.contract.filter.info import ContractFilterInfo
from lib.aci.contract.filter.audit.main import ContractFilterAudit
from lib.aci.contract.filter.event.main import ContractFilterEvent
from lib.aci.contract.filter.fault.main import ContractFilterFault


class ContractFilter(
        ContractFilterApi,
        ContractFilterInfo,
        ContractFilterAudit,
        ContractFilterEvent,
        ContractFilterFault
        ):
    def __init__(self):
        ContractFilterApi.__init__(self)
        ContractFilterInfo.__init__(self)
        ContractFilterAudit.__init__(self)
        ContractFilterEvent.__init__(self)
        ContractFilterFault.__init__(self)
