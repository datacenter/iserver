from lib.aci.policy.interface.mcp.attachment.main import PolicyInterfaceMcpAttachment
from lib.aci.policy.interface.mcp.api import PolicyInterfaceMcpApi
from lib.aci.policy.interface.mcp.context import PolicyInterfaceMcpContext
from lib.aci.policy.interface.mcp.info import PolicyInterfaceMcpInfo


class PolicyInterfaceMcp(PolicyInterfaceMcpAttachment, PolicyInterfaceMcpApi, PolicyInterfaceMcpContext, PolicyInterfaceMcpInfo):
    def __init__(self):
        PolicyInterfaceMcpAttachment.__init__(self)
        PolicyInterfaceMcpApi.__init__(self)
        PolicyInterfaceMcpContext.__init__(self)
        PolicyInterfaceMcpInfo.__init__(self)
