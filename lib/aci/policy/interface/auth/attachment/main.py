from lib.aci.policy.interface.auth.attachment.api import PolicyInterfaceAuthAttachmentApi
from lib.aci.policy.interface.auth.attachment.info import PolicyInterfaceAuthAttachmentInfo


class PolicyInterfaceAuthAttachment(PolicyInterfaceAuthAttachmentApi, PolicyInterfaceAuthAttachmentInfo):
    def __init__(self):
        PolicyInterfaceAuthAttachmentApi.__init__(self)
        PolicyInterfaceAuthAttachmentInfo.__init__(self)
