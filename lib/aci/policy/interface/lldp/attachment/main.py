from lib.aci.policy.interface.lldp.attachment.api import PolicyInterfaceLldpAttachmentApi
from lib.aci.policy.interface.lldp.attachment.info import PolicyInterfaceLldpAttachmentInfo


class PolicyInterfaceLldpAttachment(PolicyInterfaceLldpAttachmentApi, PolicyInterfaceLldpAttachmentInfo):
    def __init__(self):
        PolicyInterfaceLldpAttachmentApi.__init__(self)
        PolicyInterfaceLldpAttachmentInfo.__init__(self)
