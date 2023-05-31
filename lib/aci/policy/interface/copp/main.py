from lib.aci.policy.interface.copp.attachment.main import PolicyInterfaceCoppAttachment
from lib.aci.policy.interface.copp.api import PolicyInterfaceCoppApi
from lib.aci.policy.interface.copp.context import PolicyInterfaceCoppContext
from lib.aci.policy.interface.copp.info import PolicyInterfaceCoppInfo
from lib.aci.policy.interface.copp.protocol.main import PolicyInterfaceCoppProtocol


class PolicyInterfaceCopp(PolicyInterfaceCoppAttachment, PolicyInterfaceCoppApi, PolicyInterfaceCoppContext, PolicyInterfaceCoppInfo, PolicyInterfaceCoppProtocol):
    def __init__(self):
        PolicyInterfaceCoppAttachment.__init__(self)
        PolicyInterfaceCoppApi.__init__(self)
        PolicyInterfaceCoppContext.__init__(self)
        PolicyInterfaceCoppInfo.__init__(self)
        PolicyInterfaceCoppProtocol.__init__(self)
