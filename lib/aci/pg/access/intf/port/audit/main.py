from lib.aci.pg.access.intf.port.audit.api import PolicyGroupAccessInterfacePortAuditApi
from lib.aci.pg.access.intf.port.audit.info import PolicyGroupAccessInterfacePortAuditInfo


class PolicyGroupAccessInterfacePortAudit(PolicyGroupAccessInterfacePortAuditApi, PolicyGroupAccessInterfacePortAuditInfo):
    def __init__(self):
        PolicyGroupAccessInterfacePortAuditApi.__init__(self)
        PolicyGroupAccessInterfacePortAuditInfo.__init__(self)
