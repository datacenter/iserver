from lib.aci.policy.interface.link_level.attachment.main import PolicyInterfaceLinkLevelAttachment
from lib.aci.policy.interface.link_level.api import PolicyInterfaceLinkLevelApi
from lib.aci.policy.interface.link_level.context import PolicyInterfaceLinkLevelContext
from lib.aci.policy.interface.link_level.info import PolicyInterfaceLinkLevelInfo


class PolicyInterfaceLinkLevel(PolicyInterfaceLinkLevelAttachment, PolicyInterfaceLinkLevelApi, PolicyInterfaceLinkLevelContext, PolicyInterfaceLinkLevelInfo):
    def __init__(self):
        PolicyInterfaceLinkLevelAttachment.__init__(self)
        PolicyInterfaceLinkLevelApi.__init__(self)
        PolicyInterfaceLinkLevelContext.__init__(self)
        PolicyInterfaceLinkLevelInfo.__init__(self)
