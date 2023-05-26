from lib.aci.policy.general.aae.api import PolicyGeneralAaeApi
from lib.aci.policy.general.aae.info import PolicyGeneralAaeInfo


class PolicyGeneralAae(PolicyGeneralAaeApi, PolicyGeneralAaeInfo):
    def __init__(self):
        PolicyGeneralAaeApi.__init__(self)
        PolicyGeneralAaeInfo.__init__(self)
