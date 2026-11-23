from lib.aci.policy.interface.storm_control.attachment.main import PolicyInterfaceStormControlAttachment
from lib.aci.policy.interface.storm_control.api import PolicyInterfaceStormControlApi
from lib.aci.policy.interface.storm_control.context import PolicyInterfaceStormControlContext
from lib.aci.policy.interface.storm_control.info import PolicyInterfaceStormControlInfo


class PolicyInterfaceStormControl(PolicyInterfaceStormControlAttachment, PolicyInterfaceStormControlApi, PolicyInterfaceStormControlContext, PolicyInterfaceStormControlInfo):
    def __init__(self):
        PolicyInterfaceStormControlAttachment.__init__(self)
        PolicyInterfaceStormControlApi.__init__(self)
        PolicyInterfaceStormControlContext.__init__(self)
        PolicyInterfaceStormControlInfo.__init__(self)
