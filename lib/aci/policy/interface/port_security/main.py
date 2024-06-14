from lib.aci.policy.interface.port_security.attachment.main import PolicyInterfacePortSecurityAttachment
from lib.aci.policy.interface.port_security.api import PolicyInterfacePortSecurityApi
from lib.aci.policy.interface.port_security.context import PolicyInterfacePortSecurityContext
from lib.aci.policy.interface.port_security.info import PolicyInterfacePortSecurityInfo


class PolicyInterfacePortSecurity(PolicyInterfacePortSecurityAttachment, PolicyInterfacePortSecurityApi, PolicyInterfacePortSecurityContext, PolicyInterfacePortSecurityInfo):
    def __init__(self):
        PolicyInterfacePortSecurityAttachment.__init__(self)
        PolicyInterfacePortSecurityApi.__init__(self)
        PolicyInterfacePortSecurityContext.__init__(self)
        PolicyInterfacePortSecurityInfo.__init__(self)
