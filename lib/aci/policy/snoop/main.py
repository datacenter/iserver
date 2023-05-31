from lib.aci.policy.snoop.igmp import PolicySnoopIgmp
from lib.aci.policy.snoop.mld import PolicySnoopMld


class PolicySnoop(PolicySnoopIgmp, PolicySnoopMld):
    def __init__(self):
        PolicySnoopIgmp.__init__(self)
        PolicySnoopMld.__init__(self)
