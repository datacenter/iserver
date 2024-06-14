from lib.aci.policy.interface.mcp.attachment.api import PolicyInterfaceMcpAttachmentApi
from lib.aci.policy.interface.mcp.attachment.info import PolicyInterfaceMcpAttachmentInfo


class PolicyInterfaceMcpAttachment(PolicyInterfaceMcpAttachmentApi, PolicyInterfaceMcpAttachmentInfo):
    def __init__(self):
        PolicyInterfaceMcpAttachmentApi.__init__(self)
        PolicyInterfaceMcpAttachmentInfo.__init__(self)
