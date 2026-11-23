from lib.aci.policy.general.aae.vm.api import PolicyGeneralAaeVmApi
from lib.aci.policy.general.aae.vm.info import PolicyGeneralAaeVmInfo


class PolicyGeneralAaeVm(PolicyGeneralAaeVmApi, PolicyGeneralAaeVmInfo):
    def __init__(self):
        PolicyGeneralAaeVmApi.__init__(self)
        PolicyGeneralAaeVmInfo.__init__(self)
