from lib.aci.policy.interface.pfc.attachment.main import PolicyInterfacePfcAttachment
from lib.aci.policy.interface.pfc.api import PolicyInterfacePfcApi
from lib.aci.policy.interface.pfc.context import PolicyInterfacePfcContext
from lib.aci.policy.interface.pfc.info import PolicyInterfacePfcInfo


class PolicyInterfacePfc(PolicyInterfacePfcAttachment, PolicyInterfacePfcApi, PolicyInterfacePfcContext, PolicyInterfacePfcInfo):
    def __init__(self):
        PolicyInterfacePfcAttachment.__init__(self)
        PolicyInterfacePfcApi.__init__(self)
        PolicyInterfacePfcContext.__init__(self)
        PolicyInterfacePfcInfo.__init__(self)
