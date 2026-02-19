from lib.k8s.tetragon_network_policy_namespaced.api import K8sTetragonNetworkPolicyNamespacedApi
from lib.k8s.tetragon_network_policy_namespaced.info import K8sTetragonNetworkPolicyNamespacedInfo


class K8sTetragonNetworkPolicyNamespaced(
        K8sTetragonNetworkPolicyNamespacedApi,
        K8sTetragonNetworkPolicyNamespacedInfo
        ):
    def __init__(self):
        K8sTetragonNetworkPolicyNamespacedApi.__init__(self)
        K8sTetragonNetworkPolicyNamespacedInfo.__init__(self)
