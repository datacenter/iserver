from lib.aci.policy.interface.port_channel_member.attachment.main import PolicyInterfacePortChannelMemberAttachment
from lib.aci.policy.interface.port_channel_member.api import PolicyInterfacePortChannelMemberApi
from lib.aci.policy.interface.port_channel_member.context import PolicyInterfacePortChannelMemberContext
from lib.aci.policy.interface.port_channel_member.info import PolicyInterfacePortChannelMemberInfo


class PolicyInterfacePortChannelMember(PolicyInterfacePortChannelMemberAttachment, PolicyInterfacePortChannelMemberApi, PolicyInterfacePortChannelMemberContext, PolicyInterfacePortChannelMemberInfo):
    def __init__(self):
        PolicyInterfacePortChannelMemberAttachment.__init__(self)
        PolicyInterfacePortChannelMemberApi.__init__(self)
        PolicyInterfacePortChannelMemberContext.__init__(self)
        PolicyInterfacePortChannelMemberInfo.__init__(self)
