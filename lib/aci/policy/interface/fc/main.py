from lib.aci.policy.interface.fc.attachment.main import PolicyInterfaceFcAttachment
from lib.aci.policy.interface.fc.api import PolicyInterfaceFcApi
from lib.aci.policy.interface.fc.context import PolicyInterfaceFcContext
from lib.aci.policy.interface.fc.info import PolicyInterfaceFcInfo


class PolicyInterfaceFc(PolicyInterfaceFcAttachment, PolicyInterfaceFcApi, PolicyInterfaceFcContext, PolicyInterfaceFcInfo):
    def __init__(self):
        PolicyInterfaceFcAttachment.__init__(self)
        PolicyInterfaceFcApi.__init__(self)
        PolicyInterfaceFcContext.__init__(self)
        PolicyInterfaceFcInfo.__init__(self)
