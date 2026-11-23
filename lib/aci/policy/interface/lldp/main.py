from lib.aci.policy.interface.lldp.attachment.main import PolicyInterfaceLldpAttachment
from lib.aci.policy.interface.lldp.api import PolicyInterfaceLldpApi
from lib.aci.policy.interface.lldp.context import PolicyInterfaceLldpContext
from lib.aci.policy.interface.lldp.info import PolicyInterfaceLldpInfo
from lib.aci.policy.interface.lldp.create import PolicyInterfaceLldpCreate
from lib.aci.policy.interface.lldp.delete import PolicyInterfaceLldpDelete


class PolicyInterfaceLldp(
        PolicyInterfaceLldpAttachment,
        PolicyInterfaceLldpApi,
        PolicyInterfaceLldpContext,
        PolicyInterfaceLldpInfo,
        PolicyInterfaceLldpCreate,
        PolicyInterfaceLldpDelete
    ):
    def __init__(self):
        PolicyInterfaceLldpAttachment.__init__(self)
        PolicyInterfaceLldpApi.__init__(self)
        PolicyInterfaceLldpContext.__init__(self)
        PolicyInterfaceLldpInfo.__init__(self)
        PolicyInterfaceLldpCreate.__init__(self)
        PolicyInterfaceLldpDelete.__init__(self)
