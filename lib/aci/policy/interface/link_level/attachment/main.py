from lib.aci.policy.interface.link_level.attachment.api import PolicyInterfaceLinkLevelAttachmentApi
from lib.aci.policy.interface.link_level.attachment.info import PolicyInterfaceLinkLevelAttachmentInfo


class PolicyInterfaceLinkLevelAttachment(PolicyInterfaceLinkLevelAttachmentApi, PolicyInterfaceLinkLevelAttachmentInfo):
    def __init__(self):
        PolicyInterfaceLinkLevelAttachmentApi.__init__(self)
        PolicyInterfaceLinkLevelAttachmentInfo.__init__(self)
