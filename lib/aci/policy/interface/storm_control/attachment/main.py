from lib.aci.policy.interface.storm_control.attachment.api import PolicyInterfaceStormControlAttachmentApi
from lib.aci.policy.interface.storm_control.attachment.info import PolicyInterfaceStormControlAttachmentInfo


class PolicyInterfaceStormControlAttachment(PolicyInterfaceStormControlAttachmentApi, PolicyInterfaceStormControlAttachmentInfo):
    def __init__(self):
        PolicyInterfaceStormControlAttachmentApi.__init__(self)
        PolicyInterfaceStormControlAttachmentInfo.__init__(self)
