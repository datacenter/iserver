from lib.aci.policy.interface.auth.attachment.main import PolicyInterfaceAuthAttachment
from lib.aci.policy.interface.auth.api import PolicyInterfaceAuthApi
from lib.aci.policy.interface.auth.context import PolicyInterfaceAuthContext
from lib.aci.policy.interface.auth.info import PolicyInterfaceAuthInfo


class PolicyInterfaceAuth(PolicyInterfaceAuthAttachment, PolicyInterfaceAuthApi, PolicyInterfaceAuthContext, PolicyInterfaceAuthInfo):
    def __init__(self):
        PolicyInterfaceAuthAttachment.__init__(self)
        PolicyInterfaceAuthApi.__init__(self)
        PolicyInterfaceAuthContext.__init__(self)
        PolicyInterfaceAuthInfo.__init__(self)
