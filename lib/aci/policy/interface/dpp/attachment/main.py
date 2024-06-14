from lib.aci.policy.interface.dpp.attachment.api import PolicyInterfaceDppAttachmentApi
from lib.aci.policy.interface.dpp.attachment.info import PolicyInterfaceDppAttachmentInfo


class PolicyInterfaceDppAttachment(PolicyInterfaceDppAttachmentApi, PolicyInterfaceDppAttachmentInfo):
    def __init__(self):
        PolicyInterfaceDppAttachmentApi.__init__(self)
        PolicyInterfaceDppAttachmentInfo.__init__(self)
