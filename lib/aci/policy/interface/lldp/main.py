from lib.aci.policy.interface.lldp.attachment.main import PolicyInterfaceLldpAttachment
from lib.aci.policy.interface.lldp.api import PolicyInterfaceLldpApi
from lib.aci.policy.interface.lldp.context import PolicyInterfaceLldpContext
from lib.aci.policy.interface.lldp.info import PolicyInterfaceLldpInfo


class PolicyInterfaceLldp(PolicyInterfaceLldpAttachment, PolicyInterfaceLldpApi, PolicyInterfaceLldpContext, PolicyInterfaceLldpInfo):
    def __init__(self):
        PolicyInterfaceLldpAttachment.__init__(self)
        PolicyInterfaceLldpApi.__init__(self)
        PolicyInterfaceLldpContext.__init__(self)
        PolicyInterfaceLldpInfo.__init__(self)
