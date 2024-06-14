from lib.aci.policy.interface.link_flap.attachment.main import PolicyInterfaceLinkFlapAttachment
from lib.aci.policy.interface.link_flap.api import PolicyInterfaceLinkFlapApi
from lib.aci.policy.interface.link_flap.context import PolicyInterfaceLinkFlapContext
from lib.aci.policy.interface.link_flap.info import PolicyInterfaceLinkFlapInfo


class PolicyInterfaceLinkFlap(PolicyInterfaceLinkFlapAttachment, PolicyInterfaceLinkFlapApi, PolicyInterfaceLinkFlapContext, PolicyInterfaceLinkFlapInfo):
    def __init__(self):
        PolicyInterfaceLinkFlapAttachment.__init__(self)
        PolicyInterfaceLinkFlapApi.__init__(self)
        PolicyInterfaceLinkFlapContext.__init__(self)
        PolicyInterfaceLinkFlapInfo.__init__(self)
