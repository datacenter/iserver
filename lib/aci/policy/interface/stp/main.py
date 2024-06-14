from lib.aci.policy.interface.stp.attachment.main import PolicyInterfaceStpAttachment
from lib.aci.policy.interface.stp.api import PolicyInterfaceStpApi
from lib.aci.policy.interface.stp.context import PolicyInterfaceStpContext
from lib.aci.policy.interface.stp.info import PolicyInterfaceStpInfo


class PolicyInterfaceStp(PolicyInterfaceStpAttachment, PolicyInterfaceStpApi, PolicyInterfaceStpContext, PolicyInterfaceStpInfo):
    def __init__(self):
        PolicyInterfaceStpAttachment.__init__(self)
        PolicyInterfaceStpApi.__init__(self)
        PolicyInterfaceStpContext.__init__(self)
        PolicyInterfaceStpInfo.__init__(self)
