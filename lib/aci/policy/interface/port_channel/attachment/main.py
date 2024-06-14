from lib.aci.policy.interface.port_channel.attachment.api import PolicyInterfacePortChannelAttachmentApi
from lib.aci.policy.interface.port_channel.attachment.info import PolicyInterfacePortChannelAttachmentInfo


class PolicyInterfacePortChannelAttachment(PolicyInterfacePortChannelAttachmentApi, PolicyInterfacePortChannelAttachmentInfo):
    def __init__(self):
        PolicyInterfacePortChannelAttachmentApi.__init__(self)
        PolicyInterfacePortChannelAttachmentInfo.__init__(self)
