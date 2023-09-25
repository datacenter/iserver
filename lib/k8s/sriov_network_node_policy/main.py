from lib.k8s.sriov_network_node_policy.api import K8sSriovNetworkNodePolicyApi
from lib.k8s.sriov_network_node_policy.info import K8sSriovNetworkNodePolicyInfo


class K8sSriovNetworkNodePolicy(
        K8sSriovNetworkNodePolicyApi,
        K8sSriovNetworkNodePolicyInfo
        ):
    def __init__(self):
        K8sSriovNetworkNodePolicyApi.__init__(self)
        K8sSriovNetworkNodePolicyInfo.__init__(self)
