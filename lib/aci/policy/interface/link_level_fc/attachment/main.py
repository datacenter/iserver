from lib.aci.policy.interface.link_level_fc.attachment.api import PolicyInterfaceLinkLevelFcAttachmentApi
from lib.aci.policy.interface.link_level_fc.attachment.info import PolicyInterfaceLinkLevelFcAttachmentInfo


class PolicyInterfaceLinkLevelFcAttachment(PolicyInterfaceLinkLevelFcAttachmentApi, PolicyInterfaceLinkLevelFcAttachmentInfo):
    def __init__(self):
        PolicyInterfaceLinkLevelFcAttachmentApi.__init__(self)
        PolicyInterfaceLinkLevelFcAttachmentInfo.__init__(self)
