from lib.aci.policy.snoop.igmp import PolicySnoopIgmp
from lib.aci.policy.snoop.mld import PolicySnoopMld


class PolicySnoop(PolicySnoopIgmp, PolicySnoopMld):
    def __init__(self, log_id=None):
        PolicySnoopIgmp.__init__(self, log_id=log_id)
        PolicySnoopMld.__init__(self, log_id=log_id)
