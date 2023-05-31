from lib.aci.policy.interface.port_channel.attachment.main import PolicyInterfacePortChannelAttachment
from lib.aci.policy.interface.port_channel.api import PolicyInterfacePortChannelApi
from lib.aci.policy.interface.port_channel.context import PolicyInterfacePortChannelContext
from lib.aci.policy.interface.port_channel.info import PolicyInterfacePortChannelInfo


class PolicyInterfacePortChannel(PolicyInterfacePortChannelAttachment, PolicyInterfacePortChannelApi, PolicyInterfacePortChannelContext, PolicyInterfacePortChannelInfo):
    def __init__(self):
        PolicyInterfacePortChannelAttachment.__init__(self)
        PolicyInterfacePortChannelApi.__init__(self)
        PolicyInterfacePortChannelContext.__init__(self)
        PolicyInterfacePortChannelInfo.__init__(self)
