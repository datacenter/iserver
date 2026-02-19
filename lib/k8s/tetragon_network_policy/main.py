from lib.k8s.tetragon_network_policy.api import K8sTetragonNetworkPolicyApi
from lib.k8s.tetragon_network_policy.info import K8sTetragonNetworkPolicyInfo


class K8sTetragonNetworkPolicy(
        K8sTetragonNetworkPolicyApi,
        K8sTetragonNetworkPolicyInfo
        ):
    def __init__(self):
        K8sTetragonNetworkPolicyApi.__init__(self)
        K8sTetragonNetworkPolicyInfo.__init__(self)
