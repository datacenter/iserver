from lib.aci.policy.interface.transceiver.attachment.api import PolicyInterfaceTransceiverAttachmentApi
from lib.aci.policy.interface.transceiver.attachment.info import PolicyInterfaceTransceiverAttachmentInfo


class PolicyInterfaceTransceiverAttachment(PolicyInterfaceTransceiverAttachmentApi, PolicyInterfaceTransceiverAttachmentInfo):
    def __init__(self):
        PolicyInterfaceTransceiverAttachmentApi.__init__(self)
        PolicyInterfaceTransceiverAttachmentInfo.__init__(self)
