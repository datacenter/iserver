from lib.aci.policy.interface.synce.attachment.api import PolicyInterfaceSynceAttachmentApi
from lib.aci.policy.interface.synce.attachment.info import PolicyInterfaceSynceAttachmentInfo


class PolicyInterfaceSynceAttachment(PolicyInterfaceSynceAttachmentApi, PolicyInterfaceSynceAttachmentInfo):
    def __init__(self):
        PolicyInterfaceSynceAttachmentApi.__init__(self)
        PolicyInterfaceSynceAttachmentInfo.__init__(self)
