from lib.aci.policy.general.aae.fault.api import PolicyGeneralAaeFaultApi
from lib.aci.policy.general.aae.fault.info import PolicyGeneralAaeFaultInfo


class PolicyGeneralAaeFault(PolicyGeneralAaeFaultApi, PolicyGeneralAaeFaultInfo):
    def __init__(self):
        PolicyGeneralAaeFaultApi.__init__(self)
        PolicyGeneralAaeFaultInfo.__init__(self)
