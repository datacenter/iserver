from lib.aci.pg.access.intf.vpc.audit.api import PolicyGroupAccessInterfaceVpcAuditApi
from lib.aci.pg.access.intf.vpc.audit.info import PolicyGroupAccessInterfaceVpcAuditInfo


class PolicyGroupAccessInterfaceVpcAudit(PolicyGroupAccessInterfaceVpcAuditApi, PolicyGroupAccessInterfaceVpcAuditInfo):
    def __init__(self):
        PolicyGroupAccessInterfaceVpcAuditApi.__init__(self)
        PolicyGroupAccessInterfaceVpcAuditInfo.__init__(self)
