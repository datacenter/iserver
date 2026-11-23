from lib.aci.policy.interface.cdp.attachment.main import PolicyInterfaceCdpAttachment
from lib.aci.policy.interface.cdp.api import PolicyInterfaceCdpApi
from lib.aci.policy.interface.cdp.context import PolicyInterfaceCdpContext
from lib.aci.policy.interface.cdp.info import PolicyInterfaceCdpInfo
from lib.aci.policy.interface.cdp.create import PolicyInterfaceCdpCreate
from lib.aci.policy.interface.cdp.delete import PolicyInterfaceCdpDelete


class PolicyInterfaceCdp(
        PolicyInterfaceCdpAttachment,
        PolicyInterfaceCdpApi,
        PolicyInterfaceCdpContext,
        PolicyInterfaceCdpInfo,
        PolicyInterfaceCdpCreate,
        PolicyInterfaceCdpDelete
    ):
    def __init__(self):
        PolicyInterfaceCdpAttachment.__init__(self)
        PolicyInterfaceCdpApi.__init__(self)
        PolicyInterfaceCdpContext.__init__(self)
        PolicyInterfaceCdpInfo.__init__(self)
        PolicyInterfaceCdpCreate.__init__(self)
        PolicyInterfaceCdpDelete.__init__(self)
