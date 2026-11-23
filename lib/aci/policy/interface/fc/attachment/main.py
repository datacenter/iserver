from lib.aci.policy.interface.fc.attachment.api import PolicyInterfaceFcAttachmentApi
from lib.aci.policy.interface.fc.attachment.info import PolicyInterfaceFcAttachmentInfo


class PolicyInterfaceFcAttachment(PolicyInterfaceFcAttachmentApi, PolicyInterfaceFcAttachmentInfo):
    def __init__(self):
        PolicyInterfaceFcAttachmentApi.__init__(self)
        PolicyInterfaceFcAttachmentInfo.__init__(self)
