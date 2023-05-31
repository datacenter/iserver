from lib.aci.policy.interface.copp.protocol.api import PolicyInterfaceCoppProtocolApi
from lib.aci.policy.interface.copp.protocol.info import PolicyInterfaceCoppProtocolInfo


class PolicyInterfaceCoppProtocol(PolicyInterfaceCoppProtocolApi, PolicyInterfaceCoppProtocolInfo):
    def __init__(self):
        PolicyInterfaceCoppProtocolApi.__init__(self)
        PolicyInterfaceCoppProtocolInfo.__init__(self)
