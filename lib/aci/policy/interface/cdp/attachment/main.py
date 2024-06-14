from lib.aci.policy.interface.cdp.attachment.api import PolicyInterfaceCdpAttachmentApi
from lib.aci.policy.interface.cdp.attachment.info import PolicyInterfaceCdpAttachmentInfo


class PolicyInterfaceCdpAttachment(PolicyInterfaceCdpAttachmentApi, PolicyInterfaceCdpAttachmentInfo):
    def __init__(self):
        PolicyInterfaceCdpAttachmentApi.__init__(self)
        PolicyInterfaceCdpAttachmentInfo.__init__(self)
