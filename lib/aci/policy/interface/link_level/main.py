from lib.aci.policy.interface.link_level.attachment.main import PolicyInterfaceLinkLevelAttachment
from lib.aci.policy.interface.link_level.api import PolicyInterfaceLinkLevelApi
from lib.aci.policy.interface.link_level.context import PolicyInterfaceLinkLevelContext
from lib.aci.policy.interface.link_level.info import PolicyInterfaceLinkLevelInfo
from lib.aci.policy.interface.link_level.create import PolicyInterfaceLinkLevelCreate
from lib.aci.policy.interface.link_level.delete import PolicyInterfaceLinkLevelDelete


class PolicyInterfaceLinkLevel(
        PolicyInterfaceLinkLevelAttachment,
        PolicyInterfaceLinkLevelApi,
        PolicyInterfaceLinkLevelContext,
        PolicyInterfaceLinkLevelInfo,
        PolicyInterfaceLinkLevelCreate,
        PolicyInterfaceLinkLevelDelete
    ):
    def __init__(self):
        PolicyInterfaceLinkLevelAttachment.__init__(self)
        PolicyInterfaceLinkLevelApi.__init__(self)
        PolicyInterfaceLinkLevelContext.__init__(self)
        PolicyInterfaceLinkLevelInfo.__init__(self)
        PolicyInterfaceLinkLevelCreate.__init__(self)
        PolicyInterfaceLinkLevelDelete.__init__(self)
