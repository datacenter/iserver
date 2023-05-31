from lib.aci.policy.interface.stp.attachment.api import PolicyInterfaceStpAttachmentApi
from lib.aci.policy.interface.stp.attachment.info import PolicyInterfaceStpAttachmentInfo


class PolicyInterfaceStpAttachment(PolicyInterfaceStpAttachmentApi, PolicyInterfaceStpAttachmentInfo):
    def __init__(self):
        PolicyInterfaceStpAttachmentApi.__init__(self)
        PolicyInterfaceStpAttachmentInfo.__init__(self)
