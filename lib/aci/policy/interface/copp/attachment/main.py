from lib.aci.policy.interface.copp.attachment.api import PolicyInterfaceCoppAttachmentApi
from lib.aci.policy.interface.copp.attachment.info import PolicyInterfaceCoppAttachmentInfo


class PolicyInterfaceCoppAttachment(PolicyInterfaceCoppAttachmentApi, PolicyInterfaceCoppAttachmentInfo):
    def __init__(self):
        PolicyInterfaceCoppAttachmentApi.__init__(self)
        PolicyInterfaceCoppAttachmentInfo.__init__(self)
