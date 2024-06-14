from lib.aci.policy.interface.l2.attachment.main import PolicyInterfaceL2Attachment
from lib.aci.policy.interface.l2.api import PolicyInterfaceL2Api
from lib.aci.policy.interface.l2.context import PolicyInterfaceL2Context
from lib.aci.policy.interface.l2.info import PolicyInterfaceL2Info


class PolicyInterfaceL2(PolicyInterfaceL2Attachment, PolicyInterfaceL2Api, PolicyInterfaceL2Context, PolicyInterfaceL2Info):
    def __init__(self):
        PolicyInterfaceL2Attachment.__init__(self)
        PolicyInterfaceL2Api.__init__(self)
        PolicyInterfaceL2Context.__init__(self)
        PolicyInterfaceL2Info.__init__(self)
