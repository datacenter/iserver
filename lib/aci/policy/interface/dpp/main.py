from lib.aci.policy.interface.dpp.attachment.main import PolicyInterfaceDppAttachment
from lib.aci.policy.interface.dpp.api import PolicyInterfaceDppApi
from lib.aci.policy.interface.dpp.context import PolicyInterfaceDppContext
from lib.aci.policy.interface.dpp.info import PolicyInterfaceDppInfo


class PolicyInterfaceDpp(PolicyInterfaceDppAttachment, PolicyInterfaceDppApi, PolicyInterfaceDppContext, PolicyInterfaceDppInfo):
    def __init__(self):
        PolicyInterfaceDppAttachment.__init__(self)
        PolicyInterfaceDppApi.__init__(self)
        PolicyInterfaceDppContext.__init__(self)
        PolicyInterfaceDppInfo.__init__(self)
