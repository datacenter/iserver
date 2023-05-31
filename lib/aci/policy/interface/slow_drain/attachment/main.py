from lib.aci.policy.interface.slow_drain.attachment.api import PolicyInterfaceSlowDrainAttachmentApi
from lib.aci.policy.interface.slow_drain.attachment.info import PolicyInterfaceSlowDrainAttachmentInfo


class PolicyInterfaceSlowDrainAttachment(PolicyInterfaceSlowDrainAttachmentApi, PolicyInterfaceSlowDrainAttachmentInfo):
    def __init__(self):
        PolicyInterfaceSlowDrainAttachmentApi.__init__(self)
        PolicyInterfaceSlowDrainAttachmentInfo.__init__(self)
