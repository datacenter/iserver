from lib.aci.intf.policy.group.main import InterfacePolicyGroup
from lib.aci.intf.policy.profile.main import InterfacePolicyProfile


class InterfacePolicy(InterfacePolicyGroup, InterfacePolicyProfile):
    def __init__(self):
        InterfacePolicyGroup.__init__(self)
        InterfacePolicyProfile.__init__(self)
