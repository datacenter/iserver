from lib.aci.policy.interface.link_flap.attachment.api import PolicyInterfaceLinkFlapAttachmentApi
from lib.aci.policy.interface.link_flap.attachment.info import PolicyInterfaceLinkFlapAttachmentInfo


class PolicyInterfaceLinkFlapAttachment(PolicyInterfaceLinkFlapAttachmentApi, PolicyInterfaceLinkFlapAttachmentInfo):
    def __init__(self):
        PolicyInterfaceLinkFlapAttachmentApi.__init__(self)
        PolicyInterfaceLinkFlapAttachmentInfo.__init__(self)
