from lib.aci.policy.general.aae.node.api import PolicyGeneralAaeNodeApi
from lib.aci.policy.general.aae.node.info import PolicyGeneralAaeNodeInfo


class PolicyGeneralAaeNode(PolicyGeneralAaeNodeApi, PolicyGeneralAaeNodeInfo):
    def __init__(self):
        PolicyGeneralAaeNodeApi.__init__(self)
        PolicyGeneralAaeNodeInfo.__init__(self)
