from lib.aci.pg.access.intf.vpc.nodes.api import PolicyGroupAccessInterfaceVpcNodesApi
from lib.aci.pg.access.intf.vpc.nodes.info import PolicyGroupAccessInterfaceVpcNodesInfo


class PolicyGroupAccessInterfaceVpcNodes(PolicyGroupAccessInterfaceVpcNodesApi, PolicyGroupAccessInterfaceVpcNodesInfo):
    def __init__(self):
        PolicyGroupAccessInterfaceVpcNodesApi.__init__(self)
        PolicyGroupAccessInterfaceVpcNodesInfo.__init__(self)
