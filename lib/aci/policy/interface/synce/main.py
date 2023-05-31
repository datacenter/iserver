from lib.aci.policy.interface.synce.attachment.main import PolicyInterfaceSynceAttachment
from lib.aci.policy.interface.synce.api import PolicyInterfaceSynceApi
from lib.aci.policy.interface.synce.context import PolicyInterfaceSynceContext
from lib.aci.policy.interface.synce.info import PolicyInterfaceSynceInfo


class PolicyInterfaceSynce(PolicyInterfaceSynceAttachment, PolicyInterfaceSynceApi, PolicyInterfaceSynceContext, PolicyInterfaceSynceInfo):
    def __init__(self):
        PolicyInterfaceSynceAttachment.__init__(self)
        PolicyInterfaceSynceApi.__init__(self)
        PolicyInterfaceSynceContext.__init__(self)
        PolicyInterfaceSynceInfo.__init__(self)
