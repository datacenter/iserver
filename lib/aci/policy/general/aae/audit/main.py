from lib.aci.policy.general.aae.audit.api import PolicyGeneralAaeAuditApi
from lib.aci.policy.general.aae.audit.info import PolicyGeneralAaeAuditInfo


class PolicyGeneralAaeAudit(PolicyGeneralAaeAuditApi, PolicyGeneralAaeAuditInfo):
    def __init__(self):
        PolicyGeneralAaeAuditApi.__init__(self)
        PolicyGeneralAaeAuditInfo.__init__(self)
