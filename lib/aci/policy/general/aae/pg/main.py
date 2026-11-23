from lib.aci.policy.general.aae.pg.api import PolicyGeneralAaePgApi
from lib.aci.policy.general.aae.pg.info import PolicyGeneralAaePgInfo


class PolicyGeneralAaePg(PolicyGeneralAaePgApi, PolicyGeneralAaePgInfo):
    def __init__(self):
        PolicyGeneralAaePgApi.__init__(self)
        PolicyGeneralAaePgInfo.__init__(self)
