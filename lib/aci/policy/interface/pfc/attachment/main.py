from lib.aci.policy.interface.pfc.attachment.api import PolicyInterfacePfcAttachmentApi
from lib.aci.policy.interface.pfc.attachment.info import PolicyInterfacePfcAttachmentInfo


class PolicyInterfacePfcAttachment(PolicyInterfacePfcAttachmentApi, PolicyInterfacePfcAttachmentInfo):
    def __init__(self):
        PolicyInterfacePfcAttachmentApi.__init__(self)
        PolicyInterfacePfcAttachmentInfo.__init__(self)
