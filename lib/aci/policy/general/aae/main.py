from lib.aci.policy.general.aae.api import PolicyGeneralAaeApi
from lib.aci.policy.general.aae.info import PolicyGeneralAaeInfo
from lib.aci.policy.general.aae.audit.main import PolicyGeneralAaeAudit
from lib.aci.policy.general.aae.event.main import PolicyGeneralAaeEvent
from lib.aci.policy.general.aae.fault.main import PolicyGeneralAaeFault
from lib.aci.policy.general.aae.node.main import PolicyGeneralAaeNode


class PolicyGeneralAae(
        PolicyGeneralAaeApi,
        PolicyGeneralAaeInfo,
        PolicyGeneralAaeAudit,
        PolicyGeneralAaeEvent,
        PolicyGeneralAaeFault,
        PolicyGeneralAaeNode
        ):
    def __init__(self):
        PolicyGeneralAaeApi.__init__(self)
        PolicyGeneralAaeInfo.__init__(self)
        PolicyGeneralAaeAudit.__init__(self)
        PolicyGeneralAaeEvent.__init__(self)
        PolicyGeneralAaeFault.__init__(self)
        PolicyGeneralAaeNode.__init__(self)
