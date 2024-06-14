from lib.aci.policy.interface.port_channel_member.attachment.api import PolicyInterfacePortChannelMemberAttachmentApi
from lib.aci.policy.interface.port_channel_member.attachment.info import PolicyInterfacePortChannelMemberAttachmentInfo


class PolicyInterfacePortChannelMemberAttachment(PolicyInterfacePortChannelMemberAttachmentApi, PolicyInterfacePortChannelMemberAttachmentInfo):
    def __init__(self):
        PolicyInterfacePortChannelMemberAttachmentApi.__init__(self)
        PolicyInterfacePortChannelMemberAttachmentInfo.__init__(self)
