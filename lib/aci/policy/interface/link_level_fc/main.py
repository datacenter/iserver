from lib.aci.policy.interface.link_level_fc.attachment.main import PolicyInterfaceLinkLevelFcAttachment
from lib.aci.policy.interface.link_level_fc.api import PolicyInterfaceLinkLevelFcApi
from lib.aci.policy.interface.link_level_fc.context import PolicyInterfaceLinkLevelFcContext
from lib.aci.policy.interface.link_level_fc.info import PolicyInterfaceLinkLevelFcInfo


class PolicyInterfaceLinkLevelFc(PolicyInterfaceLinkLevelFcAttachment, PolicyInterfaceLinkLevelFcApi, PolicyInterfaceLinkLevelFcContext, PolicyInterfaceLinkLevelFcInfo):
    def __init__(self):
        PolicyInterfaceLinkLevelFcAttachment.__init__(self)
        PolicyInterfaceLinkLevelFcApi.__init__(self)
        PolicyInterfaceLinkLevelFcContext.__init__(self)
        PolicyInterfaceLinkLevelFcInfo.__init__(self)
