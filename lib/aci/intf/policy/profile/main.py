from lib.aci.intf.policy.profile.api import InterfacePolicyProfileApi
from lib.aci.intf.policy.profile.info import InterfacePolicyProfileInfo


class InterfacePolicyProfile(InterfacePolicyProfileApi, InterfacePolicyProfileInfo):
    def __init__(self):
        InterfacePolicyProfileApi.__init__(self)
        InterfacePolicyProfileInfo.__init__(self)
