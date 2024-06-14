from lib.aci.policy.interface.transceiver.attachment.main import PolicyInterfaceTransceiverAttachment
from lib.aci.policy.interface.transceiver.api import PolicyInterfaceTransceiverApi
from lib.aci.policy.interface.transceiver.context import PolicyInterfaceTransceiverContext
from lib.aci.policy.interface.transceiver.info import PolicyInterfaceTransceiverInfo


class PolicyInterfaceTransceiver(PolicyInterfaceTransceiverAttachment, PolicyInterfaceTransceiverApi, PolicyInterfaceTransceiverContext, PolicyInterfaceTransceiverInfo):
    def __init__(self):
        PolicyInterfaceTransceiverAttachment.__init__(self)
        PolicyInterfaceTransceiverApi.__init__(self)
        PolicyInterfaceTransceiverContext.__init__(self)
        PolicyInterfaceTransceiverInfo.__init__(self)
