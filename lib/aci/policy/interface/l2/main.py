from lib.aci.policy.interface.l2.attachment.main import PolicyInterfaceL2Attachment
from lib.aci.policy.interface.l2.api import PolicyInterfaceL2Api
from lib.aci.policy.interface.l2.context import PolicyInterfaceL2Context
from lib.aci.policy.interface.l2.info import PolicyInterfaceL2Info
from lib.aci.policy.interface.l2.create import PolicyInterfaceL2Create
from lib.aci.policy.interface.l2.delete import PolicyInterfaceL2Delete


class PolicyInterfaceL2(
        PolicyInterfaceL2Attachment,
        PolicyInterfaceL2Api,
        PolicyInterfaceL2Context,
        PolicyInterfaceL2Info,
        PolicyInterfaceL2Create,
        PolicyInterfaceL2Delete
    ):
    def __init__(self):
        PolicyInterfaceL2Attachment.__init__(self)
        PolicyInterfaceL2Api.__init__(self)
        PolicyInterfaceL2Context.__init__(self)
        PolicyInterfaceL2Info.__init__(self)
        PolicyInterfaceL2Create.__init__(self)
        PolicyInterfaceL2Delete.__init__(self)
