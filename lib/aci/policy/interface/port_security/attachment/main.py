from lib.aci.policy.interface.port_security.attachment.api import PolicyInterfacePortSecurityAttachmentApi
from lib.aci.policy.interface.port_security.attachment.info import PolicyInterfacePortSecurityAttachmentInfo


class PolicyInterfacePortSecurityAttachment(PolicyInterfacePortSecurityAttachmentApi, PolicyInterfacePortSecurityAttachmentInfo):
    def __init__(self):
        PolicyInterfacePortSecurityAttachmentApi.__init__(self)
        PolicyInterfacePortSecurityAttachmentInfo.__init__(self)
