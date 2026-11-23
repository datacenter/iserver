from lib.aci.policy.interface.slow_drain.attachment.main import PolicyInterfaceSlowDrainAttachment
from lib.aci.policy.interface.slow_drain.api import PolicyInterfaceSlowDrainApi
from lib.aci.policy.interface.slow_drain.context import PolicyInterfaceSlowDrainContext
from lib.aci.policy.interface.slow_drain.info import PolicyInterfaceSlowDrainInfo


class PolicyInterfaceSlowDrain(PolicyInterfaceSlowDrainAttachment, PolicyInterfaceSlowDrainApi, PolicyInterfaceSlowDrainContext, PolicyInterfaceSlowDrainInfo):
    def __init__(self):
        PolicyInterfaceSlowDrainAttachment.__init__(self)
        PolicyInterfaceSlowDrainApi.__init__(self)
        PolicyInterfaceSlowDrainContext.__init__(self)
        PolicyInterfaceSlowDrainInfo.__init__(self)
