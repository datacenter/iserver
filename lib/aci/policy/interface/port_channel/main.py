from lib.aci.policy.interface.port_channel.attachment.main import PolicyInterfacePortChannelAttachment
from lib.aci.policy.interface.port_channel.api import PolicyInterfacePortChannelApi
from lib.aci.policy.interface.port_channel.context import PolicyInterfacePortChannelContext
from lib.aci.policy.interface.port_channel.info import PolicyInterfacePortChannelInfo
from lib.aci.policy.interface.port_channel.create import PolicyInterfacePortChannelCreate
from lib.aci.policy.interface.port_channel.delete import PolicyInterfacePortChannelDelete


class PolicyInterfacePortChannel(
        PolicyInterfacePortChannelAttachment,
        PolicyInterfacePortChannelApi,
        PolicyInterfacePortChannelContext,
        PolicyInterfacePortChannelInfo,
        PolicyInterfacePortChannelCreate,
        PolicyInterfacePortChannelDelete
    ):
    def __init__(self):
        PolicyInterfacePortChannelAttachment.__init__(self)
        PolicyInterfacePortChannelApi.__init__(self)
        PolicyInterfacePortChannelContext.__init__(self)
        PolicyInterfacePortChannelInfo.__init__(self)
        PolicyInterfacePortChannelCreate.__init__(self)
        PolicyInterfacePortChannelDelete.__init__(self)
