from lib.aci.policy.general.aae.api import PolicyGeneralAaeApi
from lib.aci.policy.general.aae.create import PolicyGeneralAaeCreate
from lib.aci.policy.general.aae.delete import PolicyGeneralAaeDelete
from lib.aci.policy.general.aae.update import PolicyGeneralAaeUpdate
from lib.aci.policy.general.aae.info import PolicyGeneralAaeInfo
from lib.aci.policy.general.aae.audit.main import PolicyGeneralAaeAudit
from lib.aci.policy.general.aae.event.main import PolicyGeneralAaeEvent
from lib.aci.policy.general.aae.fault.main import PolicyGeneralAaeFault
from lib.aci.policy.general.aae.node.main import PolicyGeneralAaeNode
from lib.aci.policy.general.aae.pg.main import PolicyGeneralAaePg
from lib.aci.policy.general.aae.vm.main import PolicyGeneralAaeVm


class PolicyGeneralAae(
        PolicyGeneralAaeApi,
        PolicyGeneralAaeCreate,
        PolicyGeneralAaeDelete,
        PolicyGeneralAaeUpdate,
        PolicyGeneralAaeInfo,
        PolicyGeneralAaeAudit,
        PolicyGeneralAaeEvent,
        PolicyGeneralAaeFault,
        PolicyGeneralAaeNode,
        PolicyGeneralAaePg,
        PolicyGeneralAaeVm
        ):
    def __init__(self):
        PolicyGeneralAaeApi.__init__(self)
        PolicyGeneralAaeCreate.__init__(self)
        PolicyGeneralAaeDelete.__init__(self)
        PolicyGeneralAaeUpdate.__init__(self)
        PolicyGeneralAaeInfo.__init__(self)
        PolicyGeneralAaeAudit.__init__(self)
        PolicyGeneralAaeEvent.__init__(self)
        PolicyGeneralAaeFault.__init__(self)
        PolicyGeneralAaeNode.__init__(self)
        PolicyGeneralAaePg.__init__(self)
        PolicyGeneralAaeVm.__init__(self)
