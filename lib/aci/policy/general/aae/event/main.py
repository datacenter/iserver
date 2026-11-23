from lib.aci.policy.general.aae.event.api import PolicyGeneralAaeEventApi
from lib.aci.policy.general.aae.event.info import PolicyGeneralAaeEventInfo


class PolicyGeneralAaeEvent(PolicyGeneralAaeEventApi, PolicyGeneralAaeEventInfo):
    def __init__(self):
        PolicyGeneralAaeEventApi.__init__(self)
        PolicyGeneralAaeEventInfo.__init__(self)
