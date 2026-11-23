from lib.aci.policy.interface.l2.attachment.api import PolicyInterfaceL2AttachmentApi
from lib.aci.policy.interface.l2.attachment.info import PolicyInterfaceL2AttachmentInfo


class PolicyInterfaceL2Attachment(PolicyInterfaceL2AttachmentApi, PolicyInterfaceL2AttachmentInfo):
    def __init__(self):
        PolicyInterfaceL2AttachmentApi.__init__(self)
        PolicyInterfaceL2AttachmentInfo.__init__(self)
