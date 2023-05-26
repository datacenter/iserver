from lib.aci.node.policy.profile.api import NodeInterfacePolicyProfileApi
from lib.aci.node.policy.profile.info import NodeInterfacePolicyProfileInfo


class NodeInterfacePolicyProfile(NodeInterfacePolicyProfileApi, NodeInterfacePolicyProfileInfo):
    def __init__(self):
        NodeInterfacePolicyProfileApi.__init__(self)
        NodeInterfacePolicyProfileInfo.__init__(self)
